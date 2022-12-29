from functions_debug import dprint

def importName(modulename, name):
    ''' Import a named object from a module in the context of this function.
    Source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch15s04.html
    '''
    try:
        module = __import__(modulename, globals(), locals(), [name])
    except ImportError:
        return None
    return vars(module)[name]

def parseJsonGame(matchID, spellbookData, langCode, matchPlayersInit, matchJsonFname):
	''' Initiate game variables and play a game using JSON file as a source or orders.

	Classes and variables are loaded dynamically from selected spellbook files. 
	For example, for Warlocks spellbook and for English language we load the following:
	from class_warlocks_matchdata import WarlocksMatchData
	from class_warlocks_spellbook import WarlocksSpellBook
	from class_warlocks_orders import WarlocksOrders
	from loc_warlocks_en import warlocksStringsEN, warlocksMonsterNamesEN, warlocksMonsterClassesEN, warlocksSpellNamesEN, warlocksSpellEffectsEN
	'''

	# Init match data
	matchData = importName('class_' + spellbookData['code'].lower() + '_matchdata', 
								spellbookData['code'] + 'MatchData')(matchID)

	spellbookTextStrings = importName('loc_' + spellbookData['code'].lower() + '_' + langCode.lower(), 
								spellbookData['code'].lower() + 'TextStrings' + langCode)
	commonTextStrings = importName('loc_common_' + langCode.lower(), 
								'commonTextStrings' + langCode)
	matchData.initTextStrings(spellbookTextStrings | commonTextStrings)

	spellbookSpellNames = importName('loc_' + spellbookData['code'].lower() + '_' + langCode.lower(), 
								spellbookData['code'].lower() + 'SpellNames' + langCode)
	matchData.initSpellNames(spellbookSpellNames)

	spellbookSpellEffects = importName('loc_' + spellbookData['code'].lower() + '_' + langCode.lower(), 
								spellbookData['code'].lower() + 'SpellEffects' + langCode)	
	matchData.initEffectNames(spellbookSpellEffects)

	spellbookMonsterNames = importName('loc_' + spellbookData['code'].lower() + '_' + langCode.lower(), 
								spellbookData['code'].lower() + 'MonsterNames' + langCode)	
	spellbookMonsterClasses = importName('loc_' + spellbookData['code'].lower() + '_' + langCode.lower(), 
								spellbookData['code'].lower() + 'MonsterClasses' + langCode)	
	matchData.initMonsterNames(spellbookMonsterNames, spellbookMonsterClasses)

	matchSpellBook = importName('class_' + spellbookData['code'].lower() + '_spellbook', 
								spellbookData['code'] + 'SpellBook')(matchData.spellNames)

	matchOrders = importName('class_' + spellbookData['code'].lower() + '_orders', 
								spellbookData['code'] + 'Orders')()
	matchOrders.setFilename(matchJsonFname)

	matchData.initActorsTmp(matchPlayersInit)
	matchData.processMatchStart()

	# Make turns
	while 1:

		# Turn startup and orders loading
		status = matchData.processTurnPhase0(matchOrders, matchSpellBook)
		if status != 1:
			break

		# Spellcasting
		status = matchData.processTurnPhase1(matchOrders, matchSpellBook)
		if status != 1:
			break

		# Combat
		status = matchData.processTurnPhase2(matchOrders)
		if status != 1:
			break

		# Clean-up
		status = matchData.processTurnPhase3(matchOrders)
		if status != 1:
			break

	return matchData

if __name__ == '__main__':

	availableSpellbooks = {
	1: {'code': 'Warlocks', 'title': "RavenBlack's Warlocks - ParaFC Maladroit"},
	2: {'code': 'SpellBinder', 'title': "Bartle's Original Ruleset [not implemented]"},
	3: {'code': 'MortalSpell', 'title': "Naigsa's MortalSpell Ruleset [not implemented]"},
	}
	matchID = 123456
	matchSpellbook = 1
	matchPlayersInit = [
	{'playerID': 123, 'playerName': 'BioLogIn', 'gender': 1, 'teamID': 1, 'lang': 'EN'},
	{'playerID': 445, 'playerName': 'TestFoe', 'gender': 0, 'teamID': 2, 'lang': 'EN'},
	#{'playerID': 666, 'playerName': 'TestAlly', 'gender': 2, 'teamID': 1, 'lang': 'EN'},
	#{'playerID': 777, 'playerName': 'TestFoe2', 'gender': 2, 'teamID': 2, 'lang': 'EN'},
	]
	matchJsonFname = 'tests/test_spell_35_fireball_G_monster.json'
	#matchJsonFname = 'tests/test_special_seeded_random_targets.json'
	
	# Placeholder. Should be chosen from the settings of participant we render for.
	langCode = 'EN'

	matchData = parseJsonGame(matchID, availableSpellbooks[matchSpellbook], langCode, 
										matchPlayersInit, matchJsonFname)
