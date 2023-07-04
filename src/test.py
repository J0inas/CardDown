import sys
from cardparser import block_parser, simple_parser


get_cards = block_parser.get_cards_from_file

if len(sys.argv) > 1:
    cards = get_cards(str(sys.argv[1]))
else:
    print("Enter file to search: ")
    cards = get_cards(str(input()))

for card in cards:
    print(str(card))
    print("== = ==")

# get_cards = simple_parser.get_cards_from_file
##
##
# if len(sys.argv) > 1:
# cards = get_cards(str(sys.argv[1]))
# else:
# print("Enter file to search: ")
# cards = get_cards(str(input()))
##
# print("test")
# for card in cards:
# print(str(card))
# print("== = ==")
