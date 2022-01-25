import unittest
from unittest.mock import patch
from github_pr_fetcher.pr_title_fetcher import HttpGitHubFetchPRGit



class TestPRFetcher(unittest.TestCase):
    # GIVEN-WHEN-THEN
    # test_given_a_yaml_file__when_yaml_file_contains_full_job_definition__then_expect_yaml_file_read_successfully
    @patch('pr_title_fetcher.HttpGitHubFetchPRGit.get_github_pr_title(pr_query_url)', "https://api.github.com/repos/bagaco-ramp-up/python-102/pulls")    
    def test_given_wrong_hhtp_address_when_reading_the_prs__then_it_should_fail(
        self,
    ):
        # Arrange
        #@patch('HttpGitHubFetchPRGit.pr_query_url', "https://api.github.com/repos/bagaco-ramp-up/python-102/pulls")    
        # Act
        HttpGitHubFetchPRGit.get_github_pr_title()
        # Assert
        expected_value = "<Response [404]>"
        self.assertEqual(HttpGitHubFetchPRGit.pull_request_data, expected_value)

        HttpGitHubFetchPRGit.get_github_pr_title.


