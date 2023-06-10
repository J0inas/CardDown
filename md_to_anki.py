import random
import genanki
from tags import *
from learningcards import *

# Generates anki-stacks from md-files
def md_to_anki(
    flashcards : list,  # ToDo: create as a new type LearningCardList 
    deck_name : str,
    ):
    anki_deck = genanki.Deck(id_generator(),deck_name) # Optional ToDo: give a description for the deck
    
    for i in range(len(flashcards)):
        note = generate_anki_cards(flashcards[i])
        anki_deck.add_note()
    
    card_package = genanki.Package(anki_deck)
    # ToDo adding Mediafiles - genanki.media_files = ['sound.mp3', 'images/image.jpg']
    card_package.write_to_file(deck_name + '.apkg')

def generate_anki_cards(card : LearningCard):
    """
    Generates anki-notes from the given Learningcard.
    """
    model = genanki.BASIC_MODEL
    pass

def id_generator():
    """
    Creates a random id for the model- and deck-identification.
    
    returns: random number that can be used as an id
    """
    return random.randrange(1 << 30, 1 << 31)