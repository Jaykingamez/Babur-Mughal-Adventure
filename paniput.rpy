# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character('Babur', color="#419121") #babur
define n = Character (None, what_slow_cps=0) #narrator
define i = Character ("Ibrahim Lodi, Sultan of Delhi")
image bg war = im.FactorScale("war.png", 2)
image bg black = im.FactorScale("black.jpg", 3)

# The game starts here.

label paniput:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    ##scene bg mountains
    ##with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "audio/punch-deck-bhangra-bass.mp3"
    show babur

    # These display lines of dialogue.

    b "Now, I am the ruler of a small kingdom nested in the mountains and valleys of Afganistan"

    b "But this is not enough!"

    b "The riches of India call out to me... So I must invade."

    b "It won't be easy, I will have to face Sultan Ibrahim Lohi of the powerful Delhi Sultanate, the dominant power of the Indian subcontinent"

    b "But I will do it anyway, with much planning, a secret trump card and some luck"

    hide babur
    n """{i}So Babur set off on his risky military campaign to the Delhi Sultanate.{/i}"""

    ##scene bg palace with dissolve

    show lodi
    i "So some random Babur is marching towards our frontier at Punjab?"

    i "We will see to the easy destruction of his pitiable army"

    hide lodi

    show babur

    n "{i}On the 21st April 1526, Babur's invading army of 12,000 met Lohi's army of 70,000 near the city of Panipat.{/i}"

    b "I know my outnumbered army would be utterly crushed if I didn't have {i}my secret weapon{/i}..."

    b "... Gunpowder firearms and cannons"

    hide babur
    scene bg war

    n "{i}Babur's field artillery proved to be a key advantage in the battle{/i}"

    n "{i}His cannons were set on wheels, making them highly manuverable{/i}"

    n "{i}The cannons were protected by a line of 700 movable carts linked by rope, positioned in front.{/i}"

    n "{i}On the other hand, Lodi's army lacked ground artillery, putting him at significant disadvantage{/i}"

    n "{i}To make matters worse, the loud noises of Babur's artillery scared Lodi's war elephants into trampling many of his soldiers{/i}"

    scene bg black
    show babur

    b "Of course, my military genius play a great role too"

    b "I flanked Lodi's panicked retreating army on both sides and quickly brought the battle to an end"

    b "In total, Ibrahim Lodi along with 20,000 of his men died that day."

    b "And in an unprecedented way, I secured a base for myself in the heart of the Indian subcontinent"

    b "And from there, I expanded onwards to forge the great Mughal Empire!"

    # This ends the game.

    jump chanderi
