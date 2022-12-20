import random
from class_matchdata import MatchData
from class_warlocks_actor import WarlocksParticipant, WarlocksMonster


class WarlocksMatchData(MatchData):
	'''This class contains current match state, with some exceptions.
	- matchID and currentTurn are obvious.
	- participantList and monsterList contain all match actors, alive and dead.
	- matchGestures contain history of gestures for all players all hands.
	- matchLog contain history of all events happened
	- textStings contains all warlocks text strings in the current loc
	TODO Currently of all match info only matchOrders are not stored here (consider).
	'''
	
	def __init__(self, matchID):
	
		MatchData.__init__(self, matchID)

		self.currentTurnType = 1 # 1 - normal, 2 - hasted, 3 - timestopped
		self.prevTurnType = 1

		self.handIDOffset = 10
		self.monsterIDOffset = 100

		self.monsterTypes = {
1: {'startHP': 1, 'maxHP': 2, 'attackDamage': 1, 'attackType': 'Physical', 'attacksAll': 0, 'initialStatuses' : {} }, 
2: {'startHP': 2, 'maxHP': 3, 'attackDamage': 2, 'attackType': 'Physical', 'attacksAll': 0, 'initialStatuses' : {} }, 
3: {'startHP': 3, 'maxHP': 4, 'attackDamage': 3, 'attackType': 'Physical', 'attacksAll': 0, 'initialStatuses' : {} }, 
4: {'startHP': 4, 'maxHP': 5, 'attackDamage': 4, 'attackType': 'Physical', 'attacksAll': 0, 'initialStatuses' : {} },
5: {'startHP': 3, 'maxHP': 4, 'attackDamage': 3, 'attackType': 'Fire', 'attacksAll': 1, 'initialStatuses' : {'ResistHeat': 9999}}, 
6: {'startHP': 3, 'maxHP': 4, 'attackDamage': 3, 'attackType': 'Ice', 'attacksAll': 1, 'initialStatuses' : {'ResistCold': 9999}}
}

	# INIT and ADD functions

	def initActorsTmp(self, participants):
		''' Populate self.participantList with match participants.

		Arguments:
		participants -- list of participants initial data
		'''

		for p in participants:
			# Create new Participant instance
			newParticipant = self.createParticipant(p['playerID'], p['playerName'], p['teamID'])
			# Set participant ID and hand IDs
			newParticipant.setIDs(self.getNextParticipantID())
			newParticipant.setHandIDs(self.handIDOffset)
			# Get and set pronouns
			pronouns = self.getPronouns(p['gender'])
			newParticipant.pronounA = pronouns[0]
			newParticipant.pronounB = pronouns[1]
			newParticipant.pronounC = pronouns[2]
			# Add participant to the match
			self.participantList.append(newParticipant)

	def initMonsterNames(self, monsterNamesLoc, monsterClassesLoc):
		''' Import localized names and then shuffle them using matchID
			as a seed, so that for each match order or names is different,
			but it is always the same if loading the same match data.

			Arguments:
			monsterNamesLoc -- dictionary with list of names for each monsterType
			monsterClassesLoc -- list of monster class names
		'''

		for monsterType in [1,2,3,4,5,6]:
			self.matchMonsterNames[monsterType] = monsterNamesLoc[monsterType]
			random.Random(self.matchID).shuffle(self.matchMonsterNames[monsterType])

		for monsterType in [1,2,3,4,5,6]:
			self.matchMonsterClasses[monsterType] = monsterClassesLoc[monsterType]

	def getNewMonsterName(self, monsterType):
		''' Request a new name from name repository.
		For elemental the name is always the same (Fire Elemental and Ice Elemental respectively).
		For Goblins, Ogres, Trolls and Giants we cycle through previously shuffled list;
		if we have exhaused the list, we start over adding 'Very ' in front of name;
		this can be repeated indefinitely (i.e. at some moment there might be 'Very Very Green Goblin').

		Arguments:
		monsterType: integer [1..6], monster type
		'''

		monsterName = ''
		if monsterType in [1, 2, 3, 4]:
			# Count all monsters of the monsterType, alive and dead
			count = self.getCountNamedMonsters(monsterType)
			# Compare with the size of name list for this monsterType
			size = len(self.matchMonsterNames[monsterType])
			monsterName = (self.getTextStingsByCode('nameMonsterExtra') * (count // size) 
							+ self.matchMonsterNames[monsterType][count % size] 
							+ ' ' + self.matchMonsterClasses[monsterType])
		elif monsterType in [5, 6]:
			monsterName = self.matchMonsterNames[monsterType][0]

		return monsterName

	def getCountNamedMonsters(self, monsterType):
		''' Counts the amount of already named (= already created) monsters of monsterType in this match.

		Arguments:
		monsterType: integer [1..6], monster type

		Returns:
		Integer, monster count.
		'''

		c = 0
		for m in self.monsterList:
			if m.monsterType == monsterType and m.name > '':
				c += 1
		return c

	def createParticipant(self, playerID, playerName, teamID):
		''' Creates an instance of Participant-inherited class.

		Arguments:
		playerID -- integer, a user ID to link game profile to in-match participant ID
		playerName -- string, player name to display
		teamID -- integer [1..8], selected at the start of the match.

		Returns:
		An instance of Participant-inherited class.
		'''

		newParticipant = WarlocksParticipant(playerID, playerName, teamID)
		return newParticipant

	def createMonster(self, controllerID, monsterType, 
					summonerID, summonerHandID, summonTurn, 
					pronounA, pronounB, pronounC):
		''' Creates an instance of Monster-inherited class.

		Arguments:
		controllerID -- integer [1..8], ID of the participant that controls the monster
		monsterType -- integer [1..6], monster type
		summonerID -- integer [1..8], ID of the participant that summoned the monster
		summonerHandID -- integer, ID of the hand that was used to summon monster
		summonTurn -- integer, the numbre of turn when the monster was summoned
		pronounA, pronounB, pronounC -- strings, three forms of participant pronoun

		Returns:
		An instance of Monster-inherited class.
		'''

		newMonster = None
		if monsterType in self.monsterTypes:
			newMonster = WarlocksMonster(self.monsterTypes, controllerID, monsterType, 
											summonerID, summonerHandID, summonTurn,
											pronounA, pronounB, pronounC)
		return newMonster

	# GET functions

	def getGestureLogEntry(self, gestureLH, gestureRH):
		''' Get codes for localized strings for LH and RH gestures to use in log.

		Arguments:
		gestureLH, gestureRH -- str(1), gestures for LH and RH

		Returns:
		tuple with codes of strings
		'''

		textLH = ''
		textRH = ''

		if gestureLH == 'C' and gestureRH == 'C':
			textLH = 'gestureC'
			return (textLH, textRH)

		match gestureLH:
			case '-':
				textLH = 'gestureN'
			case 'C':
				textLH = 'gestureC2'
			case 'D':
				textLH = 'gestureD'
			case 'F':
				textLH = 'gestureF'
			case 'P':
				textLH = 'gestureP'
			case 'S':
				textLH = 'gestureS'
			case 'W':
				textLH = 'gestureW'
			case '>':
				textLH = 'gestureT'

		match gestureRH:
			case '-':
				textRH = 'gestureN'
			case 'C':
				textRH = 'gestureC2'
			case 'D':
				textRH = 'gestureD'
			case 'F':
				textRH = 'gestureF'
			case 'P':
				textRH = 'gestureP'
			case 'S':
				textRH = 'gestureS'
			case 'W':
				textRH = 'gestureW'
			case '>':
				textRH = 'gestureT'

		return (textLH, textRH)

	def getListOfParticipantsIDsHasted(self):
		''' Get list of participants that are affected by Haste this turn.

		Returns:
		List with integer IDs
		'''
		
		l = []
		for pID in self.getListOfParticipantsIDs():
			p = self.getParticipantByID(pID)
			if p.affectedByHaste():
				l.append(pID)
		return l

	def getListOfParticipantsIDsTimestopped(self):
		''' Get list of participants that are affected by Timestop this turn.

		Returns:
		List with integer IDs
		'''
		
		l = []
		for pID in self.getListOfParticipantsIDs():
			p = self.getParticipantByID(pID)
			if p.affectedByTimeStop():
				l.append(pID)
		return l

	def getListOfParticipantsIDsActiveThisTurn(self):
		''' Get list of participants that are active this turn.

		Returns:
		List with integer IDs
		'''
		
		if self.isCurrentTurnTimestopped():
			return self.getListOfParticipantsIDsTimestopped()
		if self.isCurrentTurnHasted():
			return self.getListOfParticipantsIDsHasted()
		return self.getListOfParticipantsIDs()

	def isCurrentTurnHasted(self):
		''' Check if the current turn is Hasted

		Returns:
		Boolean, 1 is turn is Hasted, 0 otherwise
		'''

		if self.currentTurnType == 2:
			return 1
		else:
			return 0

	def isCurrentTurnTimestopped(self):
		''' Check if the current turn is Timestopped

		Returns:
		Boolean, 1 is turn is Timestopped, 0 otherwise
		'''

		if self.currentTurnType == 3:
			return 1
		else:
			return 0

	# SET functions
	
	def setCurrentTurnType(self):
		''' Determine current turn type.
		{1: Normal; 2: Hasted; 3: Timestopped}
		'''

		self.prevTurnType = self.currentTurnType

		if self.getListOfParticipantsIDsTimestopped():
			self.currentTurnType = 3 # timestopped
		elif self.getListOfParticipantsIDsHasted():
			if self.prevTurnType == 2:
				self.currentTurnType = 1 # normal
			else:	
				self.currentTurnType = 2 # hasted
		else:
			self.currentTurnType = 1 # normal

	# GAME LOGIC functions #TODO rework names and maybe move functions

	def checkSicknessStatuses(self):
		''' Check participants affected by Disease or Poison. 
		Those who reached status 1, die EOT.
		'''

		for p in self.participantList:
			if p.isAlive:
				if p.statuses['Disease'] == 1:
					self.addLogEntry(p.ID, 9, 'effectDiseaseFatal', name = p.name)
					p.destroyEOT = 1

				if p.statuses['Poison'] == 1:
					self.addLogEntry(p.ID, 9, 'effectPoisonFatal', name = p.name)
					p.destroyEOT = 1

	def checkAntiSpellStatuses(self):
		''' Check participants affected by Anti-Spell and update their last gestures with -/-
		We do this EOT, since we need to do stabs after spell casting, and other way around is even messy-er.
		'''

		for p in self.participantList:
			if p.isAlive:
				if p.statuses['AntiSpell'] == 1:
					self.setGestures(p.ID, self.currentTurn, '-', '-')

	def killSuicidedParticipants(self, matchOrders):
		''' Set isAlive to 0 for participants who were affectedd by perm mindspell and gave the suicide order.

		Arguments:
		matchOrders -- an instance of spellbook-specific Orders class with orders for this turn.
		'''

		for pID in self.getListOfParticipantsIDs():
			order = matchOrders.searchOrders(self.matchID, self.currentTurn, pID)
			p = self.getParticipantByID(pID)
			if (p.affectedByPermanentMindspell()) and (order.commitSuicide == 1):
				p.isAlive = 0
				self.addLogEntry(p.ID, 11, 'resultActorSuicides', name = p.name)

	def killSurrenderedParticipants(self, turnNum):
		''' Set isAlive to 0 for participants who showed P/P

		Arguments:
		turnNum -- integer, turn number
		'''

		for p in self.participantList:
			if (p.isAlive 
					and self.getGesture(p.ID, turnNum, 1) == 'P' 
					and self.getGesture(p.ID, turnNum, 2) == 'P'):
				p.isAlive = 0
				self.addLogEntry(p.ID, 11, 'resultActorSurrenders', name = p.name)

	def updateStatusesOnMonstersEOT(self):
		''' EOT tick down all statuses on monsters.
		Skipped for timestopped turns.
		'''

		for m in self.monsterList:
			if m.isAlive:
				for s in m.statuses:
					if not self.isCurrentTurnTimestopped():
						m.decreaseStatus(s)
				m.stateMindSpellsThisTurn = 0

	def updateStatusesOnParticipantsEOT(self):
		''' EOT tick down all statuses on participants.
		Skipped for turns that are followed by hasted or timestopped turns.
		'''

		# Tmp determine next turn type
		nextTurnType = 1
		nextTurnHasteCounter = 0
		nextTurnTimeStopCounter = 0
		for p in self.participantList:
			if p.isAlive:
				if (p.statuses['TimeStop'] > 1 
						or (p.statuses['TimeStop'] == 1 and self.currentTurnType == 1) 
						or p.statusesNext['TimeStop']):
					nextTurnTimeStopCounter += 1
				if (p.statuses['Haste'] > 1 
						or (p.statuses['Haste'] == 1 and self.currentTurnType == 1) 
						or p.statusesNext['Haste']):
					nextTurnHasteCounter += 1
		if nextTurnTimeStopCounter:
			nextTurnType = 3
		elif nextTurnHasteCounter:
			nextTurnType = 2

		for p in self.participantList:
			if p.isAlive:
				for s in p.statuses:
					# Log the end of Blindness / Invisibility
					if s == 'Blindness' and p.statuses[s] == 1:
						self.addLogEntry(p.ID, 8, 'effectBlindness2', name = p.name)
					if s == 'Invisibility' and p.statuses[s] == 1:
						self.addLogEntry(p.ID, 8, 'effectInvisibility2', name = p.name)
					# Decrease statues if next turn is normal.
					# TODO - what about 2 consecutive timestopped turns?
					if (((self.currentTurnType in [1]) and nextTurnType == 1)
						or (self.currentTurnType in [2, 3])):
						p.decreaseStatus(s)
					# Push statusesNext into statuses; 
					# this is used for statuses which start affecting players on the turn after cast turn
					if s in p.statusesNext and (p.statusesNext[s] > p.statuses[s]):
						p.statuses[s] = p.statusesNext[s]
						p.statusesNext[s] = 0
					# Log the start of Blindness / Invisibility						
					if s == 'Blindness' and p.statuses[s] == 3:
						self.addLogEntry(p.ID, 8, 'effectBlindness1', name = p.name)
					if s == 'Invisibility' and p.statuses[s] == 3:
						self.addLogEntry(p.ID, 8, 'effectInvisibility1', name = p.name)

				# A lot of Paralyze housekeeping - we need to keep track
				# who paralyzed partiicpant of turns before and after, and which hand
				p.paralyzedByIDPrev = p.paralyzedByID
				p.paralyzedByID = p.paralyzedByIDNext
				p.paralyzedByIDNext = 0
				p.paralyzedHandIDPrev = p.paralyzedHandID
				p.paralyzedHandID = 0
				# Charm Person housekeeping
				p.charmedByID = p.charmedByIDNext
				p.charmedByIDNext = 0
				# Housekeeping for flags that are used for spells that clash during turn
				# elementals, storms, mindspells
				# TODO - move p.stateFireStormsThisTurn and p.stateIceStormsThisTurn to matchData level
				p.stateMindSpellsThisTurn = 0
				p.stateFireStormsThisTurn = 0
				p.stateIceStormsThisTurn = 0

	def attackAction(self, a, d, checkVisibility = 1, checkShields = 1):
		''' Resolve a single attack action.

		a -- object, Monster or Participant
		d -- object, Monster or Participant
		checkVisibility -- boolean, flag to check visibility (Blindness, Invis)
		checkShields -- boolean, flag to chech shields (PShield, Protection, Resists)
			also used for mindspells, which maybe should be reworked?
		'''

		# If we check shields and other effects that prevent attacks, we check for mindspells on attacker
		if checkShields == 1 and a.affectedByParalysis():
			self.addLogEntry(a.ID, 8, 'effectParalysis2', targetname = a.name)
			return
		if checkShields == 1 and a.affectedByAmnesia():
			self.addLogEntry(a.ID, 8, 'effectAmnesia2', targetname = a.name)
			return
		if checkShields == 1 and a.affectedByFear():
			self.addLogEntry(a.ID, 8, 'effectFear2', targetname = a.name)
			return
		if checkShields == 1 and a.affectedByMaladroitness():
			self.addLogEntry(a.ID, 8, 'effectMaladroitness2', targetname = a.name)
			return

		# If we check visibility, we check visibility between attacker and defender
		if checkVisibility == 1 and a.affectedByBlindness():
			self.addLogEntry(a.ID, 10, 'attackMissesBlindness', 
								name = a.name, 
								attackname = d.name)
			return
		if checkVisibility == 1 and d.affectedByInvisibility():
			self.addLogEntry(a.ID, 10, 'attackMissesInvisibility', 
								name = a.name, 
								attackname = d.name)
			return

		# If we got here, we can actually attack.
		# a = Fire elem
		if a.attackType == 'Fire':
			if checkShields == 1 and d.affectedByResistHeat():
				self.addLogEntry(a.ID, 7, 'effectResistHeat', name = d.name)
			elif checkShields == 1 and d.affectedByPShield():
				self.addLogEntry(a.ID, 10, 'effectShieldFromElemental', 
									attackname = d.name, name = a.name)
			else:	
				d.decreaseHP(a.attackDamage)
				self.addLogEntry(a.ID, 9, 'damagedByFireElem', 
									attackname = d.name, damage = a.attackDamage)
		# a = Ice elem
		elif a.attackType == 'Ice': 
			if checkShields == 1 and d.affectedByResistCold():
				self.addLogEntry(a.ID, 7, 'effectResistCold', name = d.name)
			elif checkShields == 1 and d.affectedByPShield():
				self.addLogEntry(a.ID, 10, 'effectShieldFromElemental', 
									attackname = d.name, name = a.name)
			else:	
				d.decreaseHP(a.attackDamage)
				self.addLogEntry(a.ID, 9, 'damagedByIceElem', 
									attackname = d.name, damage = a.attackDamage)
		# a = monster or stabbing participant
		elif a.attackType == 'Physical': 
			# if a is a timestopped monster, then it deals damage anyways
			# if a is a timestopped participant, then we should check d.affectedByPShield(1, 0) - shield but not protection
			# if a is a regular participant, then we should check d.affectedByPShield(1, 1) or simply d.affectedByPShield()
			if (checkShields == 0 and a.type == 2
				or checkShields == 0 and a.type == 1 and d.affectedByPShield(1, 0) == 0
				or d.affectedByPShield() == 0):
				d.decreaseHP(a.attackDamage)
				self.addLogEntry(a.ID, 9, 'damagedByMonster', name = a.name,
									attackname = d.name, damage = a.attackDamage)
			else:	
				self.addLogEntry(a.ID, 10, 'effectShieldFromMonster', 
									name = a.name, attackname = d.name)

	def checkStabs(self, matchOrders):
		''' Check for stab orders and resolve them.

		Arguments:
		matchOrders - object, an instance of Spellbook-inherited Orders
		'''

		for p in self.participantList:
			if p.isAlive:
				gLH = self.getGesture(p.ID, self.currentTurn, 1)
				gRH = self.getGesture(p.ID, self.currentTurn, 2)
				playerOrders = matchOrders.searchOrders(self.matchID, 
									self.currentTurn, p.ID)
				# Get current turn gestures for all participants
				attackID = 0
				stabHandName=''
				# If RH or LH tried to stab, use that as an order.
				# If both stabbed, Lh is ignored, consider that dagger is in RH.
				if gRH == '>':
					attackID = playerOrders.orderTargetRH
					stabHandName = self.getTextStingsByCode('nameRightHand')
				elif gLH == '>':
					attackID = playerOrders.orderTargetLH
					stabHandName = self.getTextStingsByCode('nameLeftHand')
				else:
					continue
				# Check if there was a target order. If not, get random opponent ID.
				if attackID == -1:
					attackID = self.getRandomOpponentID(p.ID)
				# Get target object
				if attackID > 0:
					target=self.getParticipantByID(attackID)
					if target is None:
						target=self.getMonsterByID(attackID)
					if target is None:
						target=self.getMonsterByTurnAndHand(self.currentTurn, attackID)
					if target is None:
						attackID = 0					
				# Adjust shield and visibility checks based on turn type.
				if stabHandName:
					if self.isCurrentTurnTimestopped():
						checkVisibility = 0
						checkShields = 0
					else:
						checkVisibility = 1
						checkShields = 1
					# Commence stab
					if attackID > 0:
						self.attackAction(p, target, checkVisibility, checkShields)
					else:
						self.addLogEntry(p.ID, 10, 'stabMissesNobody', 
												name = p.name)

	def attackPhase(self, phaseType):
		''' Process attack phase of a normal turn (and skip phase for hasted and timestopped turns).
		Note the difference. On timestopped or hasted turns (turns when there are 
		timestopped or hasted participants); on such turns there is no attack phase at all.
		But on normal turns there can be up to 3 attack phases, first for normal monsters, 
		second for hasted monsters and third for timestopped monsters.

		Arguments:
		phaseType -- integer; {1: Normal monsters; 2: Hasted monsters; 3: Timestopped monsters}
		'''

		# Skip attack phase entirely if turn is for timestopped or hasted participants
		# Note that a monster summoned during timestopped turn would not attack as well. 
		if self.isCurrentTurnHasted() or self.isCurrentTurnTimestopped():
			return

		# For all monsters alive and of status appropriate to phaseType
		for m in self.monsterList:
			if m.isAlive and (phaseType == 1 
							or (phaseType == 2 and m.affectedByHaste())
							or (phaseType == 3 and m.affectedByTimeStop())):
				# If monsters attacks everyone
				if m.attacksAll:

					checkVisibility = 0
					if phaseType == 1:
						if m.monsterType == 5:
							self.addLogEntry(m.ID, 9, 'attackFireElem')
						elif m.monsterType == 6:
							self.addLogEntry(m.ID, 9, 'attackIceElem')
						checkShields = 1
					elif phaseType == 2:
						if m.monsterType == 5:
							self.addLogEntry(m.ID, 9, 'attackFireElemHasted')
						elif m.monsterType == 6:
							self.addLogEntry(m.ID, 9, 'attackIceElemHasted')
						checkShields = 1
					elif phaseType == 3:
						if m.monsterType == 5:
							self.addLogEntry(m.ID, 9, 'attackFireElemTimestopped')
						elif m.monsterType == 6:
							self.addLogEntry(m.ID, 9, 'attackIceElemTimestopped')
						checkShields = 0
					# Try to attack all participants
					for p in self.participantList:
						if p.isAlive:
							self.attackAction(m, p, checkVisibility, checkShields)
					# Try to attack all monsters (except self)
					for mm in self.monsterList:
						if mm.isAlive and m.ID != mm.ID:
							self.attackAction(m, mm, checkVisibility, checkShields)
				# If monster attacks one target
				else:
					# Get target
					if m.attackID > 0:
						target=self.getParticipantByID(m.attackID)
						if target is None:
							target=self.getMonsterByID(m.attackID)
						if target is None:
							target=self.getMonsterByTurnAndHand(currentTurn, m.attackID)
						if target is None:
							m.attackID = 0
					# Determine if visibility and shields affect attacks in this phase
					if phaseType == 1:
						checkVisibility = 1
						checkShields = 1
					elif phaseType == 2:
						self.addLogEntry(m.ID, 9, 'attackMonsterHasted', 
												name = m.name)
						checkVisibility = 1
						checkShields = 1
					elif phaseType == 3:
						self.addLogEntry(m.ID, 9, 'attackMonsterTimestopped', 
												name = m.name)
						checkVisibility = 0
						checkShields = 0

					if m.attackID > 0:
						self.attackAction(m, target, checkVisibility, checkShields)
					else:
						self.addLogEntry(m.ID, 10, 'attackMissesNobody', 
												name = m.name)
