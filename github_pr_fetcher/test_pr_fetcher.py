import unittest
from unittest.mock import patch
from github_pr_fetcher.pr_fetcher import HttpGitHubFetchPRGit, NotFoundException


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