import re
import random


class Spell:
	''' Class for Spells (duh).

	Each spell has a lot of stuff, see comments below for now.
	'''

	def __init__(self, spellID, spellPriority, spellName, spellGestures, 
				spellDefaultTarget, spellDuration, spellbookDictionary):

		# Spell ID
		self.ID = spellID
		# spell priority, the lower priority = the earlier spell is cast
		self.priority = spellPriority
		# A string with spell name
		self.name = spellName
		# A string with default target types {nobody, self, opponent}
		self.defaultTarget = spellDefaultTarget
		# Integer, spell duration in turns
		self.duration = spellDuration
		# Gesture pattern(s) that can be used to cast this spell
		self.patterns = []

		# Transform ingame pattern notation to (reversed) patterns for both hands.
		# For example, 'SWDDc' is transformed into 'CDDWS' for the main hand
		# and 'C....' for the offhand.
		for spellNotation in spellGestures:
			notation = spellNotation
			notationReversed = spellNotation[::-1]
			offhandPatternReversedTmp = notationReversed.translate(
				notationReversed.maketrans(spellbookDictionary)
				)
			mainhandReversed = notationReversed.upper()
			offhandReversed = offhandPatternReversedTmp.upper()
			length = len(notation)
			requiresBothHandsTmp = (offhandReversed[0] != '.') + 1
			pattern = {'notation': notation, 
						'mainhandReversed': mainhandReversed, 
						'offhandReversed': offhandReversed, 
						'length': offhandReversed, 
						'handsRequired': requiresBothHandsTmp}
			self.patterns.append(pattern)

		# Dictionary entry with info about pattern used to cast an instance of a spell
		self.usedPattern = {}

		# Integer ID of caster
		self.casterID = 0
		# Integer ID of target
		self.targetID = 0
		# Integer [1, 2] of [left, right] hand used to cast the spell
		self.usedHand = 0
		# Integer, number of the turn on which the spell was cast
		self.castTurn = 0
		# Boolean flag to mark spell for future resolution
		self.resolve = 0
		# Boolean flag to check if the spell was mirrored during the resolution
		self.mirrored = 0
		# Boolean flag to check if the spell was delayed and later fired
		self.delayed = 0

	'''
	def printSpellDataTmp(self):

		print('ID: ' + str(self.ID) 
			+ ' Name: ' + self.name 
			+ ' CasterID: ' + str(self.casterID) 
			+ ' TargetID: ' + str(self.targetID) 
			+ ' UsedHand: ' + str(self.usedHand) 
			+ ' castTurn: ' + str(self.castTurn) 
			+ ' Resolve: ' + str(self.resolve))
	'''


class SpellBook:
	''' Basic SpellBook class. To be inherited by different spellbook implementations.

	Mostly has spell roster and gesture dictionary (for the match), 
	and two heaps and a stack of spells to cast (for the turn)
	'''

	def __init__(self, spellbookTitle, spellbookDictionary):
		
		self.title = spellbookTitle
		# Dictionary of possible gestures
		self.dictionary = spellbookDictionary
		# List of Spell instances possible for this spellbook
		self.spells = []

		# Lists of Spell instances that were matched with gestures on a specific turn for a specific player
		self.possibleSpellsLH = []
		self.possibleSpellsRH = []

		# List of Spell instances that were selected to cast for a specific turn
		self.stack = []

		# default value to be overridden by custom spellbooks
		self.maxSpellLength = 10

	def addSpell(self, spellDefinition, spellNames):
		''' Import spell information and populate self.spells

		Arguments:
		spellDefinition -- a dictionary with spell definitions
		'''
		
		spell = Spell(spellDefinition['ID'], 
						spellDefinition['priority'], 
					  	spellNames[spellDefinition['ID']],
						spellDefinition['patterns'], 
						spellDefinition['defaultTarget'], 
						spellDefinition['duration'],
						self.dictionary)
		self.spells.append(spell)

	def selectSpellTarget(self, orderTargetID, spellDefaultTarget, 
							participantID, matchData):
		''' Select target for the spell based on participant's orders and the 
		default target for this particular spell. 

		Arguments:
		orderTargetID -- int, targetID submitted by the participant
		spellDefaultTarget -- str, default target type of the spell (self, opponent, nobody)
		participantID -- int, ID of caster
		matchData -- MatchData-inherited object, match data

		Returns:
		targetID -- int, selected spell target
		'''

		targetID = -1
		if orderTargetID == 0:
			# Target nobody
			targetID = 0
		elif (orderTargetID > 0) and (orderTargetID in matchData.getListOfTargetsIDs()):
			# target existing actor or hand
			targetID = orderTargetID
		elif spellDefaultTarget == 'self':
			# target caster
			targetID = participantID
		elif spellDefaultTarget == 'opponent':
			# target random opponent
			targetOptions = matchData.getListOfOpponentsIDs(participantID)
			targetID = random.choice(targetOptions)
		else: # castSpellLH.defaulTarget == 'nobody':
			# Target nobody
			targetID = 0
		return targetID

	def clearStack(self):
		''' Clear stack and heaps. To be called between turns.

		This placeholder is unlikely to be used after switching to web version, 
		but we need this for JSON-fed version of engine.
		'''

		self.stack = []
		self.possibleSpellsLH = []
		self.possibleSpellsRH = []

	def addSpellToStack(self, spell):
		''' Add a spell to the self.stack to be cast this turn.

		Arguments:
		spell -- an Spell object to be added to the list
		'''

		self.stack.append(spell)

	def sortByPriority(self):
		'''Sort spells in spell.stack by priority.
		(Spells with lesser priority get cast first, so technically this is 
		not a stack, but queue.)
		'''

		self.stack.sort(key = lambda spell: spell.priority)

	def castSpells(self, matchData):
		''' Cast spells waiting in the queue, calling spell-specific function
		For example, for Dispel Magic spell we use SpellDispelMagic parameter
		from Definitions to call self.castSpellDispelMagic()

		Arguments:
		matchData -- MatchData-inherited object, match data
		'''

		for spell in self.stack:
			for d in self.spellDefinitions:
				if spell.ID == d['ID']:
					funcName = getattr(self, 'castSpell' + d['code'])
					funcName(spell, matchData)
					break

	def resolveSpells(self, matchData):
		''' Resolve spells waiting in the queue, calling spell-specific function
		For example, for Dispel Magic spell we use SpellDispelMagic parameter
		from Definitions to call self.resolveSpellDispelMagic()
		
		We resolve only spells with spell.resolve == 1, which allows to omit 
		some of the previously cast spells that were countered, clashed, etc.

		Arguments:
		matchData -- MatchData-inherited object, match data
		'''

		for spell in self.stack:
			if spell.resolve == 1:
				for d in self.spellDefinitions:
					if spell.ID == d['ID']:
						funcName = getattr(self, 'resolveSpell' + d['code'])
						funcName(spell, matchData)
						break

	def matchSpellPattern(self, matchData):
		'''Check participant's gestures to form two lists (possibleSpellsLH 
		and possibleSpellsRH) of matched spells, that could potentially be cast 
		by participant this turn.
		
		Arguments:
		participantID -- ID of the participant 
		matchData -- MatchData-inherited object, match data
		spells -- dictionary of spells from match spellBook 
		'''
		
		for participantID in matchData.getListOfParticipantsIDs():
			# Cycle through all (reversed) patterns of all spells.
			# Check these patterns against current player (reversed) pattern.
			# If specific pattern is matches, add spell to the list of
			# possible spells for the respective hand.
			gesturesLH = matchData.getGestureHistory(participantID, 1)
			gesturesRH = matchData.getGestureHistory(participantID, 2)
			# We cut all patterns to maxSpellLength cause we do not need more for matching
			patternLHReversed = gesturesLH[:-self.maxSpellLength-1:-1]
			patternRHReversed = gesturesRH[:-self.maxSpellLength-1:-1]
			for spell in self.spells:
				for pattern in spell.patterns:
					# check spell pattern for LH as mainhand
					MainhandMatch = re.search('^' + pattern['mainhandReversed'] 
										+ '.*$', patternLHReversed)
					OffhandMatch = re.search('^' + pattern['offhandReversed'] 
										+ '.*$', patternRHReversed)
					if MainhandMatch and OffhandMatch:
						l = [pattern['notation']]
						spellTmp = Spell(spell.ID,
							spell.priority,
						  	spell.name, 
							l, 
							spell.defaultTarget, 
							spell.duration,
							self.dictionary)
						spellTmp.usedPattern = pattern
						spellTmp.casterID = participantID
						self.possibleSpellsLH.append(spellTmp)
					# check spell pattern for RH as mainhand
					MainhandMatch = re.search('^' + pattern['mainhandReversed'] 
										+ '.*$', patternRHReversed)
					OffhandMatch = re.search('^' + pattern['offhandReversed'] 
										+ '.*$', patternLHReversed)
					if MainhandMatch and OffhandMatch:
						#spellTmp = spell
						l = [pattern['notation']]
						spellTmp = Spell(spell.ID,
							spell.priority, 
						  	spell.name, 
							l, 
							spell.defaultTarget, 
							spell.duration,
							self.dictionary)
						spellTmp.usedPattern = pattern
						spellTmp.casterID = participantID
						self.possibleSpellsRH.append(spellTmp)

	def searchSpellSetByID(self, hand, orderedSpellID, casterID):
		'''Search previously formed spell lists by ID.
		This is used to choose the spell to cast if
		- the player ordered this spell for this hand,
		- and this spell exists in the list of spells with matched patterns.
	
		Arguments:
		hand -- 1 for LH, 2 for RH
		orderedSpellID -- spell ID from participant's orders for the turn
		casterID -- ID of the participant that cast this spell

		Returns:
		selectedSpell -- an instance of of Spell class if spell is found,
		None otherwise.
		'''

		selectedSpell = None
		if hand == 1:
			for spell in self.possibleSpellsLH:
				if (spell.ID == orderedSpellID) and (spell.casterID == casterID):
					# return fresh instance of Spell since possibleSpellsLH is mutable
					l=[spell.usedPattern['notation']]
					selectedSpell = Spell(spell.ID, 
					  	spell.name, 
						l, 
						spell.defaultTarget, 
						spell.duration,
						self.dictionary)
					selectedSpell.usedPattern = spell.usedPattern
					selectedSpell.casterID = spell.casterID
					selectedSpell.usedHand = hand
					break
		elif hand == 2:
			for spell in self.possibleSpellsRH:
				if (spell.ID == orderedSpellID) and (spell.casterID == casterID):
					# return fresh instance of Spell since possibleSpellsRH is mutable
					l=[spell.usedPattern['notation']]
					selectedSpell = Spell(spell.ID, 
					  	spell.name, 
						l, 
						spell.defaultTarget, 
						spell.duration,
						self.dictionary)
					selectedSpell.usedPattern = spell.usedPattern
					selectedSpell.casterID = spell.casterID
					selectedSpell.usedHand = hand
					break
		return selectedSpell

	def searchSpellSetByLength(self, hand, selectedSpell, handCount, casterID):
		'''Search previously formed spell lists by length and number of hands.
		This is used to choose the spell to cast if
		- the player ordered nothing 
		- or we didn't find what player ordered in the lists.
		The longest spell gets selected.
		
		Arguments:
		hand -- 1 for LH, 2 for RH
		selectedSpell -- Spell instance previously selected by other means
		handCount -- 1 to look for 1-handed patterns only, 
		2 to look for 2-handed patterns
		casterID -- ID of the participant that cast this spell

		Returns:
		selectedSpell -- updated value for argument, None or spell.
		'''
		
		if hand == 1:
			possibleSpells = self.possibleSpellsLH
		elif hand == 2:
			possibleSpells = self.possibleSpellsRH
		for spell in possibleSpells:
			if ((spell.usedPattern['handsRequired'] == handCount) 
					and (spell.casterID == casterID)):
				if ((selectedSpell is None) or (selectedSpell.usedPattern['length'] 
						< spell.usedPattern['length'])):
					# return fresh instance of Spell since possibleSpells is mutable
					l=[spell.usedPattern['notation']]
					selectedSpell = Spell(spell.ID,
						spell.priority, 
					  	spell.name, 
						l, 
						spell.defaultTarget, 
						spell.duration,
						self.dictionary)
					selectedSpell.usedPattern = spell.usedPattern
					selectedSpell.casterID = spell.casterID
					selectedSpell.usedHand = hand
		return selectedSpell
