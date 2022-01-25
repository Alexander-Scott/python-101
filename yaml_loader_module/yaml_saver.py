import os
import yaml


class YamlSaver:
    @staticmethod
    def save_file(file_content: list, file_path: str):
        with open(file_path, "w") as new_file:
            # new_file.write(yaml.dump(file_content))
            yaml.dump(file_content, new_file)  # convert in to a string
