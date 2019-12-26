import os
import copy as cp

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")


def cut(n, deck):
	cut_cards = deck[0:n]
	return deck[n:]+cut_cards


def increment(n, deck):
	placed_cards = 0
	deck_size = len(deck)
	empty_deck = [-1]*deck_size
	index = 0
	while placed_cards < deck_size:
		if empty_deck[index] == -1:
			empty_deck[index] = deck[placed_cards]
			#print(empty_deck)
			placed_cards+=1
		index = (index+n)%deck_size
		

	return empty_deck


def negative_cut(n, deck):
	cut_cards = deck[n:] #n is negative so cut_cards is the bottom of the deck
	return cut_cards+deck[0:n]

def stack(deck):
	deck.reverse()
	return deck

deck = [x for x in range(10007)]
#print(deck)
for line in lines:
	#print(line)
	text = line.split()
	if text[0] == "cut":
		n = int(text[-1])
		if n<0:
			deck = negative_cut(n, deck)
		else:
			deck = cut(n, deck)

	else:	#text is deal
		if text[-1] == "stack":
			deck = stack(deck)
		else:
			deck = increment(int(text[-1]), deck)

jump_map = dict()
for i, card in enumerate(deck):#Create a map for how the different will not work at all
	jump_map[card] = i

print(jump_map[2])




