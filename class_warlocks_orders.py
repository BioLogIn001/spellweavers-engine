import json


class WarlocksOrder:
	''' Order class for Warlocks.
	Contains all possible / accepted types of orders from a participant for a turn.
	'''

	def __init__(self):

		# Order belongs to a specific match and a specific turn
		self.matchID = 0,
		self.turnNum = 0,
		# Order comes from a specific participant (to be improved in the web version)
		self.participantID = 0,

		# Str(1) - gestures for LH and RH
		self.gestureLH = '',
		self.gestureRH = '',
		# Integer spell IDs for LH and RH
		# Used to select a spell cast for overlapping patterns like WPP and P
		self.orderSpellLH = -1,
		self.orderSpellRH = -1,
		# Integer target IDs for LH and RH
		self.orderTargetLH = -1,
		self.orderTargetRH = -1,

		# Hand ID(s) to be paralyzed
		self.paralyzeOrders = {}
		# Hand ID(s) to be charmed, and respective gestures
		self.charmOrders = {}

		# Monster ID(s) and their respective targets
		self.attackOrders = {}

		# Special order - store spell
		self.delaySpell = 0,
		# Special order - fire stored spell
		self.castDelayedSpell = 0,
		# Special order - make spell permanent
		self.makeSpellPermanent = 0,
		# Special order - commit suicide (if affected by perm mindspell)
		self.commitSuicide = 0,


class WarlocksOrders:
	''' Orders class for Warlocks.
	Contains a list of orders and methods that parse them.
	'''

	def __init__(self):

		self.orders = []

	def setFilename(self, filename):
		''' Set filename to import orders from. Placeholder.

		Arguments:
		filename -- string, name of a JSON file with Orders
		'''

		self.filename = filename

	def loadOrdersFromFile(self, filename):
		''' Placeholder orders load from JSON file for console engine implementation

		Arguments:
		filename -- string, name of a JSON file with Orders
		'''

		data = None
		with open(filename, 'r') as f:
			data = json.load(f)
		return data

	def getTurnOrders(self, matchData, matchSpellBook):
		''' Get and validate orders for the turn

		Arguments:
		matchData -- object, MatchData-inherited
		matchSpellBook -- object, SpellBook-inherited
		'''

		validParticipantIDs = matchData.getListOfParticipantsIDsActiveThisTurn()

		data = self.loadOrdersFromFile(self.filename)		
		self.validateOrders(data, matchData.matchID, matchData.currentTurn, 
									matchData.handIDOffset, validParticipantIDs, 
									matchSpellBook.validGestures, matchSpellBook.validSpellIDs)

	def checkMissingOrders(self, matchData):
		''' Check for missing orders for the turn using submitted active participants list.

		Arguments:
		matchData -- object, MatchData-inherited

		Returns:
		A list of IDs of participants that have not submitted their orders yet.
		'''

		validParticipantIDs = matchData.getListOfParticipantsIDsActiveThisTurn()
		missingOrders = []
		for p in validParticipantIDs:
			order = self.searchOrders(matchData.matchID, matchData.currentTurn, p)
			if order is not None:
				pass
			else:
				missingOrders.append(p)	
		return missingOrders

	def searchOrders(self, matchID, turnNum, participantID):
		''' Search for Orders for the specific match - turn - participant.

		Arguments:
		matchID -- integer, match ID
		turnNum -- integer, turn number
		participantID -- integer, ID of participant

		Returns:
		Order object if found, None otherwise
		'''

		for order in self.orders:
			if ((order.matchID == matchID) 
					and (order.turnNum == turnNum)
					and (order.participantID == participantID)):
				return order
		return None

	def validateOrders(self, data, matchID, turnNum, handOffset, validParticipantIDs, validGestures, validSpellIDs):
		''' Validate incoming orders.

		data -- string, raw JSON data
		matchID -- integer, match ID
		turnNum -- integer, turn number
		handOffset -- integer, offset to calculate hand IDs
		validParticipantIDs -- a list of integer IDs of participants that are expected to act this turn
		validGestures -- a list of gestures (str(1)) that are valid for selected SpellBook
		validSpellIDs -- a list of spell IDs (integer) that are valid for selected SpellBook
		'''

		for o in data:

			# Determine match ID, turn number, and participant ID from Orders
			# and check them against current match - turn - participants.
			if ('matchID' not in data[o]):
				continue
			else: 
				matchIDt = int(data[o]['matchID'])
			if ('turnNum' not in data[o]):
				continue
			else: 
				turnNumt = int(data[o]['turnNum'])
			if ('participantID' not in data[o]):
				continue
			else: 
				participantIDt = int(data[o]['participantID'])

			if (matchIDt != matchID) or (turnNumt != turnNum) or (participantIDt not in validParticipantIDs):
				continue

			# If we expect an order from this participant on this turn of this match
			# create order instance
			newOrder = WarlocksOrder()
			newOrder.matchID = matchIDt
			newOrder.turnNum = turnNumt
			newOrder.participantID = participantIDt
			
			# Get and validate LH and RH gestures
			if ('gestureLH' not in data[o]) or (data[o]['gestureLH'][0] not in validGestures):
				newOrder.gestureLH = '-'
			else:
				newOrder.gestureLH = data[o]['gestureLH'][0]
			if ('gestureRH' not in data[o]) or (data[o]['gestureRH'][0] not in validGestures):
				newOrder.gestureRH = '-'
			else:
				newOrder.gestureRH = data[o]['gestureRH'][0]

			# Get and validate requested LH and RH spell IDs
			if ('orderSpellLH' not in data[o]) or (int(data[o]['orderSpellLH']) not in validSpellIDs):
				newOrder.orderSpellLH = -1
			else:
				newOrder.orderSpellLH = int(data[o]['orderSpellRH'])
			if ('orderSpellRH' not in data[o]) or (int(data[o]['orderSpellRH']) not in validSpellIDs):
				newOrder.orderSpellRH = -1
			else:
				newOrder.orderSpellRH = int(data[o]['orderSpellRH'])

			# Get and validate requested LH and RH targets
			if ('orderTargetLH' not in data[o]):
				newOrder.orderTargetLH = -1
			else:
				newOrder.orderTargetLH = int(data[o]['orderTargetLH'])
			if ('orderTargetRH' not in data[o]):
				newOrder.orderTargetRH = -1
			else:
				newOrder.orderTargetRH = int(data[o]['orderTargetRH'])

			# Get and validate special action - delay spell
			if ('delaySpell' not in data[o]):
				newOrder.delaySpell = 0
			else:
				newOrder.delaySpell = int(data[o]['delaySpell'])

			# Get and validate special action - fire delayed spell
			if ('castDelayedSpell' not in data[o]) or (int(data[o]['castDelayedSpell']) not in [1]):
				newOrder.castDelayedSpell = 0
			else:
				newOrder.castDelayedSpell = int(data[o]['castDelayedSpell'])

			# Get and validate special action - make spell permanent
			if ('makeSpellPermanent' not in data[o]):
				newOrder.makeSpellPermanent = 0
			else:
				newOrder.makeSpellPermanent = int(data[o]['makeSpellPermanent'])

			# Get and validate special action - commit suicide (if under a permanent mindspell)
			if ('commitSuicide' not in data[o]) or (int(data[o]['commitSuicide']) not in [1]):
				newOrder.commitSuicide = 0
			else:
				newOrder.commitSuicide = int(data[o]['commitSuicide'])

			# Get and validate orders for paralyze
			if ('paralyzeOrders' in data[o]):
				for i in data[o]['paralyzeOrders']:
					if data[o]['paralyzeOrders'][i] is not None:
						newOrder.paralyzeOrders[int(i) // handOffset] = int(i) #int(data[o]['paralyzeOrders'][i])

			# Get and validate orders for charm person
			if ('charmOrders' in data[o]):
				for i in data[o]['charmOrders']:
					if data[o]['charmOrders'][i] is not None:
						newOrder.charmOrders[int(i) // handOffset] = (int(i), data[o]['charmOrders'][i])

			# Get and validate attack orders
			if ('attackOrders' in data[o]):
				for i in data[o]['attackOrders']:
					if data[o]['attackOrders'][i] is not None:
						newOrder.attackOrders[int(i)] = int(data[o]['attackOrders'][i])

			self.orders.append(newOrder)
