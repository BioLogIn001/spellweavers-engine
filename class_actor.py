class Actor:
	'''Base class for game actor (a participant or a monster).
	Contains data common to all actors.
	'''

	def __init__(self, actorType, name, HP, maxHP):

		self.type = actorType # { 1: 'Player', 2: 'Monster' }
		self.name = name
		self.HP = HP
		self.maxHP = maxHP
		self.isAlive = 1

	def setIDs(self, ID):
		''' Set actor ID.

		Arguments:
		ID - integer, ID of actor.
		'''

		self.ID = ID

	def decreaseHP(self, diff):
		''' Decrease actor's HP by diff amount

		Arguments:
		diff - integer, amoun of HP to be substracted.
		'''

		self.HP -= diff

	def increaseHP(self, diff):
		''' Increase actor's HP by diff amount, respecting maxHP.

		Arguments:
		diff - integer, amoun of HP to be added.
		'''

		self.HP += diff
		if self.HP > self.maxHP:
			self.HP = self.maxHP
