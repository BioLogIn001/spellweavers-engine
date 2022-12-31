from class_actor import Actor


class WarlocksActor(Actor):
    """Expands Actor class with Ravenblack's Warlocks-specific statuses.
    """

    def __init__(self, actor_type, name, hp, max_hp):
        """Default init for Actor + init statuded
        
        Args:
            actor_type (int): 1: participant, 2: monster
            name (string): player name
            hp (int): participant's current hit points
            max_hp (TYPE): participant's maximum hit points
        """

        Actor.__init__(self, actor_type, name, hp, max_hp)
        self.init_statuses()

    def init_statuses(self):
        """Initiate statuses that might affect the participant.
        """

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
            'AntiSpell': 0,

            'Disease': 0,
            'Poison': 0,
            'Blindness': 0,
            'Invisibility': 0,
            'Permanency': 0,
            'DelayEffect': 0
        }

        self.statuses_next = {
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

        self.state_mindspells_this_turn = 0
        self.paralyzed_by_id_next = 0
        self.paralyzed_by_id = 0
        self.paralyzed_by_id_prev = 0
        self.paralyzed_hand_id = 0
        self.paralyzed_hand_id_prev = 0
        self.charmed_by_id = 0
        self.charmed_by_id_next = 0
        self.charmed_hand_id = 0
        self.charmed_same_gestures = 0

    def decrease_status(self, status_name):
        """Decrease the current value of a requested status by one, 
        if the status is positive and not permanent (9999)
        
        Args:
            status_name (string): status code for self.statuses
        """

        if status_name in self.statuses:
            if self.statuses[status_name] != 9999 and self.statuses[status_name] > 0:
                self.statuses[status_name] -= 1

    def remove_enchantments(self):
        """Reset statuses that are affected by Remove Enchantment spell.
        """

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

        self.statuses_next['Haste'] = 0
        self.statuses_next['TimeStop'] = 0

        self.statuses_next['Paralysis'] = 0
        self.statuses_next['Amnesia'] = 0
        self.statuses_next['Fear'] = 0
        self.statuses_next['Maladroitness'] = 0
        self.statuses_next['CharmPerson'] = 0

        self.statuses_next['Disease'] = 0
        self.statuses_next['Poison'] = 0
        self.statuses_next['Blindness'] = 0
        self.statuses_next['Invisibility'] = 0
        self.statuses_next['Permanency'] = 0
        self.statuses_next['DelayEffect'] = 0

        self.state_mindspells_this_turn = 0
        self.paralyzed_by_id_next = 0
        self.charmed_by_id_next = 0

    def remove_mindspell_effects(self):
        """Reset statuses that are affected by mindspells in case if mindspells clash.
        """

        self.statuses['Paralysis'] = 0
        self.statuses['Amnesia'] = 0
        self.statuses['Fear'] = 0
        self.statuses['Maladroitness'] = 0
        self.statuses['CharmPerson'] = 0

        self.statuses_next['Paralysis'] = 0
        self.statuses_next['Amnesia'] = 0
        self.statuses_next['Fear'] = 0
        self.statuses_next['Maladroitness'] = 0
        self.statuses_next['CharmPerson'] = 0

        self.state_mindspells_this_turn = 0
        self.paralyzed_by_id_next = 0
        self.charmed_by_id_next = 0

    def affected_by_permanent_mindspell(self):
        """Check if actor is affected by a permanent mindspell.
        
        Returns:
            bool: 0: no affected, 1: affected
        """
        if (self.statuses['Paralysis'] == 9999
            or self.statuses['Amnesia'] == 9999
            or self.statuses['Fear'] == 9999
            or self.statuses['Maladroitness'] == 9999
                or self.statuses['CharmPerson'] == 9999):
            return 1
        return 0

    def affected_by_blindness(self):
        """Check if actor is affected by Blindness.
        
        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.statuses['Blindness'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_invisibility(self):
        """Check if actor is affected by Invisibility.
        
        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.statuses['Invisibility'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_haste(self):
        """Check if actor is affected by Haste.
        
        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.statuses['Haste'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_haste_permanent(self):
        """Check if actor is affected by Haste permanently.
        
        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.statuses['Haste'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_timestop(self):
        """Check if actor is affected by Timestop.
        
        Returns:
            bool: 0: no affected, 1: affected
        """
        if self.statuses['TimeStop'] in [1]:
            return 1
        else:
            return 0

    def affected_by_paralysis(self):
        """Check if actor is affected by Paralysis.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['Paralysis'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_fear(self):
        """Check if actor is affected by Fear.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['Fear'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_amnesia(self):
        """Check if actor is affected by Amnesia.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['Amnesia'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_maladroitness(self):
        """Check if actor is affected by Maladroitness.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['Maladroitness'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_charm_person(self):
        """Check if actor is affected by Charm Person.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['CharmPerson'] in [1, 9999]:
            return 1
        else:
            return 0

    def affected_by_resist_heat(self):
        """Check if actor is affected by Resist Heat.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['ResistHeat'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_resist_cold(self):
        """Check if actor is affected by Resist Cold.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['ResistCold'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_pshield(self, check_pshield=1, check_protection=1):
        """Check if actor is affected by Shield or Protection.
        
        Args:
            check_pshield (bool, optional): flag to check Shield
            check_protection (bool, optional): flag to check Protection
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if check_pshield == 1 and self.statuses['PShield'] in [1]:
            return 1
        elif check_protection == 1 and self.statuses['Protection'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_pshield_permanent(self, check_pshield=1, check_protection=1):
        """Check if actor is affected by Protection permanently.
        
        Args:
            check_pshield (bool, optional): ignored, since PShield cannot be permanent
            check_protection (bool, optional): flag to check Protection
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if check_protection == 1 and self.statuses['Protection'] in [9999]:
            return 1
        else:
            return 0

    def affected_by_mshield(self):
        """Check if actor is affected by MShield (Counter Spell).
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['MShield'] in [1]:
            return 1
        else:
            return 0

    def affected_by_mmirror(self):
        """Check if actor is affected by MMirror (Magic Mirror).
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['MagicMirror'] in [1]:
            return 1
        else:
            return 0

    def affected_by_permanency(self):
        """Check if actor is affected by Permanency.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['Permanency'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_delay_effect(self):
        """Check if actor is affected by Delay Effect.
        Notice that this does check for the effect that allows to delay spells, 
        not for already delayed / stored spells.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['DelayEffect'] in [1, 2, 3, 9999]:
            return 1
        else:
            return 0

    def affected_by_disease(self):
        """Check if actor is affected by Disease.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['Disease'] in [1, 2, 3, 4, 5, 6, 7]:
            return 1
        else:
            return 0

    def affected_by_poison(self):
        """Check if actor is affected by Poison.
        
        Returns:
            bool: 0: no affected, 1: affected
        """

        if self.statuses['Poison'] in [1, 2, 3, 4, 5, 6, 7]:
            return 1
        else:
            return 0


class WarlocksParticipant(WarlocksActor):
    """Expands WarlocksActor class with functions specific to participants.
    """

    def __init__(self, player_id, player_name, team_id):
        """Init participant.
        
        Args:
            player_id (int): user ID
            player_name (string): user name
            team_id (int): team ID for the match (1..8)
        """

        participant_starting_hp = 15
        participant_max_hp = 16
        actor_type = 1  # participant
        WarlocksActor.__init__(self, actor_type, player_name,
                               participant_starting_hp, participant_max_hp)

        self.player_id = player_id
        self.team_id = team_id

        self.state_delayed_spell = None

        self.state_stab = 0
        self.state_cast_clap_of_lightning = 0
        self.state_surrender = 0
        self.destroy_eot = 0

        self.attack_type = 'Physical'
        self.attack_damage = 1

        self.pronoun_a = ''
        self.pronoun_b = ''
        self.pronoun_c = ''

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
                 summoner_hand_id, summon_turn, pronoun_a, pronoun_b, pronoun_c):
        """Init Monster.
        
        Args:
            monster_types (list): List of alloweb monster types
            controller_id (int): ID of participant that controls the monster
            monster_type (int): Type of the monster according to monster_types
            summoner_id (int): ID of participant that summoned the monster
            summoner_hand_id (int): ID of hand that summoned the monster
            summon_turn (int): turn number on which the monster was summoned
            pronoun_a (string): preferred pronoun A (They / She / He)
            pronoun_b (string): preferred pronoun B (Them / Her / Him)
            pronoun_c (string): preferred pronoun C (Their / Hers / His)
        """

        actor_type = 2  # monster
        monster_name = ''  # self.getNewMonsterName(monster_type)
        WarlocksActor.__init__(self, actor_type, monster_name,
                               monster_types[monster_type]['start_hp'],
                               monster_types[monster_type]['max_hp'])

        self.summoner_id = summoner_id
        self.summoner_hand_id = summoner_hand_id
        self.summon_turn = summon_turn
        self.controller_id = controller_id
        self.monster_type = monster_type
        self.attack_id = 0
        self.attack_damage = monster_types[monster_type]['attack_damage']
        # Physical, Fire, Ice
        self.attack_type = monster_types[monster_type]['attack_type']
        self.attacks_all = monster_types[monster_type]['attacks_all']

        self.destroy_before_attack = 0
        self.destroy_eot = 0

        self.pronoun_a = pronoun_a
        self.pronoun_b = pronoun_b
        self.pronoun_c = pronoun_c

        # This is to initialize monsters with pre-defined statuses, f.e.
        # Fire Elems come with built-in Resist Heat
        if monster_types[monster_type]['initial_statuses']:
            for s in monster_types[monster_type]['initial_statuses']:
                self.statuses[s] = monster_types[monster_type]['initial_statuses'][s]

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
