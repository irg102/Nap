from deck import *
from player import *

class Game (object):
	""" Nap game object.

	Stores game state and handles game logic and rules.

	Attributes:
		_players (list): A list of the players in the game.
		_kitty (float): Value of money currently in kitty.
		_deck (Deck): A deck of playing cards as defined in deck.py.
		_floater (Card): The floater card for the current round of the game.
	"""
	def __init__(self, playerList):
		""" Sets the defaults for starting a new game.

		Args:
			playerList (list of strings): Contains the strings of the names of the players to be used when creating 
											the players for the game.
		"""
		self._players = []
		for player in playerList:
			self._players.append(Player(player))
		self._kitty = 0
		self._deck = Deck(5)
		self._floater = []

	def playGame(self):
		""" Handles game logic for playing the game. """
		self._deck.newRound()
		self._floater.append(self._deck.deal())
		for i in range(5):
			for player in self._players:
				player.receiveCard(self._deck.deal())
		for person in self._players:
			person.sortPlayerHand()
			print(person)
		floater = "The floater is: "
		floater += str(self._floater[0])
		print(floater)
			
