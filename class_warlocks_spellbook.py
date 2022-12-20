from class_spellbook import SpellBook


class WarlocksSpellBook(SpellBook):
	def __init__(self):

		title = "Ravenblack's Warlocks (ParaFC Maladroit)"
		spellDict = {'C': '.', 'D': '.', 'F': '.', 'P': '.', 'S': '.', 'W': '.', 'T': '.'}
		SpellBook.__init__(self, title, spellDict)
		
		self.spellDictParaFC = {'C': 'C', 'D': 'D', 'F': 'C', 'P': 'P', 'S': 'D', 'W': 'P', 'T': 'T'}
		self.spellDictFear = {'C': 'W', 'D': 'W', 'F': 'W', 'P': 'P', 'S': 'W', 'W': 'W', 'T': 'T'}
		self.validGestures = ['C','D','F','P','S','W','>','-']
		self.validSpellIDs = range(1, 41)
		
		self.maxSpellLength = 8

		self.spellDefinitions = [
{'ID': 1,'name':"Dispel Magic",'patterns':["cDPW"],'defaultTarget':'self','duration':1,'funcName':'SpellDispelMagic'},
{'ID': 2,'name':"Counter Spell",'patterns':["WPP","WWS"],'defaultTarget':'self','duration':1,'funcName':'SpellCounterSpell'},
{'ID': 3,'name':"Magic Mirror",'patterns':["cw"],'defaultTarget':'self','duration':1,'funcName':'SpellMagicMirror'},
{'ID': 4,'name':"Summon Goblin",'patterns':["SFW"],'defaultTarget':'self','duration':1,'funcName':'SpellSummonGoblin'},
{'ID': 5,'name':"Summon Ogre",'patterns':["PSFW"],'defaultTarget':'self','duration':1,'funcName':'SpellSummonOgre'},
{'ID': 6,'name':"Summon Troll",'patterns':["FPSFW"],'defaultTarget':'self','duration':1,'funcName':'SpellSummonTroll'},
{'ID': 7,'name':"Summon Giant",'patterns':["WFPSFW"],'defaultTarget':'self','duration':1,'funcName':'SpellSummonGiant'},
{'ID': 8,'name':"Summon Fire Elemental",'patterns':["cWSSW"],'defaultTarget':'nobody','duration':1,'funcName':'SpellSummonFireElemental'},
{'ID': 9,'name':"Summon Ice Elemental",'patterns':["cSWWS"],'defaultTarget':'nobody','duration':1,'funcName':'SpellSummonIceElemental'},
{'ID':10,'name':"Haste",'patterns':["PWPWWc"],'defaultTarget':'self','duration':3,'funcName':'SpellHaste'},
{'ID':11,'name':"Time Stop",'patterns':["SPPc","SPPFD"],'defaultTarget':'self','duration':1,'funcName':'SpellTimeStop'},
{'ID':12,'name':"Protection",'patterns':["WWP"],'defaultTarget':'self','duration':3,'funcName':'SpellProtection'},
{'ID':13,'name':"Resist Heat",'patterns':["WWFP"],'defaultTarget':'self','duration':9999,'funcName':'SpellResistHeat'},
{'ID':14,'name':"Resist Cold",'patterns':["SSFP"],'defaultTarget':'self','duration':9999,'funcName':'SpellResistCold'},
{'ID':15,'name':"Paralysis",'patterns':["FFF"],'defaultTarget':'opponent','duration':1,'funcName':'SpellParalysis'},
{'ID':16,'name':"Amnesia",'patterns':["DPP"],'defaultTarget':'opponent','duration':1,'funcName':'SpellAmnesia'},
{'ID':17,'name':"Fear",'patterns':["SWD"],'defaultTarget':'opponent','duration':1,'funcName':'SpellFear'},
{'ID':18,'name':"Maladroitness",'patterns':["DSF"],'defaultTarget':'opponent','duration':1,'funcName':'SpellMaladroitness'},
{'ID':19,'name':"Charm Monster",'patterns':["PSDD"],'defaultTarget':'self','duration':1,'funcName':'SpellCharmMonster'},
{'ID':20,'name':"Charm Person",'patterns':["PSDF"],'defaultTarget':'opponent','duration':1,'funcName':'SpellCharmPerson'},
{'ID':21,'name':"Disease",'patterns':["DSFFFc"],'defaultTarget':'opponent','duration':6,'funcName':'SpellDisease'},
{'ID':22,'name':"Poison",'patterns':["DWWFWD"],'defaultTarget':'opponent','duration':6,'funcName':'SpellPoison'},
{'ID':23,'name':"Cure Light Wounds",'patterns':["DFW"],'defaultTarget':'self','duration':1,'funcName':'SpellCureLightWounds'},
{'ID':24,'name':"Cure Heavy Wounds",'patterns':["DFPW"],'defaultTarget':'self','duration':1,'funcName':'SpellCureHeavyWounds'},
{'ID':25,'name':"Anti-Spell",'patterns':["SPFP"],'defaultTarget':'opponent','duration':1,'funcName':'SpellAntiSpell'},
{'ID':26,'name':"Blindness",'patterns':["DFWFd","DWFFd"],'defaultTarget':'opponent','duration':3,'funcName':'SpellBlindness'},
{'ID':27,'name':"Invisibility",'patterns':["PPws"],'defaultTarget':'self','duration':3,'funcName':'SpellInvisibility'},
{'ID':28,'name':"Permanency",'patterns':["SPFPSDW"],'defaultTarget':'self','duration':3,'funcName':'SpellPermanency'},
{'ID':29,'name':"Delay Effect",'patterns':["DWSSSP"],'defaultTarget':'self','duration':3,'funcName':'SpellDelayEffect'},
{'ID':30,'name':"Remove Enchantment",'patterns':["PDWP"],'defaultTarget':'opponent','duration':1,'funcName':'SpellRemoveEnchantment'},
{'ID':31,'name':"Shield",'patterns':["P"],'defaultTarget':'self','duration':1,'funcName':'SpellShield'},
{'ID':32,'name':"Magic Missile",'patterns':["SD"],'defaultTarget':'opponent','duration':1,'funcName':'SpellMagicMissile'},
{'ID':33,'name':"Cause Light Wounds",'patterns':["WFP"],'defaultTarget':'opponent','duration':1,'funcName':'SpellCauseLightWounds'},
{'ID':34,'name':"Cause Heavy Wounds",'patterns':["WPFD"],'defaultTarget':'opponent','duration':1,'funcName':'SpellCauseHeavyWounds'},
{'ID':35,'name':"Fireball",'patterns':["FSSDD"],'defaultTarget':'opponent','duration':1,'funcName':'SpellFireball'},
{'ID':36,'name':"Lightning Bolt",'patterns':["DFFDD"],'defaultTarget':'opponent','duration':1,'funcName':'SpellLightningBolt'},
{'ID':37,'name':"Clap of Lightning",'patterns':["WDDc"],'defaultTarget':'opponent','duration':1,'funcName':'SpellClapOfLightning'},
{'ID':38,'name':"Finger of Death",'patterns':["PWPFSSSD"],'defaultTarget':'opponent','duration':1,'funcName':'SpellFingerOfDeath'},
{'ID':39,'name':"Fire Storm",'patterns':["SWWc"],'defaultTarget':'nobody','duration':1,'funcName':'SpellFireStorm'},
{'ID':40,'name':"Ice Storm",'patterns':["WSSc"],'defaultTarget':'nobody','duration':1,'funcName':'SpellIceStorm'}
]

		for spellDefinition in self.spellDefinitions:
			self.addSpell(spellDefinition)

	def getListOfIDsOfPermanentableSpells(self):
		''' Return a list of spell IDs that can be made permanent:
		Haste, Protection, Paralysis, Amnesia, Maladroitness, Fear, Charm Person, 
		Blindness, Invisibility, Permanency, Delay Effect
		'''

		return [10, 12, 15, 16, 17, 18, 20, 26, 27, 28, 29]

	def getListOfIDsOfMindSpells(self):
		''' Return a list of spell IDs that are considered mind spells:
		Paralysis, Amnesia, Fear, Maladroitness, Charm Monster, Charm Person
		'''

		return [15,16,17,18,19,20]

	def getListOfIDsOfStormSpells(self):
		''' Return a list of spell IDs that are considered storms:
		Fire Storm, Ice Storm
		'''

		return [39, 40]

	def getListOfIDsOfDispelMagicSpells(self):
		''' Return a list of spell IDs that are considered Dispel Magic:
		Dispel Magic
		'''

		return [1]

	def getListOfIDsOfFireStormSpells(self):
		''' Return a list of spell IDs that are considered Fire Storm:
		Fire Storm
		'''

		return [39]

	def getListOfIDsOfIceStormSpells(self):
		''' Return a list of spell IDs that are considered Ice Storm:
		Ice Storm
		'''

		return [40]

	def effectParalysis(self, gesture):
		''' Filter gestures according to ParaFC rules

		Arguments:
		gesture -- str[1], gesture to be filtered

		Returns:
		newGesture -- str[1], filtered gesture
		'''

		newGesture = gesture.translate(gesture.maketrans(self.spellDictParaFC))
		return newGesture

	def effectFear(self, gesture):
		''' Filter gestures according to Fear rules

		Arguments:
		gesture -- str[1], gesture to be filtered

		Returns:
		newGesture -- str[1], filtered gesture
		'''

		newGesture = gesture.translate(gesture.maketrans(self.spellDictFear))
		return newGesture

	def logEffectsSOT(self, matchOrders, matchData):
		''' Log messages related to effects that are checked at the Start of the Turn

		Arguments:
		matchOrders -- object, Orders-inherited
		matchData -- object, MatchData-inherited
		'''

		# Log entries for timestopped and hasted turns
		if matchData.isCurrentTurnTimestopped():
			matchData.addLogEntry(0, 7, 'effectTimeStop')
		if matchData.isCurrentTurnHasted():
			matchData.addLogEntry(0, 7, 'effectHaste')

		# Check other turn effects
		# Ignore all effects on timestopped turn
		if not matchData.isCurrentTurnTimestopped():
			for pID in matchData.getListOfParticipantsIDs():
				p = matchData.getParticipantByID(pID)
				
				# Check participant for Disease and Poison
				if p.affectedByDisease():
					if p.statuses['Disease'] in [1, 2, 3, 4, 5, 6]:
						strtmp='effectSickness'+str(p.statuses['Disease'])
						matchData.addLogEntry(p.ID, 9, strtmp, 
									name = p.name)				
				if p.affectedByPoison():
					if p.statuses['Poison'] in [1, 2, 3, 4, 5, 6]:
						strtmp='effectSickness'+str(p.statuses['Poison'])
						matchData.addLogEntry(p.ID, 9, strtmp, 
									name = p.name)

				# Check participant for mindspells
				if p.affectedByParalysis():
					if p.paralyzedHandID == p.getLHID():
						handname = matchData.getTextStingsByCode('nameLeftHand')
					# Default to RH para if for some reasons there were no clear order
					else:
						handname = matchData.getTextStingsByCode('nameRightHand')
					matchData.addLogEntry(p.ID, 8, 'effectParalysis1', 
												targetname = p.name, handname = handname)
				if p.affectedByAmnesia():
					matchData.addLogEntry(p.ID, 8, 'effectAmnesia1', 
												targetname = p.name)
				if p.affectedByFear():
					matchData.addLogEntry(p.ID, 8, 'effectFear1', 
												targetname = p.name)
				if p.affectedByMaladroitness():
					matchData.addLogEntry(p.ID, 8, 'effectMaladroitness1', 
												targetname = p.name)
				if p.affectedByCharmPerson():
					if p.charmedHandID == p.getLHID():
						handname = matchData.getTextStingsByCode('nameLeftHand')
					# Default to RH charm if for some reasons there were no clear order
					else:
						handname = matchData.getTextStingsByCode('nameRightHand')
					#TODO we need to pass here info if the charmed gesture was the same as intended.
					# if yes, we call:
					# matchData.addLogEntry(p.ID, 8, 'effectCharmPerson2', targetname = p.name, pronoun = p.pronounA)
					# if no:
					matchData.addLogEntry(p.ID, 8, 'effectCharmPerson1', 
												targetname = p.name, pronoun = p.pronounC, handname = handname)

	def logGestureMessages(self, matchData):
		''' Log messages related to shown gestures

		Arguments:
		matchData -- object, MatchData-inherited
		'''

		for participantID in matchData.getListOfParticipantsIDsActiveThisTurn():
			p = matchData.getParticipantByID(participantID)
			# For each participant taking action this turn get gestures
			gestureLH = matchData.getGestureLast(participantID, 1)
			gestureRH = matchData.getGestureLast(participantID, 2)
			# Get respective unformatted text strings
			gestureTexts = matchData.getGestureLogEntry(gestureLH, gestureRH)
			handname = matchData.getTextStingsByCode('nameLeftHand')
			# Log entried for LH (and RH if available)
			# For Warlocks, RH is omitted in case of a clap
			matchData.addLogEntry(p.ID, 1, gestureTexts[0], 
											name = p.name, pronoun = p.pronounC, handname = handname)
			if gestureTexts[1]:
				handname = matchData.getTextStingsByCode('nameRightHand')
				matchData.addLogEntry(p.ID, 1, gestureTexts[1], 
											name = p.name, pronoun = p.pronounC, handname = handname)		

	def determineGestures(self, matchOrders, matchData):
		''' Determine participants gesture for the turn based on the orders and
		effects they are affected with.

		Arguments:
		ordersTurn -- Orders object, match orders
		matchData -- WarlocksMatchData object, match data
		'''

		for participantID in matchData.getListOfParticipantsIDsActiveThisTurn():
			# For each participant consider their orders
			p = matchData.getParticipantByID(participantID)
			order = matchOrders.searchOrders(matchData.matchID, 
									matchData.currentTurn, participantID)
			gestureLH = order.gestureLH
			gestureRH = order.gestureRH
			#if matchData.currentTurnType in [1, 2]: # ignore effects on timestop turn
			if not matchData.isCurrentTurnTimestopped():
				if p.affectedByParalysis():
					# If participant is affected by Para, alter gestures in 
					# paralysed hand using spellbook rules
					if p.paralyzedByID == p.paralyzedByIDPrev:
						p.paralyzedHandID = p.paralyzedHandIDPrev
					else:
						orderOppo = matchOrders.searchOrders(matchData.matchID, 
											matchData.currentTurn, p.paralyzedByID)
						if p.ID in orderOppo.paralyzeOrders:
							p.paralyzedHandID = orderOppo.paralyzeOrders[p.ID]
					if p.paralyzedHandID == p.getLHID():
						prevGesture = matchData.getGesture(participantID, matchData.currentTurn-1, 1)
						gestureLH = self.effectParalysis(prevGesture)
						#handname = matchData.getTextStingsByCode('nameLeftHand')
					#elif paralyzeHandID == p.getRHID():
					else:
						prevGesture = matchData.getGesture(participantID, matchData.currentTurn-1, 2)
						gestureRH = self.effectParalysis(prevGesture)
						#handname = matchData.getTextStingsByCode('nameRightHand')
					#matchData.addLogEntry(p.ID, 8, 'effectParalysis1', 
					#							targetname = p.name, handname = handname)
				if p.affectedByAmnesia():
					# If participant is affected by Amnesia, for both hands 
					# use their previous gestures
					gestureLH = matchData.getGesture(participantID, matchData.currentTurn-1, 1)
					gestureRH = matchData.getGesture(participantID, matchData.currentTurn-1, 2)
					#matchData.addLogEntry(p.ID, 8, 'effectAmnesia1', 
					#							targetname = p.name)
				if p.affectedByFear():
					# If participant is affected by Fear, alter gestures in 
					# paralysed hand using spellbook rules
					gestureLH = self.effectFear(gestureLH)
					gestureRH = self.effectFear(gestureRH)
					#matchData.addLogEntry(p.ID, 8, 'effectFear1', 
					#							targetname = p.name)
				if p.affectedByMaladroitness():
					# If participant is affected by Maladroitness, use RH gesture
					# for both hands
					gestureLH = gestureRH
					#matchData.addLogEntry(p.ID, 8, 'effectMaladroitness1', 
					#							targetname = p.name)
				if p.affectedByCharmPerson():
					# If participant is affected by Charm Person, use gesture
					# selected by charmer for selected hand
					handname = ''
					charmOrder = ()
					orderOppo = matchOrders.searchOrders(matchData.matchID, 
											matchData.currentTurn, p.charmedByID)
					if p.ID in orderOppo.charmOrders:
						charmOrder = orderOppo.charmOrders[p.ID]
					#order = ordersTurn[p.charmedByID]['charmOrders'][p.ID]
					if charmOrder[0] == p.LHID:
						p.charmedHandID = p.LHID
						gestureLH = charmOrder[1]
					elif charmOrder[0] == p.RHID:
						p.charmedHandID = p.RHID
						gestureRH = charmOrder[1]
					else:
						p.charmedHandID = p.RHID
						gestureRH = '-'
			# Save updated gestures
			matchData.addGestures(participantID, matchData.currentTurn, gestureLH, gestureRH)

	def makePrecastTargetChecks(self, spell, matchData, checkBlindness = 1, checkInvisibility = 1, checkMMirror = 1):
		''' Make pre-cast checks for the spell target.
		The first type of checks is checking target ID (hand, monster, participant) and getting target object.
		The second type of checks is target visibility and mirrors.

		Arguments:
		spell -- Spell object, spell to be checked
		matchData -- WarlocksMatchData object, match data
		checkBlindness, checkInvisibility, checkMMirror -- flags to ignore or trigger specific checks
		'''

		# For timestopped turns all existing effects are ignored.
		if matchData.isCurrentTurnTimestopped():
			checkBlindness = 0
			checkInvisibility = 0
			checkMMirror = 0

		# TODO 
		# 1. currently for delayed spell cast there is no option of blindness / invis / mirroed message
		# 2. also the logic of this function in general seems convoluted. 
		# Consider maybe reworking and creating a complex message mechanism for cast report?
		caster = matchData.getActorByID(spell.casterID)

		# Check if target is a hand ID.
		if spell.targetID in matchData.getListOfParticipantsHandsIDs():
			# if the spell is cast at a hand, there is not need to check anything else ATM
			if spell.targetID % 2 == 1:
				handname = matchData.getTextStingsByCode('nameLeftHand')
			else:
				handname = matchData.getTextStingsByCode('nameRightHand')
			handowner = matchData.getParticipantByID(spell.targetID // matchData.handIDOffset)
			spell.resolve = 1
			matchData.addLogEntry(caster.ID, 2, 'castGeneralHand', 
								name = caster.name, 
								spellname = spell.name, 
								targetname = handowner.name,
								pronoun = caster.pronounC,
								handname = handname)
		# Check if target is a monster.
		elif spell.targetID in matchData.getListOfMonstersIDs():
			# If spell is cast at monster, we only need to check for 
			# Blindness and MMirror, since monsters cannot be invisible
			target = matchData.getMonsterByID(spell.targetID)
			if (spell.casterID != spell.targetID) and checkBlindness and caster.affectedByBlindness():
				matchData.addLogEntry(caster.ID, 5, 'castGeneralMissesBlindness', 
								name = caster.name, 
								spellname = spell.name, 
								targetname = target.name)
			# If a target is covered by a mirror, then it gets tricky.
			elif (spell.casterID != spell.targetID) and checkMMirror and target.affectedByMMirror():
				# If spell.mirrored flag is not set, we log spell cast message
				if spell.mirrored == 0:
					matchData.addLogEntry(caster.ID, 2, 'castGeneral', 
									name = caster.name, 
									spellname = spell.name, 
									targetname = target.name)
				# If spell.mirrored flag is set, this is the second time this function was called
				# And both caster and target are covered byu mirrors.
				# We dissolve the spell then to prevent endless loop.
				if spell.mirrored > 0:
					matchData.addLogEntry(caster.ID, 5, 'castGeneralDoubleMagicMirror',
								name = caster.name, 
								spellname = spell.name, 
								targetname = target.name)
				# If we are still on the first iteration, then we mark the spell as mirrored
				# and check the spell again after reversing caster and target IDs.
				else:
					spell.mirrored = 1
					spell.casterID = spell.targetID
					spell.targetID = caster.ID
					matchData.addLogEntry(caster.ID, 5, 'castGeneralMagicMirrorReflect',
								spellname = spell.name, 
								targetname = target.name)
					self.makePrecastTargetChecks(spell, matchData)
			# Caster sees the target with no mirrors between them, hooray
			else:
				spell.resolve = 1
				if spell.mirrored == 0:
					if spell.delayed == 0:
						matchData.addLogEntry(caster.ID, 2, 'castGeneral', 
										name = caster.name, 
										spellname = spell.name, 
										targetname = target.name)
					else:
						matchData.addLogEntry(caster.ID, 6, 'castGeneralDelayed', 
										name = caster.name, 
										spellname = spell.name, 
										pronoun = caster.pronounC,
										targetname = target.name)
		# Check if target is a participant.
		# Same logic as for monsters above, but with added invisibility checks.
		elif spell.targetID in matchData.getListOfParticipantsIDs():
			target = matchData.getParticipantByID(spell.targetID)
			if (spell.casterID != spell.targetID) and checkBlindness and caster.affectedByBlindness():
				matchData.addLogEntry(caster.ID, 5, 'castGeneralMissesBlindness', 
									name = caster.name, 
									spellname = spell.name, 
									targetname = target.name)
			elif (spell.casterID != spell.targetID) and checkInvisibility and target.affectedByInvisibility():
				matchData.addLogEntry(caster.ID, 5, 'castGeneralMissesInvisibility',
								name = caster.name, 
								spellname = spell.name, 
								targetname = target.name)
			elif (spell.casterID != spell.targetID) and checkMMirror and target.affectedByMMirror():
				if spell.mirrored == 0:
					matchData.addLogEntry(caster.ID, 2, 'castGeneral', 
									name = caster.name, 
									spellname = spell.name, 
									targetname = target.name)
				if spell.mirrored > 0:
					matchData.addLogEntry(caster.ID, 5, 'castGeneralDoubleMagicMirror',
								name = caster.name, 
								spellname = spell.name, 
								targetname = target.name)
				else:
					spell.mirrored = 1
					spell.casterID = spell.targetID
					spell.targetID = caster.ID
					matchData.addLogEntry(caster.ID, 5, 'castGeneralMagicMirrorReflect',
								spellname = spell.name, 
								targetname = target.name)
					self.makePrecastTargetChecks(spell, matchData, 
							checkBlindness, checkInvisibility, checkMMirror)
			else:
				spell.resolve = 1
				if spell.mirrored == 0:
					if spell.delayed == 0:
						matchData.addLogEntry(caster.ID, 2, 'castGeneral', 
										name = caster.name, 
										spellname = spell.name, 
										targetname = target.name)
					else:
						matchData.addLogEntry(caster.ID, 6, 'castGeneralDelayed', 
										name = caster.name, 
										spellname = spell.name, 
										pronoun = caster.pronounC,
										targetname = target.name)

		else:
			spell.targetID = 0
			spell.resolve = 1
			matchData.addLogEntry(caster.ID, 2, 'castGeneralNobody', 
								name = caster.name, spellname = spell.name)
	
	def selectSpellsForStack(self, matchOrders, matchData):
		''' Select spells to be cast this turn by this participant 
		from those they theoretically could cast based on their spellflow. 

		Arguments:
		matchOrders -- Orders object, orders for the match
		matchData -- WarlocksMatchData object, match data
		'''
		for participantID in matchData.getListOfParticipantsIDsActiveThisTurn():
		
			playerOrders = matchOrders.searchOrders(matchData.matchID, 
									matchData.currentTurn, participantID)

			castSpellLH=None
			castSpellRH=None
			castSpellBH=None
			# If participant ordered to cast a spell with a specific ID
			# search for it in the heap for each hand
			if playerOrders.orderSpellLH > 0:
				castSpellLH = self.searchSpellSetByID(1, 
								playerOrders.orderSpellLH, 
								playerOrders.participantID)
			if playerOrders.orderSpellRH > 0:
				castSpellRH = self.searchSpellSetByID(2, 
								playerOrders.orderSpellRH, 
								playerOrders.participantID)

			# If no valid orders were given, start selecting the spell from heap(s)
			# based on the following criteria:
			# - number of hands required (2-handed get priority over 1-handed)
			# - length of spell pattern (longer gets priority)
			# This way WPP is cast over P, PWPWWc over SWWc, and DWWFWD over DFWFd.
			if (castSpellLH is None) and (castSpellRH is None): # check if we can cast a spell from both hands
				castSpellBH = self.searchSpellSetByLength(1, castSpellBH, 
								2, playerOrders.participantID)
				castSpellBH = self.searchSpellSetByLength(2, castSpellBH, 
								2, playerOrders.participantID)
			if (castSpellBH is None) and (castSpellLH is None): # we cannot cast anything from BH and nothing pre-selected for LH
				castSpellLH = self.searchSpellSetByLength(1, castSpellLH, 
								1, playerOrders.participantID)
			if (castSpellBH is None) and (castSpellRH is None):  # we cannot cast anything from BH and nothing pre-selected for RH
				castSpellRH = self.searchSpellSetByLength(2, castSpellRH, 
								1, playerOrders.participantID)

			if castSpellLH:
				# If the spell was selected, choose it's target.
				castSpellLH.targetID = self.selectSpellTarget(playerOrders.orderTargetLH, 
										castSpellLH.defaultTarget, 
										playerOrders.participantID, 
										matchData)
				castSpellLH.casterID = playerOrders.participantID
				castSpellLH.castTurn = matchData.currentTurn
				caster = matchData.getParticipantByID(castSpellLH.casterID)
				# Check if it should be made permanent
				if ((castSpellLH.ID in self.getListOfIDsOfPermanentableSpells()) 
						and (caster.affectedByPermanency()) 
						and (playerOrders.makeSpellPermanent == caster.LHID)):
					castSpellLH.duration = 9999
					caster.statuses['Permanency'] = 0
					matchData.addLogEntry(caster.ID, 7, 'effectPermanency', 
											name = caster.name)
				# Check if it should be made delayed
				if ((caster.affectedByDelayEffect()) 
						and (playerOrders.delaySpell == caster.LHID)):
					caster.stateDelayedSpell = castSpellLH
					caster.stateDelayedSpell.delayed = 1
					caster.statuses['DelayEffect'] = 0
					matchData.addLogEntry(caster.ID, 7, 'effectDelaySpell', 
											name = caster.name)
				# Else add if to stack
				else:
					self.addSpellToStack(castSpellLH)

			# Repeat the same process for spell(s) selected from other hands.
			if castSpellRH:
				castSpellRH.targetID = self.selectSpellTarget(playerOrders.orderTargetRH, 
											castSpellRH.defaultTarget, 
											playerOrders.participantID, 
											matchData)
				castSpellRH.casterID = playerOrders.participantID
				castSpellRH.castTurn = matchData.currentTurn
				caster=matchData.getParticipantByID(castSpellRH.casterID)
				if ((castSpellRH.ID in self.getListOfIDsOfPermanentableSpells()) 
						and (caster.affectedByPermanency()) 
						and (playerOrders.makeSpellPermanent == caster.RHID)):
					castSpellRH.duration = 9999
					caster.statuses['Permanency'] = 0
					matchData.addLogEntry(caster.ID, 7, 'effectPermanency', 
											name = caster.name)
				if ((caster.affectedByDelayEffect()) 
						and (playerOrders.delaySpell == caster.RHID)):
					caster.stateDelayedSpell = castSpellRH
					caster.stateDelayedSpell.delayed = 1
					caster.statuses['DelayEffect'] = 0
					matchData.addLogEntry(caster.ID, 7, 'effectDelaySpell', 
											name = caster.name)
				else:
					self.addSpellToStack(castSpellRH)

			# Repeat the same process for spell(s) selected from other hands.
			if castSpellBH:
				caster = matchData.getParticipantByID(castSpellBH.casterID)
				if castSpellBH.usedHand == 1:
					castSpellBH.targetID = self.selectSpellTarget(playerOrders.orderTargetLH, 
											castSpellBH.defaultTarget, 
											playerOrders.participantID, 
											matchData)
					if ((castSpellBH.ID in self.getListOfIDsOfPermanentableSpells()) 
							and (caster.affectedByPermanency()) 
							and (playerOrders.makeSpellPermanent == caster.LHID)):
						castSpellBH.duration = 9999
						caster.statuses['Permanency'] = 0
						matchData.addLogEntry(caster.ID, 7, 'effectPermanency', 
											name = caster.name)
				if castSpellBH.usedHand == 2:
					castSpellBH.targetID = self.selectSpellTarget(playerOrders.orderTargetRH, 
											castSpellBH.defaultTarget, 
											playerOrders.participantID, 
											matchData)
					if ((castSpellBH.ID in self.getListOfIDsOfPermanentableSpells()) 
							and (caster.affectedByPermanency()) 
							and (playerOrders.makeSpellPermanent == caster.RHID)):
						castSpellBH.duration = 9999
						caster.statuses['Permanency'] = 0
						matchData.addLogEntry(caster.ID, 7, 'effectPermanency', 
											name = caster.name)
				castSpellBH.casterID = playerOrders.participantID
				castSpellBH.castTurn = matchData.currentTurn
				if ((caster.affectedByDelayEffect()) 
							and (castSpellBH.usedHand == 1) 
							and (playerOrders.delaySpell == caster.LHID)):
					caster.stateDelayedSpell = castSpellBH
					caster.stateDelayedSpell.delayed = 1
					caster.statuses['DelayEffect'] = 0
					matchData.addLogEntry(caster.ID, 7, 'effectDelaySpell', 
											name = caster.name)
				elif ((caster.affectedByDelayEffect()) 
							and (castSpellBH.usedHand == 2) 
							and (playerOrders.delaySpell == caster.RHID)):
					caster.stateDelayedSpell = castSpellBH
					caster.stateDelayedSpell.delayed = 1
					caster.statuses['DelayEffect'] = 0
					matchData.addLogEntry(caster.ID, 7, 'effectDelaySpell', 
											name = caster.name)
				else:
					self.addSpellToStack(castSpellBH)

	def checkDelayedSpellCast(self, matchOrders, matchData):
		''' Put delayed spell in queue if participant had a delayed spell 
		and gave respective orders. 

		Arguments:
		matchOrders -- Orders object, orders for the match
		matchData -- WarlocksMatchData object, match data
		'''

		for participantID in matchData.getListOfParticipantsIDsActiveThisTurn():

			playerOrders = matchOrders.searchOrders(matchData.matchID, 
									matchData.currentTurn, participantID)

			if playerOrders.castDelayedSpell == 1:
				caster = matchData.getParticipantByID(participantID)
				if caster.stateDelayedSpell is not None:
					target = matchData.getActorByID(caster.stateDelayedSpell.targetID)
					if target is not None:
						targetname = target.name
					else:
						targetname = 'nobody'
						spell.targetID = 0
					self.addSpellToStack(caster.stateDelayedSpell)
					caster.stateDelayedSpell = None

	def checkMindSpellsClash(self, matchData):
		''' Mind spells (that alter gestures for the next turn) clash 
		and fizzle (i.e. negate each other) if cast at the same target. 
		When we attempt to cast a mind spell (for example with .castSpellFear())
		we increase .stateMindSpellsThisTurn counter for the mind spell target.
		After resolving those spells (f.e. calling .resolveSpellFear()) we check
		for clashes here and remove effects for all actors that have a clash.

		Arguments:
		matchData -- WarlocksMatchData object, match data
		'''

		for p in matchData.participantList:
			if p.isAlive and p.stateMindSpellsThisTurn > 1:
				p.removeMindSpellEffects()
				#for s in self.stack:
				#	if ((s.targetID == p.ID) and (s.resolve == 1) 
				#			and (s.ID in self.getListOfIDsOfMindSpells())):
				#		s.resolve = 0
				matchData.addLogEntry(p.ID, 6, 'effectMindSpellCancel', 
										targetname = p.name, gender = p.pronounC)
		for m in matchData.monsterList:
			if m.isAlive and m.stateMindSpellsThisTurn > 1:
				m.removeMindSpellEffects()
				#for s in self.stack:
				#	if ((s.targetID == m.ID) and (s.resolve == 1) 
				#			and (s.ID in self.getListOfIDsOfMindSpells())):
				#		s.resolve = 0
				matchData.addLogEntry(m.ID, 6, 'effectMindSpellCancel', 
										targetname = m.name, gender = m.pronounC)

	def checkElementalSpellsClash(self, matchData):
		''' Elemental spells (storms and elementals) clash 
		and fizzle (i.e. negate each other) if cast / present at the turn. 
		When we attempt to cast an elemental spell, we increase 
		.stateFireStormsThisTurn counter for the caster. Here we tally all these
		counters and check here for clashes before resolving those spells.

		Arguments:
		matchData -- WarlocksMatchData object, match data
		'''

		fireStormsThisTurn = 0
		iceStormsThisTurn = 0
		for p in matchData.participantList:
			if p.isAlive:
				fireStormsThisTurn += p.stateFireStormsThisTurn
				iceStormsThisTurn += p.stateIceStormsThisTurn
		fireElementalIDs = matchData.getListOfMonstersByType(5)
		fireElementalExists = len(fireElementalIDs)
		iceElementalIDs = matchData.getListOfMonstersByType(6)
		iceElementalExists = len(iceElementalIDs)

		if fireStormsThisTurn and iceStormsThisTurn:
			# If both Firestorm(s) and Icestorm(s) were cast, fizzle storms
			for s in self.stack:
				if s.resolve == 1 and s.ID in self.getListOfIDsOfStormSpells():
					s.resolve = 0
			matchData.addLogEntry(0, 10, 'effectFireStormIceStormCancel')
	
		if fireElementalExists:
			if fireStormsThisTurn:
				# If Firestorm(s) were cast and Ice Elemental present, absorb elem
				for e in fireElementalIDs:
					matchData.setDestroyMonsterNowByID(e)
				elemname = matchData.matchMonsterNames[6][0]
				matchData.addLogEntry(0, 10, 'effectElementalAbsorbedByStorm', 
										name = elemname)
			elif iceStormsThisTurn:
				# If Icestorm(s) were cast and Fire Elemental present, fizzle storms and destroy elem
				for s in self.stack:
					if s.resolve == 1 and s.ID in self.getListOfIDsOfIceStormSpells():
						s.resolve = 0
				for e in fireElementalIDs:
					matchData.setDestroyMonsterNowByID(e)
				matchData.addLogEntry(0, 10, 'effectIceStormFireElementalCancel')

		if iceElementalExists:
			if iceStormsThisTurn:
				# If Icestorm(s) were cast and Ice Elemental present, absorb elem
				for e in iceElementalIDs:
					matchData.setDestroyMonsterNowByID(e)
				elemname = matchData.matchMonsterNames[6][0]
				matchData.addLogEntry(0, 10, 'effectElementalAbsorbedByStorm', 
										name = elemname)
			elif fireStormsThisTurn:
				# If Firestorm(s) were cast and Ice Elemental present, fizzle storms and destroy elem
				for s in self.stack:
					if s.resolve == 1 and s.ID in self.getListOfIDsOfFireStormSpells():
						s.resolve = 0
				for e in iceElementalIDs:
					matchData.setDestroyMonsterNowByID(e)
				matchData.addLogEntry(0, 10, 'effectFireStormIceElementalCancel')

	# SPELL CAST section

	''' All spells are cast in two stage - 'cast' (or 'fired' or 'started') and 'resolve'. 
	This is because some spells interact with each other before taking effect 
	(for example, Ice Storm and Fire Storm negate each other and produce a single message).
	This means we have to 'start' casting all spells, then take note of such collisions, then resolve all.

	However, this approach had to be modified due to the way targetting works (specifically we need 
	to track effects on monsters that are not yet summoned - and might not be resolved - 
	and were targeted by hand ID).

	To avoid having additional target list that would have to be mapped to existing targets later,
	we not resolve Dispel Magic, CounterSpell, Magic Mirror and all Summons (i.e. spell with IDs 1..9) 
	during cast phase, then do checks, then resolve everything else. It is not elegant, but it gets job done.

	'''

	def castSpellDispelMagic(self, spell, matchData):
		
		self.makePrecastTargetChecks(spell, matchData, 1, 1, 0)

		matchData.addLogEntry(spell.casterID, 7, 'castDispelMagicResolved')

		# Remove all non-DispelMagic spells from queue
		for s in self.stack:
			if s.ID not in self.getListOfIDsOfDispelMagicSpells():
				self.stack.remove(s)
				#s.resolve = 0
		
		# Remove all effects from all participants
		for p in matchData.participantList:
			if p.isAlive:
				p.initStatuses()

		# Shield target
		target = matchData.getActorByID(spell.targetID)
		if target is not None:
			target.statuses['PShield'] = 1
			matchData.addLogEntry(spell.casterID, 7, 'castShieldResolved', 
									targetname = target.name)

		# Destroy all monsters EOT
		for m in matchData.monsterList:
			if m.isAlive:
				m.setDestroyEOT()

	def resolveSpellDispelMagic(self, spell, matchData):

		return
				
	def castSpellCounterSpell(self, spell, matchData):
		
		self.makePrecastTargetChecks(spell, matchData, 1, 1, 0)

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castCounterSpellNobody')
		else:
			matchData.addLogEntry(spell.casterID, 7, 'castCounterSpellResolved', 
									targetname = target.name)
			target.statuses['PShield'] = 1
			target.statuses['MShield'] = 1

	def resolveSpellCounterSpell(self, spell, matchData):

		return

	def castSpellMagicMirror(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 0)

		target = matchData.getActorByID(spell.targetID)
		caster = matchData.getActorByID(spell.casterID)

		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMagicMirrorNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castMagicMirrorCountered', 
								name = caster.name)
		else: #cast at target
			matchData.addLogEntry(spell.casterID, 7, 'castMagicMirrorResolved',
									targetname = target.name)
			target.statuses['MagicMirror'] = 1

	def resolveSpellMagicMirror(self, spell, matchData):

		return

	def castSpellSummonGoblin(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

		caster = matchData.getParticipantByID(spell.casterID)
		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'сastSummonMonsterNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castSummonMonsterCountered', 
								name = caster.name, targetname = spell.name)
		else:
			monsterType = 1
			self.resolveSpellSummonMonster(spell, monsterType, matchData)

	def resolveSpellSummonGoblin(self, spell, matchData):

		return

	def castSpellSummonOgre(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

		caster = matchData.getParticipantByID(spell.casterID)
		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'сastSummonMonsterNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castSummonMonsterCountered', 
								name = caster.name, targetname = spell.name)
		else:
			monsterType = 2
			self.resolveSpellSummonMonster(spell, monsterType, matchData)

	def resolveSpellSummonOgre(self, spell, matchData):

		return

	def castSpellSummonTroll(self, spell, matchData):
		
		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

		caster = matchData.getParticipantByID(spell.casterID)
		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'сastSummonMonsterNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castSummonMonsterCountered', 
								name = caster.name, targetname = spell.name)
		else:
			monsterType = 3
			self.resolveSpellSummonMonster(spell, monsterType, matchData)

	def resolveSpellSummonTroll(self, spell, matchData):

		return

	def castSpellSummonGiant(self, spell, matchData):
		
		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

		caster = matchData.getParticipantByID(spell.casterID)
		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'сastSummonMonsterNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castSummonMonsterCountered', 
								name = caster.name, targetname = spell.name)
		else:
			monsterType = 4
			self.resolveSpellSummonMonster(spell, monsterType, matchData)

	def resolveSpellSummonGiant(self, spell, matchData):

		return

	def castSpellSummonFireElemental(self, spell, matchData):
		
		self.makePrecastTargetChecks(spell, matchData, 0, 0, 0)

		monsterType = 5
		self.resolveSpellSummonMonster(spell, monsterType, matchData)

	def resolveSpellSummonFireElemental(self, spell, matchData):

		return

	def castSpellSummonIceElemental(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 0, 0, 0)
		
		monsterType = 6
		self.resolveSpellSummonMonster(spell, monsterType, matchData)

	def resolveSpellSummonIceElemental(self, spell, matchData):

		return

	def resolveSpellSummonMonster(self, spell, monsterType, matchData):
		''' This is template monster summon function that is called by
		specific monster summon functions.
		'''
		
		# Get random pronouns and create a temporary monster.
		pronouns = matchData.getPronouns()
		newMonster = matchData.createMonster(spell.casterID, monsterType, 
										spell.casterID, 
										spell.casterID * matchData.handIDOffset + spell.usedHand, 
										spell.castTurn,
										pronouns[0], pronouns[1], pronouns[2])

		# For Goblins, Ogres, Trolls, Giants
		if monsterType in [1,2,3,4]:
			target = matchData.getActorByID(spell.targetID)
			# Determine monster controller - if monster is summoned 
			# at another monster, they share controller
			if target.type == 1: #player
				newMonster.controllerID = target.ID
			elif target.type == 2: #monster
				newMonster.controllerID = target.controllerID
			controller = matchData.getParticipantByID(newMonster.controllerID)
			monsterID = matchData.getNextMonsterID()
			# Get new ID
			newMonster.setIDs(monsterID)
			# Get a random attack target (might be overridden with orders later)
			newMonster.attackID = matchData.getRandomOpponentID(controller.ID)
			# Get name
			name = matchData.getNewMonsterName(monsterType)
			newMonster.setName(name)
			# Add monster to the list and log the event
			matchData.monsterList.append(newMonster)
			matchData.addLogEntry(spell.casterID, 3, 'castSummonMonsterResolved', 
								name = controller.name, targetname=newMonster.name)
	
		# For Fire and Ice elementals
		elif monsterType in [5,6]:
			newMonster.controllerID = spell.casterID
			# Check for other elems present on the field.
			fireElementalIDs = matchData.getListOfMonstersByType(5)
			fireElementalExists = len(fireElementalIDs)
			iceElementalIDs = matchData.getListOfMonstersByType(6)
			iceElementalExists = len(iceElementalIDs)
			# Remove previous elem of the same type right now
			if monsterType == 5 and fireElementalExists: #there are previous fire elems
				for e in fireElementalIDs:
					elem = matchData.getMonsterByID(e)
					elem.setDestroyNow()
			if monsterType == 6 and iceElementalExists: #there are previous ice elems
				for e in iceElementalIDs:
					elem = matchData.getMonsterByID(e)
					elem.setDestroyNow()

			# Request ID and name
			monsterID = matchData.getNextMonsterID()
			newMonster.setIDs(monsterID)
			name = matchData.getNewMonsterName(monsterType)
			newMonster.setName(name)
			# Add monster to the list and log the event
			matchData.monsterList.append(newMonster)
			if monsterType == 5:
				matchData.addLogEntry(spell.casterID, 4, 'castFireElementalResolved2')
				if fireElementalExists: #there are previous fire elems
					matchData.addLogEntry(spell.casterID, 6, 'effectFireElementalsMerge')
			elif monsterType == 6:
				matchData.addLogEntry(spell.casterID, 4,'castIceElementalResolved2')
				if iceElementalExists: #there are previous ice elems
					matchData.addLogEntry(spell.casterID, 6, 'effectIceElementalsMerge')

			# If both types of elems present, mark them for death before attacks
			# We do not kill them now because other elems might resolve later, and they need to merge
			fireElementalIDs = matchData.getListOfMonstersByType(5)
			fireElementalExists = len(fireElementalIDs)
			iceElementalIDs = matchData.getListOfMonstersByType(6)
			iceElementalExists = len(iceElementalIDs)

			if fireElementalExists and iceElementalExists:
				for e in fireElementalIDs:
					matchData.setDestroyMonsterBeforeAttackByID(e)
				for e in iceElementalIDs:
					matchData.setDestroyMonsterBeforeAttackByID(e)
				# TODO it seems like if multiple elems are cast on the same turn, this message would trigger many times.
				# Check and move to post-cast checks (to storms).
				matchData.addLogEntry(spell.casterID, 10, 'effectFireElementalIceElementalCancel')
			
	def castSpellHaste(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellHaste(self, spell, matchData):

		# TODO test mindspells with Haste - probably they do not work right now
		target = matchData.getActorByID(spell.targetID)

		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castHasteNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castHasteCountered', targetname = target.name)
		elif target.type == 2:
			target.statuses['Haste'] = spell.duration
		else:
			if target.statuses['Haste'] < 9999:
				target.statusesNext['Haste'] = spell.duration
				matchData.addLogEntry(spell.casterID, 7, 'castHasteResolved', targetname = target.name)

	def castSpellTimeStop(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellTimeStop(self, spell, matchData):

		# TODO consider how timestop should work with permamindspell if a new mindspell is cast during timestop
		# RB implementation allows to cancel a mindspell resolved before timestopped turn with a mindspell cast on the timestopped turn, which is tricky
		# Quote from RB rules:
		## It's possible, therefore, to negate an enchantment by casting another on yourself during a time-stopped turn. 
		## Essentially, no persistent effects are relevant in a time-stopped turn. 
		## Also, a counter-spell or shield cast during a time-stopped turn will not last into the next turn.
		target = matchData.getActorByID(spell.targetID)

		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castTimeStopNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castTimeStopCountered', targetname = target.name)
		else:
			if target.type == 1:
				target.statusesNext['TimeStop'] = 1
			else:
				target.statuses['TimeStop'] = 1	
			matchData.addLogEntry(spell.casterID, 7, 'castTimeStopResolved', 
								targetname = target.name)

	def castSpellProtection(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellProtection(self, spell, matchData):
		
		target = matchData.getActorByID(spell.targetID)

		if target is None:
			matchData.addLogEntry(spell.casterID, 5 ,'castProtectionNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castProtectionCountered', 
							targetname = target.name)
		else:
			if target.statuses['Protection'] < 9999:
				target.statuses['Protection'] = spell.duration
				matchData.addLogEntry(spell.casterID, 7, 'castProtectionResolved', 
								targetname = target.name)

	def castSpellResistHeat(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellResistHeat(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castResistHeatNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castResistHeatCountered', 
							targetname = target.name)
		elif target.type == 2 and target.monsterType == 5:
			matchData.setDestroyMonsterBeforeAttackByID(spell.targetID)
			matchData.addLogEntry(spell.casterID, 6, 'castResistHeatDestroysFireElemental')
		else:
			target.statuses['ResistHeat'] = spell.duration
			matchData.addLogEntry(spell.casterID, 7, 'castResistHeatResolved', 
							targetname = target.name)

	def castSpellResistCold(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellResistCold(self, spell, matchData):
		
		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castResistColdNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castResistColdCountered', 
							targetname = target.name)
		elif target.type == 2 and target.monsterType == 6:
			matchData.setDestroyMonsterBeforeAttackByID(spell.targetID)
			matchData.addLogEntry(spell.casterID, 6, 'castResistColdDestroysIceElemental')
		else:
			target.statuses['ResistCold'] = spell.duration
			matchData.addLogEntry(spell.casterID, 7, 'castResistColdResolved', 
							targetname = target.name)

	def castSpellMindSpell(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)
		target = matchData.getActorByID(spell.targetID)
		if target is not None:
			target.stateMindSpellsThisTurn += 1

	def castSpellParalysis(self, spell, matchData):

		self.castSpellMindSpell(spell,matchData)

	def resolveSpellParalysis(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMindSpellNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castMindSpellCountered', 
							targetname = target.name)
		elif target.affectedByPermanentMindspell():
			matchData.addLogEntry(spell.casterID, 6, 'castMindSpellOverridenByPermanent', 
							targetname = target.name, spellname = spell.name)
		else:
			if target.type == 1: # participant
				target.statusesNext['Paralysis'] = spell.duration
				target.paralyzedByIDNext = spell.casterID
			else: 
				target.statuses['Paralysis'] = spell.duration
			matchData.addLogEntry(spell.casterID, 8, 'castParalysisResolved', 
								targetname = target.name)

	def castSpellAmnesia(self, spell, matchData):

		self.castSpellMindSpell(spell,matchData)

	def resolveSpellAmnesia(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMindSpellNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castMindSpellCountered', 
							targetname = target.name)
		elif target.affectedByPermanentMindspell():
			matchData.addLogEntry(spell.casterID, 6, 'castMindSpellOverridenByPermanent', 
							targetname = target.name, spellname = spell.name)
		else:
			if target.type == 1: # participant
				target.statusesNext['Amnesia'] = spell.duration
			else: 
				target.statuses['Amnesia'] = spell.duration
			matchData.addLogEntry(spell.casterID, 8, 'castAmnesiaResolved', 
								targetname = target.name)

	def castSpellFear(self, spell, matchData):

		self.castSpellMindSpell(spell,matchData)

	def resolveSpellFear(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMindSpellNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castMindSpellCountered', 
							targetname = target.name)
		elif target.affectedByPermanentMindspell():
			matchData.addLogEntry(spell.casterID, 6, 'castMindSpellOverridenByPermanent', 
							targetname = target.name, spellname = spell.name)
		else:
			if target.type == 1: # participant
				target.statusesNext['Fear'] = spell.duration
			else: 
				target.statuses['Fear'] = spell.duration
			matchData.addLogEntry(spell.casterID, 8, 'castFearResolved', 
								targetname = target.name)

	def castSpellMaladroitness(self, spell, matchData):

		self.castSpellMindSpell(spell,matchData)

	def resolveSpellMaladroitness(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMindSpellNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castMindSpellCountered', 
							targetname = target.name)
		elif target.affectedByPermanentMindspell():
			matchData.addLogEntry(spell.casterID, 6, 'castMindSpellOverridenByPermanent', 
							targetname = target.name, spellname = spell.name)
		else:
			if target.type == 1: # participant
				target.statusesNext['Maladroitness'] = spell.duration
			else: 
				target.statuses['Maladroitness'] = spell.duration
			matchData.addLogEntry(spell.casterID, 8, 'castMaladroitnessResolved', 
								targetname = target.name)

	def castSpellCharmMonster(self, spell, matchData):

		self.castSpellMindSpell(spell,matchData)

	def resolveSpellCharmMonster(self, spell, matchData):

		caster = matchData.getActorByID(spell.casterID)
		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMindSpellNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castMindSpellCountered', 
							targetname = target.name)
		elif target.affectedByPermanentMindspell():
			matchData.addLogEntry(spell.casterID, 6, 'castMindSpellOverridenByPermanent', 
							targetname = target.name, spellname = spell.name)
		else:
			if target.type == 1: #participant
				matchData.addLogEntry(spell.casterID, 8, 'castCharmMonsterWrongTargetType', 
								targetname = target.name, pronoun = target.pronounC, name = caster.name)
			else:
				target.controllerID = caster.ID
				matchData.addLogEntry(spell.casterID, 8, 'castCharmMonsterResolved', 
								targetname = target.name, name = caster.name)

	def castSpellCharmPerson(self, spell, matchData):

		self.castSpellMindSpell(spell,matchData)

	def resolveSpellCharmPerson(self, spell, matchData):

		caster = matchData.getActorByID(spell.casterID)
		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMindSpellNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castMindSpellCountered', 
							targetname = target.name)
		elif target.affectedByPermanentMindspell():
			matchData.addLogEntry(spell.casterID, 6, 'castMindSpellOverridenByPermanent', 
							targetname = target.name, spellname = spell.name)
		else:
			if target.type == 2: #monster
				matchData.addLogEntry(spell.casterID, 8, 'castCharmPersonWrongTargetType', 
								targetname = target.name, name = caster.name)
			else:
				target.statusesNext['CharmPerson'] = spell.duration
				target.charmedByIDNext = caster.ID
				matchData.addLogEntry(spell.casterID, 8, 'castCharmPersonResolved', 
								targetname = target.name, name = caster.name)

	#def castSpellSickness(self, spell, matchData):

	#	self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellSickness(self, spell, matchData, sicknessType):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castSicknessNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castSicknessCountered', 
							targetname = target.name)
		else:
			if target.type == 2:
				matchData.setDestroyActorEOTByID(spell.targetID)
				target.statuses[sicknessType] = 1
				matchData.addLogEntry(spell.casterID, 9, 'effectSickness1', 
								name = target.name)
			else:
				target.statusesNext[sicknessType] = spell.duration
				matchData.addLogEntry(spell.casterID, 9, 'castSicknessResolved', 
								targetname = target.name)

	def castSpellDisease(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellDisease(self, spell, matchData):

		sicknessType='Disease'
		self.resolveSpellSickness(spell, matchData, sicknessType)

	def castSpellPoison(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellPoison(self, spell, matchData):

		sicknessType='Poison'
		self.resolveSpellSickness(spell, matchData, sicknessType)

	#def castSpellCureWounds(self, spell, matchData):

	#	self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellCureWounds(self, spell,matchData, healAmount):

		target = matchData.getActorByID(spell.targetID)

		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castCureWoundsNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castCureWoundsCountered', 
								targetname = target.name)
		else:
			target.increaseHP(healAmount)
			if healAmount == 2:
				target.statuses['Disease'] = 0
			matchData.addLogEntry(spell.casterID, 7, 'castCureWoundsResolved', 
								targetname = target.name)

	def castSpellCureLightWounds(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellCureLightWounds(self, spell, matchData):

		healAmount = 1
		self.resolveSpellCureWounds(spell, matchData, healAmount)

	def castSpellCureHeavyWounds(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellCureHeavyWounds(self, spell, matchData):

		healAmount=2
		self.resolveSpellCureWounds(spell, matchData, healAmount)

	def castSpellAntiSpell(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellAntiSpell(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castAntiSpellNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castAntiSpellCountered', 
							targetname = target.name)
		else:
			if target.type == 1: #participant
				target.statuses['AntiSpell'] = 1
				#target.setLastGestures(spell.targetID, '-', '-')
				matchData.addLogEntry(spell.casterID, 8, 'castAntiSpellResolved', 
								targetname = target.name)

	def castSpellBlindness(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellBlindness(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castBlindnessNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castBlindnessCountered', 
							targetname = target.name)
		else:
			# TODO consider if perm blindness is cast and then regular blindness is cast on the same turn
			# check statusesNext['Blindness'] < 9999 also?
			# same for invis perm and delay below
			if target.type == 1 and target.statuses['Blindness'] < 9999: #participant
				target.statusesNext['Blindness'] = spell.duration
				matchData.addLogEntry(spell.casterID, 8, 'castBlindnessResolved', 
								targetname = target.name)
			elif target.type == 2: #monster
				matchData.setDestroyMonsterBeforeAttackByID(spell.targetID)
				matchData.addLogEntry(spell.casterID, 11, 'castBlindnessResolvedMonster', 
								targetname = target.name)

	def castSpellInvisibility(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellInvisibility(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castInvisibilityNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castInvisibilityCountered', 
							targetname = target.name)
		else:
			if target.type == 1 and target.statuses['Invisibility'] < 9999: #participant
				target.statusesNext['Invisibility'] = spell.duration
				matchData.addLogEntry(spell.casterID, 8, 'castInvisibilityResolved', 
								targetname = target.name)
			elif target.type == 2: #monster
				matchData.setDestroyMonsterBeforeAttackByID(spell.targetID)
				matchData.addLogEntry(spell.casterID, 11, 'castInvisibilityResolvedMonster', 
								targetname = target.name)

	def castSpellPermanency(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellPermanency(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castPermanencyAndDelayNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castPermanencyAndDelayCountered', 
							targetname = target.name)
		else:
			if target.type == 1 and target.statuses['Permanency'] < 9999: #participant
				target.statusesNext['Permanency'] = spell.duration
				matchData.addLogEntry(spell.casterID, 7, 'castPermanencyAndDelayResolved', 
								targetname = target.name)

	def castSpellDelayEffect(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellDelayEffect(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castPermanencyAndDelayNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castPermanencyAndDelayCountered', 
							targetname = target.name)
		else:
			if target.type == 1 and target.statuses['DelayEffect'] < 9999: #participant
				target.statusesNext['DelayEffect'] = spell.duration
				matchData.addLogEntry(spell.casterID, 7, 'castPermanencyAndDelayResolved', 
								targetname = target.name)

	def castSpellRemoveEnchantment(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellRemoveEnchantment(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castRemoveEnchantmentNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castRemoveEnchantmentCountered', 
							targetname = target.name)
		else:
			target.removeEnchantments()
			if target.type == 1: #participant
				matchData.addLogEntry(spell.casterID, 8, 'castRemoveEnchantmentResolved', 
								targetname = target.name)
			elif target.type == 2: #monster
				matchData.setDestroyActorEOTByID(spell.targetID)
				matchData.addLogEntry(spell.casterID, 11, 'castRemoveEnchantmentResolvedMonster', 
								targetname = target.name)

	def castSpellShield(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellShield(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castShieldNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castShieldCountered')
		else:
			target.statuses['PShield'] = 1
			matchData.addLogEntry(spell.casterID, 7, 'castShieldResolved', 
								targetname = target.name)

	def castSpellMagicMissile(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellMagicMissile(self, spell, matchData):

		# ignore protection during timestopped turns, but still check shields
		checkPShield = 1
		checkProtection = not matchData.isCurrentTurnTimestopped()

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castMagicMissileNobody')
		elif target.affectedByPShield(checkPShield, checkProtection):
				matchData.addLogEntry(spell.casterID, 9, 'castMagicMissileCountered', 
								targetname = target.name)
		else:
			target.decreaseHP(1)
			matchData.addLogEntry(spell.casterID, 9, 'castMagicMissileResolved', 
								targetname = target.name)

	def resolveSpellCauseWounds(self, spell, matchData, damageAmount):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castCauseWoundsNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castCauseWoundsCountered', 
							targetname = target.name)
		else:
			target.decreaseHP(damageAmount)
			matchData.addLogEntry(spell.casterID, 9, 'castCauseWoundsResolved', 
								targetname = target.name)

	def castSpellCauseLightWounds(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellCauseLightWounds(self, spell, matchData):

		damageAmount = 2
		self.resolveSpellCauseWounds(spell, matchData, damageAmount)

	def castSpellCauseHeavyWounds(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellCauseHeavyWounds(self, spell, matchData):

		damageAmount = 3
		self.resolveSpellCauseWounds(spell, matchData, damageAmount)

	def castSpellFireball(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellFireball(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castFireballNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castFireballCountered', 
							targetname = target.name)
		else:
			if target.type == 2 and target.monsterType == 6:
				matchData.setDestroyMonsterBeforeAttackByID(spell.targetID)
				matchData.addLogEntry(spell.casterID, 11, 'castFireballIceElemental')
			elif (not matchData.isCurrentTurnTimestopped()) and target.affectedByResistHeat():
				matchData.addLogEntry(spell.casterID, 7, 'castFireballResistHeat', 
								targetname = target.name, pronoun = target.pronounA.capitalize())
			else:
				target.decreaseHP(5)
				matchData.addLogEntry(spell.casterID, 9, 'castFireballResolved', 
								targetname = target.name, pronoun = target.pronounB)

	#def castSpellLightningThingie(self, spell, matchData):

	#	self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def castSpellLightningBolt(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellLightningBolt(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castLightningBoltNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castLightningBoltCountered', 
							targetname = target.name)
		else:
			target.decreaseHP(5)
			matchData.addLogEntry(spell.casterID, 9, 'castLightningBoltResolved', 
								targetname = target.name)

	def castSpellClapOfLightning(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellClapOfLightning(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castLightningBoltNobody')
		elif target.affectedByMShield():
			matchData.addLogEntry(spell.casterID, 10, 'castLightningBoltCountered', 
							targetname = target.name)
		else:
			caster=matchData.getActorByID(spell.casterID)
			if caster.stateCastClapOfLightning == 0:
				target.decreaseHP(5)
				matchData.addLogEntry(spell.casterID, 9, 'castLightningBoltResolved', 
								targetname = target.name)
				caster.stateCastClapOfLightning += 1
			else:
				matchData.addLogEntry(spell.casterID, 10, 'castClapOfLightningFizzle',
								name = caster.name)

	def castSpellFingerOfDeath(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 1, 1, 1)

	def resolveSpellFingerOfDeath(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is None:
			matchData.addLogEntry(spell.casterID, 5, 'castFingerOfDeathNobody')
		else:
			#if target.type == 2:
			#	matchData.setDestroyEOTByID(spell.targetID)
			#elif target.type == 1:
			matchData.setDestroyActorEOTByID(spell.targetID)
			matchData.addLogEntry(spell.casterID, 9, 'castFingerOfDeathResolved', 
							targetname = target.name)		

	def castSpellFireStorm(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 0, 0, 0)
		caster = matchData.getParticipantByID(spell.casterID)
		caster.stateFireStormsThisTurn += 1

	def resolveSpellFireStorm(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is not None:
			targetname = target.name
		else:
			targetname = matchData.getTextStingsByCode('nameNobody')

		matchData.addLogEntry(spell.casterID, 9, 'castFireStormResolved')
		for p in matchData.participantList:
			if p.isAlive:
				if (not matchData.isCurrentTurnTimestopped()) and p.affectedByResistHeat():
					matchData.addLogEntry(spell.casterID, 9, 'effectResistHeat', 
									name = p.name)
				elif p.affectedByMShield():
					matchData.addLogEntry(spell.casterID, 9, 'effectStormProtectedByMShield', 
									name = p.name)
				else:	
					p.decreaseHP(5)
					matchData.addLogEntry(spell.casterID, 9, 'effectFireStormDamaged',
									targetname = p.name)		
		for m in matchData.monsterList:
			if m.isAlive:
				if (not matchData.isCurrentTurnTimestopped()) and m.affectedByResistHeat():
					matchData.addLogEntry(spell.casterID,9, 'effectResistHeat', 
									name = m.name)
				elif m.affectedByMShield():
					matchData.addLogEntry(spell.casterID, 9, 'effectStormProtectedByMShield', 
									name = m.name)
				else:	
					m.decreaseHP(5)
					matchData.addLogEntry(spell.casterID, 9, 'effectFireStormDamaged', 
									targetname = m.name)		

	def castSpellIceStorm(self, spell, matchData):

		self.makePrecastTargetChecks(spell, matchData, 0, 0, 0)
		caster = matchData.getParticipantByID(spell.casterID)
		caster.stateIceStormsThisTurn += 1

	def resolveSpellIceStorm(self, spell, matchData):

		target = matchData.getActorByID(spell.targetID)
		if target is not None:
			targetname = target.name
		else:
			targetname = matchData.getTextStingsByCode('nameNobody')

		matchData.addLogEntry(spell.casterID, 9, 'castIceStormResolved')

		for p in matchData.participantList:
			if p.isAlive:
				if (not matchData.isCurrentTurnTimestopped()) and p.affectedByResistCold():
					matchData.addLogEntry(spell.casterID, 9, 'effectResistCold', 
									name = p.name)
				elif p.affectedByMShield():
					matchData.addLogEntry(spell.casterID, 9, 'effectStormProtectedByMShield', 
									name = p.name)
				else:	
					p.decreaseHP(5)
					matchData.addLogEntry(spell.casterID, 9, 'effectIceStormDamaged', 
									targetname = p.name)		
		for m in matchData.monsterList:
			if m.isAlive:
				if (not matchData.isCurrentTurnTimestopped()) and m.affectedByResistCold():
					matchData.addLogEntry(spell.casterID, 9, 'effectResistCold', 
									name = m.name)
				elif m.affectedByMShield():
					matchData.addLogEntry(spell.casterID, 9, 'effectStormProtectedByMShield', 
									name = m.name)
				else:	
					m.decreaseHP(5)
					matchData.addLogEntry(spell.casterID, 9, 'effectIceStormDamaged', 
									targetname = m.name)		
