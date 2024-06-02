label peter_mod:

##define our shit
image house_interior_OG normal = "mods/Highway Dreams/OG/assets/house_interior_normal.png"
image peter_OG normal = "mods/Highway Dreams/OG/assets/peter_normal.png"
image lois_OG normal = "mods/Highway Dreams/OG/assets/lois_normal.png"
define peter_OG = Character("Peter")
define lois_OG = Character("lois")

##our intro
stop music fadeout 1.0 ##shut the music up
$ renpy.movie_cutscene("mods/Highway Dreams/OG/assets/house_intro.webm") ##family guy house intro

##story starts here
show house_interior_OG normal onlayer background
show peter_OG normal onlayer forward:
    zoom 0.1 xpos 800 ypos 480
show lois_OG normal onlayer forward:
    zoom 0.3 xpos 650 ypos 450

play sound "mods/Highway Dreams/OG/assets/lois.mp3"
lois_OG "peter i think someone is in the house"
play sound "mods/Highway Dreams/OG/assets/peter.mp3"
peter_OG "it's nothing lois"

show amber handhip neutral onlayer forward:
     zoom 0.1 xalign 0.54 yalign 0.47
show marina concerned neutral onlayer middle:
    zoom 0.15 xalign 0.60 yalign 0.47

Marina "Amber i think we took a wrong turn..."
Amber "Yea, I think you're right..."
play sound "mods/Highway Dreams/OG/assets/peter.mp3"
peter_OG "holy crap lois it's Amber and Marina from highway Blossoms!"
##story ends here

##play ending
$ renpy.pause(3, hard=True)
    
stop ambient fadeout 0.5

window hide

show black onlayer flatoverlay with dissolve

show logoanimation onlayer flatoverlay:
    zoom 1.2 xalign 0.5 yalign 0.65

$ layer_move("middle", 1001)

play music "mods/Highway Dreams/OG/assets/ending.mp3" noloop
$ music_notify()
pause 31.0

hide logoanimation onlayer flatoverlay
with Dissolve(1.0)
$ MainMenu(confirm=False)()
return