from yaml import load


def open_yaml_file(filepath: str) -> dict:
    with open(filepath) as file:
        return load(file)
