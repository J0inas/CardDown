from cli_processor import get_cli_args
from config_processor import load_cfg_args
from md_to_anki import md_to_anki
from cardparser import simple_parser, block_parser
from os import curdir, getcwd
import carddown_defaults


def main():

    cli_args, cfg_args = load_args()

    overwrite_cfg_with_cli_input(cli_args, cfg_args)

    execute(cfg_args)


def load_args():
    cli_args = get_cli_args()

    cfg_args = load_cfg_args(cli_args.configpath)

    return cli_args, cfg_args


def overwrite_cfg_with_cli_input(cli_args, cfg_args):

    if cli_args.path:
        # TODO provide bash completion
        # TODO support multiple paths
        cfg_args["deck"]["card_path"] = cli_args.path
        print(cli_args.path)

    else:
        # cfg_args["deck"]["card_path"] = curdir
        cfg_args["deck"]["card_path"] = getcwd()

    if cli_args.decktag:
        cfg_args["deck"]["tag"] = cli_args.decktag

    # TODO implement
    if cli_args.mediapath:
        cfg_args["media"]["path"] = cli_args.mediapath

    if cli_args.parser:

        if cli_args.parser == "block":
            cfg_args["parser"]["type"] = block_parser

        else:
            cfg_args["parser"]["type"] = simple_parser

    # TODO implement
    if cli_args.savepath:
        cfg_args["deck"]["save_path"] = cli_args.savepath
    else:
        if not cfg_args["deck"]["save_path"]:
            cfg_args["deck"]["save_path"] = cfg_args["deck"]["card_path"]


def execute(cfg):
    md_to_anki(cfg["deck"]["card_path"], cfg["deck"]["start_tag"], cfg["deck"]
               ["tag"], cfg["deck"]["name"], cfg["parser"]["type"], cfg["media"]["path"])


if __name__ == "__main__":
    main()
