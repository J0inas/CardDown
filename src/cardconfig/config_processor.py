import os
from tomllib import load
from typing import BinaryIO


def get_cfg_args(path: str):
    cfg_path = str
    if path != "":
        if os.path.isdir(path):
            cfg_path = __get_cfg_path_from_dir(path)

        if not os.path.isfile(cfg_path):
            return

    cfg_file_handle = open(cfg_path, "r")
    cfg = load(cfg_file_handle)
    cfg_file_handle.close()
    return cfg


def __get_cfg_path_from_dir(path: str) -> str:

    files = os.listdir(path)

    for filename in files:
        if filename == "config.ini":
            return os.path.join(path, filename)

    return ""
