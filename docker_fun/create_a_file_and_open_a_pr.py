from time import sleep
"""
  Create a python script that creates a file and opens up a new PR with GraphQL/REST.
 - [x] Find relevant GraphQL or REST endpoints. Specially createFile and openPR
 - [x] Create a class and use requests to access the API.
 - [x] The createCommitOnBranch is not able to automatically create a branch, so we must make a prior request that pre-creates the branch. 
 Use https://docs.github.com/en/graphql/reference/mutations#createref.
 - [ ] Create a PR after creating the file on the new branch.
"""
import base64
import requests
import datetime


class FileCreation:

    pr_query_url = "https://api.github.com/graphql"

    @staticmethod
    def create_file_in_github(args):

        query = FileCreation.generate_query_to_fetch_repo_id()
        headers = {"Authorization": "Bearer " + args.token}
        response = requests.post(FileCreation.pr_query_url, json=query, headers=headers)
        response_dict = response.json()
        oid_repo=response_dict["data"]["organization"]["repository"]["ref"]["target"]["oid"]
        print(response_dict)
        print("oid:" + oid_repo)

        branch = "refs/heads/branch_" + datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        print(branch)
        mutation = FileCreation.generate_mutation_to_create_a_branch(branch, oid_repo)
        headers = {"Authorization": "Bearer " + args.token}
        response = requests.post(FileCreation.pr_query_url, json=mutation, headers=headers)
        print(response.json())
        response_dict = response.json()

        mutation = FileCreation.generate_mutation_to_create_a_file_on_a_branch(args, branch, oid_repo)
        headers = {"Authorization": "Bearer " + args.token}
        response = requests.post(FileCreation.pr_query_url, json=mutation, headers=headers)
        print(response.reason)
        response_dict = response.json()

        mutation = FileCreation.generate_mutation_to_create_a_pull_request(args, branch)
        headers = {"Authorization": "Bearer " + args.token}
        response = requests.post(FileCreation.pr_query_url, json=mutation, headers=headers)
        print("Pr_name:" , response.json())


        print(response.json())
        print("\n")
        return response_dict

    @staticmethod
    def generate_mutation_to_create_a_branch(branch, oid_repo):
        query = """
                mutation AddBranch($branch: String!,$oid_repo: String! ) {
                    createRef(
                        input: {
                            name: $branch
                            oid: $oid_repo
                            repositoryId: "R_kgDOGqj_7Q"
                        }
                    ) {
                        clientMutationId
                    }
                }
                """

        # head_id = "refs/heads/main"  # 6c891cdc8e7e557094c9f619c72985a8ead698f2
        # branch = "branch_" + datetime.datetime.now().strftime()
        variables = {
            "branch": branch,
            "oid_repo": oid_repo
        }
        return {"query": query, "variables": variables}

    @staticmethod
    def generate_mutation_to_create_a_file_on_a_branch(args, branch, oid_repo):
        query = """
                mutation createCommitOnBranch($branch: String!, $head_id: String!, $file_changes: String!, $commit_message: String!,$path: String!) {
                    createCommitOnBranch (
                        input: {
                            branch: {
                                repositoryNameWithOwner: "bagaco-ramp-up/python-101",
                                branchName: $branch
                            }
                            expectedHeadOid: $head_id
                            fileChanges: {
                                additions: [
                                    {
                                        path: $path,
                                        contents: $file_changes
                                    }
                                ]
                            }

                            message: {
                                headline: $commit_message
                            }

                        }
                    ) {
                        clientMutationId

                    }
                } 
            """
        # branch = "branch_3"
        head_id = oid_repo
        file_changes = base64.b64encode(bytes(args.Content, "utf-8")).decode("ascii")
        commit_message = "hello commit"
        path= "docs/" + args.file_name
        variables = {
            "branch": branch,
            "head_id": head_id,
            "file_changes": file_changes,
            "commit_message": commit_message,
            "path": path
        }   
        return {"query": query, "variables": variables}

    @staticmethod
    def generate_mutation_to_create_a_pull_request(args, branch):
        query = """
                mutation CreatePullRequest($branch: String!,$title: String! ) {
                    createPullRequest(
                        input: {
                            baseRefName: "refs/heads/main"
                            headRefName: $branch
                            repositoryId: "R_kgDOGqj_7Q"
                            title: $title
                        }
                    ) {
                        pullRequest {
                            number
                        }
                    }
                }
                """
        title = "adding new file " + args.file_name
        variables = {
            "branch": branch,
            "title": title
        }
        return {"query": query, "variables": variables}

    @staticmethod
    def generate_query_to_fetch_repo_id():
        query = """
                query FetchRepo {
                    organization(login: "bagaco-ramp-up") {
                        repository(name: "python-101") {
                            ref(qualifiedName: "refs/heads/main") {
                                target {
                                    oid
                                }
                            }
                        }
                    }
                }
            """
        return {"query": query}
