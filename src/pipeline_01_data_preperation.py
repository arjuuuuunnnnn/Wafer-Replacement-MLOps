import os
import argparse
import yaml
import logging


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml_file.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)





if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config", "params.yaml") # this is done because if I give config/params.yaml directly it might not correctly work in windows system
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--datasource", default=None)
    # adding command line arguements

    parsed_args = args.parse_args()
    # print(parsed_args) # to know the values passed by the user in the command line as arguments

    main(config_path=parsed_args.config, datasource=parsed_args.datasource)
    