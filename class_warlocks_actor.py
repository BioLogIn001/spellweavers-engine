from class_actor import Actor


class WarlocksActor(Actor):
    """Expands Actor class with Ravenblack's Warlocks-specific effects and states.
    """

    def __init__(self, actor_type, name, hp, max_hp, turn_num):
        """Default init for Actor + init statuded
        
        Args:
            actor_type (int): 1: participant, 2: monster
            name (string): player name
            hp (int): participant's current hit points
            max_hp (int): participant's maximum hit points
            turn_num (int): turn number
        """

        Actor.__init__(self, actor_type, name, hp, max_hp)
        self.effects = {}
        self.states = {}
        self.init_effects_and_states(turn_num)
        self.init_effects_and_states(turn_num + 1)

    def init_effects_and_states(self, turn_num):
        """Initiate effects that might affect the participant.
        
        Args:
            turn_num (int): turn number
        """

        self.effects[turn_num] = {
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
            'AntiSpell': 0,

            'Disease': 0,
            'Poison': 0,
            'Blindness': 0,
            'Invisibility': 0,
            'Permanency': 0,
            'DelayEffect': 0,
        }

        self.states[turn_num] = {
            'mindspells_this_turn': 0,
            'paralyzed_by_id': 0,
            'paralyzed_hand_id': 0,
            'charmed_by_id': 0,
            'charmed_hand_id': 0,
            'charmed_same_gestures': 0,
        }

    def decrease_effect(self, effect_name, turn_num):
        """Decrease the current value of a requested effect by one, 
        if the effect is positive and not permanent (9999)
        
        Args:
            effect_name (string): effect code for self.effects
            turn_num (int): turn number
        """

        if effect_name in self.effects[turn_num]:
            if self.effects[turn_num][effect_name] != 9999 and self.effects[turn_num][effect_name] > 0:
                self.effects[turn_num][effect_name] -= 1

    def remove_enchantments(self, turn_num):
        """Reset effects that are affected by Remove Enchantment spell.
        
        Args:
            turn_num (int): turn number
        """

        self.effects[turn_num]['Haste'] = 0
        self.effects[turn_num]['TimeStop'] = 0
        self.effects[turn_num]['Protection'] = 0
        self.effects[turn_num]['ResistHeat'] = 0
        self.effects[turn_num]['ResistCold'] = 0

        self.effects[turn_num]['Paralysis'] = 0
        self.effects[turn_num]['Amnesia'] = 0
        self.effects[turn_num]['Fear'] = 0
        self.effects[turn_num]['Maladroitness'] = 0
        self.effects[turn_num]['CharmPerson'] = 0

        self.effects[turn_num]['Disease'] = 0
        self.effects[turn_num]['Poison'] = 0
        self.effects[turn_num]['Blindness'] = 0
        self.effects[turn_num]['Invisibility'] = 0
        self.effects[turn_num]['Permanency'] = 0
        self.effects[turn_num]['DelayEffect'] = 0

        self.effects[turn_num + 1]['Haste'] = 0
        self.effects[turn_num + 1]['TimeStop'] = 0

        self.effects[turn_num + 1]['Paralysis'] = 0
        self.effects[turn_num + 1]['Amnesia'] = 0
        self.effects[turn_num + 1]['Fear'] = 0
        self.effects[turn_num + 1]['Maladroitness'] = 0
        self.effects[turn_num + 1]['CharmPerson'] = 0

        self.effects[turn_num + 1]['Disease'] = 0
        self.effects[turn_num + 1]['Poison'] = 0
        self.effects[turn_num + 1]['Blindness'] = 0
        self.effects[turn_num + 1]['Invisibility'] = 0
        self.effects[turn_num + 1]['Permanency'] = 0
        self.effects[turn_num + 1]['DelayEffect'] = 0

    def remove_mindspell_effects(self, turn_num):
        """Reset effects that are affected by mindspells in case if mindspells clash.
        
        Args:
            turn_num (int): turn number
        """

        self.effects[turn_num]['Paralysis'] = 0
        self.effects[turn_num]['Amnesia'] = 0
        self.effects[turn_num]['Fear'] = 0
        self.effects[turn_num]['Maladroitness'] = 0
        self.effects[turn_num]['CharmPerson'] = 0

        self.effects[turn_num + 1]['Paralysis'] = 0
        self.effects[turn_num + 1]['Amnesia'] = 0
        self.effects[turn_num + 1]['Fear'] = 0
        self.effects[turn_num + 1]['Maladroitness'] = 0
        self.effects[turn_num + 1]['CharmPerson'] = 0

    def affected_by_permanent_mindspell(self, turn_num):
        """Check if actor is affected by a permanent mindspell.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """
        if (self.effects[turn_num]['Paralysis'] == 9999
            or self.effects[turn_num]['Amnesia'] == 9999
            or self.effects[turn_num]['Fear'] == 9999
            or self.effects[turn_num]['Maladroitness'] == 9999
                or self.effects[turn_num]['CharmPerson'] == 9999):
            return 1
        return 0

    def affected_by_blindness(self, turn_num):
        """Check if actor is affected by Blindness.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.effects[turn_num]['Blindness'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_invisibility(self, turn_num):
        """Check if actor is affected by Invisibility.
        
        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.effects[turn_num]['Invisibility'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_haste(self, turn_num):
        """Check if actor is affected by Haste.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.effects[turn_num]['Haste'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_haste_permanent(self, turn_num):
        """Check if actor is affected by Haste permanently.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.effects[turn_num]['Haste'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_timestop(self, turn_num):
        """Check if actor is affected by Timestop.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.effects[turn_num]['TimeStop'] in [1]:
            return 1
        else:
            return 0

    def affected_by_paralysis(self, turn_num):
        """Check if actor is affected by Paralysis.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['Paralysis'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_fear(self, turn_num):
        """Check if actor is affected by Fear.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['Fear'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_amnesia(self, turn_num):
        """Check if actor is affected by Amnesia.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['Amnesia'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_maladroitness(self, turn_num):
        """Check if actor is affected by Maladroitness.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['Maladroitness'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_charm_person(self, turn_num):
        """Check if actor is affected by Charm Person.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['CharmPerson'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_resist_heat_permanent(self, turn_num):
        """Check if actor is affected by Resist Heat.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['ResistHeat'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_resist_cold_permanent(self, turn_num):
        """Check if actor is affected by Resist Cold.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['ResistCold'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_pshield(self, turn_num, check_pshield=1, check_protection=1):
        """Check if actor is affected by Shield or Protection.
        
        Args:
            turn_num (int): turn number
            check_pshield (bool, optional): flag to check Shield
            check_protection (bool, optional): flag to check Protection
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if check_pshield == 1 and self.effects[turn_num]['PShield'] in [1]:
            return 1
        elif check_protection == 1 and self.effects[turn_num]['Protection'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_pshield_permanent(self, turn_num, check_pshield=1, check_protection=1):
        """Check if actor is affected by Protection permanently.
        
        Args:
            turn_num (int): turn number
            check_pshield (bool, optional): ignored, since PShield cannot be permanent
            check_protection (bool, optional): flag to check Protection
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if check_protection == 1 and self.effects[turn_num]['Protection'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_mshield(self, turn_num):
        """Check if actor is affected by MShield (Counter Spell).

        Args:
            turn_num (int): turn number
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['MShield'] in [1]:
            return 1
        else:
            return 0

    def affected_by_mmirror(self, turn_num):
        """Check if actor is affected by MMirror (Magic Mirror).
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['MagicMirror'] in [1]:
            return 1
        else:
            return 0

    def affected_by_permanency(self, turn_num):
        """Check if actor is affected by Permanency.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['Permanency'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_delay_effect(self, turn_num):
        """Check if actor is affected by Delay Effect.
        Notice that this does check for the effect that allows to delay spells, 
        not for already delayed / stored spells.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['DelayEffect'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_disease(self, turn_num):
        """Check if actor is affected by Disease.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['Disease'] in [1, 2, 3, 4, 5, 6, 7]:
            return 1
        else:
            return 0

    def affected_by_poison(self, turn_num):
        """Check if actor is affected by Poison.
        
        Args:
            turn_num (int): turn number

        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.effects[turn_num]['Poison'] in [1, 2, 3, 4, 5, 6, 7]:
            return 1
        else:
            return 0


class WarlocksParticipant(WarlocksActor):
    """Expands WarlocksActor class with functions specific to participants.
    """

    def __init__(self, player_id, player_name, team_id, turn_num):
        """Init participant.
        
        Args:
            player_id (int): user ID
            player_name (string): user name
            team_id (int): team ID for the match (1..8)
            turn_num (TYPE): Description
        """

        participant_starting_hp = 15
        participant_max_hp = 16
        actor_type = 1  # participant
        WarlocksActor.__init__(self, actor_type, player_name,
                               participant_starting_hp, participant_max_hp, turn_num)

        self.player_id = player_id
        self.team_id = team_id

        self.state_delayed_spell = None

        self.state_stab = 0
        self.state_cast_clap_of_lightning = 0
        self.state_surrender = 0
        self.destroy_eot = 0

        self.attack_type = 'Physical'
        self.attack_damage = 1

        #self.pronoun_a = ''
        #self.pronoun_b = ''
        #self.pronoun_c = ''

    def set_hands_ids(self, offset):
        """Set IDs for participant's hands. 
        Current implementation would set IDs to 21 and 22 for participant with ID 2, etc.
        
        Args:
            offset (int): offset for hand IDs (for Warlocks set to 10)
        """

        self.lh_id = self.id * offset + 1
        self.rh_id = self.id * offset + 2

    def get_lh_id(self):
        """Get ID of participant's LH
        
        Returns:
            int: left hand ID
        """

        return self.lh_id

    def get_rh_id(self):
        """Get ID of participant's RH
        
        Returns:
            int: right hand ID
        """

        return self.rh_id

    def set_destroy_eot(self):
        """Set flag to destroy pariticpant at the end of this turn
        """

        self.destroy_eot = 1


class WarlocksMonster(WarlocksActor):
    """Expands WarlocksActor class with functions specific to monsters.
    """

    def __init__(self, monster_types, controller_id, monster_type, summoner_id,
                 summoner_hand_id, summon_turn, gender, turn_num):
        """Init Monster.
        
        Args:
            monster_types (list): List of alloweb monster types
            controller_id (int): ID of participant that controls the monster
            monster_type (int): Type of the monster according to monster_types
            summoner_id (int): ID of participant that summoned the monster
            summoner_hand_id (int): ID of hand that summoned the monster
            summon_turn (int): turn number on which the monster was summoned
            gender (int): gender
            turn_num (int): turn number
        """

        actor_type = 2  # monster
        monster_name = ''  # self.getNewMonsterName(monster_type)
        WarlocksActor.__init__(self, actor_type, monster_name,
                               monster_types[monster_type]['start_hp'],
                               monster_types[monster_type]['max_hp'],
                               turn_num)

        self.summoner_id = summoner_id
        self.summoner_hand_id = summoner_hand_id
        self.summon_turn = summon_turn
        self.gender = gender
        self.controller_id = controller_id
        self.monster_type = monster_type
        self.attack_id = 0
        self.attack_damage = monster_types[monster_type]['attack_damage']
        # Physical, Fire, Ice
        self.attack_type = monster_types[monster_type]['attack_type']
        self.attacks_all = monster_types[monster_type]['attacks_all']

        self.destroy_before_attack = 0
        self.destroy_eot = 0

        #self.pronoun_a = pronoun_a
        #self.pronoun_b = pronoun_b
        #self.pronoun_c = pronoun_c

        # This is to initialize monsters with pre-defined effects, f.e.
        # Fire Elems come with built-in Resist Heat
        if monster_types[monster_type]['initial_effects']:
            for s in monster_types[monster_type]['initial_effects']:
                self.effects[turn_num][s] = monster_types[monster_type]['initial_effects'][s]

    def set_name(self, name):
        """Set monster name
        
        Args:
            name (string): name of the monster
        """

        self.name = name

    def destroy_now(self):
        """Destroy monster immediately.
        """

        self.is_alive = 0

    def set_destroy_before_attack(self):
        """Flag monster to be destroyed this turn before attack phase.
        """

        self.destroy_before_attack = 1

    def set_destroy_eot(self):
        """Flag monster to be destroyed before the end of this turn.
        """

        self.destroy_eot = 1
