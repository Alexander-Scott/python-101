class PrHandler:

    @staticmethod
    def get_github_pr_from_prs_data(prs_data: dict, pr: int):
        for i in range(0, len(prs_data)):
            if pr == prs_data[i]["number"]:
                print(prs_data[i]["title"])
                print(prs_data[i]["user"]["login"])
                return prs_data[i]
        return None
