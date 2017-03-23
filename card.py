class Card (object):
    
	RANK = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
	SUIT = ('H', 'C', 'D', 'S')
	
	def __init__(self, rank, suit):
		self._rank = rank
		self._suit = suit

	def getRank(self):
		return self._rank

	def getSuit(self):
		return self._suit

	def __str__(self):
		return self._rank + self._suit

	
