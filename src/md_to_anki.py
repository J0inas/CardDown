import random
import genanki
from tags import *
from learningcards import *

# Generates anki-stacks from md-files
def md_to_anki(
    flashcards : list,  # ToDo: create as a new type LearningCardList 
    deck_name : str,
    ):
    """
    Creates an anki-deck from the given flashcard-list-
    
    returns: message that anki-deck was created
    """
    anki_deck = genanki.Deck(id_generator(),deck_name)
    
    for i in range(len(flashcards)):
        note = generate_anki_cards(flashcards[i])
        anki_deck.add_note(note)
    
    card_package = genanki.Package(anki_deck)

    card_package.write_to_file(deck_name + '.apkg')

def generate_anki_cards(card : LearningCard):
    """
    Generates anki-notes from the given Learningcard.
    """
    model = genanki.BASIC_MODEL
    
    
    
    fields = [card.get_front_content, card.get_back_content]
    
    
    note = genanki.Note(model,fields)
    
    return note

def id_generator():
    """
    Creates a random id for the model- and deck-identification.
    
    returns: random number that can be used as an id
    """
    return random.randrange(1 << 30, 1 << 31)

# test
md_cards = parse_md_cards("test_card.md")
md_to_anki(md_cards, "test")