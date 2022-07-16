===================================
Technical Game Development Pipeline
===================================

Overview
========

*   `Article this section is based on. <https://unity.com/how-to/set-smart-game-development-pipeline>`_

While the game :ref:`Game Production Cycle<Production Cycle>` covers making and executing design decisions at a high
level, this guide teaches the user how to make the game run smoothly on target platforms (e.g. Mac, Windows, WebGL) at
each stage of the production cycle.


.. _Pre Production Technical Pipeline:

Pre Production Technical Pipeline
=================================

Goals
-----

*   If your game was based on a prototype, throw out the prototype code and build the game from scratch. Often prototypes contain
    hacky code for getting the game produced quickly without considering performance. Basing the game on a bunch
    of hacks is not a good start for any project.

    ..  note::

        If you are interested in prototyping a game concept first before committing to developing a full game
        see :ref:`Prototyping`

*   Check that all planned features work on all target platforms (e.g. Mac, Windows, WebGL). Consider contratins regarding
    memory management, multithreading, networking, and plugin support.
*   Establish minimally supported devices (consoles, web browsers) for your project. These should then be available
    to the developers and QA team.
*   Establish budgets to reach frame rate targets:

    *   How many models can we render
    *   How much detail should models and textures have
    *   What percentage of frame time do we allocate for scripting, rendering, effects, etc.

*   Split levels into scenes. Consider additively loading scenes if it can save on performance.
*   If levels are unlocked over time, Establish the mechanism that locks scenes.
*   Understand your asset pipeline. Establish asset formats and specs with your artists. Also (if you are working in Unity)
    setup `Asset Postprocessors <https://docs.unity3d.com/ScriptReference/AssetPostprocessor.html>`_ to automate
    asset importing
*   Designate a machine for building your game. Alternatively you can use services like
    `Unity Cloud Build <https://docs.unity3d.com/Manual/UnityCloudBuild.html>`_
    that automatically creates a build of your game when changes are pushed through by a developer.
*   Establish a process for publishing features to the release build -> testing new builds (with test automation) ->
    recording statistics for key performance indicators.

Unity Specific Goals
^^^^^^^^^^^^^^^^^^^^

*   Establish objects as prefabs and even make consider common components in objects prefabs.

What Can Go Wrong
-----------------

*   If performance issues arise in the middle of development and no roadmap has been set it may require an extensive
    overhaul of assets and features that can greatly lengthen development time in production.

Resources
---------

Unity Resources
^^^^^^^^^^^^^^^

*   `Optimizing graphics performance <https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html>`_
*   `Modeling characters for optimized performance <https://docs.unity3d.com/Manual/ModelingOptimizedCharacters.html>`_
*   `Art assets best practice guide <https://docs.unity3d.com/Manual/ImportingAssets.html>`_
*   `The new asset import pipeline in Unity <https://blog.unity.com/technology/the-new-asset-import-pipeline-solid-foundation-for-speeding-up-asset-imports>`_
*   `Nested Prefabs <https://docs.unity3d.com/Manual/NestedPrefabs.html>`_
*   `QA your code with Unity Test Framework <https://unity.com/how-to/unity-test-framework-video-game-development>`_
*   `Leverage next-gen crash and error data with Backtrace <https://www.youtube.com/watch?v=4sDK_JfXOY4&t=1s>`_


.. _Production Technical Pipeline:

Production Technical Pipeline
=============================

Goals
-----

*   Set up correct version control.
*   Consider using something like a
    `Cache Server <https://blog.unity.com/technology/cache-server-6-0-release-and-retrospective-optimizing-import>`_
    to store and retrieve multiple platform asset representations without bogging down your local machine.
    For large teams, importing new assets from project modifications takes an increasing amount of time, especially
    when developers switch between target platforms.
*   Profile and optimize early on in development. Consider frame, memory, and disk size budgets.
*   Learn as much as possible about target platforms and their bottleknecks.
*   Ensure that minimally supported devices are constantly tested and maintain realistic performance and frame rates.
    Additionally profile content on the target devices. Profiling in the editor only can cause you to miss some
    performance bottlenecks.
*   Prune unused assets, plugins, and duplicate libraries from the project. If you need them in the future
    retrieve them from version control.
*   Automate repetitive tasks.
*   Make sure you can play the game from any scene.
*   Setup QA process for the game. QA should be happening during development.
*   Establish and document architectural conventions for other developers to follow. (e.g. Define which manager
    is responsible for which objects. Don't use different methods to accomplish the same tasks like having
    2 event managers based on different conventions)
*   Use DeltaTime for FPS independent scripts.

Unity Specific Goals
^^^^^^^^^^^^^^^^^^^^

*   Setting up correct version control:

    *   Use text serialization in your unity project
    *   Setup built in YAML merge tool. (`SmartMerge <https://docs.unity3d.com/Manual/SmartMerge.html>`_)
    *   Setup `Unity Commit Hooks <https://github.com/doitian/unity-git-hooks>`_

*   Avoid storing static data in JSON or XML files since this can result in slow loading times.
    When dealing with static data use  `ScriptableObjects <https://docs.unity3d.com/Manual/class-ScriptableObject.html>`_
*   Check the dependencies of assets that you download from the Unity Asset Store. You may find that you have
    something like 5 different JSON libraries in your project after importing a few.
*   Consider a solution, such as `Cloud Build <https://docs.unity3d.com/Manual/UnityCloudBuild.html>`_,
    that automates the build process.
*   For larger teams, `Unity Build Server <https://unity.com/products/unity-build-server>`_
    licenses can be a useful option because they offload project builds to network hardware.

Resources
---------

Unity Resources
^^^^^^^^^^^^^^^

*   Use `Unity Backtrace <https://blog.unity.com/technology/simplify-game-error-reporting-with-backtrace>`_
    to automate the collection analysis of crash and exception reports.
*   Use `Unity Game Simulation <https://blog.unity.com/technology/optimize-your-game-balance-with-unity-game-simulation>`_
    to automate playtesting of your game and identify balance issues.
*   `Chosing the Correct Asset Settings <https://unity.com/how-to/set-smart-game-development-pipeline#choose-correct-asset-settings>`_
*   `Optimize CPU Performance <https://unity.com/how-to/set-smart-game-development-pipeline#optimize-cpu-performance>`_
*   `Optimize GPU Performance <https://unity.com/how-to/set-smart-game-development-pipeline#optimize-gpu-performance>`_
*   `Optimize UI Performance <https://unity.com/how-to/set-smart-game-development-pipeline#optimize-ui-performance>`_


