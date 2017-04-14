from card import *
import random

class Deck (object):
	""" A standard deck of cards of variable size.

	Contains a list of playing cards (the deck) and is aware of its size so reduced decks may be used.
	"""
	def __init__(self, size):
		""" Sets the deck size for the game and creates an empty list (deck) of cards.

		Args:
			size (int): Number of ranks in a deck. For full deck size==13. For tens to aces size==5. Etc...
		"""
		self._size = size
		self._cards = []

	def _clearDeck(self):
		while len(self._cards) > 0:
			self._cards.pop()

	def _populate(self):
		fullDeck = len(Card.RANK) + 1
		indexPosition = fullDeck - self._size
		for i in range(indexPosition, fullDeck):
			for suit in Card.SUIT:
				card = Card(Card.RANK(i), suit)
				self._cards.append(card)

	def _shuffle(self):
		random.shuffle(self._cards)

	def deal(self):
		""" Removes a card from the deck and returns it. """
		card = self._cards.pop()
		return card

	def newRound(self):
		""" Readies a new deck of cards to play another round of the game. """
		self._clearDeck()
		self._populate()
		self._shuffle()

