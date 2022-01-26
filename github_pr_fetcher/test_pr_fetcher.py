import json
import unittest
from unittest.mock import patch, MagicMock
from github_pr_fetcher.pr_fetcher import HttpGitHubFetchPRGit, NotFoundException
from github_pr_fetcher.pr_handler import PrHandler


class MockResponse:
    def __init__(self, status_code: int, path_to_json_file: str):
        self.status_code = status_code
        self.json_data = path_to_json_file
        with open(path_to_json_file, "r") as file:
            self.json_data = json.loads(file.read())

    def json(self):
        return self.json_data


class TestPRFetcher(unittest.TestCase):
    # GIVEN-WHEN-THEN
    # test_given_a_yaml_file__when_yaml_file_contains_full_job_definition__then_expect_yaml_file_read_successfully
    @patch(
        "github_pr_fetcher.pr_fetcher.HttpGitHubFetchPRGit.pr_query_url",
        "https://api.github.com/repos/bagaco-ramp-up/python-102/pulls",
    )
    def test_given_wrong_hhtp_address_when_reading_the_prs__then_it_should_fail(
        self,
    ):
        # Arrange
        # @patch('HttpGitHubFetchPRGit.pr_query_url', "https://api.github.com/repos/bagaco-ramp-up/python-102/pulls")
        # Act
        with self.assertRaises(NotFoundException):
            retuned_value = HttpGitHubFetchPRGit.get_github_all_pr()
        # Assert

    @patch("requests.get", MagicMock(return_value=MockResponse(200, "github_pr_fetcher/pr_mock_data.json")))
    def test__given_regular_data_fetched_from_github__when_data_is_regular__expect_pr_title_found(
        self,
    ):
        # pr number: 11
        # "title": "git fetch pull requests",
        # "login": "Luissprof",
        # Arrange
        expeted_author = "Luissprof"
        expeted_title = "git fetch pull requests"
        pr_number = 11
        # Act
        prs_dict = HttpGitHubFetchPRGit.get_github_all_pr()
        pr_search_result = PrHandler.get_github_pr_from_prs_data(prs_dict, pr_number)
        # Assert
        self.assertEquals(pr_search_result["title"], expeted_title)
        self.assertEquals(pr_search_result["user"]["login"], expeted_author)

    # @patch("requests.get", MagicMock(return_value=MockResponse(200, "github_pr_fetcher/corruped_file.json")))
    # def test__given_empty_data__expect_exception_raised(self):
    #     pass
