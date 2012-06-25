label night:
    scene black
    "..."
    play music "music/shadow.ogg" fadeout 1.0
    if day == 4:
        jump night4
    elif day == 5:
        jump night5
    elif day == 6:
        jump night6
    elif day == 7:
        jump night7
    elif day == 8:
        jump night8
    elif day == 9:
        jump night9
    else:
        jump fin_night

label night4:
    s "Je n'arrive pas à dormir..."
    s "Des nouveaux visages..."
    s "Je déteste ça !"
    s "De nouveaux paramètres inconnus dans l'équation..."
    s "[j], [j]..."
    s "As tu vraiment l'intention de devenir ami avec toutes ces personnes ?"
    s "Peux tu seulement le faire..."
    jump fin_night
label night5:
label night6:
label night7:
label night8:
label night9:
    
label fin_night:   
    stop music fadeout 1.0
    "..."
    centered "{size=30}Jour [day]\n\n[weekday]{/size}"
    
    if weekday == "Dimanche":
        $ weekday = "Lundi"
    elif weekday == "Lundi":
        $ weekday = "Mardi"
    elif weekday == "Mardi":
        $ weekday = "Mercredi"
    elif weekday == "Mercredi":
        $ weekday = "Jeudi"
    elif weekday == "Jeudi":
        $ weekday = "Vendredi"
    elif weekday == "Vendredi":
        $ weekday = "Samedi"
    elif weekday == "Samedi":
        $ weekday = "Dimanche"
    else:
        $ weekday = "ERREUR"
        
    $ day += 1
    
    centered "{size=30}Jour [day]\n\n[weekday]{/size}"
    return
