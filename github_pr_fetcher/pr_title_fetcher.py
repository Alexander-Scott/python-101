import requests

# import json


class NotFoundException(Exception):
    pass


class HttpGitHubFetchPRGit:
    pr_query_url = "https://api.github.com/repos/bagaco-ramp-up/python-101/pulls"

    @staticmethod
    def get_github_pr_title():
        # pr_query_url = "https://api.github.com/repos/bagaco-ramp-up/python-101/pulls"
        pr_params = {
            "state": "all",
        }
        pull_request_data = requests.get(HttpGitHubFetchPRGit.pr_query_url, params=pr_params)
        if pull_request_data.status_code == 404:
            raise NotFoundException("Link not found")
        # print(pull_request_data)
        pull_request_dic = pull_request_data.json()
        # print(json.dumps(pull_request_dic, indent=4, sort_keys=True))
        for i in range(0, len(pull_request_dic)):
            pull_request_title = pull_request_dic[i]["title"]
            pull_request_state = pull_request_dic[i]["state"]
            pull_request_number = pull_request_dic[i]["number"]
            print(pull_request_number, " " + pull_request_title + " " + pull_request_state)
        return pull_request_title


# /repos/{owner}/{repo}/pulls/{pull_number}
#  /repos/{owner}/{repo}/pulls
# https://api.github.com
