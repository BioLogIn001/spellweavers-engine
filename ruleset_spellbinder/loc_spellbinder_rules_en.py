"""Text lines for English rules for Spellbinder spells.

Sources:
http://www.gamecabinet.com/rules/WavingHands.html
https://www.andrew.cmu.edu/user/gc00/reviews/spellcaster.html
"""

spellbinder_spell_descriptions_en = {
    1: """Prevents all non-"Dispel Magic" spells from being cast this turn. Removes all active (temporary and permanent) effects from all participants and monsters (but does not remove spells already stored by Delay Effect). Kills all monsters at the end of turn, allowing them to attack. If the target is a monster or a player, affect them with Physical Shield for 1 turn.
    Note that while Dispel Magic would also remove visibility effects (Blindness and Invisibility), the visibility changes will take place only on the next turn. For the cast turn of Dispel Magic visibility would still affect gesture and log visibility, spell targetting, and attack targetting.
    Can be successfully cast at any target, including nobody (however, the Physical Shield is only granted if the target is a player or a monster). Cannot cannot be made permanent.""",
    2: """Affects the target with Magic Shield and Physical Shield for 1 turn. Magic Shield counters most spells cast at the target (except for Finger of Death) and negates Fire Storm and Ice Storm effects on the target. Physical Shield protects the target from attacks.
    Fizzles if cast at nobody or at illegal targets (hands / not summoned monster). Casting at a monster that is summoned this turn fizzles Counter Spell since the monster is summoned only after all Counter Spells resolve.
    Can be cast at a player or a monster. Cannot be made permanent.""",
    3: """Affects the target with Magic Mirror for 1 turn. The Magic Mirror effect reflects all spells directed at the target back to the caster but does not affect other actions (monster attacks, stabs).
    Magic Mirror does not trigger for spells cast at self.
    Magic Mirror effect triggers if the spell is about to hit its target, so if a caster casts a spell at another target that is not visible to them (either the caster is affected with Blindness or the target is affected with invisibility) then Magic Mirror does not trigger (since the spell had missed). The same is true for the reflected spells - if the spell is reflected from the Magic Mirror, but the initial target does not see the initial caster, then the spell is considered to be cast at nobody (this is how the RB rules were worded but not how RB was implemented). If both caster and target are covered with Magic Mirrors, the spell also fizzles (this is not how it was implemented by RB).
    Magic Mirror can be countered, which normally is a non-issue since Magic Shield also counters everything that could potentially be mirrored. However, if a spell that cannot be countered (such as Finger of Death) is cast at the same target as Counter Spell, then the target's Magic Mirror would be countered and Finger of Death would hit.
    Note that if the effect of reflected spell required an order (f.e. reflected Paralysis or Charm Person), the orders will be given by the player affected by Magic Mirror effect, not by Magic Mirror caster. If Magic Mirror was cast at a monster, the orders will be given by monsters controller (in RB's implementation the effect didn't take place in this case).
    Can be successfully cast at players and monsters. Cannot be made permanent.""",
    4: """Summons a Goblin with 1 physical attack damage, 1 HP, and 2 max HP.
    Can be successfully cast at players and monsters. If cast at a player, this player would be the monster's controller. If cast at a monster, the new monster's controller would be the same as the old monster's controller. Casting at a monster summoned this turn works the same way as casting it at nobody.
    Unless monster controller gives specific order, newly summoned monsters attack a random opponent player. If monster's controller is dead, the monster will continue attacking the same target until killed or charmed and re-targeted.
    Cannot be made permanent.""",
    5: """Summons an Ogre with 2 physical attack damage, 2 HP, and 3 max HP.
    Can be successfully cast at players and monsters. If cast at a player, this player would be the monster's controller. If cast at a monster, the new monster's controller would be the same as the old monster's controller. Casting at a monster summoned this turn works the same way as casting it at nobody.
    Unless monster controller gives specific order, newly summoned monsters attack a random opponent player. If monster's controller is dead, the monster will continue attacking the same target until killed or charmed and re-targeted.
    Cannot be made permanent.""",
    6: """Summons a Troll with 3 physical attack damage, 3 HP, and 4 max HP.
    Can be successfully cast at players and monsters. If cast at a player, this player would be the monster's controller. If cast at a monster, the new monster's controller would be the same as the old monster's controller. Casting at a monster summoned this turn works the same way as casting it at nobody.
    Unless monster controller gives specific order, newly summoned monsters attack a random opponent player. If monster's controller is dead, the monster will continue attacking the same target until killed or charmed and re-targeted.
    Cannot be made permanent.""",
    7: """Summons a Giant with 4 physical attack damage, 4 HP, and 5 max HP.
    Can be successfully cast at players and monsters. If cast at a player, this player would be the monster's controller. If cast at a monster, the new monster's controller would be the same as the old monster's controller. Casting at a monster summoned this turn works the same way as casting it at nobody.
    Unless monster controller gives specific order, newly summoned monsters attack a random opponent player. If monster's controller is dead, the monster will continue attacking the same target until killed or charmed and re-targeted.
    Cannot be made permanent.""",
    8: """Summons a Fire Elemental with 3 fire attack damage, 3 HP, and 4 max HP. Fire Elemental attacks all players and monsters each turn, ignoring visibility. Fire Elemental is affected with a permanent Resist Heat effect. Fire Elemental has no controller.
    The latest Fire Elemental absorbs the previous Fire Elemental. Fire Elemental and Ice Elemental negate each other, both dissolving without attacks.
    Fire Elemental is absorbed by Fire Storm without additional effects (and does not get to attack this turn). Fire Elemental negates Ice Storm and is destroyed by it (and does not get to attack this turn).
    Note that in RB's implementation Elementals attacked despite being affected with Fear or Maladroitness. In this implementation this is not the case.
    Can be successfully cast at any target. Cannot be countered. Cannot be made permanent.""",
    9: """Summons an Ice Elemental with 3 ice attack damage, 3 HP, and 4 max HP. Ice Elemental attacks all players and monsters each turn, ignoring visibility. Ice Elemental is affected with a permanent Resist Cold effect. Ice Elemental has no controller.
    The latest Ice Elemental absorbs the previous Ice Elemental. Fire Elemental and Ice Elemental negate each other, both dissolving without attacks.
    Ice Elemental is absorbed by Ice Storm without additional effects (and does not get to attack this turn). Ice Elemental negates Fire Storm and is destroyed by it (and does not get to attack this turn). Ice Elemental is instantly destroyed by Fireball (and does not get to attack this turn).
    Note that in RB's implementation Elementals attacked despite being affected with Fear or Maladroitness. In this implementation this is not the case.
    Can be successfully cast at any target. Cannot be countered. Cannot be made permanent.""",
    10: """If the target is a monster, this monster gains an additional attack for the duration of the spell effect (3 turns). These additional attacks happen after regular attacks and have the same target as the regular attack. The monster dealt lethal damage during the regular attack gets to have hasted attack before dying. This affects all monsters, including elementals (which is not how it worked at RB).
    If the target is a player, this player gets additional (hasted) turns after their regular turns for the duration of the effect (3 turns). If several players are affected by Haste, their hasted turns happen at the same time. Hasted turns are considered to be an extension of normal turns, so if the next turn is hasted, the effects (except Magic Mirror) do not expire or trickle down; thus it is possible, for example, to break a mindspell that was resolved during the normal turn by casting another mindspell at the same target during the hasted turn. Similarly, it is possible to cast a Counter Spell during the normal turn to protect the target from spells on both normal and hasted turns (and, f.e. cast Storm on the hasted turn). However, if an effect requires orders from a non-hasted player (f.e. Paralysis and Charm Person), it does not occur during the hasted turn, which, in turn, resets the hand choice for Paralysis.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    11: """If the target is a monster, this monster gains an additional attack this turn. This additional attack happens after regular attacks (and after hasted attacks, if any) and has the same target as the regular attack, but ignores all types of shields and protections, as well as visibility. The monster dealt lethal damage during the regular attack still gets to have a timestopped attack before dying.
    If the target is a player, this player gets an additional (timestopped) turn after this turn ends. If several players are affected by Timestop, their timestopped turns happen at the same time. During timestopped turns all lasting effects (including protection, resists, blindness) are ignored by timestopped players (note that Shield spells and Magic Mirror spells resolved during timestoped turns take their effect) but are preserved in the same way as hasted turn would behave. However, non-timestopped players do not see gestures of timestopped players (as if the timestopped players were both hasted and invisible).
    While lasting effects are ignored during Timestopped turns, a Timestopped player still can take special actions like delaying (banking) spells, firing banked spells, and making spells permanent.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    12: """Grants Physical Shield to the target for 3 turns, starting with the cast turn.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    13: """Grants permanent Resist Heat effect to the target, starting with the cast turn. Targets affected by this status ignore all fire damage (Fireball, Fire Elemental attacks, Fire Storm).
    If the target is Fire Elemental, it is instantly destroyed and does not get to attack this turn.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Always permanent.""",
    14: """Grants permanent Resist Cold effect to the target, starting with the cast turn. Targets affected by this status ignore all cold damage (Ice Elemental attacks, Ice Storm).
    If the target is Ice Elemental, it is instantly destroyed and does not get to attack this turn.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Always permanent.""",
    15: """If the target is a monster, it cannot attack this turn, expect for elementals, which ignore this effect.
    If the target is a player, for the next turn caster may choose the hand; the gesture for the chosen hand will be determined from the previous gesture of the same hand using the following method: - = -, > = >, C = F, D = D, F = F, P = P, S = D, W = P. If the target was paralyzed by the same caster during the previous turn and is paralyzed again, the caster does not get to choose the hand again and the same hand is paralyzed (please check Haste and Timestop descriptions for specifics of Paralysis during additional turns).
    Is a mindspell, clashes with other mindspells (Paralysis, Maladroitness, Fear, Amnesia, Charm Monster, Charm Person).
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    16: """If the target is a monster, this turn it will attack the same target as the last turn.
    If the target is a player, for the next turn both their hands repeat the same gestures.
    Is a mindspell, clashes with other mindspells (Paralysis, Maladroitness, Fear, Amnesia, Charm Monster, Charm Person).
    Can be successfully cast at monsters (including newly summoned) and players. Can be made permanent.""",
    17: """If the target is a monster, if has not effect.
    If the target is a player, for the next turn they cannot show gestures C, D, F, S in either hand.
    Is a mindspell, clashes with other mindspells (Paralysis, Maladroitness, Fear, Amnesia, Charm Monster, Charm Person).
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    18: """If the target is a monster, it will attack a random target this turn.
    If the target is a player, next turn a random hand of theirs gestures a random gesture out of six (CDFPSW).
    Is a mindspell, clashes with other mindspells (Paralysis, Maladroitness, Fear, Amnesia, Charm Monster, Charm Person).
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    19: """If the target is a monster, the caster becomes its controller and can command the monster (including the cast turn).
    If the target is a player, the spell has no effect.
    Is a mindspell, clashes with other mindspells (Paralysis, Maladroitness, Fear, Amnesia, Charm Monster, Charm Person).
    Note, that while this is a mindspell, it takes place immediately and does not produce a lasting effect as other mindspells do. Thus, its duration cannot be affected by Permanency, Haste, Timestop, etc, and it cannot be removed with Remove Enchantment or Dispel Magic.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    20: """If the target is a monster, the spell has no effect.
    If the target is a player, next turn the caster can choose the hand and the gesture to be shown by the selected target's hand.
    Is a mindspell, clashes with other mindspells (Paralysis, Maladroitness, Fear, Amnesia, Charm Monster, Charm Person).
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    21: """If the target is a monster, it dies at the end of the cast turn, after attacks.
    If the target is a player, it dies at the end of the sixth turn, counting the cast turn, unless the effect is cured with Cure Heavy Wounds or Remove Enchantment (or Dispel Magic).
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    22: """Same as Disease, except cannot be cured by Cure Serious Wounds.
    If the target is a monster, it dies at the end of the cast turn, after attacks.
    If the target is a player, it dies at the end of the sixth turn, counting the cast turn, unless the effect is cured with Remove Enchantment (or Dispel Magic).
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    23: """Heals target for 1 HP, respecting target max HP.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    24: """Heals target for 2 HP, respecting target max HP. Removes Disease effect from the target.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    25: """If the target is a monster, the spell has no effect.
    If the target is a player, their gestures up to and including this turn do not count for the upcoming turns. Please note that under this ruleset the gestures themselves are still preserved, so spells like Paralyse and Amnesia will work based on the gestures shown by target, and not based on non-gesture ('-').
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    26: """If the target is a monster, it is instantly destroyed and does not get to attack this turn.
    If the target is a player, they become blind for the duration of the spell (3 turns), starting from the next turn. Blind players cannot cast spells at or attack anyone but themselves. For targetting purposes Blindness effect is checked at the beginning of the turn, so if a Blindness is removed during the turn (by Remove Enchantment or Dispel Magic), the target cannot cast spells or attack others no matter the spell priority.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    27: """If the target is a monster, it is instantly destroyed and does not get to attack this turn.
    If the target is a player, they become invisible for the duration of the spell (3 turns), starting from the next turn. Invisible players cannot be the target of spells or be the attack target (unless they are the caster or the attacker themselves). For targetting purposes Invisibility effect is checked at the beginning of the turn, so if Invisibility is removed during the turn (by Remove Enchantment or Dispel Magic), the target cannot be hit by spells or attacks no matter spell priority.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Can be made permanent.""",
    28: """If the target is a monster, this spell has no effect.
    If the target is a player, for the next 3 turns the player gets an option to make the spell they cast with the selected hand permanent (i.e. have its duration set to infinity). Only the following spells can be made permanent Haste, Protection, Paralysis, Amnesia, Maladroitness, Fear, Charm Person, Blindness, Invisibility, Permanency, Delay Effect. Note that making Permanency or Delay Effect permanent means only removing the 3-turn duration of an effect, but once the order (to make a spell permanent or to delay a spell) is given, the effect is still gone.
    Moreover, a spell will only be made permanent if it was successfully resolved. However, you only get one attempt to make something permanent - an order to make a spell permanent would remove the permanency effect no matter what else.
    If a mindspell was successfully made permanent, other mindspells cast at the same target later will fail. If a player is affected with a mindspell that prevents them from surrendering (Paralysis, Amnesia, Charm Person), they get a special forfeit option.
    Please note that under this spellbook permanent mindspells like Confusion, Paralysis and Charm Person have their fist effect repeated (the gesture that ended up being shown initially will be shown repeatedly, rather than each time playing the effect as a new cast).
    Can be countered. Can be made permanent.""",
    29: """If the target is a monster, this spell has no effect.
    If the target is a player, for the next 3 turns the player gets an option to delay the spell they cast with the selected hand. Any spell can be delayed. If the order is given, and there is a spell that could be cast from the selected hand, this spell is removed from the spell queue (before any other checks or effects, even Dispel Magic, take effect). If the spell is successfully delayed ("banked"), it can be fired by submitting a special order during any turn. The spell uses the same targets, if any, that were set when it was originally cast.
    Only one spell can be delayed by one player; subsequent delays replace previous delayed spells. However, the player can fire delayed spell and then store another spell on the same turn.
    Dispel Magic and Remove Enchantment remove the delay effect state from a player if the spell has not been delayed yet. However, they do not remove the successfully delayed spell.
    Can be countered. Can be made permanent.""",
    30: """If the target is a monster, all "enchantment" effects affecting this monster are immediately removed, and the monster dies after attack.
    If the target is a player, all effects affecting this player are immediately removed.
    The following effects are considered to be "enchantment" for the purposes of the spell: Haste, TimeStop, Protection, Resist Heat, Resist Cold, Paralysis, Amnesia, Fear, Maladroitness, Charm Person, Disease, Poison, Blindness, Invisibility, Permanency, Delay Effect. Note that Shield (P) is not considered to be an enchantment, and neither is Charm Monster (despite being considered a mind spell).
    Can be countered. Cannot be made permanent.""",
    31: """Grants Physical Shield to the target for 1 turn, starting with the cast turn.
    Can be successfully cast at monsters (including newly summoned) and players. Cannot be countered (but since Counterspell also provides a Shield, that does not affect anything). Cannot be made permanent.""",
    32: """Deals 1 physical damage to any target. Is negated by the Physical shield effect.
    Can be successfully cast at monsters (including newly summoned) and players. Cannot be countered (but since Counterspell also provides a Shield, the damage is not done anyway). Cannot be made permanent.""",
    33: """Deals 2 magical damage to any target.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    34: """Deals 3 magical damage to any target.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    35: """Deals 5 fire damage to any target that does not have Resist Heat effect. Instantly destroys Ice Elementals before they attack.
    In RB, it negates effects of Ice Storm on the target (if the Ice Storm was cast this turn, it will deal damage to all other targets as normal). It is not implemented for now.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    36: """Deals 5 magic damage to any target.
    Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    # 37: """Deals 5 magic damage to any target. Can be cast only once each match.
    # Can be successfully cast at monsters (including newly summoned) and players. Can be countered. Cannot be made permanent.""",
    38: """Kills any target at the end of the turn (after attacks).
    Can be successfully cast at monsters (including newly summoned) and players. Cannot (!) be countered. Cannot be made permanent.""",
    39: """Deals 5 fire damage to all alive monsters and players (that are not protected by Magic Shield or Resist Heat effects), ignoring visibility. Instantly absorbs Fire Elemental (it does not get to attack this turn). Instantly absorbs and is negated by Ice Elemental (it does not get to attack this turn). Is negated by Ice Storm.
    Always cast at nobody. Cannot be countered (but the target of the CounterSpell ignores Storm damage due to the Magic Shield effect). Cannot be made permanent.""",
    40: """Deals 5 ice damage to all alive monsters and players (that are not protected by Magic Shield or Resist Cold effects or were hit by Fireball this turn), ignoring visibility. Instantly absorbs Ice Elemental (it does not get to attack this turn). Instantly absorbs and is negated by Fire Elemental (it does not get to attack this turn). Is negated by Fire Storm.
    Always cast at nobody. Cannot be countered (but the target of the CounterSpell ignores Storm damage due to the Magic Shield effect). Cannot be made permanent.""",
    41: """Revives a dead monster or a dead player. If target is a dead monster, it gets to attack on the same turn. If target is a dead warlock, it gets to submit their gestures next turn. If target is alive and would die to a Finger of Death this turn, it stays alive instead.
    The target is fully dispelled and is healed for up to 5 HP (respecting the max HP). Can be countered if cast at alive target (otherwise Counter Spell would fizzle as it cannot target dead bodies). Cannot be made permanent.""",
}
