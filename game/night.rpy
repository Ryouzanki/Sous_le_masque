label night:
    scene black
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
