label Credits:
    stop music
    window hide
    show black onlayer flatoverlay with dissolve
    play music "mods/Highway Dreams/Resources/audio/music/outro.mp3" noloop
    $ music_notify()
    $ renpy.pause(4.14, hard=True)
    show ModLogoAnimation onlayer flatoverlay:
        zoom 1.2 xalign 0.5 yalign 0.65
        pause 4.0
        easein 1.5 yalign 1.5
    $ layer_move("middle", 1001)
    $ renpy.pause(30.9, hard=True) ##always add one to account for the desolve below
    hide ModLogoAnimation onlayer flatoverlay
    with Dissolve(1.0)
    return