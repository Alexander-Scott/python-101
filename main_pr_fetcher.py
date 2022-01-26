from github_pr_fetcher.pr_fetcher import HttpGitHubFetchPRGit
from github_pr_fetcher.pr_handler import PrHandler

if __name__ == "__main__":
    prs_dict = HttpGitHubFetchPRGit.get_github_all_pr()
    PrHandler.get_github_pr_from_prs_data(prs_dict, 5)