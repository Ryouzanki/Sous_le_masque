init:
    $ define.move_transitions('entrer', 2.5, subpixel=True)
    
    $ int_points = 0 
    $ str_points = 0 
    $ agi_points = 0
    $ agi_max = 20
    $ int_max = 20
    $ str_max = 20
    $ vig = 2
    
    $ rel_ryou_max = 200#81
    $ rel_lulu_max = 200#103 #+3 ?
    $ rel_val_max = 200#59
    $ rel_lolo_max = 200#51
    $ rel_neph_max =  1000
    $ rel_lloy_max = 200#31
    $ rel_ali_max = 200#103 #+3 ?
    $ rel_sala_max = 1000

# Variables affectives
init python:
    
    
    register_stat("Ryouzanki", "rel_ryou", 0, rel_ryou_max)
    register_stat("Elusia", "rel_lulu", 0, rel_lulu_max)
    register_stat("Valeth", "rel_val", 0, rel_val_max)
    register_stat("Laura", "rel_lolo", 0, rel_lolo_max)
    register_stat("Néphénie", "rel_neph", 0, rel_neph_max)
    register_stat("Lloyd", "rel_lloy", 0, rel_lloy_max)
    register_stat("Alice", "rel_ali", 0, rel_ali_max)
    register_stat("Salazard", "rel_sala", 0, rel_ali_max)
    
    
    dp_period("Matin", "action_matin")
    dp_choice("Grasse mat'", "d")
    dp_choice("Jogging", "s")
    dp_choice("Travailler", "t")
    
    dp_period("Après midi", "action_aprem")
    dp_choice("Sortir", "s")
    dp_choice("Jouer", "j")
    dp_choice("Travailler", "t")
    
    dp_period("Après-midi", "action_aprem")
    dp_choice("Sortir *EVENT*", "s")
    dp_choice("Jouer", "j")
    dp_choice("Travailler", "t")

    dp_period("Soir", "action_soir")
    dp_choice("Dormir tôt", "d")
    dp_choice("Jouer", "j")
    dp_choice("Travailler", "t")

    # montrer la date
    show_date = False
    weekday = "Dimanche"
    day = 1
    # def date_overlay():
        # if show_date:
            # ui.text(weekday + " %d" % day, size=20, color="#ffffff")
    # 
    # config.overlay_functions.append(date_overlay)
    
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
    
    if persistent.ending != "win":
        $persistent.rec_ryou = 0
        $persistent.rec_lulu = 0
        $persistent.rec_val = 0
        $persistent.rec_lolo = 0
        $persistent.rec_neph = 0
        $persistent.rec_ali = 0
        $persistent.rec_lloy = 0
        $persistent.rec_sala = 0
        
    show screen button
    show image "back/start.jpg"
    if not persistent.preums:
        centered "{color=#000000}{size=30}Il semblerait que ce soit votre première partie.{/size}{/color}"
        centered "{color=#000000}{size=30}Vous devriez passer voir le tutoriel.{/size}{/color}"
        centered "{color=#000000}{size=30}Celui-ci contient des explications sur les mécanismes du jeu.{/size}{/color}"
        centered "{color=#000000}{size=30}Vous pourrez y accéder ultérieurement en lançant une nouvelle partie.{/size}{/color}"
label choix_game:
    menu:
        "Tutoriel":
            call tuto
            play music (main_menu1) fadein 2
            jump choix_game
        "Route classique":
            pass
        "Route bonus" if persistent.ending == "win":
            "Route vérouillée pour cette version." # TODO
            jump ryou
            
label route:
    $ j = 'Moi'
    $ inc = 'Jeune homme'
    $ fille = 'Jeune fille'
    $ en = 'Jeune fille'
    $ valou = 'Jeune homme'
    $ noble = 'Jeune homme'
    $ ali = 'Jeune fille'
    $ sha = '???'
    $ pnjj = 'osef'
    $ proftroll = 'Professeur Laroijesea'
    $ boul = 'Boulangère'
    $ persistent.preums = True
    $ mm = DynamicCharacter("j", color="#58D3F7", show_two_window=True)
    $ r = DynamicCharacter("inc", color="#4169E1", show_two_window=True)
    $ e = DynamicCharacter("fille", color="#FF69B4", show_two_window=True)
    $ l = DynamicCharacter("en", color="#8B0000", show_two_window=True)
    $ v = DynamicCharacter("valou", color="#800080", show_two_window=True)
    $ y = DynamicCharacter("noble", color="#FF8C00", show_two_window=True)
    $ a = DynamicCharacter("ali", color="#228B22", show_two_window=True)
    $ s = DynamicCharacter("sha", color="#778899", show_two_window=True)
    $ pnj = DynamicCharacter("pnjj", color="#FFFFFF", show_two_window=True)
    $ p = DynamicCharacter("proftroll", color="#2b2a64", show_two_window=True)
    $ n = DynamicCharacter("boul", color="#fd5f6e", show_two_window=True)
    $ weekday2='Dimanche'
    $ day2='19'
    $ month2='Mars'
    # $ a = Character('Alice',
                # color="#228B22",
                # window_left_padding=110,
                # show_side_image=Image("CG/mini.png", xalign=0.0, yalign=1.0), show_two_window=True)
    # 
    $ aller_sport = 0
    $ aller_art = 0
    $ aller_science = 0
    $ science_var = 0
    $ aller_home = 0
    $ matin_sport = 1
    
    $ sport = 'aucun'
    $ club = 'aucun'
    $ show_date = True
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
    call day7
    call night
    call day8
    call night
    call day9
    call night
    call day10
    call night
    call day11
label end:
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
