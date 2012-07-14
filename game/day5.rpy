# TODO intégrer un "call day4_labo"et "call day4_labo2"
# 3 cas possibles : pas inscrit, lu, inscrit
label day5:
    scene reveil with dissolve
    play sound "sound/clock.mp3"
    m "..."
    m "Courage, dernier jour de la semaine..."
    stop sound
    play music (joueur1) fadein 2
    m "Je suis prêt[ter] !"
    play sound "sound/bell.mp3"
    m "Toujours aussi ponctuels ces deux là..."
    play sound "sound/dooropen.mp3"
    scene couloir with fade
    show elusia geez at right
    extend "Ou pas..."
    show elusia sad
    e "Salutations !"
    m "Salut !"
    menu:
        "Et Ryouzanki ?":
            $ rel_lulu += 2
            m "Et Ryouzanki ?"
            show elusia geez at center with move
            e "Cet abruti ne s'est pas réveillé."
            show elusia sad
            e "Il est en train de se préparer là."
            e "Mais plutôt qu'être tous les 3 en retard, il m'a dit de partir devant."
        "On y va ?":
            $ rel_lulu -= 2
            jump day5_solo
    menu:
        "Attendre.":
            $rel_ryou += 4
            $rel_lulu += 5
            m "Personnellement, je voudrais bien l'attendre."
            e "Heu..."
            show elusia normal
            e "Bon, d'accord !"
            show elusia happy
            e "Mais il va falloir courir pour arriver à l'heure !"
            m "Pas de souci."
            e "Vraiment ?"
            show elusia satisfied
            e "Je fais pas mal de sport et Ryou, à force d'être en retard cours pas mal aussi."
            m "Ne me sous estimes pas !"
            e "C'est ce que nous verrons !"
            scene couloir with fade
            show elusia normal
            "Quelques minutes plus tard."
            e "Que fait-on ?"
            menu:
                "Sonner.":
                    play sound "sound/bell.mp3"
                    "Je sonne..."
                "Attendre.":
                    pass
            play sound "sound/dooropen.mp3"
            show ryou angry at right
            "Soudain, la porte s'ouvre sur Ryouzanki qui nous dévisage en silence."
            show ryou happy
            r "J'arriverai avant vous !!"
            hide ryou
            show elusia angry
            e "J'hallucine, quelle enflure !"
            show elusia happy
            e "Go !"
            scene street with fade
            scene classroom with fade
            $ vig -= 1
            if sport == 'tir à l\'arc':
                "Je suis arrivé en retard..."
                "Et pas eux..."
                "J'ai fait du sport mais disons que le tir à l'arc ne m'a été d'aucune utilité."
            elif vig < 0:
                "Je suis épuisé[ter]..."
                "Je n'ai pas pu arriver à l'heure car je ne dors pas assez."
            elif str_points > 0:
                "Je suis arrivé en même temps que Ryouzanki."
                "Heureusement que j'avais fait un peu de sport lundi..."
                $rel_lulu +=2
            else:
                "Je n'ai pas fait de sport depuis belle lurette..."
                "Je suis arrivé en retard..."
            jump day5_matin
        "Partir.":
            jump day5_solo

label day5_solo:
    m "On y va ?"
    show elusia sad at center with move
    e "Oui, allons-y."
    scene street with fade
    scene classroom with fade
    "Elle est restée silencieuse jursqu'en classe."
    "Ryouzanki est arrivé en même temps que le professeur, tout essouflé."
label day5_matin:
    "Le cours porte sur des rappels de SVT..."
    "Le sang est composé de 54 \% de plasma, 45 \% de globules rouges et 1 \% de globules blancs et de plaquettes."
    "Soit 4 éléments au total."
    "Ce genre de choses..."
    scene classroom with fade
    play music (matin1) fadein 2
    show ryou normal at left
    show elusia normal at right
    e "On va revoir Alice ?"
    r "Bien sur !"
    if choix2:
        call day4_labo
    else:
        scene labo with dissolve
        show ryou normal at left
        show elusia normal at center
        show lloyd normal at right
        e "Salut Lloyd !"
        e "Tu ne saurais pas où se trouve Alice par hasard ?"
        y "Oui. Elle est partie s'acheter des sandwichs."
        y "Alors je la remplace."
        show ryou sad
        r "On l'a ratée alors..."
        e "Et toi, tu ne manges pas ?"
        y "Rectification faite, elle est partie acheter nos sandwichs."
        show ryou normal
        r "Oh, bah nous on va aller manger au parc alors."
        if aller_science == 2:
            y "Une minute [j] !"
            y "Alice m'a demandé de te dire de passer de toute urgence ce soir au club."
            y "Elle a dit que c'était d'importance capitale."
            y "Ne rate pas ce rendez-vous."
        scene parc with fade
        show elusia happy at right
        show ryou happy at left
        e "Tu sais, malgré les apparences, Lloyd et Alice s'entendent plutôt bien !"
        show ryou normal
        r "Tant qu'il ne s'agit pas d'obligations..."
        show elusia normal
        e "Lloyd est quelqu'un de très à cheval sur le règlement et la hierarchie."
        e "Et Alice est quelqu'un de plutôt méticuleux qui respecte ces règles."
        "Nous avons discuté de la hierarchie de l'AE pendant la pause."
        "C'était plutôt intéressant."


    play music (jour1) fadein 2
    scene black with dissolve
    "La pause passe si vite..."
    "Il faut retourner en cours..."
    scene classroom with dissolve
    "Un cours bien difficile et un contrôle la semaine prochaine..."
    "Ce week end, je ferais mieux de travailler un peu..."
    "Juste un peu..."
    scene classroom with dissolve
    if aller_science == 2:
        show alice sad
        a "Salut !"
        a "Le noble t'a fait passer mon message... Je suppose..."
        m "Oui."
        a "Très bien, tu viens ?"
        m "OK."
        call labo
        jump day5_end
    else:
        scene classroom with fade
        show ryou sad at left
        show elusia normal at right
        r "Bon !"
        r "Moi je vais rentrer travailler."
        show elusia satisfied
        e "Travailler... Je ne pensais pas que ce mot faisait partie de ton vocabulaire !"
        show elusia normal
        e "D'où sort cette résolution ?"
        r "Je finis tout vendredi soir pour pouvoir faire ma feignasse tout le week end !"
        show elusia geez
        e "Misère... Je vois..."
        show elusia normal
        e "Et toi, [j] ?"
        m "Moi ? Je ne sais pas.. J'aviserai !"
        show alice normal
        a "Hey Baka-powa !"
        show ryou angry
        r "Quoi encore ?"
        a "J'ai d'autres papiers à te remettre, amène toi !"
        show ryou sad
        r "Ouais ouais, j'arrive... Mais arrêtes de m'appeler Baka-powa..."
        hide ryou
        show alice sad
        a "Désolée, j'ai pas vraiment le temps de discuter."
        if aller_science == 3:
            a "Et [j], pas la peine de venir aujourd'hui."
            a "On a filé le rapport à la mairie pour qu'elle l'inspecte."
        a "Bye !"
        hide alice
        e "J'ai une réunion de déléguée."
        show elusia sad
        e "Je vais devoir t'abandonner."
        m "T'en fais pas, je saurais m'occuper !"
        show elusia normal
        e "A demain !"
        hide elusia
        "Que faire, que faire..."
label day5_choix:
        window hide None
        call screen demo_imagemap
        window show None
            
        if _return == "swimming":
            "Vendredi, pas sport ..."
            jump day5_choix
        
        elif _return == "science":
            "Les locaux sont fermés."
            "Il n'y a personne."
            jump day5_choix
            
        elif _return == "art":
            if aller_art >= 1:
                "Allons tenter de battre Valeth !"
            else:
                "Et si j'allais faire un tour au bâtiments des clubs..."
            call club
    
        elif _return == "go home":
            "Je crois que je vais rentrer."
            call go_home
            
label day5_end:
        play music (joueur1) fadein 2
        scene couloir with dissolve
        play sound "sound/dooropen.mp3"
        pause(1)
        "Ouf, je suis épuisé[ter]..."
        "5 eme jour fini."
        scene chambre m with dissolve
        play sound "sound/doorclose.mp3"
        "Je crois que je vais dormir."
        stop music
        return
