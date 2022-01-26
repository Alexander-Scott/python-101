import requests
import json
class NotFoundException(Exception):
    pass
class HttpGitHubFetchPRGit:

    pr_query_url = "https://api.github.com/repos/bagaco-ramp-up/python-101/pulls"  

    @staticmethod
    def get_github_all_pr(action):
        """
        This function intends to fetch the PR data fom github
        """
        pr_params = {
            "state": "all",
        }
        pull_request_data = requests.get(HttpGitHubFetchPRGit.pr_query_url, params=pr_params)
        
        if pull_request_data.status_code == 404:   # Check for invalid github address 
            raise NotFoundException("Link not found")
        pull_request_dic = pull_request_data.json()

        # Print all Prs on --print option
        if action:
            print("PR Number -> Title -> State \n")
            for i in range(0, len(pull_request_dic)):
                pull_request_title = pull_request_dic[i]["title"]
                pull_request_state = pull_request_dic[i]["state"]
                pull_request_number = pull_request_dic[i]["number"]
                print( pull_request_number,  " -> " + pull_request_title + " -> " + pull_request_state + "\n")
        return pull_request_dic


