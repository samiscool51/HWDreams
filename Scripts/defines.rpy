##charaters
define Peter = Character("Peter", who_color="#7e3602", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/peter.png")
define Lois = Character("Lois", who_color="#f8784e", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/lois.png")
define seller = Character("seller", who_color="#a5a5a5", show_namebox_type="gui/namebox/howard.png")
define IGTCitem = Character("IGTC", who_color="#66da07", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/IGTC.png")
define unknown_voice_1 = Character("Unknown Voice", who_color="#4e4e4e", show_namebox_type="gui/namebox/generic.png")
define unknown_voice_2 = Character("{size=*0.89}Another Unknown Voice", who_color="#4e4e4e", show_namebox_type="gui/namebox/generic.png") ##do this fucked character size fix, fixes text going off screen but looks fucky if the user notices, which they will.
define unknown_voice_3 = Character("{size=*0.88}Unknown Booming Voice", who_color="#4e4e4e", show_namebox_type="gui/namebox/generic.png") ##reference code comment in line 7
define unknown_man_1 = Character("Unknown Man", who_color="#4e4e4e", show_namebox_type="gui/namebox/generic.png")
define unknown_man_2 = Character("Unknown Male Voice", who_color="#4e4e4e", show_namebox_type="gui/namebox/generic.png")
define unknown_female_1 = Character("{size=*0.89}Unknown Female Voice", who_color="#4e4e4e", show_namebox_type="gui/namebox/generic.png") ##reference code comment in line 7
define unknown_core_1 = Character("Unknown Core", who_color="#4e4e4e", show_namebox_type="gui/namebox/generic.png")
define unknown_celestialsapien_1 = Character("{image=mods/Highway Dreams/Resources/img/characters/celestialsapien/celestialsapien_logo.png}{alt}{/alt}", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/character.png") ## TODO namebox design
define TF2Engie = Character("Dell Conagher", who_color="#e84950", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/character.png") ## TODO namebox design
define GLaDOS = Character("GLaDOS", who_color="#d49735", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/GLaDOS.png")
define Alice = Character("Alice", who_color="#c8ffc8", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/character.png") ##TODO color and namebox  once alice design has been completed
define Kevin = Character("Kevin", who_color="#c8ffc8", show_namebox_type="mods/Highway Dreams/Resources/img/namebox/character.png") ##TODO color and namebox  once kevin design has been done


##logos and their animation, yoinked from the base game because redefining the native ones causes the main menu logo to unintentionly change
image ModLogoAnimation = LiveComposite(
    (1920, 1080),
    (650, 350), "road_unfurl",
    (550, 350), "family_lettering",
    (550, 580), "guy_lettering"
    )
image family_lettering:
    "mods/Highway Dreams/Resources/img/logos/LetteringFamily.png"
    subpixel True
    zoom 0.8
    yoffset -100
    alpha 0.0
    pause 1.5
    easein 1.5 yoffset 0 alpha 1.0
image guy_lettering:
    subpixel True
    "mods/Highway Dreams/Resources/img/logos/LetteringGuy.png"
    zoom 0.8
    yoffset 100
    alpha 0.0
    pause 1.5
    easein 1.5 yoffset 0 alpha 1.0