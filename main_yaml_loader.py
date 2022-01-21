from yaml_loader.yaml_loader import YamlLoader

if __name__ == "__main__":
    data_info = YamlLoader.read_file("yaml_loader/data.yaml")
    print(data_info)
