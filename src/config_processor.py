import os
from tomllib import load, loads
from carddown_defaults import config
from cardparser import block_parser, simple_parser

cfg_args = False


def load_cfg_args(cfg_path: str):

    global cfg_args

    cfg_path = find_cfg_file(cfg_path)

    # if a config could not be found til now, use the default one
    if not os.path.isfile(cfg_path):
        cfg_args = get_default_config()

        return cfg_args
    else:

        cfg_file_handle = open(cfg_path, "rb")

        cfg_args = load(cfg_file_handle)
        cfg_file_handle.close()

        cfg_args = overwrite_default_config(cfg_args)

        return cfg_args


def __get_cfg_path_from_dir(path: str) -> str:

    files = os.listdir(path)

    for filename in files:
        if filename == "config.toml":
            return os.path.join(path, filename)

    return ""


def get_default_config():

    default_cfg = loads(config)
    return default_cfg


def get_cfg_args():
    global cfg_arg
    if cfg_args is False:
        print("No config found")
        return None

    return cfg_args


def find_cfg_file(cfg_path: str):

    if os.path.isdir(cfg_path):
        # try to find config file in dir
        cfg_path = __get_cfg_path_from_dir(cfg_path)

    elif not os.path.isfile(cfg_path):

        # try to find config in working dir
        files_in_dir = os.listdir()
        for file in files_in_dir:
            if file.endswith(".toml"):
                cfg_path = os.path.join(os.getcwd(), file)
                break

    return cfg_path


def calibrate_config_args(cfg):
    """
    This method will adjust the config arguments,
    so it can be used correctly in the project
    """

    if cfg["parser"]["type"] == "block":
        cfg["parser"]["type"] = block_parser

    else:
        cfg["parser"]["type"] = simple_parser


def overwrite_default_config(new_cfg):

    default = get_default_config()

    for table_key in default.keys():
        if str(table_key) in new_cfg:
            for sub_key in default[str(table_key)]:
                # only access keys wich exists and overwrite config
                # otherwise default value will be used
                if sub_key in new_cfg[str(table_key)]:
                    default[str(table_key)][str(sub_key)
                                            ] = new_cfg[str(table_key)][str(sub_key)]

    return default
