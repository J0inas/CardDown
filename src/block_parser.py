import os
from typing import Tuple
from typing import TextIO
from utility import text_file_peek_line

tags_dict = {
    'startTag': '{card}',
    'sepTag': '----'
}

valid_tag_list = tags_dict.values()


def get_cards(file_path: str) -> list:
    """
    fetch all cards from a file with block syntax.
    return list of lists(cards)
    """

    cardlist = []
    if os.path.exists(file_path):
        f = open(file_path, 'r', encoding='utf-8')

        # until end of file is reached try to fetch cards
        while text_file_peek_line(f) != '':
            # get a card from the current file position
            next_card = get_next_card(f)
            if next_card is not None:
                # add card to the list
                cardlist.append(next_card)
    else:
        print('File could not be found:' + file_path)

    return cardlist


def get_next_card(file: TextIO) -> list:
    """
    returns next valid card content from the
     current position on the file handle
    """
    card = [list[list]]
    card = [[], [], []]

    # find start, get tag from tuple for later usage
    card[0] = get_next_Tag(file, tags_dict['startTag'])[0]

    # attempt to find card separator
    tag, content = get_next_Tags(file, valid_tag_list)

    print('Content:' + content)

    print('Tag:' + str(tag))

    if tag == tags_dict['sepTag']:
        card[1] = content
    else:
        # card is not valid
        print(str(card) + content + "is not a valid card. Missing card separator!")
        # reset progress after tag was not correctly found
        reset_position_by_tag(tag, file)
        return None

    # attempt to find card end/2nd separator

    tag, content = get_next_Tags(file, valid_tag_list)

    if tag == tags_dict['sepTag'] or tag == tags_dict['startTag']:
        card[2] = content
    else:
        # card is not valid
        print(str(card) + "is not a valid card. Missing correct card ending!")
        # reset progress after tag was not correctly found
        reset_position_by_tag(tag, file)
        return None

    return card


def get_next_Tag(file: TextIO, searchTag: str) -> Tuple[str, str]:
    """
    allows the passing of just a string wich will 
    then be put in list, so it can be passed to get_next_Tags
    """
    tag_as_list = [searchTag]
    return get_next_Tags(file, tag_as_list)


def get_next_Tags(file: TextIO, validTags: list) -> Tuple[str, str]:
    """
    gets the next Tag from the list
    """
    content = ''
    found_tag = ''
    currline = 'something thats not empty'
    # read till EOF
    while not currline == '':
        currline = text_file_peek_line(file)
        print(validTags)
        print(currline)
        for tag in validTags:
            print('CurrTag:' + str(tag))
            if currline.startswith(tag):
                found_tag = tag
                break

        file.readline()
        if found_tag != '':
            break

        content += currline
    return found_tag, content


def reset_position_by_tag(tag: str, file: TextIO):
    """
    reset the file pointer to the position before the tag was read
    """
    # dont reset if empty line was found
    if (tag == ''):
        pass
    else:
        file.seek(file.tell() - (len(tag)+1), 0)
