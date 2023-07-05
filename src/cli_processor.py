import argparse

cli_parser = argparse.ArgumentParser(
    prog="carddown",
    description="Generate Anki Cards from Markdown files.",
    epilog="Test")


cli_parser.add_argument(
    "path", type=str, nargs="+", help="Path to either a single Markdown file, or a directory containing them")
cli_parser.add_argument(
    "-mp", "--mediapath", dest="mediapath", help="Directory containing media files (default: Directory of the cards)")
cli_parser.add_argument(
    "-p", "--parser", dest="parser",  choices=["simple", "block"], help="Syntax/Parser used to create cards from the files. (Available: simple, block)")

cli_parser.add_argument(
    "-c", "--config", dest="configpath", help="Filepath or directory to a config.ini file.")


def get_cli_args():

    return cli_parser.parse_args()
