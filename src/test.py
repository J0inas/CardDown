import sys
from cardparser import block_parser, simple_parser

from md_to_anki import md_to_anki

# get_cards = block_parser.get_cards_from_file
#
# if len(sys.argv) > 1:
#    cards = get_cards(str(sys.argv[1]))
# else:
#    print("Enter file to search: ")
#    cards = get_cards(str(input()))
#
# for card in cards:
#    print(str(card))
#    print("== = ==")


if len(sys.argv) > 1:
    cards = md_to_anki(str(sys.argv[1]), "#Test", "Testt")
else:
    print("Enter file to search: ")
    cards = md_to_anki(input(), "#Test", "Testt")
