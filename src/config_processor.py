import os
from tomllib import load


def get_cfg_args(cfg_path: str):

    if os.path.isdir(cfg_path):
        # try to find config file in dir
        cfg_path = __get_cfg_path_from_dir(cfg_path)

    if not os.path.isfile(cfg_path):
        return get_default_config()

    cfg_file_handle = open(cfg_path, "rb")

    return load(cfg_file_handle)


def __get_cfg_path_from_dir(path: str) -> str:

    files = os.listdir(path)

    for filename in files:
        if filename == "config.toml":
            return os.path.join(path, filename)

    return ""


def get_default_config():

    # TODO implement?
    f = open("src/cardconfig/config.toml", "rb")
    return load(f)
