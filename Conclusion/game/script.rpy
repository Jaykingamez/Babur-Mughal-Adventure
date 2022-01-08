# Considered a national hero in Uzbekistan.
# Expanded Persian cultural influence in the Indian subcontinent
# Left signs of Islamic, artistic literary, and social aspects in India
# Stamps in his name were issued in the country to commerate his 525th birthday
# Many of his poems have become popular Uzbek folk songs
# There are also sources stating Babur as a national hero in Kyrgyzstan as well
# 

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.
define Babur = Character('Babur', color="#c8ffc8")
image Babur portrait = "Babur.png"
image uzbek_flag = 'uzbek flag.png'
image kyrgz_flag = 'kyrgz flag.png'

label start:

    Babur "Alas, the end has come for me, earlier than I thought it would."
    Babur "I died in Agra on 5th January, 1531, at the young age of 47 due to health reasons."

    Babur "However, I left behind a vast empire that will continue to grow and endure under my descendants for the next 300 years or so."

    Babur "Even though I am long gone, my legacy still endures."
    Babur "Movies are songs about me are still written today."

label sprites:

    show uzbek_flag
    with dissolve
    show kyrgz_flag
    with dissolve
    Babur "In my birthplace of Uzbekistan and Kyrgyzstan, they consider me a national hero."
    Babur "My poetry has been adapted to popular Uzbek folk songs and stamps were issued in Uzbekistan to commemorate my 525th birthday."

    show Babur portrait
    with fade
    # This ends the game.

    return
