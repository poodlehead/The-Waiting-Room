# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nol")
define b = Character("Blackheath")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg the waiting room
    #play music "waitingroom.mp3"
    #play music "tickingclock.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nol neutral at left
    show blackheath neutral at right

    # These display lines of dialogue.

    n "You did say it wasn't over"

    b "..."

    n "You never seemed short of words when you were alive"

    b "I'm not an ignoramus, you're a being who has powers that I cannot understand. I died…I was trapped in the Evergreen Castle as a ghost… and I've been seething ever since"

    n "So death {b}{i}did{/i}{/b} teach you something?"

    b "What?"

    n "Let me ask you this. \n If you were to have a second chance, what would you say you'd do differently?"

    b "Not to underestimate others and make myself more appealing to others, superficially at least. I will not compromise on my morals. \nI am, if nothing else, honest."

    n "Hmmmm, good, that's as I {i}hoped{/i}."
    
    n "To be candid, I feel you were quite a despicable character, but that drive to continue to survive. Well, it inspires me to give you… said Second chance."

    b "…I'm listening"

    n "I've found a soul which yours will resonate with in another realm If I place you there… The pair of you will become one of the same"

    b "So we would inhabit the same body? I've read of such a craft, it was rumoured that the panther deity was capable of such things"

    n "Hmmmm, the less said about him the better."

    b "So, we reside in a body together, then what?"

    n "That is for you to decide. I'll give you the opportunity, after that, you can do as you please."

    b "If… I were to quell the other soul, there would be no punishment? \nThe vessel would become mine?"

    n "Oh yes, no strings attached. The body will become vampiric by virtue of your soul being within it. It will inherit your power too"

    b "What do you require from me?"
    n "Hmmmm?"

    b "This opportunity is too good to resist, what do you gain?"

    n "I want you and the other soul to entertain me. I am a guardian of stories, if I give you a second chance, make it a tale to remember."

    show blackheath sneer

    b "{i}*sneer*{/i} \nOh I'll give you a show. I agree"

    n "Excellent \nYou may leave now… And Blackheath"

    show blackheath neutral

    b "What?"

    n "I anticipate a good performance. I'll be marking you on two things. Not to underestimating others and making yourself more appealing to others, superficially at least"

    show blackheath sneer

    b "{i}*sneer*{/i} \nFine, whatever it takes"

    # This ends the game.

    return
