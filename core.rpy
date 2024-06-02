label core:
    stop music fadeout 1.0 
    if renpy.loadable("mods/Highway Dreams/hehehehe"): ##check to see if the user is nostalgic
        call peter_mod
        return
    else:
        call ScenePrep
        call DLCCheck
        call DebugCheck
        jump Story
        $ MainMenu(confirm=False)() ##just in case we somehow don't go to the mainmenu after story is done as a last resort
    return ##shouldn't be needed but if the end of story doesn't return to the main menu this is the last resort just in case.

##check to see if user has installed the DLC.
label DLCCheck:
    if renpy.loadable("images/NextExit/bg/strato day.jpg"):
        return
    else:
        stop music fadeout 1.0 
        menu:
            "Error: \nThe DLC: \"Highway Blossoms: Next Exit\" is required for the mod. \nPlease install it. Press ok to exit game"
            "Ok":
                $ renpy.quit()

label ScenePrep:
    $ layer_move("background", 1700)
    $ layer_move("background2", 1200)
    $ layer_move("middle", 825)
    $ layer_move("forward", 600)
    call Cleanup
    return

label Story:
    call Act1
    call Act2
    call Act3
    call Act4
    call Act5
    call Act6
    call Credits
    $ MainMenu(confirm=False)()
    return ##return to core just in case something went wrong
    
    
label Cleanup: ##clean up everything just incase something is leftover and might fuckup other scenes
    ##do this bullshit since we can't hide everything in a simple command for some reason
    ##hide characters
    hide Amber
    hide Marina
    hide Tess
    hide Mariah
    hide Joseph
    hide peter
    hide lois
    hide IGTCitem
    hide unknown_celestialsapien_1
    hide unknown_voice_1
    hide TF2Engie
    hide GLaDOS
    hide Alice
    hide Kevin
    ##set all backgrounds to a transparent image for a clean state.
    show reset_scene_transparent onlayer background
    show reset_scene_transparent onlayer background2 
    show reset_scene_transparent onlayer middle
    show reset_scene_transparent onlayer forward
    return
    
label DebugCheck:
    call Cleanup ##call cleanup twice just in case we return to DebugCheck from an act and stuff is still onscreen.
    stop music ##stop music again just incase music is still playing
    if renpy.loadable("mods/Highway Dreams/debug.yes"): ##debug mode
        menu:
            "Debug activated. Select function"
            "Start mod normally":
                call DLCCheck
                return
            "act 1":
                call Act1
                jump DebugCheck
            "act 2":
                call Act2
                jump DebugCheck
            "act 3":
                call Act3
                jump DebugCheck
            "act 4":
                call Act4
                jump DebugCheck
            "act 5":
                call Act5
                jump DebugCheck
            "act 6":
                call Act6
                jump DebugCheck
            "Credits":
                call Credits
                jump DebugCheck
            "Character text test":
                call character_text_test
                jump DebugCheck
            "Character sprite test":
                call character_sprite_test
                jump DebugCheck
            "Main menu":
                $ MainMenu(confirm=False)()
                return
            "nostalgia egg test":
                jump peter_mod
                return
            "Exit game":
                $ renpy.quit()
    else:
        return