import os
from tomllib import load

cfg_args = False


def load_cfg_args(cfg_path: str):

    global cfg_args

    if os.path.isdir(cfg_path):
        # try to find config file in dir
        cfg_path = __get_cfg_path_from_dir(cfg_path)

    if not os.path.isfile(cfg_path):
        cfg_args = get_default_config()
        return cfg_args

    cfg_file_handle = open(cfg_path, "rb")

    cfg_args = load(cfg_file_handle)
    return cfg_args


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


cli_args = False

# handle cfg_args as a "singleton"


def get_cfg_args():
    global cfg_arg
    if cfg_args is False:
        print("No config found")
        return None

    return cli_args
