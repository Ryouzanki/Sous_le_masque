init:
    $ int_points = 0 
    $ str_points = 0 
    $ agi_points = 0
    $ agi_max = 20
    $ int_max = 20
    $ str_max = 20
    
    $ rel_ryou_max = 46
    $ rel_lulu_max = 50
    $ rel_val_max = 57 # max 50 au lieu de 52 WTF
    $ rel_lolo_max = 39
    $ rel_neph_max =  100
    $ rel_lloy_max = 17
    $ rel_ali_max = 27
    $ rel_sala_max = 100

# Variables affectives
init python:
    register_stat("Ryouzanki", "rel_ryou", 0, rel_ryou_max)
    register_stat("Elusia       ", "rel_lulu", 0, rel_lulu_max)
    register_stat("Valeth       ", "rel_val", 0, rel_val_max)
    register_stat("Laura        ", "rel_lolo", 0, rel_lolo_max)
    register_stat("Néphénie  ", "rel_neph", 0, rel_neph_max)
    register_stat("Lloyd         ", "rel_lloy", 0, rel_lloy_max)
    register_stat("Alice         ", "rel_ali", 0, rel_ali_max)
    register_stat("Salazard   ", "rel_sala", 0, rel_sala_max)
    
# Données persistantes
$ mp = MultiPersistent("win")

# Personnages
image elusia normal = "CG/elusia normal.png"
image elusia happy = "CG/elusia happy.png"
image elusia angry = "CG/elusia angry.png"
image elusia sad = "CG/elusia sad.png"

image laura normal = "CG/laura normal.png"
image laura happy = "CG/laura happy.png"
image laura angry = "CG/laura angry.png"
image laura sad = "CG/laura sad.png"

image ryou normal = "CG/ryou normal.png"
image ryou happy = "CG/ryou happy.png"
image ryou angry = "CG/ryou angry.png"
image ryou sad = "CG/ryou sad.png"

image valeth normal = "CG/valeth normal.png"
image valeth happy = "CG/valeth happy.png"
image valeth angry = "CG/valeth angry.png"

image lloyd normal = "CG/lloyd normal.png"
image lloyd happy = "CG/lloyd happy.png"
image lloyd angry = "CG/lloyd angry.png"

image alice normal = "CG/alice normal.png"
image alice happy = "CG/alice happy.png"
image alice angry = "CG/alice angry.png"
image alice sad = "CG/alice sad.png"
image alice geez = "CG/alice geez.png"

image salazard normal = "CG/salazard normal.png"
image salazard happy = "CG/salazard happy.png"
image salazard angry = "CG/salazard angry.png"
image salazard sad = "CG/salazard sad.png"
image salazard geez = "CG/salazard geez.png"
image salazard geez2 = "CG/salazard geez2.png"
image salazard evil = "CG/salazard evil.png"

image prof normal = "CG/prof normal.png"
image prof happy = "CG/prof happy.png"

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

# background
image chambre m = "back/m_chambre.jpg"
image chambre e = "back/e_chambre.jpg"
image chambre r = "back/r_chambre.jpg"
image chambre m_cartons = "back/m_chambre_cartons.jpg"

image classroom = "back/ecole_classe.JPG"
image labo = "back/labo.jpg"
image couloir = "back/couloir.jpg"
image black = "#000000"
image reveil = "back/reveil.jpg"
image parc = "back/parc.jpg"
image ru = "back/ru.JPG"
image street = "back/street.jpg"
image gymnase = "back/gymnase.jpg"
image gymnaseout = "back/gymnaseout.jpg"
image salledart = "back/salledart.jpg"

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
    
    $ aller_sport = 0
    $ aller_art = 0
    $ aller_science = 0
    $ aller_home = 0
    
    $ sport = 'aucun'
    
    call day0
    call day1
    call day2
    call day3

    
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
