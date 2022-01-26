import json
import unittest
from unittest.mock import patch, MagicMock
from github_pr_fetcher.pr_fetcher import HttpGitHubFetchPRGit, NotFoundException
from github_pr_fetcher.pr_handler import PrHandler


class MockResponse:
    """
    This class is used when tests make a request to github api
    """
    def __init__(self, status_code: int, path_to_json_file: str):
        self.status_code = status_code
        self.json_data = path_to_json_file
        with open(path_to_json_file, "r") as file:
            self.json_data = json.loads(file.read())

    def json(self):
        return self.json_data


class TestPRFetcher(unittest.TestCase):
    # GIVEN-WHEN-THEN
    @patch(
        "github_pr_fetcher.pr_fetcher.HttpGitHubFetchPRGit.pr_query_url",
        "https://api.github.com/repos/bagaco-ramp-up/python-102/pulls",
    )
    def test_given_wrong_http_address_when_reading_the_prs__then_it_should_fail(
        self,
    ):
        # Arrange
        # Act
        with self.assertRaises(NotFoundException):
            HttpGitHubFetchPRGit.get_github_all_pr(False)
        # Assert

    @patch("requests.get", MagicMock(return_value=MockResponse(200, "github_pr_fetcher/pr_mock_data.json")))
    def test__given_regular_data_fetched_from_github__when_data_is_regular__expect_pr_title_found(
        self,
    ):
        # Arrange
        expected_author = "Luissprof"
        expected_title = "git fetch pull requests"
        pr_number = 11
        # Act
        prs_dict = HttpGitHubFetchPRGit.get_github_all_pr(True)
        pr_search_result = PrHandler.get_github_pr_from_prs_data(prs_dict, pr_number)
        # Assert
        self.assertEqual(pr_search_result["title"], expected_title)
        self.assertEqual(pr_search_result["user"]["login"], expected_author)

    @patch("requests.get", MagicMock(return_value=MockResponse(200, "github_pr_fetcher/pr_mock_data.json")))
    def test__given_regular_data_fetched_from_github__when_pr_does_not_exist__expect_null_return(
        self,
    ):
        # Arrange
        pr_number = -1
        # Act
        prs_dict = HttpGitHubFetchPRGit.get_github_all_pr(False)
        pr_search_result = PrHandler.get_github_pr_from_prs_data(prs_dict, pr_number)
        # Assert
        self.assertIsNone(pr_search_result)
        




