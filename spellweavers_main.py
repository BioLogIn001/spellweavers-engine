from class_warlocks_matchdata import WarlocksMatchData
from class_warlocks_spellbook import WarlocksSpellBook
from class_warlocks_orders import WarlocksOrders
from loc_warlocks_en import warlocksStringsEN, warlocksMonsterNamesEN, warlocksMonsterClassesEN, warlocksSpellNamesEN, warlocksSpellEffectsEN
from functions_debug import dprint

def tmpMakeTurn(matchOrders, matchSpellBook, matchData):

	if matchData.getMatchStatus():
		return

	matchData.addLogEntry(0, 1, 'turnNum', name = matchData.currentTurn)

	matchSpellBook.clearStack()

	# Phase 1 - cast spells

	# Step 1.1 - determine gestures for the turn
	matchSpellBook.determineGestures(matchOrders, matchData)

	# Step 1.2 - print effects and gestures for the turn
	matchSpellBook.logEffectsSOT(matchOrders, matchData)
	matchSpellBook.logGestureMessages(matchData)

	# Step 1.3 - make a list of spells that match gestures for all participants
	matchSpellBook.matchSpellPattern(matchData)
	
	# Step 1.4 - select spells to cast (and their targets) for all participants
	matchSpellBook.selectSpellsForStack(matchOrders, matchData)

	# Step 1.5 - cast delayed spells, if any and if ordered, for all participants
	matchSpellBook.checkDelayedSpellCast(matchOrders, matchData)

	# Step 1.6 - sort spell queue by priority 
	matchSpellBook.sortByPriority()

	# Step 1.7 - cast spells in queue
	matchSpellBook.castSpells(matchData)

	# Step 1.8 - pre-resolution checks (elem)
	matchSpellBook.checkElementalSpellsClash(matchData)

	# Step 1.9 - resolve spells
	matchSpellBook.resolveSpells(matchData)

	# Step 1.10 - post-resolution checks (mindspells)
	matchSpellBook.checkMindSpellsClash(matchData)

	# Phase 2 - Combat

	# Step 2.1 - remove monsters killed by fast spells
	matchData.killMonstersBeforeAttack()

	# Step 2.2 - determine attack targets
	matchData.giveAttackOrders(matchOrders)

	# Step 2.3 - regular monster attacks
	matchData.attackPhase(1)

	# Step 2.4 - stabs
	matchData.checkStabs(matchOrders)

	# Step 2.5 - hasted monster attacks
	matchData.attackPhase(2)

	# Step 2.6 - timestopped monster attacks
	matchData.attackPhase(3)

	# Phase 3 - Clean-up

	# Step 3.1 - remove monsters killed in combat or by slow spells
	matchData.killMonstersEOT()

	# Step 3.2 - check spell effects that occur EOT 
	matchData.checkSicknessStatuses()
	matchData.checkAntiSpellStatuses()

	# Step 3.3 - remove players killed in combat or by spells	
	matchData.killParticipantsEOT()

	# Step 3.4 - check for game over
	matchData.checkEOTMatchEnd()
	if matchData.getMatchStatus():
		return

	# Step 3.2 - check surrender and suicide
	matchData.killSurrenderedParticipants(matchData.currentTurn)
	matchData.killSuicidedParticipants(matchOrders)

	# Step 3.3 - check for game over again, after surrenders
	matchData.checkEOTMatchEnd()
	if matchData.getMatchStatus():
		return

	# Step 3.4 - update effects on monsters
	matchData.updateStatusesOnMonstersEOT()

	# Step 3.5 - update effects on participants
	matchData.updateStatusesOnParticipantsEOT()

def parseJsonGame(matchID, matchPlayersInit, matchJsonFname):

	matchData = WarlocksMatchData(matchID)

	matchData.initTextStrings(warlocksStringsEN)

	matchData.initSpellNames(warlocksSpellNamesEN)
	matchData.initEffectNames(warlocksSpellEffectsEN)

	matchData.initMonsterNames(warlocksMonsterNamesEN, warlocksMonsterClassesEN)

	matchData.initActorsTmp(matchPlayersInit)

	matchSpellBook = WarlocksSpellBook(matchData.spellNames)

	currentTurn = 0
	matchData.setCurrentTurn(currentTurn)
	validParticipantIDs = matchData.getListOfParticipantsIDsActiveThisTurn()

	matchData.addLogEntry(0, 1, 'turnNum', name = matchData.currentTurn)
	for pID in validParticipantIDs:
		p = matchData.getParticipantByID(pID)
		matchData.addLogEntry(0, 1, 'actorBows', name = p.name)
	matchData.printLogEntriesByTurn(matchData.currentTurn)

	while 1:

		matchData.setCurrentTurn(matchData.currentTurn + 1)
		matchData.setCurrentTurnType()

		validParticipantIDs = matchData.getListOfParticipantsIDsActiveThisTurn()

		matchOrders = WarlocksOrders()
		data = matchOrders.loadOrdersFromFile(matchJsonFname)		
		matchOrders.validateOrders(data, matchData.matchID, matchData.currentTurn, 
									matchData.handIDOffset, validParticipantIDs, 
									matchSpellBook.validGestures, matchSpellBook.validSpellIDs)

		missingOrders = matchOrders.checkMissingOrders(matchData.matchID, 
										matchData.currentTurn, validParticipantIDs)
		if missingOrders:
			break

		tmpMakeTurn(matchOrders, matchSpellBook, matchData)

		matchData.printLogEntriesByTurn(matchData.currentTurn)

		matchData.printMatchActorsStatus()

	return matchData

if __name__ == '__main__':

	matchID = 123456
	matchPlayersInit = [
	{'playerID': 123, 'playerName': 'BioLogIn', 'gender': 1, 'teamID': 1},
	{'playerID': 445, 'playerName': 'TestFoe', 'gender': 0, 'teamID': 2},
	]
	matchJsonFname = 'tests/test_spell_10_haste_J_mindspells.json'

	matchData = parseJsonGame(matchID, matchPlayersInit, matchJsonFname)
