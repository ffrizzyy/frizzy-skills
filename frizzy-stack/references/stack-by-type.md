# Stack choices by project type

Cheapest first. Confirm licenses, fees, and platform support by search.

## Mobile apps

Path choice, cheapest first: a PWA (installable web app) costs nothing in store fees; Capacitor wraps a web app for the stores; Expo (React Native) or Flutter give a shared codebase with native feel; Swift and Kotlin give full platform access at twice the code. Pick the cheapest path that supports the features the MVP needs (background location, Bluetooth, widgets, and heavy graphics often force native).

## Games

Engine choice, cheapest first: Godot (MIT-licensed, no fees), Phaser or PixiJS for browser games, Bevy for Rust developers, GameMaker or Defold for 2D. Unity and Unreal have license terms that have changed more than once; read the current terms by search before recommending them and state the revenue thresholds you found.

Web builds of an engine: check the engine's current web export notes before promising browser support. Measure an empty export in the first week for size and load time, find out whether threads need special server headers, and test Safari on Mac and iPhone early, since engines have had gaps there.

## AI-powered features and agents

Cheapest first, in this order: (1) check whether the platform already ships a model, such as a browser's built-in on-device AI, which is free for you and private for the user, and read its device, language, and context limits (for example, one such API was found to be unavailable in background workers and on phones); (2) bring-your-own-key, which costs you nothing; (3) free provider tiers, but only after reading their data terms, since some free tiers let the provider use submitted content to improve its products and bar users in the EU, UK, or Switzerland, which rules them out for anything that reads private pages; (4) a paid hosted tier with caps and a no-training contract. Record any rejected option and the reason in the decision log. Show cost per request with the token assumptions written out, and say when a price is a stand-in for a newer model. Show the cost of the ideal model beside the cheap one with per-request math.
