from class_actor import Actor


class WarlocksActor(Actor):
	'''Expands Actor class with Ravenblack's Warlocks-specific statuses.
	'''

	def __init__(self, actorType, name, HP, maxHP):
		
		Actor.__init__(self, actorType, name, HP, maxHP)
		self.initStatuses()

	def initStatuses(self):

		self.statuses = {
		'PShield': 0, 
		'Protection': 0,
		'MShield': 0,
		'MagicMirror': 0,
		'Haste': 0,
		'TimeStop': 0,
		'ResistHeat': 0,
		'ResistCold': 0,
		
		'Paralysis': 0,
		'Amnesia': 0,
		'Fear': 0,
		'Maladroitness': 0,
		'CharmPerson': 0,
		#'CharmMonster': 0,
		'AntiSpell': 0,
		
		'Disease': 0,
		'Poison': 0,
		'Blindness': 0,
		'Invisibility': 0,
		'Permanency': 0,
		'DelayEffect': 0
		}

		self.statusesNext = {
		'Haste': 0,
		'TimeStop': 0,
		
		'Paralysis': 0,
		'Amnesia': 0,
		'Fear': 0,
		'Maladroitness': 0,
		'CharmPerson': 0,
		
		'Disease': 0,
		'Poison': 0,
		'Blindness': 0,
		'Invisibility': 0,
		'Permanency': 0,
		'DelayEffect': 0
		}

		self.stateMindSpellsThisTurn = 0
		self.paralyzedByIDNext = 0
		self.paralyzedByID = 0
		self.paralyzedByIDPrev = 0		
		self.paralyzedHandID = 0
		self.paralyzedHandIDPrev = 0
		self.charmedByID = 0
		self.charmedByIDNext = 0
		self.charmedHandID = 0
		self.stateFireStormsThisTurn = 0
		self.stateIceStormsThisTurn = 0

	def actorStatusReport(self):

		#TODO words for this output should be stored in loc file
		statusStr = 'Name: ' + self.name
		if self.isAlive == 0:
			statusStr += ' (DEAD)'
		statusStr += ', HP: ' + str(self.HP)
		#TODO splitting Pshield and Protection has a drawback here
		for key in self.statuses:
			if self.statuses[key] > 0:
				if self.statuses[key] == 9999:
					strLength = 'permanent'
				else:
					strLength = str(self.statuses[key])
				statusStr += ', ' + key + ': ' + strLength
		#TODO to display stored spell status, we should check spellbook-specific arguments. consider
		if self.type == 1 and self.stateDelayedSpell is not None:
			statusStr += ', Stored: ' + self.stateDelayedSpell.name

		return statusStr

	def decreaseStatus(self, statusName):

		if statusName in self.statuses:
			if self.statuses[statusName] != 9999 and self.statuses[statusName] > 0:
				self.statuses[statusName] -= 1

	def removeEnchantments(self):

		self.statuses['Haste'] = 0
		self.statuses['TimeStop'] = 0
		self.statuses['Protection'] = 0		
		self.statuses['ResistHeat'] = 0
		self.statuses['ResistCold'] = 0

		self.statuses['Paralysis'] = 0
		self.statuses['Amnesia'] = 0
		self.statuses['Fear'] = 0
		self.statuses['Maladroitness'] = 0
		self.statuses['CharmPerson'] = 0

		self.statuses['Disease'] = 0
		self.statuses['Poison'] = 0
		self.statuses['Blindness'] = 0
		self.statuses['Invisibility'] = 0
		self.statuses['Permanency'] = 0
		self.statuses['DelayEffect'] = 0

		self.statusesNext['Haste'] = 0
		self.statusesNext['TimeStop'] = 0

		self.statusesNext['Paralysis'] = 0
		self.statusesNext['Amnesia'] = 0
		self.statusesNext['Fear'] = 0
		self.statusesNext['Maladroitness'] = 0
		self.statusesNext['CharmPerson'] = 0

		self.statusesNext['Disease'] = 0
		self.statusesNext['Poison'] = 0
		self.statusesNext['Blindness'] = 0
		self.statusesNext['Invisibility'] = 0
		self.statusesNext['Permanency'] = 0
		self.statusesNext['DelayEffect'] = 0

		self.stateMindSpellsThisTurn = 0
		self.paralyzedByIDNext = 0
		self.charmedByIDNext = 0

	def removeMindSpellEffects(self):

		self.statuses['Paralysis'] = 0
		self.statuses['Amnesia'] = 0
		self.statuses['Fear'] = 0
		self.statuses['Maladroitness'] = 0
		self.statuses['CharmPerson'] = 0
		#self.statuses['CharmMonster'] = 0

		self.statusesNext['Paralysis'] = 0
		self.statusesNext['Amnesia'] = 0
		self.statusesNext['Fear'] = 0
		self.statusesNext['Maladroitness'] = 0
		self.statusesNext['CharmPerson'] = 0

		self.stateMindSpellsThisTurn = 0
		self.paralyzedByIDNext = 0
		self.charmedByIDNext = 0

	def affectedByPermanentMindspell(self):

		if (self.statuses['Paralysis'] == 9999 
			or self.statuses['Amnesia'] == 9999 
			or self.statuses['Fear'] == 9999 
			or self.statuses['Maladroitness'] == 9999 
			or self.statuses['CharmPerson'] == 9999):
			return 1
		return 0

	def affectedByBlindness(self):

		if self.statuses['Blindness'] in [1, 2, 3, 9999]:
			return 1
		else:
			return 0

	def affectedByInvisibility(self):

		if self.statuses['Invisibility'] in [1, 2, 3, 9999]:
			return 1
		else:
			return 0

	def affectedByHaste(self):

		if self.statuses['Haste'] in [1, 2, 3, 9999]:
			return 1
		else:
			return 0

	def affectedByTimeStop(self):

		if self.statuses['TimeStop'] in [1]:
			return 1
		else:
			return 0

	def affectedByParalysis(self):

		if self.statuses['Paralysis'] in [1, 9999]:
			return 1
		else:
			return 0

	def affectedByFear(self):

		if self.statuses['Fear'] in [1, 9999]:
			return 1
		else:
			return 0

	def affectedByAmnesia(self):

		if self.statuses['Amnesia'] in [1, 9999]:
			return 1
		else:
			return 0

	def affectedByMaladroitness(self):

		if self.statuses['Maladroitness'] in [1, 9999]:
			return 1
		else:
			return 0

	def affectedByCharmPerson(self):

		if self.statuses['CharmPerson'] in [1, 9999]:
			return 1
		else:
			return 0

	def affectedByResistHeat(self):

		if self.statuses['ResistHeat'] in [9999]:
			return 1
		else:
			return 0

	def affectedByResistCold(self):

		if self.statuses['ResistCold'] in [9999]:
			return 1
		else:
			return 0

	# TODO we are inconsistent and use both checkPShield and ignoreShields - this really should be unified
	def affectedByPShield(self, checkPShield = 1, checkProtection = 1):

		if checkPShield == 1 and self.statuses['PShield'] in [1]:
			return 1
		elif checkProtection == 1 and self.statuses['Protection'] in [1, 2, 3, 9999]:
			return self.statuses['Protection']
		else:
			return 0

	def affectedByMShield(self):

		if self.statuses['MShield'] in [1]:
			return 1
		else:
			return 0

	def affectedByMMirror(self):

		if self.statuses['MagicMirror'] in [1]:
			return 1
		else:
			return 0

	def affectedByPermanency(self):

		if self.statuses['Permanency'] in [1, 2, 3, 9999]:
			return 1
		else:
			return 0

	def affectedByDelayEffect(self):

		if self.statuses['DelayEffect'] in [1, 2, 3, 9999]:
			return 1
		else:
			return 0

	def affectedByDisease(self):

		if self.statuses['Disease'] in [1, 2, 3, 4, 5, 6, 7]:
			return 1
		else:
			return 0

	def affectedByPoison(self):

		if self.statuses['Poison'] in [1, 2, 3, 4, 5, 6, 7]:
			return 1
		else:
			return 0

class WarlocksParticipant(WarlocksActor):
	'''Expands WarlocksActor class with functions specific to participants.
	'''

	def __init__(self,playerID,playerName,teamID):
		
		participantStartingHP = 15
		participantMaxHP = 16
		actorType = 1 # participant		
		WarlocksActor.__init__(self, actorType, playerName, 
								participantStartingHP, participantMaxHP)

		self.playerID = playerID
		self.teamID = teamID

		self.stateDelayedSpell = None

		self.stateStab = 0
		self.stateCastClapOfLightning = 0
		self.stateSurrender = 0
		self.destroyEOT = 0

		self.attackType = 'Physical'
		self.attackDamage = 1

		self.pronounA = ''
		self.pronounB = ''
		self.pronounC = ''

	def setHandIDs(self, offset):
		self.LHID = self.ID * offset + 1
		self.RHID = self.ID * offset + 2

	def getLHID(self):

		return self.LHID

	def getRHID(self):

		return self.RHID

	def setDestroyEOT(self):

		self.destroyEOT = 1

	def printParticipantStatus(self):

		statusStr=self.actorStatusReport()
		print(statusStr)
		

class WarlocksMonster(WarlocksActor):
	'''Expands WarlocksActor class with functions specific to monsters.
	'''

	def __init__(self, monsterTypes, controllerID, monsterType, summonerID, 
					summonerHandID, summonTurn, pronounA, pronounB, pronounC):
		
		actorType = 2 # monster
		monsterName = ''#self.getNewMonsterName(monsterType)
		WarlocksActor.__init__(self, actorType, monsterName, 
							monsterTypes[monsterType]['startHP'], 
							monsterTypes[monsterType]['maxHP'])

		self.summonerID = summonerID
		self.summonerHandID = summonerHandID
		self.summonTurn = summonTurn
		self.controllerID = controllerID
		self.monsterType = monsterType
		self.attackID = 0
		self.attackDamage = monsterTypes[monsterType]['attackDamage']
		self.attackType = monsterTypes[monsterType]['attackType'] # Physical, Fire, Ice
		self.attacksAll = monsterTypes[monsterType]['attacksAll']

		self.destroyBeforeAttack = 0
		self.destroyEOT = 0

		self.pronounA = pronounA
		self.pronounB = pronounB
		self.pronounC = pronounC

		# This is to initialize monsters with pre-defined statuses, f.e. 
		# Fire Elems come with built-in Resist Heat
		if monsterTypes[monsterType]['initialStatuses']:
			for s in monsterTypes[monsterType]['initialStatuses']:
				self.statuses[s] = monsterTypes[monsterType]['initialStatuses'][s]

	def setName(self, name):

		self.name = name
	
	def setDestroyNow(self):

		self.isAlive = 0

	def setDestroyBeforeAttack(self):

		self.destroyBeforeAttack = 1

	def setDestroyEOT(self):

		self.destroyEOT = 1

	def printMonsterStatus(self, controllerName, attackTargetName):

		statusStr = self.actorStatusReport() 
		if self.monsterType in [1, 2, 3, 4]: 
			statusStr += (', Controlled by: ' + controllerName 
							+ ', attacking: ' + attackTargetName)
		print(statusStr)
