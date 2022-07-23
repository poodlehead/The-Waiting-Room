# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nol")
define b = Character("Blackheath")
define a = Character("Anthony")
define t = Character("Tom")

# The game starts here.

label start:
    
    jump thePrologue 
    
    # This ends the game.

    return
