import argparse

cli_parser = argparse.ArgumentParser(
    prog="carddown",
    description="Generate Anki Cards from Markdown files.",
    epilog="Test")


cli_parser.add_argument(
    "path", type=str, nargs="+", help="Path to either a single Markdown file, or a directory containing them")
cli_parser.add_argument(
    "-mp", "--mediapath", dest="mediapath", default="", type=str, help="Directory containing media files (default: Directory of the cards)")
cli_parser.add_argument(
    "-p", "--parser", dest="parser",  choices=["simple", "block"], default="", type=str, help="Syntax/Parser used to create cards from the files. (Available: simple, block)")
cli_parser.add_argument(
    "-dt", "--decktag", dest="decktag", default="", type=str, help="Tag used to parse Cards from files that contain it")

cli_parser.add_argument(
    "-c", "--config", dest="configpath", default="", type=str, help="Filepath or directory to a config.ini file.")

cli_parser.add_argument(
    "-o", "--output", dest="savepath", default="", type=str, help="Path were the .apkg should be saved"
)

cli_args = False

# handle cli_args as a singleton


def get_cli_args():
    global cli_args
    if cli_args is False:
        cli_args = cli_parser.parse_args()

    return cli_args
