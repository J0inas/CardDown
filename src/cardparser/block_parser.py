import os
from typing import Tuple
from typing import TextIO
from utility import text_file_peek_line
from learningcards import LearningCard, SimpleCard, QuestionCard


block_tag_dict = {"startTag": "{card}", "sepTag": "----"}

valid_tag_list = block_tag_dict.values()


def get_cards_from_file(file_path: str) -> list:
    """
    fetch all cards from a file with block syntax.
    return list of learncards
    """

    cardlist = []
    if os.path.exists(file_path):
        f = open(file_path, "r", encoding="utf-8")

        # until end of file is reached try to fetch cards
        while text_file_peek_line(f) != "":
            # get a card from the current file position
            next_card = __get_next_card(f)
            if next_card.is_valid():
                # add card to the list
                cardlist.append(next_card)
    else:
        print("File could not be found:" + file_path)

    return cardlist


def __get_next_card(file: TextIO) -> LearningCard:
    """
    returns next valid card content from the
     current position on the file handle
    """

    # find start, get tag from tuple for later usage
    tag = __get_next_Tag(file, block_tag_dict["startTag"])[0]
    card = get_type_from_cardtag(tag)

    # attempt to find card separator
    tag, content = __get_next_Tags(file, valid_tag_list)

    print("Content:" + content)

    print("Tag:" + str(tag))

    if tag == block_tag_dict["sepTag"]:
        card.set_front_content(content)
    else:
        # card is not valid
        print(str(card) + content +
              "is not a valid card. Missing card separator!")
        # reset progress after tag was not correctly found
        __reset_position_by_tag(tag, file)
        return None

    # attempt to find card end/2nd separator

    tag, content = __get_next_Tags(file, valid_tag_list)

    if tag == block_tag_dict["sepTag"] or tag == block_tag_dict["startTag"]:
        card.set_back_content(content)

    else:
        # card is not valid
        print(str(card) + "is not a valid card. Missing correct card ending!")
        # reset progress after tag was not correctly found
        __reset_position_by_tag(tag, file)
        return None

    return card


def __get_next_Tag(file: TextIO, searchTag: str) -> Tuple[str, str]:
    """
    allows the passing of just a string which will
    then be put in list, so it can be passed to get_next_Tags
    """
    tag_as_list = [searchTag]
    return __get_next_Tags(file, tag_as_list)


def __get_next_Tags(file: TextIO, validTags: list) -> Tuple[str, str]:
    """
    gets the next Tag from the list
    """
    content = ""
    found_tag = ""
    currline = "something thats not empty"
    # read till EOF
    while not currline == "":
        currline = text_file_peek_line(file)
        print(validTags)
        print(currline)
        for tag in validTags:
            print("CurrTag:" + str(tag))
            if currline.startswith(tag):
                found_tag = tag
                break

        file.readline()
        if found_tag != "":
            break

        content += currline
    return found_tag, content


def __reset_position_by_tag(tag: str, file: TextIO):
    """
    reset the file pointer to the position before the tag was read
    """
    # dont reset if empty line was found
    if tag == "":
        pass
    else:
        file.seek(file.tell() - (len(tag) + 1), 0)


def get_type_from_cardtag(card_tag: str) -> LearningCard:
    """
    currently does not have much functionality.
    can provide further value later for evaluating the card options
    in the start tag
    to allow for creation of different card types
    """

    return SimpleCard()
