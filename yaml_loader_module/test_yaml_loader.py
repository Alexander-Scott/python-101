import unittest
from yaml_loader import YamlLoader
from yaml_modify import YamlModify
from yaml_saver import YamlSaver
from unittest.mock import patch


class TestYamlLoader(unittest.TestCase):
    # GIVEN-WHEN-THEN
    # test_given_a_yaml_file__when_yaml_file_contains_full_job_definition__then_expect_yaml_file_read_successfully
    def test_given_a_yaml_file__when_yaml_file_contains_full_job_definition__then_expect_yaml_file_read_successfully(
        self,
    ):
        # Arrange
        test_file_path = "yaml_loader_module/new_data.yaml"
        # Act
        test_dict = YamlLoader.read_file(test_file_path)
        # Assert
        expected_value = [{"job": {"name": "andre_job", "parent": "my-parent", "vars": {"data": "hello world"}}}]
        self.assertEqual(test_dict, expected_value)

    def test_given_a_yaml_file__path_when_yaml_file_path_is_invalid__then_return_none(
        self,
    ):
        # Arrange
        wrong_test_file_path = "yaml_loader_module/new_data_invalid.yaml"
        # Act
        test_dict = YamlLoader.read_file(wrong_test_file_path)
        # Assert
        self.assertIsNone(test_dict)


class TestYamlModify(unittest.TestCase):
    def test_given_a_yaml_file_when_add_some_modification_expect_a_mofified_content(self):
        # Arrange
        file_content = [{"job": {"name": "Andre Job", "parent": "my-parent", "vars": {"data": "hello world"}}}]
        new_job_name = "Bagaço Team"
        expected_file_content = [
            {"job": {"name": "Bagaço Team", "parent": "my-parent", "vars": {"data": "hello world"}}}
        ]

        # Act
        new_file_content = YamlModify.yaml_modify(file_content, new_job_name)

        # Assert
        self.assertEqual(new_file_content, expected_file_content)


class TestYamlSaver(unittest.TestCase):
    def test_given_a_yaml_file__when_imput_is_normal__expect_a_open_called(self):
        # Arrange
        file_content = [{"job": {"name": "Andre Job", "parent": "my-parent", "vars": {"data": "hello world"}}}]

        # Act & Assert
        with patch("builtins.open") as mock_file:
            YamlSaver.save_file(file_content, "yaml_loader_module/save_test.yaml")
        mock_file.assert_called_with("yaml_loader_module/save_test.yaml", "w")


