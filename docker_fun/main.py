import argparse
from create_a_file_and_open_a_pr import FileCreation

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="write github comment on pr with number")
    parser.add_argument("file_name", type=str, help="Provide the name of the file to be uploaded to github")
    parser.add_argument("Content", type=str, help="content of the file to be uploaded")
    parser.add_argument("token", type=str, help="Token to access github")

    args = parser.parse_args()

    FileCreation.create_file_in_github(args)
