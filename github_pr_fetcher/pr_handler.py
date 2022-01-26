class PrHandler:

    @staticmethod
    def get_github_pr_from_prs_data(prs_data: dict, pr: int):
        for i in range(0, len(prs_data)):
            if pr == prs_data[i]["number"]:
                print(prs_data[i]["title"])
                return prs_data[i]
        return None

    @staticmethod
    def get_pr_author(prs_data: dict, pr: int):
        for i in range(0, len(prs_data)):
            if pr == prs_data[i]["number"]:
                print(prs_data[i]["user"]["login"])
                return prs_data[i]["user"]["login"]
