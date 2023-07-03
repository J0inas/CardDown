import random
import genanki
from tags import *
from learningcards import *
from file_loader import *
from md_to_html import card_content_to_html


def md_to_anki(input: str, deck_tag: str, deck_name: str):
    """
    Creates an anki-deck from the given md-file.
    :input: single file or path
    :deck_name: name of the tag that is given after the start_tag in the file - also the name of the Anki-Deck

    returns: message that anki-deck was created
    """
    # directory-converter
    if os.path.isdir(input) == True:
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
    # file-converter
    md_cards = load_one_file(file_name, deck_tag)
    # empty file has no need to be converted
    if md_cards == "":
        return
    flashcards = parse_md_cards(md_cards)
    # generating the anki file
    anki_deck = genanki.Deck(id_generator(), deck_name)
    for card in flashcards:
        note = anki_note(card)
        anki_deck.add_note(note)
    card_package = genanki.Package(anki_deck)
    card_package.write_to_file(deck_name + ".apkg")
    print("Writing file was succesful!")


def path_to_anki(path: str, deck_tag: str, deck_name: str):
    """
    :path: str of the path where the md-files are located
    :deck_tag: name of the tag that is given after the start_tag in the file
    :deck_name: name of the Anki-Deck
    """
    cardlist = load_multiple_files(path, deck_tag)
    print(cardlist)
    md_cards = []
    print(cardlist)
    media_list = get_media_from_path(path)
    for card in cardlist:
        md_cards.append(parse_md_cards(card))
        print(md_cards)

    anki_deck = genanki.Deck(id_generator(), deck_name)

    anki_deck = genanki.Deck(id_generator(),deck_name)
    
    for card in md_cards:
        note_list = anki_note_from_list(card)
        for note in note_list:
            anki_deck.add_note(note)

    card_package = genanki.Package(anki_deck)
    card_package.media_files = media_list
    card_package.write_to_file(deck_name + ".apkg")
    print("Writing file was succesful!")


def anki_note(card: LearningCard):
    """
    Generates anki-notes from the given Learningcard.
    :card: A converted MarkDown-Card
    returns: single anki-flashcard
    """
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


def get_media_from_path(path : str)-> list:
    """
    Returns every media file from the path as a list.
    Media is a png, jpeg, mp3, gif or mp4.
    """
    os.chdir(path) 
    files = os.listdir()
    media_files = []
    for x in files:
        if x[-4:] == ".png" or  x[-4:] == ".mp3" or  x[-4:] == ".gif" or  x[-4:] == ".mp4":
            media_files.append(x)
        elif x[-5:] == ".jpeg":
            media_files.append(x)
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
md_to_anki("/Users/joinas/Documents/Uni/Software-Engineering/Markdown-Anki/Markdown-LearningCards", "#AlgoGeo", "AlgoGeoTest")

# md_to_anki("/Users/joinas/Documents/Obsidian/Life","#AlgoGeo","AlgoGeoTest")