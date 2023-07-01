import os
from tags import start_tag


def load_multiple_files(path: str, deck_tag: str) -> list:
    """
    loads all files that have a start tag and are for the given deck.
    :path: directory of the flashcards
    :deck_tag: tag thats in the file right after the start_tag
    returns: list of md_cards
    """
    # go to path
    os.chdir(path)
    files = os.listdir()
    card_files = []
    for x in files:
        if x[-3:] == ".md":
            md = load_one_file(x, deck_tag)
            print(md)
            # is flashcard?
            if md == "":
                continue
            card_files.append(md)
        else:
            continue
    return card_files


def load_one_file(file_name: str, deck_tag: str) -> str:
    """
    searches file, error if not found in directory.
    returns: the file in str format
    """
    try:
        f = open(file_name, "r")
        try:
            f.readline()[-1]
            f.seek(0)
        except IndexError:
            print("File not working with tags.")
            return ""
        check_flash = contains_tag(f, start_tag)
        check_deck = contains_tag(f, deck_tag)
        if check_flash is False:
            print("No flashcards found in file.")
            return ""
        if check_deck is False:
            print("No belonging deck in file.")
            return ""
        return f.read()
    except FileNotFoundError:
        print("File not found, try again.")
        return ""


def contains_tag(file: object, tag: str) -> bool:
    """
    Looks at the first line of the given file and searches for the tag.
    """

    foundTag = False
    prevPosition = file.tell()
    file.seek(0)

    if tag in file.readline():
        foundTag = True

    if tag in file.readlines()[-1]:
        foundTag = True

    # reset position in the file handle
    file.seek(prevPosition)
    return foundTag


# str-version of tag-checker
def contains_tag_str(file: str, tag: str) -> bool:
    """
    Looks at the first line of the given file and searches for the tag.
    """

    foundTag = False
    prevPosition = file.tell()
    file.seek(0)

    if tag in file.partition("\n")[-1]:
        foundTag = True
    # reset file handle position
    file.seek(prevPosition)

    return foundTag
