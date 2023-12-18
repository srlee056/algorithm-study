import sys

n = int(sys.stdin.readline())
cards = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
count_card = map(int, sys.stdin.readline().split())

cards_by_number = {}

for card in cards:
    cards_by_number[card] = cards_by_number.get(card, 0) + 1

the_number_of_cards = [
    cards_by_number[c] if c in cards_by_number else 0 for c in count_card
]

print(" ".join(map(str, the_number_of_cards)))
