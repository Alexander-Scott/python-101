import requests


class GraphQlGitHub:

    pr_query_url = "https://api.github.com/graphql"

    @staticmethod
    def github_comment_posted_pr(args):
        """
        This function intends to comment actual PR
        """

        query = GraphQlGitHub.generate_query_to_fetch_PR_author_and_id(args.pr_number)
        headers = {"Authorization": "Bearer " + args.token}
        response = requests.post(GraphQlGitHub.pr_query_url, json=query, headers=headers)
        response_dict = response.json()

        pr_id = response_dict["data"]["organization"]["repository"]["pullRequest"]["id"]
        pr_login = response_dict["data"]["organization"]["repository"]["pullRequest"]["author"]["login"]

        print("PR  author is " + pr_login + " and id is " + pr_id + " \n")
        print(response.json())
        print("\n")

        mutation = GraphQlGitHub.generate_mutation_to_add_a_comment_to_a_pr(pr_id, args.comment, pr_login)
        mutation_response = requests.post(GraphQlGitHub.pr_query_url, json=mutation, headers=headers)
        response_dict = mutation_response.json()
        return response_dict

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
