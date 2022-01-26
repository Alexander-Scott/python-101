class PrHandler:

    @staticmethod
    def get_github_pr_from_prs_data(prs_data: dict, pr: int):
        """
        Function to fetch the PR data fom given PR Number
        """
        for i in range(0, len(prs_data)):
            if pr == prs_data[i]["number"]:
                print(" For PR number '",  pr, "'  title is '" +  prs_data[i]["title"] + "' and Owner is '" + prs_data[i]["user"]["login"]+"'")
                return prs_data[i]
        return None
