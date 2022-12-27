import random
from functions_debug import *


class MatchData:
	'''Base class for various match data.
	Contains: 
	- match ID, match status & current turn number,
	- lists of actors (participants and monsters),
	- log of match gestures for all players
	- log of match actions for output
	- localized text strings for output
	- additional information - monster names and classes

	'''

	def __init__(self, matchID):
		self.matchID = matchID
		self.matchStatus = 0  # {0: ongoing, 1: finished}
		self.currentTurn = 0

		self.participantList = []
		self.monsterList = []
		self.matchGestures = {}
		self.matchLog = []
		self.textStrings = {}
		self.spellNames = {}
		self.effectNames = {}
		self.matchMonsterNames = {}
		self.matchMonsterClasses = {}

	def addGestures(self, participantID, turnNum, gestureLH, gestureRH):
		'''Add gestures to the match history, i.e. to self.matchGestures.
		These gestures were taken from playerOrders, validated in matchOrders.validateOrders(), 
		and possibly changed by spell effects in SpellBook.determineGestures().

		Arguments: 
		participant ID -- integer [1..8], ID of the participant who made gestures
		turnNum -- integer, number of turn on which the gestures were made
		gestureLH -- str(1), a Left Hand gesture from SpellBook.validGestures set
		gestureRH -- str(1), a Right Hand gesture from SpellBook.validGestures set
		'''

		g = {
				'gLH': gestureLH,
				'gRH': gestureRH,
		}

		if participantID not in self.matchGestures:
			self.matchGestures.update({participantID: {}})
		self.matchGestures[participantID].update({turnNum: g})

	def initTextStrings(self, currentTextStrings):
		'''This function imports localized text string patterns (for user's language), 
		which would later be formatted and used to display in-game messages.
		'''

		self.textStrings = currentTextStrings

	# GET functions

	def getMatchStatus(self):
		''' Return current match status: {0: ongoing, 1: finished}
		'''

		return self.matchStatus

	def getEffectName(self, code):

		for s in self.effectNames:
			if s == code:
				return self.effectNames[s]
		return ''

	def getPronouns(self, gender = -1, seed = 0):
		''' Return a tuple with localized pronouns according to gender vaiable.
		If gender is not set, assign random pronouns. These pronouns would later be used
		to format in-game messages where the participant would be mentioned.

		Arguments:
		gender -- integer, {-1: not set, 0: they, 1: she, 2: he}

		Return:
		A tuple with three forms of the selected pronoun
		'''

		if gender == -1:
			gender = random.Random(seed).choice([0, 1, 2])
		if gender == 0:
			pronounA = self.getTextStingsByCode('pronounThey')
			pronounB = self.getTextStingsByCode('pronounThem')
			pronounC = self.getTextStingsByCode('pronounTheir')
		elif gender == 1:
			pronounA = self.getTextStingsByCode('pronounShe')
			pronounB = self.getTextStingsByCode('pronounHer')
			pronounC = self.getTextStingsByCode('pronounHers')
		elif gender == 2:
			pronounA = self.getTextStingsByCode('pronounHe')
			pronounB = self.getTextStingsByCode('pronounHim')
			pronounC = self.getTextStingsByCode('pronounHis')

		return (pronounA, pronounB, pronounC)
	
	def getTextStingsByCode(self, code):
		''' Return a string template for later formatting and output.

		Arguments:
		code -- string, test code name of a localized unformatted string

		Return:
		A localized unformatted string if the code is found, empty string otherwise
		'''

		if code in self.textStrings:
			return self.textStrings[code]
		else:
			# Debug
			#raise NameError('Missing Loc String '+code+'!')
			return ''
	
	def getGestureLast(self, participantID, hand):
		''' Return the last gesture for this participand and hand.
		Note that on some turns a participant might not have made any gestures,
		so we have to go through all gestures and check turnNum each time.

		Arguments:
		participant ID -- integer [1..8], ID of the participant who made the gesture
		hand -- integer [1, 2], flag for left or right hand

		Return:
		A gesture str(1) that was shown by this participant with this hand if any, '' otherwise
		'''

		g = ''
		turnPrev = 0
		for turnNum in self.matchGestures[participantID]:
			if turnNum > turnPrev:
				if hand == 1:
					g = self.matchGestures[participantID][turnNum]['gLH']
				elif hand == 2:
					g = self.matchGestures[participantID][turnNum]['gRH']
				turnPrev = turnNum

		return g

	def getGesture(self, participantID, turnNum, hand):
		''' Return the gesture for this participand and this turn and hand.

		Arguments:
		participantID -- integer [1..8], ID of the participant who made the gesture
		turnNum -- integer, the number of the turn
		hand -- integer [1, 2], flag for left or right hand

		Return:
		A gesture str(1) that was shown by this participant on this turn with this hand if any, '' otherwise
		'''

		g = ''
		if ((participantID in self.matchGestures) 
				and (turnNum in self.matchGestures[participantID])):
			if hand == 1:
				g = self.matchGestures[participantID][turnNum]['gLH']
			elif hand == 2:
				g = self.matchGestures[participantID][turnNum]['gRH']
		return g

	def getGestureHistory(self, participantID, hand, spaced = 0):
		''' Return all gestures shown by this participand with this hand during this match.
		Note that on some turns a participant might not have made any gestures,
		and depending on 'spaced' flag we either ignore these turns (if this string is used to match spells)
		or add space (if this string is used for user output / turn log).

		Arguments:
		participantID -- integer [1..8], ID of the participant who made the gesture
		hand -- integer [1, 2], flag for left or right hand
		spaced -- integer [0, 1], flag for using spaces instead of missing gestures

		Return:
		A gesture history string that was shown by this participant with this hand if any, '' otherwise
		'''

		g = ''
		if participantID in self.matchGestures:
			for turnNum in range(1,self.currentTurn + 1):
				if turnNum in self.matchGestures[participantID]:
					if hand == 1:
						g += self.matchGestures[participantID][turnNum]['gLH']
					elif hand == 2:
						g += self.matchGestures[participantID][turnNum]['gRH']
				elif spaced==1:
					g += ' '
		return g

	def getNextParticipantID(self):
		''' Return next free ID for a participant (normally in [1..8] range)
		'''

		return len(self.participantList) + 1

	def getNextMonsterID(self):
		''' Return next free ID for a monster (normally in [101..] range)
		'''

		return self.monsterIDOffset + len(self.monsterList) + 1

	def getActorByID(self, ID, searchAliveOnly = 1):
		''' Return a SpellBook-specific inheritant of an Actor object.

		Arguments:
		ID -- integer, which can be participantID, handID or monsterID.
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		An object of Participant or Monster classes - or their SpellBook-specific 
		inheritants like WarlocksParticipant and WarlocksMonster.
		'''

		target = None
		if ID in self.getListOfParticipantsIDs(searchAliveOnly):
			target = self.getParticipantByID(ID, searchAliveOnly)
		elif ID in self.getListOfMonstersIDs(searchAliveOnly):
			target = self.getMonsterByID(ID, searchAliveOnly)
		elif ID in self.getListOfParticipantsHandsIDs(searchAliveOnly):
			target = self.getMonsterByTurnAndHand(self.currentTurn, ID, searchAliveOnly)
		return target

	def getListOfTargetsIDs(self, searchAliveOnly = 1):
		''' Return a list of all viable target IDs (participants, hands, monsters).

		Arguments:
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		A list of integer IDs.
		'''

		return (self.getListOfParticipantsIDs(searchAliveOnly) 
				+ self.getListOfParticipantsHandsIDs(searchAliveOnly) 
				+ self.getListOfMonstersIDs(searchAliveOnly))

	def getListOfParticipantsIDs(self, searchAliveOnly = 1):
		''' Return a list of all viable IDs of participants.

		Arguments:
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		A list of integer IDs.
		'''
		
		l = []
		for p in self.participantList:
			if (not searchAliveOnly) or (searchAliveOnly and p.isAlive):
				l.append(p.ID)
		return l

	def getListOfOpponentsIDs(self, participantID, searchAliveOnly = 1):
		''' Return a list of all viable IDs of opponents (i.e. participants with a different team number)
		of a specific participant.

		Arguments:
		participantID -- integer [1..8], a participant that wants to know IDs of their opponents
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		A list of integer IDs.
		'''
		
		p = self.getParticipantByID(participantID)
		teamID = p.teamID
		l = []
		for p in self.participantList:
			if p.teamID != teamID:
				if (not searchAliveOnly) or (searchAliveOnly and p.isAlive):
					l.append(p.ID)
		return l

	def getRandomOpponentID(self, participantID):
		''' Return an ID of a randomly-selected opponent.

		Arguments:
		participantID -- integer [1..8], a participant that wants to know IDs of their opponents

		Return:
		Integer ID.
		'''

		return random.Random(self.matchID + self.currentTurn + participantID).choice(
											self.getListOfOpponentsIDs(participantID))

	def getListOfParticipantsHandsIDs(self, searchAliveOnly = 1):
		''' Return a list of all viable IDs of participants' hands.

		Arguments:
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		A list of integer IDs.
		'''

		l = []
		for p in self.participantList:
			if (not searchAliveOnly) or (searchAliveOnly and p.isAlive):
				l.append(p.LHID)
				l.append(p.RHID)
		return l

	def getListOfMonstersByType(self, type, searchAliveOnly = 1):
		''' Return a list of all viable IDs of monsters of specified type.
		This is mostly used to control the population of elementals (types 5 and 6).

		Arguments:
		type -- integer, requested monster type. For Warlocks it would be in range [1..6]
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		A list of integer IDs.
		'''

		l = []
		for m in self.monsterList:
			if m.monsterType == type:
				if (not searchAliveOnly) or (searchAliveOnly and m.isAlive):
					l.append(m.ID)
		return l

	def getListOfMonstersIDs(self, searchAliveOnly = 1):
		''' Return a list of all viable IDs of monsters.

		Arguments:
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		A list of integer IDs.
		'''

		l=[]
		for m in self.monsterList:
			if (not searchAliveOnly) or (searchAliveOnly and m.isAlive):
				l.append(m.ID)
		return l

	def getParticipantByID(self, ID, searchAliveOnly = 1):
		''' Return a SpellBook-specific inheritant of Participant object.

		Arguments:
		ID -- integer, which is participantID.
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		An instance of a SpellBook-specific inheritant of Participant object.
		'''
		
		for p in self.participantList:
			if p.ID == ID:
				if (not searchAliveOnly) or (searchAliveOnly and p.isAlive):
					return p
				else:
					break
	
	def getMonsterByID(self, ID, searchAliveOnly = 1):
		''' Return a SpellBook-specific inheritant of Monster object.

		Arguments:
		ID -- integer, which is monsterID.
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		An instance of a SpellBook-specific inheritant of Monster object.
		'''

		for m in self.monsterList:
			if m.ID == ID:
				if (not searchAliveOnly) or (searchAliveOnly and m.isAlive):
					return m
				else:
					break

	def getMonsterByTurnAndHand(self, turnNum, handID, searchAliveOnly = 1):
		''' Return a SpellBook-specific inheritant of Monster object.
		This is used if the monster is summoned this turn, and it was originally targeted by hand ID.

		Arguments:
		turnNum -- integer, turn number.
		handID -- integer, ID of a hand that was used to summon a monster.
		searchAliveOnly -- boolean flag to search only for alive actors or for all actors.

		Return:
		An instance of a SpellBook-specific inheritant of Monster object.
		'''

		for m in self.monsterList:
			if (m.summonerHandID == handID) and (m.summonTurn == turnNum):
				if (not searchAliveOnly) or (searchAliveOnly and m.isAlive):
					return m
				else:
					break

	# SET functions

	def setMatchStatus(self, status):
		''' Update current match status.

		Arguments:
		status -- boolean, {0: ongoing, 1: finished}
		'''

		self.matchStatus = status

	def setCurrentTurn(self, turnNum):
		''' Update current turn number.

		Arguments:
		turnNum -- integer, turn number.
		'''

		self.currentTurn = turnNum

	def setDestroyMonsterNowByID(self, ID):
		''' Mark monster as dead.

		Arguments:
		ID -- integer, monster ID
		'''

		for m in self.monsterList:
			if m.isAlive and (m.ID == ID):
				m.isAlive = 0
				break

	def setDestroyMonsterBeforeAttackByID(self, ID):
		''' Flag monster to die this turn before attacks.
		We do not kill them right away as they still might be a target of another spell or interact somehow.

		Arguments:
		ID -- integer, monster ID
		'''

		if ID in self.getListOfMonstersIDs():
			m = self.getMonsterByID(ID)
			m.setDestroyBeforeAttack()
		elif ID in self.getListOfParticipantsHandsIDs():
			m = self.getMonsterByTurnAndHand(self.currentTurn, ID)
			m.setDestroyBeforeAttack()

	def setDestroyActorEOTByID(self, ID):
		''' Flag actor to die in the end of the turn.
		They still get to attack or do something else.

		Arguments:
		ID -- integer, actor ID
		'''

		for pID in self.getListOfParticipantsIDs():
			if pID == ID:
				p = self.getParticipantByID(pID)
				p.setDestroyEOT()
				break

		for mID in self.getListOfMonstersIDs():
			if mID == ID:
				m = self.getMonsterByID(mID)
				m.setDestroyEOT()
				break

		for hID in self.getListOfParticipantsHandsIDs():
			if hID == ID:
				m = self.getMonsterByTurnAndHand(self.currentTurn, hID)
				m.setDestroyEOT()
				break

	def setGestures(self, participantID, turnNum, gLH, gRH):
		''' Save gestures made by participantID on turnNum

		Arguments:
		participantID -- integer [1..8], a participant that wants to know IDs of their opponents
		turnNum -- integer, turn number.
		gLH -- str(1), left hand gesture
		gRH -- str(1), right hand gesture
		'''

		g = {
				'gLH': gLH,
				'gRH': gRH,
		}

		self.matchGestures[participantID].update({turnNum: g})

	def killMonstersBeforeAttack(self):
		''' Set isAlive to 0 for monsters marked to be destroyed before attack phase.
		'''

		for m in self.monsterList:
			if m.isAlive and (m.destroyBeforeAttack == 1):
				m.isAlive = 0
				self.addLogEntry(m.ID, 11, 'resultActorDies', name=m.name)

	def killMonstersEOT(self):
		''' Set isAlive to 0 for monsters marked to be destroyed in the end of turn.
		'''

		for m in self.monsterList:
			if m.isAlive and (m.HP <= 0 or m.destroyEOT == 1):
				m.isAlive = 0 
				self.addLogEntry(m.ID, 11, 'resultActorDies', name = m.name)

	def killParticipantsEOT(self):
		''' Set isAlive to 0 for participants marked to be destroyed in the end of turn.
		'''

		for p in self.participantList:
			if p.isAlive and (p.HP <= 0 or p.destroyEOT == 1):
				p.isAlive = 0
				self.addLogEntry(p.ID, 11, 'resultActorDies', name = p.name)	

	def checkEOTMatchEnd(self):
		''' End of Turn check for match end. Match end is triggered 
		and match status is updated if all alive players belong to the same team.
		'''
		
		# Make a list to flag teams still present in the match
		# max 8 teams, l[0] and l[9] not used
		l = [0] * self.handIDOffset
		for p in self.participantList:
			if p.isAlive:
				l[p.teamID] = 1
		
		# If more than one team left, do nothing.

		# If only one team left, get tead ID, then get participant names, 
		# and print names of all participants (even dead) of the team.
		if sum(l) == 1:
			teamWon = 0
			for i in range(len(l)):
				if l[i] == 1:
					teamWon = i
					break
			names = []
			if teamWon:
				for p in self.participantList:
					if p.teamID == teamWon:
						names.append(p.name)			
			if len(names) == 1:
				namestr = names[0]
				self.addLogEntry(p.ID, 12, 'resultActorVictorious', name = namestr)
			else:
				namestr = ', '.join(names[0:-1:1]) + ' & ' +  names[-1]
				self.addLogEntry(p.ID, 12, 'resultTeamVictorious', name = namestr)
			self.setMatchStatus(1)

		# If no teams left, declare a draw.
		elif sum(l) == 0:
			self.addLogEntry(p.ID, 12, 'resultDraw')
			self.setMatchStatus(1)

	def giveSingleAttackOrder(self, m, attackID):
		''' Process single attack order for a single monster.

		Arguments:
		m -- an instance of SpellBook-specific Monster-inherited object
		attackID -- ID of attack target from player Orders.
		'''

		target = None
		searchAliveOnly = 1
		attackIDprev = m.attackID
		orderCounted = 0 
		# If there are no orders this turn
		if attackID == -1:
			# if there are no orders from previous turn as well
			# choose random opponent as a target.
			if attackIDprev == -1:
				attackID = self.getRandomOpponentID(m.controllerID)
				target = self.getParticipantByID(attackID)
			# else take orders from previous turn.
			else: 
				attackID = attackIDprev
				target = self.getParticipantByID(attackID)
		# else (if there are orders this turn)
		else:
			# Try to find requested target among valid targets
			if attackID == 0:
				orderCounted = 1
			elif attackID in self.getListOfMonstersIDs(searchAliveOnly):
				target = self.getMonsterByID(attackID)
				orderCounted = 1
			elif attackID in self.getListOfParticipantsHandsIDs(searchAliveOnly):
				target = self.getMonsterByTurnAndHand(self.currentTurn, attackID)
				attackID = target.ID
				orderCounted = 1
			elif attackID in self.getListOfParticipantsIDs(searchAliveOnly):
				target = self.getParticipantByID(attackID)
				orderCounted = 1
			# If target not found, redirect to nobody
			else:
				attackID = 0
		# save updated target
		m.attackID = attackID
		
		# print report if a valid order was given
		if orderCounted:
			if target is None:
				targetname = self.getTextStingsByCode('nameNobody')
			else:
				targetname = target.name
			controller = self.getParticipantByID(m.controllerID)
			self.addLogEntry(controller.ID, 6, 'attackOrder', 
								name = controller.name, 
								targetname = m.name, 
								attackname = targetname)

	def giveAttackOrders(self, matchOrders):
		''' Process portion of turn Orders related to attacks.

		Arguments:
		matchOrders -- a list of Order-objects
		'''

		searchAliveOnly = 1
		# checking all attack orders for participants acting this turn
		for participantID in self.getListOfParticipantsIDsActiveThisTurn():
			playerOrders = matchOrders.searchOrders(self.matchID, 
									self.currentTurn, participantID)
			if playerOrders.attackOrders:
				for ID in playerOrders.attackOrders:
					# trying to locate the object this order belongs to among monsters
					if ID in self.getListOfMonstersIDs(searchAliveOnly):
						m = self.getMonsterByID(ID)
					# trying to locate the object this order belongs to among new summons
					elif ID in self.getListOfParticipantsHandsIDs(searchAliveOnly):
						m = self.getMonsterByTurnAndHand(self.currentTurn, ID)
					# if object found, check check if order source is correct
					# ignore orders that do not come from anyone other than monster controller
					if m and (m.controllerID == participantID):
						attackID = playerOrders.attackOrders[ID]
						self.giveSingleAttackOrder(m, attackID)

	def addLogEntry(self, actorID, strType, strCode, name = '', pronoun = '', 
						targetname = '', spellname = '', attackname = '', 
						damage = '', handname = ''):
		''' Log a game action.

		Arguments:
		actorID -- integer, ID of actor related to the action (i.e. caster of a spell)
		strType -- integer, type of action, at the moment not well researched / follows RB colours
		strCode -- string, code to fetch unformatted string from localization files
		name, pronoun, targetname, spellname, attackname, damage, handname - strings that 
			are used to format string (fetched using strCode) later.
		'''
		
		newLogID = len(self.matchLog)
		logEntry = {'logID': newLogID, 'matchID': self.matchID, 
					'turnNum': self.currentTurn, 'actorID': actorID, 
					'strType': strType, 'strCode': strCode, 
					'name': name, 'pronoun': pronoun, 'targetname': targetname, 
					'spellname': spellname, 'attackname': attackname, 
					'damage': damage, 'handname': handname
		}
		self.matchLog.append(logEntry)

	# OUTPUT functions

	def printActorStatusByID(self, ID):
		''' Output actor status, including name, HP, statuses, controller and attack target (for monsters), etc.

		This is a placeholder that should be reworked for future front-end implementation.

		Arguments:
		ID -- integer, actor ID
		'''

		a = self.getActorByID(ID, 0)

		slist = []
		s = self.getTextStingsByCode('statusName').format(name = a.name)
		if a.isAlive == 0:
			s += self.getTextStingsByCode('statusDead')
		slist.append(s)
		s = self.getTextStingsByCode('statusHP').format(damage = a.HP)
		slist.append(s)

		if a.type == 2 and a.controllerID:
			controller = self.getParticipantByID(a.controllerID, 0)
			s = self.getTextStingsByCode('statusController').format(name = controller.name)
			slist.append(s)
	
			attackTarget = self.getActorByID(a.attackID)
			if attackTarget:
				attackTargetName = attackTarget.name
			else:
				attackTargetName = self.getTextStingsByCode('nameNobody')
			s = self.getTextStingsByCode('statusAttacking').format(attackname = attackTargetName)
			slist.append(s)

		for key in a.statuses:
			if a.statuses[key] > 0:
				s1 = self.getEffectName(key)
				if a.statuses[key] == self.permanentDuration:
					s2 = self.getTextStingsByCode('statusPermanent')
				else:
					s2 = str(a.statuses[key])
				s = self.getTextStingsByCode('statusEffectLength').format(spellname = s1, damage = s2)
				slist.append(s)
		if a.type == 1 and a.stateDelayedSpell is not None:
			s = self.getTextStingsByCode('statusStored').format(spellname = a.stateDelayedSpell.name)
			slist.append(s)

		s = ', '.join(slist)
		print(s)

	def printMatchActorsStatus(self):
		''' Output statuses for all actors and gesture history for all participants).

		This is a placeholder that should be reworked for future front-end implementation.
		'''

		for pID in self.getListOfParticipantsIDs(0):
			self.printActorStatusByID(pID)
			tstr = ''
			for i in range(0, self.currentTurn + 1):
				tstr += str(i % 10)
			print(self.getTextStingsByCode('statusTurn') + tstr)
			print(self.getTextStingsByCode('statusLH') + 'B' + self.getGestureHistory(pID, 1, 1))
			print(self.getTextStingsByCode('statusRH') + 'B' + self.getGestureHistory(pID, 2, 1))
		for mID in self.getListOfMonstersIDs():
			self.printActorStatusByID(mID)

	def printLogEntry(self, logID):
		''' Format and output a log entry.

		This is a placeholder that should be reworked for future front-end implementation.

		Arguments:
		logID -- integer, ID of log entry
		'''
		
		logEntry = self.matchLog[logID]

		if self.getTextStingsByCode(logEntry['strCode']):
			strf = self.getTextStingsByCode(logEntry['strCode']).format(name = logEntry['name'], 
													pronoun = logEntry['pronoun'],
													targetname = logEntry['targetname'],
													spellname = logEntry['spellname'],
													attackname = logEntry['attackname'],
													damage = logEntry['damage'],
													handname = logEntry['handname'])
			print(strf)
		else:
			#dprint(logEntry)
			pass

	def printLogEntriesByTurn(self, turnNum):
		''' Select log entried related to a specific turn and print them.

		This is a placeholder that should be reworked for future front-end implementation.

		Arguments:
		turnNum -- integer, turn number.
		'''
		
		for l in self.matchLog:
			if l['turnNum'] == turnNum:
				self.printLogEntry(l['logID'])

		print(' ')
