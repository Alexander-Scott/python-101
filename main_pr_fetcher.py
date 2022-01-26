import argparse
from github_pr_fetcher.pr_fetcher import HttpGitHubFetchPRGit
from github_pr_fetcher.pr_handler import PrHandler

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Fetching PR data from github")
    parser.add_argument("pr_number", type=int, help="Provide pr number to filter the fetched PR")
    parser.add_argument(
        "--print", action="store_true", default=False, help="Print on screen the PR list"
    )
    args = parser.parse_args()

    prs_dict = HttpGitHubFetchPRGit.get_github_all_pr(args.print)

    PrHandler.get_github_pr_from_prs_data(prs_dict, args.pr_number)
