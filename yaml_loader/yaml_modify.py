import os

class YamlModify:
    @staticmethod
    def yaml_modify(loader_file: list, key: dict):
        # list = [{'job': {'name': 'my-job', 'parent': 'my-parent', 'vars': {'data': 'hello world'}}}]
        list = loader_file
        