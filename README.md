# Spellweavers

In 1977 Richard A. Bartle (https://en.wikipedia.org/wiki/Richard_Bartle) created a pencil-and-paper game Spellbinder (a.k.a. Waving Hands). In this game players cast various spells by creating sequences of gestures with their two hands. You can read more at Bartle's website and at Wikipedia:
https://mud.co.uk/richard/spellbnd.htm, https://en.wikipedia.org/wiki/Spellbinder_(paper-and-pencil_game)

The game had a number of implementations (some of which are mentioned in the articles above), some with their own rulesets (spellbooks). Most of those implementations are currently (early 2023) not available, and some (like mortalspell.com) are both not available and not mentioned in the list above. 

Probably the most popular version during the last 15+ years is the web version of the game named Warlocks and implemented by RavenBlack (https://games.ravenblack.net) back in early 2000s. This version also probably has the best available ruleset variation (ParaFC Maladroit) in terms of (meta)game balance, based on limited testing and discussions done by the community at Slartucker's Refuge: https://slarty.proboards.com/.

In early 2020s a mobile game client was introduced by Galbarad (https://github.com/Pz1c/WavingHands); it acts as a 3rd party front-end to Warlocks web version, but, probably, it has to do by parsing Warlocks HTML output, which introduces some other challenges and limits it's functionality.

This project is an open-source version of the core game engine that strives to support multiple rulesets (spellbooks), which hopefully would:
- allow for easier re-creation and preservation of various rulesets
- allow for easier creation of new rulesets and thus updates to game balance
- provide the foundation for future web client with improved functionality, and possibly an API interface for existing and future mobile clients.
