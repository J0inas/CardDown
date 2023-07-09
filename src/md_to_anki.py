from md_to_html import card_content_to_html
from file_loader import is_valid_cardfile, get_valid_cardfiles_from_dir
from cardparser import simple_parser
from learningcards import LearningCard
import os
import genanki
import random


def md_to_anki(path: str, start_tag: str, deck_tag: str, deck_name: str, parser=simple_parser, media_path=None, save_path=None):
    """
    Creates an anki-deck from the given md-file.
    :input: single file or path
    :deck_name: name of the tag that is given after the start_tag in the file 
    - also the name of the Anki-Deck

    returns: message that anki-deck was created
    """

    # make sure we are working with an absolute path
    path = os.path.abspath(path)

    if not media_path:
        if not os.path.isdir(media_path):
            media_path = path

    if not save_path:
        save_path = path

    # directory-converter

    if os.path.isdir(path) is True:
        path_to_anki(path, start_tag, deck_tag,
                     deck_name, media_path, parser, save_path)
        return

    # single-file-converter
    file_to_anki(path, deck_tag, deck_name, parser, save_path)
    return


def file_to_anki(file_name: str, deck_tag: str, deck_name: str, parser, save_path: str):
    """
    :file_name: str of file that should be converted
    :deck_tag: name of the tag that is given after the start_tag in the file
    :deck_name: name of the Anki-Deck
    """
    # check file for valid card file
    card_filename = is_valid_cardfile(file_name, deck_tag)

    # empty/unvalid file has no need to be converted
    if card_filename is None:
        return
    flashcards = parser.get_cards_from_file(card_filename)
    # generating the anki file
    anki_deck = genanki.Deck(id_generator(), deck_name)
    for card in flashcards:
        note = anki_note(card)
        anki_deck.add_note(note)
    card_package = genanki.Package(anki_deck)
    card_package.write_to_file(save_path + deck_name + ".apkg")
    print("Writing file was successful!")
    # TODO move deck generation/writing to file from notelist to separate function


def path_to_anki(path: str, start_tag: str, deck_tag: str, deck_name: str,  media_path, parser, save_path: str):
    """
    :path: str of the path where the md-files are located
    :deck_tag: name of the tag that is given after the start_tag in the file
    :deck_name: name of the Anki-Deck
    """

    filenames = get_valid_cardfiles_from_dir(path, start_tag, deck_tag)

    learningcards = []

    media_list = get_media_from_path(media_path)

    for card in filenames:
        learningcards.append(parser.get_cards_from_file(card))
        print(learningcards)

    anki_deck = genanki.Deck(id_generator(), deck_name)

    for cards in learningcards:
        note_list = anki_note_from_list(cards)
        for note in note_list:
            anki_deck.add_note(note)

    card_package = genanki.Package(anki_deck)
    card_package.media_files = media_list
    save_path = os.path.join(save_path+deck_name+".apkg")
    print(save_path)
    card_package.write_to_file(save_path + deck_name + ".apkg")
    print("Writing file was successful!")


def anki_note(card: LearningCard):
    """
    Generates anki-notes from the given Learningcard.
    :card: A converted MarkDown-Card
    returns: single anki-flashcard
    """
    print(card.get_front_content())
    model = genanki.BASIC_MODEL
    front = card_content_to_html(card.get_front_content())
    back = card_content_to_html(card.get_back_content())
    fields = [front, back]

    note = genanki.Note(model, fields)

    return note


def anki_note_from_list(card_list: list):
    """
    Generates anki-notes from the given Learningcard.
    :card_list: List of LearningCards
    returns: single anki-flashcard
    """
    note_list = []
    for x in card_list:
        print(x.get_front_content())
        model = genanki.BASIC_MODEL
        front = card_content_to_html(x.get_front_content())
        back = card_content_to_html(x.get_back_content())
        fields = [front, back]
        note_list.append(genanki.Note(model, fields))

    return note_list


def get_media_from_path(path: str) -> list:
    """
    Returns every media file from the path as a list.
    Media is a png, jpeg, mp3, gif or mp4.
    """
    files = os.listdir()
    media_files = []
    supportedMediaTypes = [".png", "mp3", ".gif", ".mp4", ".jpeg"]
    for filename in files:
        for type in supportedMediaTypes:
            if filename.endswith(type):
                media_files.append(filename)
            else:
                continue
    return media_files


def id_generator():
    """
    Creates a random id for the model- and deck-identification.

    returns: random number that can be used as an id
    """
    return random.randrange(1 << 30, 1 << 31)
