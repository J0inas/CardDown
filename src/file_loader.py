import os
from typing import TextIO
from tags import start_tag


def get_valid_cardfiles_from_dir(path: str, deck_tag: str) -> list:
    """
    loads all files that have a start tag and are for the given deck.
    :path: directory of the flashcards
    :deck_tag: tag thats in the file right after the start_tag
    returns: list of md_cards
    """
    # go to path
    os.chdir(path)
    files = os.listdir()
    card_filenames = [str]
    for filename in files:
        if filename.endswith(".md"):
            print(filename)
            if is_valid_cardfile(filename, [start_tag, deck_tag]):
                card_filenames.append(filename)

        else:
            continue
    return card_filenames


def is_valid_cardfile(file_name: str, deck_tag: str) -> str:
    """
    searches file, error if not found in directory.
    returns: the file in str format
    """
    if deck_tag == "":
        return file_name

    try:
        f = open(file_name, "r")
        f.seek(0)

        check_tags = contains_cardTags(f, [start_tag, deck_tag])

        if check_tags is False:
            f.close()
            return ""

        f.close()
        return file_name
    except FileNotFoundError:
        print("File not found, try again.")
        return ""


def contains_cardTags(file: TextIO, tags: list[str]) -> bool:
    """
    Looks at the first line of the given file and searches for the tag.
    """
    foundDeckTag = False
    foundCardTag = False
    prevPosition = file.tell()
    file.seek(0)

    for line in file:
        for tag in tags:
            if tag in line:
                if tag == tags[0]:
                    foundCardTag = True
                else:
                    foundDeckTag = True
                if foundCardTag and foundDeckTag:
                    break

    # reset position in the file handle
    file.seek(prevPosition)
    # TODO print whats missing
    return foundDeckTag and foundCardTag
