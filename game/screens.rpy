﻿# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"       
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                       

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Nouvelle partie") action Start()
        textbutton _("Charger sauvegarde") action ShowMenu("load")
        textbutton _("Préférences") action ShowMenu("preferences")
        # textbutton _("Aide") action Help()
        textbutton _("Galerie de CG") action void()
        textbutton _("Quitter") action Quit(confirm=False)

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox

        textbutton _("Retour") action Return()
        textbutton _("Préférences") action ShowMenu("preferences")
        textbutton _("Sauvegarder") action ShowMenu("save")
        textbutton _("Charger") action ShowMenu("load")
        textbutton _("Menu principal") action MainMenu()
        textbutton _("Aide") action Help()
        textbutton _("Relations") action ShowMenu('stat_rel')
        textbutton _("Quitter") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            
            textbutton _("Précédant"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Rapide"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Suivant"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n%s"% (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Slot vide.")),
                        FileSaveName(i))

                    text description

                    key "save_delete"action FileDelete(i)
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen stat_rel:
    
    tag menu
    
    grid 1 1:
        style_group "prefs"
        xfill True
        hbox:
            frame:
                style_group "pref"
                has vbox
                textbutton _("Retour") action ui.returns("goback")
                textbutton _("") action display_stats(name=True, bar=True, value=True, max=False)
                


    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Affichage")
                textbutton _("Fenétré") action Preference("display", "window")
                textbutton _("Plein écran") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("Toutes") action Preference("transitions", "all")
                textbutton _("Aucune") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Vitesse défilement texte")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Sauter les textes")
                textbutton _("Texte déjà lu") action Preference("skip", "seen")
                textbutton _("Tous les textes") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Sauter") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("Après un choix")
                textbutton _("Arrêter de sauter") action Preference("after choices", "stop")
                textbutton _("Continuer de sauter") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Vitesse automatique")
                bar value Preference("auto-forward time")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Volume musique ")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Volume sonore")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton "Test":
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"


                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 0.95
        yalign 0.97
        
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Sauvegarde") action ShowMenu('save')
        textbutton _("Avance rapide") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Paramètres") action ShowMenu('preferences')
        #textbutton _("Relations") action ShowMenu('stats')
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

        
screen button:
    grid 5 1:
         vbox:
             textbutton "Stats"action ui.callsinnewcontext("stats_screen")
         vbox:
             textbutton "Relations"action ShowMenu('stat_rel')
         vbox:
             textbutton "Records"action ui.callsinnewcontext("record_screen")
         vbox:
             textbutton _("Résumé") action  void()#ShowMenu("stats")
         vbox:
             textbutton _("Aide") action void() # faire un menu d'aide qui explique les stats


label stats_screen:
    python:
        
        ui.hbox()
        ui.frame(xpos=0,
             ypos=0,
             xanchor='left',
             yanchor='top',
             xfill=True,
             )
        # Column 1
        ui.vbox(xpos=0, ypos=0, xanchor='left', yanchor='top') # this positions the text/bars

        ui.text("")
        ui.text("")
        ui.text("Intelligence : ")
        ui.bar(int_max, int_points)
        ui.text("Force: ")
        ui.bar(str_max, str_points)
        ui.text("Agilité: ")
        ui.bar(agi_max, agi_points)
        ui.text("\nVigueur: [vig]")
        ui.close() # for the vbox
        
        ui.close() # for the hbox
        
        ui.textbutton("Return", clicked=ui.returns("goback"))

        
    $ picked = ui.interact()
    if picked == "goback":
        return
        
label record_screen:
    python:
        
        ui.hbox()
        ui.frame(xpos=0,
             ypos=0,
             xanchor='left',
             yanchor='top',
             xfill=True,
             )
        # Column 1
        ui.vbox(xpos=0, ypos=0, xanchor='left', yanchor='top') # this positions the text/bars

        ui.text("")
        ui.text("Ryouzanki : ")
        ui.bar(rel_ryou_max, persistent.rec_ryou)
        ui.text("Elusia : ")
        ui.bar(rel_lulu_max, persistent.rec_lulu)
        ui.text("Valeth : ")
        ui.bar(rel_val_max, persistent.rec_val)
        ui.text("Laura : ")
        ui.bar(rel_lolo_max, persistent.rec_lolo)
        ui.text("Néphénie : ")
        ui.bar(rel_neph_max, persistent.rec_neph)
        ui.text("Lloyd : ")
        ui.bar(rel_lloy_max, persistent.rec_lloy)
        ui.text("Alice : ")
        ui.bar(rel_ali_max, persistent.rec_ali)
        ui.text("Salazard : ")
        ui.bar(rel_sala_max, persistent.rec_sala)
        
        ui.close() # for the vbox
        
        ui.close() # for the hbox
        
        ui.textbutton("Return", clicked=ui.returns("goback"))

        
    $ picked = ui.interact()
    if picked == "goback":
        return
        