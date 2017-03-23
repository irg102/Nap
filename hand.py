from card import *

class Hand (object):

	def __init__(self):
		self._hand = []

	def addCard(self, card):
		self._hand.append(card)

	def removeCard(self, index):
		card = self._hand.pop(index)
		return card

	def clearCards(self):
		while len(self._hand) > 0:
			self._hand.pop()

	def __str__(self):
		handString = ""
		for card in self._hand:
			handString += str(card)
			handString += "  "
		return handString	
