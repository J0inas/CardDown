import os
from typing import TextIO


def get_valid_cardfiles_from_dir(path: str, start_tag="", deck_tag="") -> list:
    """
    loads all files that have a start tag and are for the given deck.
    :path: directory of the flashcards
    :deck_tag: tag thats in the file right after the start_tag
    returns: list of md_cards
    """

    # go to path
    files = os.listdir(path)
    card_filenames = []
    for filename in files:
        if filename.endswith(".md"):
            filename = os.path.join(path, filename)
            print(filename)
            if is_valid_cardfile(filename, start_tag, deck_tag):
                card_filenames.append(filename)

        else:
            continue

    return card_filenames


def is_valid_cardfile(file_name: str, start_tag="", deck_tag="") -> bool:
    """
    searches file, error if not found in directory.
    returns: the file in str format
    """
    file_name = os.path.abspath(file_name)

    if deck_tag == "":
        return True

    try:
        f = open(file_name, "r")
    except FileNotFoundError:
        print("File not found again.")
        return False

    f.seek(0)

    check_tags = contains_cardTags(f, start_tag, deck_tag)

    f.close()
    return check_tags


def contains_cardTags(file: TextIO, start_tag: str, deck_tag: str) -> bool:
    """
    Looks at the first line of the given file and searches for the tag.
    """
    foundDeckTag = False
    foundCardTag = False
    prevPosition = file.tell()
    file.seek(0)

    for line in file:
        # remove trailing whitespace (especially newlines)
        line = line.rstrip()
        if line == start_tag:
            foundCardTag = True
            if foundDeckTag:
                break
        if line == deck_tag:
            foundDeckTag = True
            if foundCardTag:
                break

    # reset position in the file handle
    file.seek(prevPosition)
    # TODO print whats missing
    return foundDeckTag and foundCardTag
