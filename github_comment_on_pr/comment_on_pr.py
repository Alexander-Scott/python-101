import argparse
import requests

from my_token import Token


class GraphQlGitHub:

    pr_query_url = "https://api.github.com/graphql"

    @staticmethod
    def github_comment_posted_pr():
        """
        This function intends to fetch the PR data fom github
        """
        print("test")

        query = GraphQlGitHub.generate_query_to_fetch_PR_author_and_id(args.pr_number)
        headers = {"Authorization": "Bearer " + Token.Token}
        response = requests.post(GraphQlGitHub.pr_query_url, json=query, headers=headers)
        response_dic = response.json()

        pr_id = response_dic["data"]["organization"]["repository"]["pullRequest"]["id"]
        pr_login = response_dic["data"]["organization"]["repository"]["pullRequest"]["author"]["login"]

        print("PR  author is " + pr_login + " and id is " + pr_id + " \n")
        print(response.json())
        print("\n")

        mutation = GraphQlGitHub.generate_mutation_to_add_a_comment_to_a_pr(pr_id, args.comment, pr_login)
        mutation_response = requests.post(GraphQlGitHub.pr_query_url, json=mutation, headers=headers)
        response_dic = mutation_response.json()
        print(response_dic)

    @staticmethod
    def generate_mutation_to_add_a_comment_to_a_pr(pr_id, comment, pr_login):
        query = """
                mutation AddCommentToPR($pr_id: String!, $body: String!) {
                    addComment (
                        input: {
                            body: $body
                            subjectId: $pr_id
                        }
                    ) {
                        clientMutationId
                    }
                }
            """
        body = comment + " " + pr_login
        variables = {"pr_id": pr_id, "body": body}
        return {"query": query, "variables": variables}

    #  Fetch PR author and id
    @staticmethod
    def generate_query_to_fetch_PR_author_and_id(pr_number):
        query = """
                query FetchRepo($pr_number: Int!) {
                    organization(login: "bagaco-ramp-up") {
                        repository(name: "python-101") {
                            pullRequest(number: $pr_number) {
                                author {
                                    login
                                }
                            id
                            }
                        }
                    }
                }
            """
        variables = {"pr_number": pr_number}
        return {"query": query, "variables": variables}


# pullRequest(number: 10)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="write github comment on pr with number")
    parser.add_argument("pr_number", type=int, help="Provide pr number where to add comment on")
    parser.add_argument("comment", type=str, help="Comment to be made in the PR")
    args = parser.parse_args()

    GraphQlGitHub.github_comment_posted_pr()

# - [x] Create a python script that opens a comment on a PR in Github.
# - [ ] The content of the comment should be "Hello " + pr_author
# - [ ] Github can only be communicated with via GraphQL (and not REST).
# - [ ] A job is created that runs our python script. The job runs on all opened PRs.
