define b = Character('Babur', color="#419121")

label chanderi:

    scene bg samarkand

    play music "audio/sapajou-zurna-instrumental.mp3"

    show babur

    # begin of Khanwa summary

    "{i}Okay so for the sake of not turning this into a scary history class...{/i}"

    "{i}We're gonna skip the Battle of Khanwa in which the Babur had defeated the Rajput Confederacy...{/i}"

    "{i}...and firmly establish Mughal rule while crushing regrowing Rajput powers as the battle was fought for supremacy of Northern India between Rajputs and Mughals.{/i}"

    # end of Khanwa summary

    b "That Rajput must have learned a lesson. I shall now be able to take short break."
    
    "Informer" "Your Majesty..."

    b "Say it."
    
    "Informer" "Our source said that Rana Sanga is preparing for a revenge."

    b "Hmm... This dude never learned a thing."

label choices1:

    b "Hey you modern man, got any idea?"

    "Me" "..."

    hide babur

menu:

    "Negotiate for peace?":
        jump choices1_a

    "No idea.":
        jump choices1_b

label choices1_a:

    show babur

    b "Ridiculous!"

    jump choices1_common

label choices1_b:

    show babur

    b "Aiz, I already knew you unambitious people."

    jump choices1_common

label choices1_common:

    b "Well, I need to isolate Sanga so that he won't be plotting any nonsense in near future."

    b "Hmm..."

    b "Oh isn't one of his vassals, Medini Rai ruling Malwa now?!"

    b "Then incflicting a military defeat there would solve the problem!"

    hide babur

    "{i}Babur then prepared for the attack at Malwa as planned...{/i}"
    
    "{i}December 1527, Babur finally marched to the capital of Malwa, Chanderi.{/i}"
    
    "{i}On 20 Januray 1528, Babur initiated an offer with Rai.{/i}"

    show babur

    "Me" "Didn't you say negotiation is a ridculous thing, did you?"
    
    b "What do you know? Thing depends!"

label choices2:
    
    b "Well, since you've asked, do you wanna know the result? Arghhh"
    
    "Me" "..."

    hide babur

menu:

    "I would love to hear your brilliant idea!":
        jump choices2_common

    "I already know everything. Yall have become history anyways...":
        jump choices2_b

label choices2_b:

    show babur

    b "Just let me finish!!"
    
    "Me" "Alright..."

label choices2_common:

    b "I am going to win the battle anyway, but continuing it only brings about more deaths."

    b "So I offered Shamsabad in exchange for Chanderi as a peace overture. And then no more unnecessary casualties."

    b "But you know what? He dared to reject it!!"

    b "Then what has to come finally comes. My greatest army has taken Chnderi down over a night."
    
    b "Honestly I was quite surprised *laugh*"

    hide babur

    "{i}Consequently, Rai, the ruler Malwa, toghether with the people organized the Jauhar ceremony where Rajput women and children committed self-immolation to save their honour...{/i}"

label choices3:
    
    "{i}Do you think such an action ever touched Babur?{/i}"
    
    "Me" "..."

    hide babur

menu:

    "Definitely!":
        jump choices3_common

    "Nah he couldn't care less.":
        jump choices3_common

label choices3_common:

    "{i}Well, let's see what Babur says...{/i}"

    show babur

    b "Oh that thing? Meh what else can they do?!"
    
    hide babur

    "{i}Rather, Babur ordered a tower of skulls, which was used to be erected in an act of barbarism, in order to record his record monumental victory.{/i}"

    jump conclusion
