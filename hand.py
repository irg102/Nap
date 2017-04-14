from card import *

def keyFunction(playingCard):
	return playingCard.suit, playingCard.rank

class Hand (object):
	""" A hand of playing cards. """

	def __init__(self):
		""" Creates an empty list (hand) of playing cards. """
		self._hand = []

	def sortCards(self):
		""" Orders cards in Hand according to Card.RANK and Card.SUIT. """
		self._hand.sort(key=keyFunction, reverse=True)

	def addCard(self, card):
		""" Appends the given card to the hand.

		Args:
			card (Card): A playing card from the created type in Card.py.
		"""
		self._hand.append(card)

	def removeCard(self, index):
		""" Pops and returns the card from the given index position of the hand.

		Args:
			index (int): position of the card to be removed and returned.
		"""
		card = self._hand.pop(index)
		return card

	def clearCards(self):
		""" Removes all cards from the hand. """
		while len(self._hand) > 0:
			self._hand.pop()

	def __str__(self):
		handString = ""
		for card in self._hand:
			handString += str(card)
			handString += "  "
		return handString	
