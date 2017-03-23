from card import *
import random

class Deck (object):

	def __init__(self, size):
		self._size = size
		self._cards = []

	def clearDeck(self):
		while len(self._cards) > 0:
			self._cards.pop()

	def populate(self):
		fullDeck = len(Card.RANK)
		indexPosition = fullDeck - self._size
		for i in range(indexPosition, fullDeck):
			for suit in Card.SUIT:
				card = Card(Card.RANK[i], suit)
				self._cards.append(card)

	def shuffle(self):
		random.shuffle(self._cards)

	def deal(self):
		card = self._cards.pop()
		return card

	def newRound(self):
		self.clearDeck()
		self.populate()
		self.shuffle()

