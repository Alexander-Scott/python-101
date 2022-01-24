from yaml_loader.yaml_loader import YamlLoader
from yaml_loader.yaml_modify import YamlModify
from yaml_loader.yaml_saver import YamlSaver
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('job_name', type=str, help='its a name for existing job')
    args = parser.parse_args()
    data_info = YamlLoader.read_file("yaml_loader/data.yaml")
    print(data_info)
    changed_job = YamlModify.yaml_modify(data_info, args.job_name)
    print(changed_job)
    YamlSaver.save_file(changed_job, "yaml_loader/new_data.yaml")
    print(YamlLoader.read_file("yaml_loader/new_data.yaml"))