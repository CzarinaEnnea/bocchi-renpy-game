# TODO: Set flags and its endings
label flags:

stop music
stop sound
play music "03_Chasing_Fortune.ogg"

scene bg1
with dissolve
show niji happy
with dissolve

$ nijika_affection = 0
$ ordertaker = 0

n "Now we're going to try out flags to determine 3 different endings."

n "I'll ask you 3 questions."

n "Tas nakadipende sa mga isasagot mo anong ending lalabas."

n "G na."

n "Meron ba kayong chopsuey?"
menu:
    "Meron po":
        $ nijika_affection += 1

        show niji
        n "Yown!"

    "Wala po":
        $ ordertaker += 1

        show niji none
        n "Aaa"

show niji happy

n "Meron ba kayong Adobo??"

menu:
    "Meron po":
        $ nijika_affection += 1

        show niji
        n "Naysuu! Isa nalang!"

    "Wala rin po":
        $ ordertaker += 1

        show niji none
        n "Hmmmm?"

show niji happy

n "Meron ba kayong Bulalo?"

menu:
    "Meron po":
        $ nijika_affection += 1

        show niji
        n "Buti meron pa!"

    "Ubos na po":
        $ ordertaker += 1

        show niji none
        n "..."


if nijika_affection >= 2:
    jump happy_end

elif nijika_affection == 1:
    jump normal_end

else:
    pass

if ordertaker == 3:
    stop music fadeout 1.0

    n "...."

    play music "CT_Gustaf.ogg"

    show niji cat

    n "Meron bang kahit na ano?"
    g "Wala."
    n "Wala?!"
    with vpunch
    play sound "Blow5.ogg"

    n "Waiter!{w} Pa-order naman ako ng Porkchop."
    n "At tsaka ng dalawa ngang kanin."

    show niji angry

    n "Lagyan mo na rin ng konting ketchup."
    n "Meron ba kayong chopsuey?"

    show niji cat
    g "Wala po."
    n "Meron ba kayong Adobo?"

    show niji disgust
    g "Wala rin po."
    n "Meron ba kayong Bulalo?"

    show niji angry
    g "Ubos na po"
    n "Wala namang ma-order,{w} oh waiter"

    
    with hpunch
    n "Pa-ooooooorder!"

    "The Ordertaker Ending"
    
    jump concert_scene
    #return

label happy_end:
    n "Yown! Lahat meron."
    "Happy Ending!"
    return

label normal_end:
    n "Okay na rin kahit isa lang meron."
    "Normal Ending"
    return