label night:
    scene black
    "..."
    play music (shadow1) fadeout 1.0
    if day == 4:
        jump night4
    elif day == 7:
        jump night7
    else:
        jump fin_night

label night4:
    show shadow ombre with dissolve
    s "Je n'arrive pas à dormir..."
    s "Des nouveaux visages..."
    s "Je déteste ça !"
    s "De nouveaux paramètres inconnus dans l'équation..."
    s "[j], [j]..."
    s "As tu vraiment l'intention de devenir ami avec toutes ces personnes ?"
    s "Peux tu seulement le faire..."
    s "Avant qu'il ne soit trop tard..."
    hide shadow with dissolve
    jump fin_night
label night7:
    show shadow ombre with dissolve
    s "Pourquoi j'y suis allé ?"
    s "Je ne suis pas un pion, ni une pièce de rechange..."
    s "Je les déteste !"
    s "Je vais les briser en miette un à un..."
    
label fin_night:   
    stop music fadeout 1.0

    # Il sera possible d'actualiser les barres de stats ici mais je ne le fait pas tout de suite pour
    # aider au debuggage. On peut faire avancer les barres en simultané avec un while
    if weekday == "Dimanche":
        show roue at RotoZoom(0, 50, 2, 0, 1, 0, rot_anim_timebase=True, opaque=False, xpos = -400, ypos=-80)
        $ renpy.pause(3.0)
        $ weekday = "Lundi"
    elif weekday == "Lundi":
        show roue at RotoZoom(51, 101, 2, 0, 1, 0, rot_anim_timebase=True, opaque=False, xpos = -400, ypos=-80)
        $ renpy.pause(3.0)
        $ weekday = "Mardi"
    elif weekday == "Mardi":
        show roue at RotoZoom(102, 152, 2, 0, 1, 0, rot_anim_timebase=True, opaque=False, xpos = -400, ypos=-80)
        $ renpy.pause(3.0)
        $ weekday = "Mercredi"
    elif weekday == "Mercredi":
        show roue at RotoZoom(153, 203, 2, 0, 1, 0, rot_anim_timebase=True, opaque=False, xpos = -400, ypos=-80)
        $ renpy.pause(3.0)
        $ weekday = "Jeudi"
    elif weekday == "Jeudi":
        show roue at RotoZoom(204, 254, 2, 0, 1, 0, rot_anim_timebase=True, opaque=False, xpos = -400, ypos=-80)
        $ renpy.pause(3.0)
        $ weekday = "Vendredi"
    elif weekday == "Vendredi":
        show roue at RotoZoom(255, 305, 2, 0, 1, 0, rot_anim_timebase=True, opaque=False, xpos = -400, ypos=-80)
        $ renpy.pause(3.0)
        $ weekday = "Samedi"
    elif weekday == "Samedi":
        show roue at RotoZoom(306, 356, 2, 0, 1, 0, rot_anim_timebase=True, opaque=False, xpos = -400, ypos=-80)
        $ renpy.pause(3.0)
        $ weekday = "Dimanche"
    else:
        $ weekday = "ERREUR"
        
    $ day += 1
    
    #centered "{size=30}Jour [day]\n\n[weekday]{/size}" # ancien changement de jour
    return
