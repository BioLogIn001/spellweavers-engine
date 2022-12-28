# spellweavers

In 1977 Richard Bartle (https://en.wikipedia.org/wiki/Richard_Bartle) created a pencil-and-paper game Spellbinder (a.k.a. Waving Hands). In this game players cast various spells by creating sequences of gestures with their two hands. You can read more at Bartle's website or at Wikipedia:
https://mud.co.uk/richard/spellbnd.htm
https://en.wikipedia.org/wiki/Spellbinder_(paper-and-pencil_game)

The game had a number of implementations (some of which are mentioned in the articles above), some with their own rulesets (spellbooks). Most of those implementations are currently (December 2022) not available, and some (like mortalspell.com) are both not available and not mentioned. In the last 20 years the majority of players used the web version of the game implemented by RavenBlack (https://games.ravenblack.net) and named "Warlocks". This version is still available (as of December 2022), but, unfortunately, it has some limitations due to not being actively developed for the last 10+ years. There is also a mobile game client that acts as a 3rd party front-end to Warlocks (https://github.com/Pz1c/WavingHands), but it has to do by parsing Warlocks HTML output, which introduces some other challenges.

This project is an open-source version of the core game engine that supports multiple rulesets (spellbooks), which should:
- allow for easier re-creation and preservation of older rulesets
- allow for easier creation of new rulesets
- provide the foundation for future web client with improved functionality, and possibly an API interface for existing and future mobile clients.
