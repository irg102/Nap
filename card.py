import enum
from functools import total_ordering

@total_ordering
class OrderedEnum (enum.Enum):

	def __str__(self):
		return "%s" % (self._name_)

	def __lt__(self, other):
		if isinstance(other, type(self)):
			return self.value < other.value
		return NotImplemented

class Card (object):

	""" Standard playing card.

	Creates a playing card with hidden suit and rank attributes.
	"""
    
	RANK = OrderedEnum('Rank', ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'])
	SUIT = OrderedEnum('Suit', ['Hearts', 'Clubs', 'Diamonds', 'Spades'])
	
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
		return "{:s} of {:s}".format(self._rank, self._suit)

	
