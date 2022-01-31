import argparse
from comment_on_pr import GraphQlGitHub

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="write github comment on pr with number")
    parser.add_argument("pr_number", type=int, help="Provide pr number where to add comment on")
    parser.add_argument("comment", type=str, help="Comment to be made in the PR")
    parser.add_argument("token", type=str, help="Token to access github")

    args = parser.parse_args()

    GraphQlGitHub.github_comment_posted_pr(args)
