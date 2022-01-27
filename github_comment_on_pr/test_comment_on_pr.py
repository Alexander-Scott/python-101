import unittest
from unittest.mock import patch, MagicMock
from github_pr_fetcher.test_pr_fetcher import MockResponse
from comment_on_pr import GraphQlGitHub


class MockArgs:
    """
    This class is used when tests make a request to github api
    """
    def __init__(self, pr_number: int, comment: str, token: str):
        self.pr_number = pr_number
        self.comment = comment
        self.token = token

class TestCommentOnPR(unittest.TestCase):
    # GIVEN-WHEN-THEN
    @patch(
        "requests.post",
        MagicMock(
            side_effect=[
                MockResponse(200, "github_comment_on_pr/response_pr.json"),
                MockResponse(200, "github_comment_on_pr/response_mutation.json"),
            ]
        ),
    )
    def test_comment_to_pr(
        self,
    ):
        # Arrange
        pr_number = 1
        comment = "Hello World"
        token = "any_token"

        # Act
        GraphQlGitHub.github_comment_posted_pr(MockArgs(pr_number, comment, token))

        # Assert
