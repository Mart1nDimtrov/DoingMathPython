'''
#4: Shuffling a Deck of Cards
Consider a standard deck of 52 playing cards. Your challenge here is to 
write a program to simulate the shuffling of this deck.
'''

import random

class Card: 
	def __init__(self, suit, rank): 
		self.suit = suit 
		self.rank = rank 


ten_spades = Card(10, 'spades')
six_clubs = Card(6, 'clubs')
jack_spades = Card('jack', 'spades')
nine_spades = Card(9, 'spades')

cards = [ten_spades, six_clubs, jack_spades, nine_spades]
random.shuffle(cards)
for card in cards:
	print("{0} of {1}".format(card.suit, card.rank))