from github_pr_fetcher.pr_fetcher import HttpGitHubFetchPRGit
from github_pr_fetcher.pr_handler import PrHandler
import argparse

if __name__ == "__main__":
    parser =argparse.ArgumentParser(description="fetching PR data from github")
    parser.add_argument("pr_number", type=int, help="to get the pr name")
    args = parser.parse_args()

    prs_dict = HttpGitHubFetchPRGit.get_github_all_pr()        
    
    PrHandler.get_github_pr_from_prs_data(prs_dict, args.pr_number)
    