from deck import *
from player import *

class Game (object):

	def __init__(self, playerList):
		self._players = []
		for player in playerList:
			self._players.append(Player(player))
		self._kitty = 0
		self._deck = Deck(5)

	def playGame(self):
		self._deck.newRound()
		for i in range(5):
			for player in self._players:
				player.receiveCard(self._deck.deal())
		for person in self._players:
		 	print(person)

			
