from hand import *

class Player (object):

	def __init__(self, name):
		self._playerName = name
		self._playerHand = Hand()
		self._playerMoney = 0
		
	def __str__(self):
		playerString = "Player: "
		playerString += self._playerName
		playerString += "  Money: "
		playerString += str(self._playerMoney)
		playerString += "  Hand: "
		playerString += str(self._playerHand)
		return playerString

	def receiveCard(self, card):
		self._playerHand.addCard(card)

