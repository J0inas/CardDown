import sys
from block_parser import get_cards

if len(sys.argv) > 1:
    cards = get_cards(str(sys.argv[1]))
else:
    print("Enter file to search: ")
    cards = get_cards(str(input()))

for card in cards:
    print("\n".join(card))
