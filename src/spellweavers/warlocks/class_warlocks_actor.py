from spellweavers.default.class_default_actor import DefaultActor, DefaultMonster, DefaultParticipant


class WarlocksActor(DefaultActor):
    """Thin Warlocks wrapper over Default Actor."""

    def remove_enchantments(self, turn_num: int) -> None:
        """Overrides DefaultActor.remove_enchantments: 
        Removes Maladroitness instead of Confusion.
        Reset effects that are affected by Remove Enchantment spell.

        Both for this turn and next turn due to the fact that spells 
        (except for Protection, ResistHeat, ResistCold) start
        affecting a participant only from the next turn.

        Arguments:
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

    def remove_mindspell_effects(self, turn_num: int) -> None:
        """Overrides DefaultActor.remove_mindspell_effects: 
        Removes Maladroitness instead of Confusion.
        Reset mindspell-related effects (in case if mindspells clash).

        Arguments:
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

    def affected_by_permanent_mindspell(self, turn_num: int) -> bool:
        """Overrides DefaultActor.affected_by_permanent_mindspell: 
        Checks Maladroitness instead of Confusion.
        Check if actor is affected by a permanent mindspell.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        if (self.effects[turn_num]['Paralysis'] == self.permanent_duration
                or self.effects[turn_num]['Amnesia'] == self.permanent_duration
                or self.effects[turn_num]['Fear'] == self.permanent_duration
                or self.effects[turn_num]['Maladroitness'] == self.permanent_duration
                or self.effects[turn_num]['CharmPerson'] == self.permanent_duration):
            return True
        return False

    def affected_by_maladroitness(self, turn_num: int) -> bool:
        """Check if actor is affected by Maladroitness.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Maladroitness'] in [1, self.permanent_duration]

    def affected_by_maladroitness_permanent(self, turn_num: int) -> bool:
        """Check if actor is affected by Maladroitness permanently.

        Arguments:
            turn_num (int): turn number

        Returns:
            bool: False: not affected, True: affected
        """
        return self.effects[turn_num]['Maladroitness'] in [self.permanent_duration]


class WarlocksParticipant(WarlocksActor, DefaultParticipant):
    """Thin Warlocks wrapper over Default Participant."""

    def __init__(self, player_id: int, player_gender: int, player_name: str, 
                    team_id: int, turn_num: int, permanent_duration: int) -> None:
        """Overrides DefaultParticipant.__init__: calls it, then sets max_hp at 16.
        Init participant.

        Arguments:
            player_id (int): user ID
            player_gender (int): player gender (for pronouns)
            player_name (string): user name
            team_id (int): team ID for the match (1..8)
            turn_num (int): participant creation turn (to init effects and states; always 1 for participants)
            permanent_duration (int): constant value for permanent effect duration inherited from match_data
        """
        super().__init__(player_id, player_gender, player_name, team_id, turn_num, permanent_duration)
        self.max_hp = 16

    def get_effects_template(self) -> dict:
        """Overrides DefaultParticipant.get_effects_template: 
        Maladroitness instead of Confusion.
        Return initial dictionary for participants effects.

        Returns:
            dict: a dictionary with Warlocks participant effects
        """
        return {
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

            'Disease': 0,
            'Poison': 0,
            'Blindness': 0,
            'Invisibility': 0,
            'Permanency': 0,
            'DelayEffect': 0,
        }

    def get_states_template(self) -> dict:
        """Overrides DefaultParticipant.get_states_template: 
        Maladroitness instead of Confusion.
        Return initial dictionary for participants states.

        Returns:
            dict: a dictionary with Warlocks participant states
        """
        return {
            'hp': 0,
            'is_alive': False,
            'mindspells_this_turn': 0,
            'paralyzed_by_id': 0,
            'paralyzed_hand_id': 0,
            'charmed_by_id': 0,
            'charmed_hand_id': 0,
            'charmed_same_gestures': 0,
            'blind': 0,
            'invisible': 0,
            'outatime': 0,
            'fireballed': 0,
            'antispelled': 0,
            'clap_of_lightning': 0,
            'delayed_spell': None,
        }


class WarlocksMonster(WarlocksActor, DefaultMonster):
    """Thin Warlocks wrapper over Default Monster."""

    def get_effects_template(self) -> dict:
        """Overrides DefaultMonster.get_effects_template: 
        Maladroitness instead of Confusion.
        Return initial dictionary for monsters effects.

        Returns:
            dict: a dictionary with Warlocks monster effects
        """
        return {
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

            'Disease': 0,
            'Poison': 0,
            'Blindness': 0,
            'Invisibility': 0,
            'Permanency': 0,
            'DelayEffect': 0,
        }

    def get_states_template(self) -> dict:
        """Overrides DefaultMonster.get_states_template: 
        No 'risenfromdead' key.
        Return initial dictionary for monsters states.

        Returns:
            dict: a dictionary with Warlocks monster states
        """
        return {
            'hp': 0,
            'is_alive': False,
            'controller_id': 0,
            'attack_id': 0,
            'mindspells_this_turn': 0,
            'blind': 0,
            'invisible': 0,
            'outatime': 0,
            'fireballed': 0,
        }
