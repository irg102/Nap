from deck import *
from player import *

class Game (object):

	def __init__(self, playerList):
		self._players = []
		for player in playerList:
			self._players.append(Player(player))
		self._kitty = 0
		self._deck = Deck(5)
		self._floater = []

	def playGame(self):
		self._deck.newRound()
		self._floater.append(self._deck.deal())
		for i in range(5):
			for player in self._players:
				player.receiveCard(self._deck.deal())
		for person in self._players:
		 	print(person)
		floater = "The floater is: "
		floater += str(self._floater[0])
		print(floater)
			
