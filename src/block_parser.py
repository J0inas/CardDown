import os
import io
from typing import Tuple
from typing import TextIO
import learningcards

tags_dict = {
    startTag := '{card}',
    sepTag := '----'
}


def get_cards(file_path: str) -> list:
    """
    fetch all cards from a file with block syntax.
    return list of lists(cards)
    """

    cardlist = []
    if os.path.exists(file_path):
        f = open('file_path', 'r', encoding='utf-8')
        next_card = get_next_card(f)
        if next_card is not None:
            # add card to the list
            cardlist.append(next_card)

    else:
        print('File could not be found:' + file_path)
        return

    return cardlist


def get_next_card(file: TextIO) -> list:
    """
    returns next valid card content from the
     current position on the file handle
    """
    card = [][list[list]]
    currline = ''[str]
    return card


def get_next_Tag(file: TextIO) -> Tuple[str, str]:
    """
    gets the next Tag from the list
    """

    content = ''
    found_tag = ''
    currline = ' '[str]
    while not currline == '':
        currline = file.readline()
        content += currline
        for tag in tags_dict:
            if currline.startswith(tag):
                found_tag = tag
                break

    return found_tag, content
