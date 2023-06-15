import os
from tags import start_tag

def load_multiple_files(
    path : str,
    deck_tag : str,
    ) -> list:
    """
    loads all files that have a start tag for the 
    :deck_tag: tag thats in the file right after the start_tag 
    """
    # if start_tag is in first line and the deck-tag is correct
    # then put file in queue for parsing to md_cards
    
    # go to path
    os.chdir(path)
    files = os.listdir()
    card_files = []
    for x in files:
        # is flashcard?
        if (load_one_file == ""):
            continue
        # is the right flashcard?
        if (contains_tag(x,deck_tag) == False):
            continue
        card_files.append(x)
             
    return card_files

def load_one_file(
    file_name : str,
    ) -> str:
    """
    searches file, error if not found in directory.
    returns: the file in str format
    """
    try:
        f = open(file_name,'r')
        check = contains_tag(f,start_tag)
        if (check == False):
            print ("No flashcards found.")
            return ""
        return f.read()
    except FileNotFoundError:
        print("File not found, try again.")
        return ""

def contains_tag(file : object, tag : str) -> bool:
    """
    Looks at the first line of the given file and searches for the tag.
    """
    if (tag in file.readline()):
        return True
    return False