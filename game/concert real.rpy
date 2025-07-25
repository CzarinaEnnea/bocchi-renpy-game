# TODO: Fix the zoomies of the concert
image concert:
    subpixel True
    size (1280, 720)
    xalign 0.5
    yalign 0.5

    parallel:
        "ccg145"
        pause 1.0
        time 43.0

    parallel:
        # Ryo
        crop (150, 900, 590, 332)
        pause 0.1
        easeout .6 crop (180, 950, 469, 264)
        
        crop (87, 370, 590, 332)
        easein .8 crop (14, 306, 791, 445)

        # Nijika
        crop (1380, 778, 900, 507)
        easeout .5 crop (1280, 790, 750, 422)

        
        time 2.9
        crop (400, 350, 900, 506)
        time 3.4
        crop (564, 545, 552, 311)
        time 3.9
        crop (400, 350, 900, 506)
        time 4.4
        crop (564, 545, 552, 311)
        

        time 17.0
        crop (1047, 849, 1132, 637)

        linear 4.0 crop (868, 58, 1532, 862)

        time 22.25


        time 5.0
        linear 4.0 crop (0, 482, 1738, 978)
        easein 4.0 crop (267, 91, 2133, 1200)
        easeout 4.0 crop (0, 91, 2133, 1200)



        # Lucy and Mary
        time 26.97
        zoom 1
        crop (0, 482, 1738, 978)
        pause 1.0

        # Mary
        crop (0, 775, 984, 554)
        easein 5.5 crop (0, 279, 984, 554)

        # Final shot.
        easeout 4.0 crop (0, 91, 2133, 1200)
        easein 4.0 crop (267, 91, 2133, 1200)

        time 5.0
        linear 4.0 crop (0, 482, 1738, 978)
        easein 4.0 crop (267, 91, 2133, 1200)


    time 20.0




label concert_scene:

    $ second_loop = True
    
    stop sound

    play music "TV_size__Drum_Bass_modified_.ogg"

    scene concert
    with dissolve

    pause 120.0 

    r "Angas."

    n "Di ko alam san nanggaling instruments natin pero ayos."