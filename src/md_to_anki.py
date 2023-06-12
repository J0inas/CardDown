import random
import genanki
from tags import *
from learningcards import *
from md_to_html import card_content_to_html

# Generates anki-stacks from md-files
def md_to_anki(
    file_name : list, 
    deck_name : str,
    ):
    """
    Creates an anki-deck from the given md-file.
    
    returns: message that anki-deck was created
    """
    # currently only for one file
    md_cards = load_one_file(file_name)
    flashcards = parse_md_cards(md_cards)
    
    anki_deck = genanki.Deck(id_generator(),deck_name)
    
    for card in flashcards:
        note = anki_note(card)
        anki_deck.add_note(note)
    
    card_package = genanki.Package(anki_deck)

    card_package.write_to_file(deck_name + '.apkg')
    print("Writing file was succesful!")

def anki_note(card : LearningCard):
    """
    Generates anki-notes from the given Learningcard.
    
    returns: single anki-flashcard
    """
    model = genanki.BASIC_MODEL
    front = card_content_to_html(card.get_front_content())
    back = card_content_to_html(card.get_back_content())
    fields = [front, back]

    note = genanki.Note(model,fields)
    
    return note

def id_generator():
    """
    Creates a random id for the model- and deck-identification.
    
    returns: random number that can be used as an id
    """
    return random.randrange(1 << 30, 1 << 31)

# test
md_to_anki("test_card.md", "test")