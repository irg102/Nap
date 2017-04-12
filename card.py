class Card (object):

	""" Standard playing card.

	Creates a playing card with hidden suit and rank attributes.
	"""
    
	RANK = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
	SUIT = ('H', 'C', 'D', 'S')
	
	def __init__(self, rank, suit):

		""" Initializes the hidden rank and suit attributes.

		Args:
			rank (RANK): A string of type Card.RANK is expected to initialize card to rank.
			suit (SUIT): A string of type Card.SUIT is expected to initialize card to suit. 
		
		"""
		self._rank = rank
		self._suit = suit

	@property
	def rank(self):
		""" Returns read-only rank variable. """
		return self._rank

	@property
	def suit(self):
		""" Returns read-only suit variable. """
		return self._suit

	def __str__(self):
		""" Returns a unique string for each card. """
		return self._rank + self._suit

	
