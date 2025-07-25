define r = Character("Ryo", color="#31298a")
define n = Character("Nijika", color="#f5d833")
define k = Character("Kita", color="#b63434")
define g = Character("[name]", color="#db345d")
define nvlg = Character("[name]", color="#db345d", kind=nvl)

define us = Character(
    None,
    window_background=None,
    what_outlines=[(4, "#7a1931", 0, 0)],
    what_size=28,
    what_xalign=0.5,
    what_textalign=0.5,
    #what_layout='subtitle',
    what_bold=True
)

image ryo animated:
    "ryo"
    pause 0.5
    "ryo none"
    pause 0.4
    "ryo cry"
    linear 0.2 xoffset -50


image ending text = Text("Happier End", size=30)


define slowdissolve = Dissolve(1.0)

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0


label start:

    stop music fadeout 0.5

    n "Wow, It's really really dark in here."

    r "Better watch out. You don't want to be eaten by a \"Grue\"."

    n "I know what I'm doing Ryo."

    n "And what's a Grue?"

    scene bg1 
    show niji 
    with dissolve

    play music "a-Gentle-Breeze.ogg" fadeout 1.0   
    # queue music "03_Cathedral.ogg"  (This will queue music and play after the first music is finished)

    n "Aaaand there! I'm done!"

    show niji at right
    with move
    show ryo none at left
    with dissolve

    r "....."

    show niji cat
    
    n "Why aren't you saying anything?"
    
    show ryo

    r "I don't know what to say."

    r "I don't have money..."

    show ryo cry

    r "Nijikaaa"

    show niji disgust

    n "Ughh"

    r "..."

    n "....."

    r "......."

    r "Nevermind"

    play music "march-of-the-tiny-soldier.ogg"

    show kwek at top behind niji
    show ryo none

    r "Kain ka muna kwek-kwek bhoszx Nijika."

    show niji angry

    n "Amaccana Ryo tapon mo na yan baka san san mo lang hinugot yan."

    r "Omsim."
    play sound "Wind4.ogg"
    hide kwek

    r "Oks na."

    show kita shock at center
    with dissolve

    k "Huh? Asan ako?"
    k "Ryo? Nijika? Bat ka may pakpak Nijika-senpai"

    show niji

    n "Kita-chan!"
    n "Di ko rin alam eh naccaw asset lang tong sprite ko."

    r "Si Kita-chan pla to eh.{w} Pautang."

    show kita happy at slightleft
    with move

    k "Sige lang Ryo-senpai magkano ba?"

    show ryo cry

    r "Yown salamat buti ka pa."
    r "Di katulad nung isa dyan."

    show niji cat

    n "Gusto mo ba ng {b}{size=+10}sapak{/size}{/b} Ryo?"

    show ryo front

    r "Da't nakaharap din tayo kase nakaharap sprite ni Kita-chan."

    with vpunch
    play sound "Blow8.ogg"
    show niji disgust
    show ryo animated

    n "Wag mo binabago usapan."

    show niji front1

    n "Pero sige yan na."

    r "Salamat boss."

    show ryo front

    r "Wala na rin pala akong maisip na dialogue kaya end scene na natin to."

    k "At dahil d'yan magta-timeskip na tayo guys."

    #us "At dahil d'yan\n magta-timeskip na tayo"

    us "Pagtapos ng pag-uusap nila na walang kakwenta-kwenta ay lumipas na ang maraming oras."

    stop music fadeout 1.0

    $ first_loop = False
    $ second_loop = False


label end:

    scene black
    with slowdissolve
    play music "03_Cathedral.ogg" fadein 1.0

    pause 0.5

    scene cg111
    with fade
    
    n "Tanghali na pala"

    r "mm.."

    scene cg3555

    n "Parang kanina lang kung ano ano pinagsasabe natin"

    scene cg333

    n "Ngayon wala na tayong masabe"

    r "..."

    r "Nijika"

    if first_loop:

        r "Snap back to reality"

        r "Please.."

        r "{cps=25}Tigil mo na {s}pagshashabu{/s} pagiging delulu{/cps}"

        play sound "Bell1.ogg"
        queue sound "Bell1.ogg"
        queue sound "Bell1.ogg"

        menu:
            "I don't want to (shashabu pa)":
                jump flags
        
            "Snap back to reality (titigil na)":
                jump real_end
    else:

        r "Snap back to reality"
   
    play sound "Bell1.ogg"
    # queue sound "Bell1.ogg"

    menu:
        
        "I don't want to":
            jump name_input
        
        "Snap back to reality":
            jump bad_end



label name_input:

    $ first_loop = True

    play music "march-of-the-tiny-soldier.ogg"
    scene bg1
    with dissolve

    show niji happy
    with dissolve

    n "Ayaw ko pa Ryo may mga bagay pa kong gustong gawin."

    n "Katulad ng name input!"

    python:
        name = "Reader" 

    n "Okay what's your name [name]?"

    python:
        name = renpy.input("What's your name?")

    n "What was that?"

    n "Is it Gae?"

    n "Sorry I didn't heard what you said can you say it again?"

    python:
        name = renpy.input("What's your name again?")

        name = name.strip() or "Dimagiba Batumbakal" # removes value and replace with default

    n "Oh! It's [name] right? I heard it loud and clear this time."

    n "It's a nice name."

    g "Yes I know."

    nvl show dissolve

    nvlg "This is NVL mode."

    nvlg "NVL mode also supports showing menus or choices to the player, providing it's the last thing on the screen."

    nvlg "Did you understand?"

    nvlg "Nevermind don't answer that. I'm just using your name to type this out" 

    nvlg "At notes ko lang talaga to sa sarili ko."

    nvlg "Anyways goodbye."

    nvl clear

    jump end


label bad_end:
    
    stop music fadeout 1.0

    n "I guess this is goodbye"

    play music "ma meno.ogg" fadeout 1.0

    scene black
    with dissolve
    scene be
    with slowdissolve

    pause 5.0

    return




