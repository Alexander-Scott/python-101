import os


class YamlModify:
    @staticmethod
    def yaml_modify(loader_file: list):
        # list = [
        #     {"job": {"name": "my-job", "parent": "my-parent", "vars": {"data": "hello world"}}},
        #     {"job": {"name": "my-job_2", "parent": "my-job", "vars": {"data": "hello world"}}},
        # ]
        list = loader_file
        for job in loader_file:
            for key in job["job"]:
                print("what vaue for  " + key)
                if key == "name":
                    job["job"][key] = "testestring"
                if isinstance(job["job"][key], dict):
                    for nested_key in job["job"][key]:
                        print("what vaue for  " + nested_key)
        return loader_file


# job["job"] = {"name": "my-job", "parent": "my-parent", "vars": {"data": "hello world"}}
# job["job"]["name"] = "my-job"
# job["job"]["vars"] = {"data": "hello world", "daata2": "fsfdsf"}

# for job in loader_file:
# .  print(job)
# .  print(job["name"])
