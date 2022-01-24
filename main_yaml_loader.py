from yaml_loader.yaml_loader import YamlLoader
from yaml_loader.yaml_modify import YamlModify
from yaml_loader.yaml_saver import YamlSaver

if __name__ == "__main__":
    data_info = YamlLoader.read_file("yaml_loader/data.yaml")
    print(data_info)
    changed_job = YamlModify.yaml_modify(data_info)
    print(changed_job)
    YamlSaver.save_file(changed_job, "yaml_loader/new_data.yaml")
    print(YamlLoader.read_file("yaml_loader/new_data.yaml"))