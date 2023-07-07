from cli_processor import get_cli_args
from config_processor import load_cfg_args
from md_to_anki import md_to_anki
from os import getcwd
import carddown_defaults


def main():

    cli_args, cfg_args = load_args()

    overwrite_cfg_with_cli_input(cli_args, cfg_args)

    print(cfg_args)

    execute(cfg_args)


def load_args():
    cli_args = get_cli_args()

    cfg_args = load_cfg_args(cli_args.configpath)

    return cli_args, cfg_args


def overwrite_cfg_with_cli_input(cli_args, cfg_args):

    if cli_args.path:
        # TODO provide bash completion
        # TODO support multiple paths
        cfg_args["deck"]["card_path"] = cli_args.path[0]

    else:
        cfg_args["deck"]["card_path"] = getcwd()

    if cli_args.decktag:
        cfg_args["deck"]["tag"] = cli_args.decktag

    if cli_args.mediapath:
        cfg_args["media"]["path"] = cli_args.mediapath

    if cli_args.parser:
        cfg_args["parser"]["type"] = cli_args.parser

    if cli_args.savepath:
        cfg_args["deck"]["save_path"] = cli_args.savepath
    else:
        if not cfg_args["deck"]["save_path"]:
            cfg_args["deck"]["save_path"] = cfg_args["deck"]["card_path"]


def execute(cfg):
    print(cfg["deck"]["card_path"] is str)
    md_to_anki(cfg["deck"]["card_path"], cfg["deck"]
               ["tag"], cfg["deck"]["name"])


if __name__ == "__main__":
    main()
