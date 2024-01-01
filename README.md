# PyGame-Snake-Game
First attempt with PyGame - Snake Game

Used a brute-force grid declaration, to avoid having references clashing by iterating through 'grid elements' to create the grid.  An alternate method would be to iterate and only use values rather than creating a list of values which are then referenced.
Classes are used, but could have been used more extensively.  Having instances of gameState and player fields help to prevent issues of scope in the various methods that reference essential variables.
In future projects, it would be wise to exploit classes, as problems of scope and references are clarified by having instances to call directly.  Also - the dunder constructor initialization could be used to set initial values far more concisely - there are likely duplicate declarations of values that could have been avoided.

Overall - PyGame is a blast.  It's fun to stick in the Python code, rather than making gameplay alterations in a Unity, Godot or Unreal menu screen.  It's like the Apple ][ days again - more code, less 'engine-manipulation', and so - more fun.
