.. _Prototyping:

###########
Prototyping
###########

Taken from https://learn.unity.com/tutorial/introduction-to-real-time-3d-experience-design

Prototyping Process
###################

#.  Treat the prototype like a game jam.
#.  Define the scope in a design document. You can find a template for a prototype design document here:
    `Prototype Design Document Template #1 <https://docs.google.com/document/d/1lQxQYo1qt55mUxdVlgoll0gXl2SqieE8K9oTEE7WIHg/edit?usp=sharing>`_
#.  Give yourself a deadline to a playable prototype.
#.  Playtest with yourself and others to gather feedback.
#.  Iterate over the feedback you recieve.
#.  After 1 or multiple iterations decide on wheter to pursue the prototype into a full game.
#.  If you choose to make a complete game, make sure you ditch the prototype code and start a new project
    (see tips below for more info on why) Given that you know what does and does not work, you should be able to pull
    out the bits of your prototype that were successful and make good headway towards a full game.

Prototyping Tips
################

Taken from the video `Prototyping Games in Unity? <https://www.youtube.com/watch?v=x10P0RNHm4M>`_

#.  Don't plan on keeping the code. You should throw away the code when it is time to start production.
    From the prototyping phase you will know what works and what doesnt work and we should be able to quickly
    rebuild the parts that do work (without dragging behind the old non essential code).
#.  Don't over-engineer / over-organize things. Don't debate whether something should be a Monobehavior or not. When you move from
    prototyping to production (and throw away the old code) then you will know what the proper structure should be.
#.  Make components small and modular: This allows for easy adjusting of systems. You are going to want to turn things off, toggle things etc.
    You don't want to be stuck with a big player / character class that has a lot of intertwined functionalities.
#.  Don't do test driven development (TDD) / Unit Testing. TDD is for creating code you will keep for a long time (used in production). Prototype code
    should be discarded once the prototype is complete (see earlier tip)
#.  Keep your code clean. Give your classes, functions, and variables descriptive names so when you revisit them it will be easy to
    tell what they do. If you are not using a piece of code / prefabs delete them. If you really need to go back to old
    code, use source control.
#.  Use temporary but decent Art, Sound, Models, and Textures. Using just a grey box and some capsules is good for testing
    if things work but part of the game experience and fun is seeing real characters and models interacting on screen.
    (For finding game assets see :ref:`Game_Assets`)
#.  Use starter kits (if available) to speed up development time. You can quickly build out projects from starter kits
    or use them as reference, pulling art assets, characters, animations, and scripts from them into your project.
#.  Decide early on on where you will be deploying your game (iOS, Windows, WebGL, VR). 99% of the time you should go
    with a Windows / Mac build but if you are going on mobile or VR you should have a mobile / VR device during
    testing to see how it feels on the target device (also if you consider devices other than keyboard and mouse
    to be the primary input (like xbox controllers) then have those input devices at hand for testing).
#.  Be Lazy: don't overengineer your prototype. Don't over think it. Get this prototype in your hands and in the hands
    of others quickly to see if they think its fun. Don't think too much about how everything is going to fit together.
    You want an NPC to cast 10 abilities, don't have them cast 1 in a demo scene.
#.  Don't get fixated on fixing all the problems in your prototype. Just get your game to a playable state. Cutting
    corners / hardcoding things to get there is fine. You will be throwing the code away anyways. You just want to
    see if what you are playing is fun.

Taken from the video `Prototyping Games in Unity? <https://www.youtube.com/watch?v=NU29QKag8a0>`_

#.  Pick the right scope: You don't need to prototype everything in the game. Ask yourself: where do you want to
    experiment? What do you want to demonstrate?
#.  Focus on the unknown: Don't prototype something that already works. Focus on what the core features are
    and what is unique to your game. (Not just unique gameplay but also art, sound and more)
#.  Keep things separate (especially if you are part of a team). This will allow multiple people to work independently.
    Gameplay / Art, characters, animations / Meta
#.  Embrace failure. Kill bad ideas early (avoid sunk cost fallacy) and learn from your mistakes. You could also
    kill part of your concept early. Developing a prototype for an online game but don't have online figured out even
    after a week of trial and error? Ditch the online portion for now and just fight against the AI or require multiple
    people to playtest locallly. Leave online for production and test to see if the game as it stands is fun.
#.  Fake it till you make it: The prototype has to only be just good enough. Reuse systems and assets as often as you can.
    Good to determine the minimum amount of effort required. You don't even have to make a prototype playable as
    long as you can see how the gameplay would look (at that point it would be more like a trailer).
#.  Move fast and fix things: The foundation you build your prorotype on should be flexible enough for
    experimentation. When feedback comes in it should be easy and not take that much time for you to change gravity
    (for a physics game), change car speed (for a racing game), add new character models (for an RPG)
#.  Use the right tool for the right job. You can use mspaint to paint or use Photoshop to make creating art faster
    and easier. You can create your own models from scratch in Blender or use Asset Forge to quickly create 3D assets.
#.  Make it awesome and focus on the core feature that the player will be doing all the time. Put your effort where
    it will have the most impact.
#.  Test often and test correctly. Have random people play it and let them figure out what is fun or not.
    useful to observe / film playtesters to capture their reactions.
#.  Have fun and create a game you are proud of.
#.  Make sure to keep things simple (part of focusing only on core features)
#.  Make sure you test on the devices you plan on deploying to. Don't test mobile game on a laptop for example.
