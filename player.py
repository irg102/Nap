from hand import *

class Player (object):
	""" Creates a generic player to participate in a card game.

	Player has a name, a hand of cards and a value of money.

	Attributes:
		_playerName (string): Name of player
		_playerHand (Hand): Hand of cards as defined in hand.py
		_playerMoney (float): Amount of money won/lost by player.
	"""
	def __init__(self, name):
		""" Sets defaults for a newly created player and sets name.

		Args:
			name (string): name to be set for player.
		"""
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
		""" Append card to the players hand.

		Args:
			card (Card): Playing card as defined in card.py.
		"""
		self._playerHand.addCard(card)

	def sortPlayerHand(self):
		""" Invoke Hand.sortCards to make playerHand member a sorted list. """
		self._playerHand.sortCards()

