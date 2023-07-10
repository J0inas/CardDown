from md_to_html import card_content_to_html
from file_loader import is_valid_cardfile, get_valid_cardfiles_from_dir
from cardparser import simple_parser
from learningcards import LearningCard
import os
import genanki
import random


def md_to_anki(input: str, deck_tag: str, deck_name: str):
    """
    Creates an anki-deck from the given md-file.
    :input: single file or path
    :deck_name: name of the tag that is given after the start_tag in the file 
    - also the name of the Anki-Deck

    returns: message that anki-deck was created
    """
    # directory-converter
    if os.path.isdir(input) is True:
        path_to_anki(input, deck_tag, deck_name)
        return
    # single-file-converter
    file_to_anki(input, deck_tag, deck_name)
    return


def file_to_anki(file_name: str, deck_tag: str, deck_name: str):
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
    flashcards = simple_parser.get_cards_from_file(card_filename)
    # generating the anki file
    anki_deck = genanki.Deck(id_generator(), deck_name)
    for card in flashcards:
        note = anki_note(card)
        anki_deck.add_note(note)
    card_package = genanki.Package(anki_deck)
    card_package.write_to_file(deck_name + ".apkg")
    print("Writing file was successful!")


def path_to_anki(path: str, deck_tag: str, deck_name: str):
    """
    :path: str of the path where the md-files are located
    :deck_tag: name of the tag that is given after the start_tag in the file
    :deck_name: name of the Anki-Deck
    """

    filenames = get_valid_cardfiles_from_dir(path, deck_tag)

    learningcards = []
    media_list = get_media_from_path(path)
    for card in filenames:
        learningcards.append(simple_parser.get_cards_from_file(card))
        print(learningcards)

    anki_deck = genanki.Deck(id_generator(), deck_name)

    for cards in learningcards:
        note_list = anki_note_from_list(cards)
        for note in note_list:
            anki_deck.add_note(note)

    card_package = genanki.Package(anki_deck)
    card_package.media_files = media_list
    card_package.write_to_file(deck_name + ".apkg")
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


# test
# md_to_anki("/Users/joinas/Documents/Uni/Software-Engineering/Markdown-Anki/Markdown-LearningCards/testDir", "#PresentTest", "PresentTest")

md_to_anki("/Users/joinas/Documents/Obsidian/Life","#AlgoGeo","AlgoGeo")

# md_to_anki("testDir", "#Mango", "MangoTest")
# md_to_anki("./basicCardTest.md", "#Mango", "MangoTest")
