init:
    $ int_points = 0 
    $ str_points = 0 
    $ agi_points = 0
    $ agi_max = 20
    $ int_max = 20
    $ str_max = 20
    
    $ rel_ryou_max = 63   # impossible a atteindre et a calculer a cause des clubs
    $ rel_lulu_max = 67
    $ rel_val_max = 59
    $ rel_lolo_max = 41
    $ rel_neph_max =  100
    $ rel_lloy_max = 17
    $ rel_ali_max = 41
    $ rel_sala_max = 100

# Variables affectives
init python:
    register_stat("Ryouzanki", "rel_ryou", 0, rel_ryou_max)
    register_stat("Elusia", "rel_lulu", 0, rel_lulu_max)
    register_stat("Valeth", "rel_val", 0, rel_val_max)
    register_stat("Laura", "rel_lolo", 0, rel_lolo_max)
    register_stat("Néphénie", "rel_neph", 0, rel_neph_max)
    register_stat("Lloyd", "rel_lloy", 0, rel_lloy_max)
    register_stat("Alice", "rel_ali", 0, rel_ali_max)
    register_stat("Salazard", "rel_sala", 0, rel_sala_max)
    
    dp_period("Matin", "action_matin")
    dp_choice("Grasse mat'", "dodo")
    dp_choice("Jogging", "jog")
    dp_choice("Grasse mat'", "dodo")
    
    dp_period("Après midi", "action_aprem")
    dp_choice("Sortir", "out")
    dp_choice("Jouer", "game")
    dp_choice("Travailler", "devoirs2")

    dp_period("Soir", "action_soir")
    dp_choice("Dormir tôt", "dodo2")
    dp_choice("Jouer", "game2")
    dp_choice("Travailler", "devoirs3")
    
# Données persistantes
$ mp = MultiPersistent("win")

# Variables
$ sexe = 'il'
$ bite = True
$ sport = 'aucun'
$ club = 'aucun'

$ choix_1 = True
$ choix_2 = True
$ choix_3 = True
$ choix_4 = True
$ choix_5 = True

label start: 
    
    show screen button
    if persistent.ending == "win":
        call ryou
    else:
        $persistent.rec_ryou = 0
        $persistent.rec_lulu = 0
        $persistent.rec_val = 0
        $persistent.rec_lolo = 0
        $persistent.rec_neph = 0
        $persistent.rec_ali = 0
        $persistent.rec_lloy = 0
        $persistent.rec_sala = 0
        

label route:
    $ weekday = "Dimanche"
    $ day = 0
    
    $ j = 'Moi'
    $ inc = 'Jeune homme'
    $ fille = 'Jeune fille'
    $ en = 'Jeune fille'
    $ valou = 'Jeune homme'
    $ noble = 'Jeune homme'
    $ ali = 'Jeune fille'
    
    $ m = DynamicCharacter("j", color="#58D3F7", show_two_window=True)
    $ r = DynamicCharacter("inc", color="#4169E1", show_two_window=True)
    $ e = DynamicCharacter("fille", color="#FF69B4", show_two_window=True)
    $ l = DynamicCharacter("en", color="#8B0000", show_two_window=True)
    $ v = DynamicCharacter("valou", color="#800080", show_two_window=True)
    $ y = DynamicCharacter("noble", color="#FF8C00", show_two_window=True)
    $ a = DynamicCharacter("ali", color="#228B22", show_two_window=True)
    
    # $ a = Character('Alice',
                # color="#228B22",
                # window_left_padding=110,
                # show_side_image=Image("CG/mini.png", xalign=0.0, yalign=1.0), show_two_window=True)
    # 
    $ aller_sport = 0
    $ aller_art = 0
    $ aller_science = 0
    $ aller_home = 0
    
    $ sport = 'aucun'
    $ club = 'aucun'
    
    call day0
    call night
    call day1
    call night
    call day2
    call night
    call day3
    call night
    call day4
    call night
    call day5
    call night
    call day6
    call night
    
    r "Fin du jeu"
    $ persistent.ending = "win"
    python:
        if persistent.plays is None:
            persistent.plays = 1
        else:
            persistent.plays += 1
            
        plays = persistent.plays
    r "Jeu gagné [plays] fois."
    
    $ record = persistent.rec_ryou 
    $ persistent.rec_ryou = max(persistent.rec_ryou , rel_ryou)
    "Record avec Ryouzanki : [record]"
    extend "\nVous avez fait : [rel_ryou]"
    $ record = persistent.rec_lulu 
    $ persistent.rec_lulu = max(persistent.rec_lulu , rel_lulu)
    "Record avec Elusia : [record]"
    extend "\nVous avez fait : [rel_lulu]"
    $ record = persistent.rec_val 
    $ persistent.rec_val = max(persistent.rec_val , rel_val)
    "Record avec Valeth : [record]"
    extend "\nVous avez fait : [rel_val]"
    $ record = persistent.rec_lolo 
    $ persistent.rec_lolo = max(persistent.rec_lolo , rel_lolo)
    "Record avec Laura : [record]"
    extend "\nVous avez fait : [rel_lolo]"
    $ record = persistent.rec_neph 
    $ persistent.rec_neph = max(persistent.rec_neph , rel_neph)
    "Record avec Néphénie : [record]"
    extend "\nVous avez fait : [rel_neph]"
    $ record = persistent.rec_lloy 
    $ persistent.rec_lloy = max(persistent.rec_lloy , rel_lloy)
    "Record avec Lloyd : [record]"
    extend "\nVous avez fait : [rel_lloy]"
    $ record = persistent.rec_ali 
    $ persistent.rec_ali = max(persistent.rec_ali , rel_ali)
    "Record avec Alice : [record]"
    extend "\nVous avez fait : [rel_ali]"
    $ record = persistent.rec_sala 
    $ persistent.rec_sala = max(persistent.rec_sala , rel_sala)
    "Record avec Salazard : [record]"
    extend "\nVous avez fait : [rel_sala]"
    
    
return
