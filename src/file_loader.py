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
            print (x)
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
        f.seek(0)
        check_flash = contains_tag(f, start_tag)
        check_deck = contains_tag(f, deck_tag)
        if check_flash is False:
            print("No flashcards found in file.")
            return ""
        if check_deck is False:
            print("No belonging deck in file.")
            return ""
        f.seek(0)
        return f.read()
    except FileNotFoundError:
        print("File not found, try again.")
        return ""


def contains_tag(file: object, tag: str) -> bool:
    """
    Looks at the first line of the given file and searches for the tag.
    """
    file.seek(0)
    
    if tag in file.readline():
        return True
    
    for x in file.readlines():
        if tag in x:
            return True
    
    return False