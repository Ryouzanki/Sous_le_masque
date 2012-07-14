label day7:
    scene reveil2 with dissolve
    play sound "sound/bell.mp3"
    m "..."
    m "Un dimanche matin..."
    play sound "sound/dooropen.mp3"
    scene couloir with fade
    play music (elusia1) fadeout 2
    show elusia normal
    e "Salutations !"
    show elusia geez
    e "Misère..."
    show elusia satisfied
    e "Si seulement tu voyais ta tête de déterré[ter] !"
    show elusia normal
    e "Mais bon, je ne suis pas venue pour ça !"
    e"As tu fais tes devoirs ?"
    e"Est-ce que tu veux les miens ?"
    menu:
        "OK.":
            m"OK."
            show elusia happy
            e"Tiens, les voila !"
        "En quel honneur ?":
            $ rel_lulu +=3
            m "En quel honneur ?"
            show elusia satisfied
            e "Comme ça, par gentillesse..."
        "Non merci.":
            $ rel_lulu+=1
            m"Non merci."
            show elusia sad
            e"Tant pis."
    show elusia normal
    e "Est-ce que tu veux que je fasses la vaisselle aussi ?"
    m "Toi, tu veux quelque chose..."
    show elusia satisfied
    e "Je suis démasquée !"
    e "Cet après midi, nous allons faire un tennis avec Laura et Ryou."
    show elusia sad
    e "Normalement on le fait avec Alice mais elle est prise."
    menu:
        "D'accord, je vais essayer.":
            m"D'accord, je vais essayer."
            show elusia satisfied
            e "Je savais qu'on pouvait compter sur toi."
            show elusia happy
            e "Rendez vous au gymnase d'à côté à 16h !"
            e "A plus !"
            $ rel_lulu+=5
            hide elusia
        "Je ne suis pas un bouche trou...":
            m"Je ne suis pas un bouche trou..."
            show elusia geez
            e"Misère..."
            show elusia sad
            e "Excuse moi, ce n'était pas ce que je voulais dire..."
            e "Bon bah à 16h, tu saura où nous trouver."
            hide elusia
    stop music fadeout 4.0
    "Bon... Qu'est ce que je vais faire de ma journée..."
    play music (weekend1) fadein 2
    $ action_matin = None
    $ action_aprem = None
    $ action_soir = None
    call day_planner(["Matin", "Après-midi", "Soir "])
    
    if action_matin == 'd':
        "Je vais reprendre des forces tiens..."
        "..."
        $ vig += 2
        scene black with fade
        jump day7_aprem
    elif action_matin == 's':
        "Je vais faire un peu de sport..."
        scene parc with fade
        "Je cours seul dans le parc."
        $ vig -= 2
        if vig < 0:
            $ str_points += 1
            "Je manque de sommeil ces temps ci..."
            "Je n'ai pas été très efficace."
            "Peut-être que je devrais me coucher tôt finalement aujourd'hui..."
            menu:
                "C'est une bonne idée...":
                    $ action_soir = 'd'
                "Non, ça ira...":
                    pass
        else:
            $  str_points += 2
            "J'ai bien couru !"
        jump day7_aprem
    elif action_matin == 't':
        scene black with fade
        $ vig -= 1
        if vig < 0:
            "Je suis trop fatigué pour me concentrer."
            $ int_points += 1
        else:
            "Une matinée productive."
            $ int_points += 2
        jump day7_aprem
    else:
        "ERROR."
label day7_aprem:
    scene chambre m with fade
    if action_aprem == 's':
        "Sortons rejoindre les autres."
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        show ryou sad at left
        show laura happy at right
        l "Tu vois ? Je t'avais dit qu'[sexe] viendrait !"
        r "Ouais ouais, ça va ..."
        l "Allons-y !"
    else:
        "Bon, ensuite, j'avais prévu de faire quoi déjà..."
        if action_aprem == 't':
            "Ah oui, travailler..."
            "Le temps que je sorte mes affaires."
        else:
            "Ah oui, jouer..."
            "Le temps que le PC s'allume..."
        play sound "sound/bell.mp3"
        m "Elle est revenue ?"
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        show ryou sad at left
        show laura normal at right
        r "Comment qu'[sexe] se la coule douce !"
        l "Salut !"
        l "On est venu te chercher au cas où tu trouve pas le chemin !"
        m "Nan mais en fait..."
        if action_aprem == 't':
            m"J'allais travailler là..."
            show laura sad
            l"Ah bon... Je croyais qu'Elusia t'avait donné les devoirs..."
            show ryou angry
            r "C'est quoi cette histoire ?"
            r "Donc tu viens !"
            r "Pas de raison que je sois le seul à souffrir !"
            "Il me prend par la main et me tire dehors."
            "Je n'ai plus trop le choix..."
        else:
            m"J'allais jouer là..."
            show ryou angry
            r "Sérieusement ?"
            l "Avec ce temps superbe ?"
            show ryou happy
            r "T'façons, il va y avoir une coupure d'électricité donc amène toi !"
            r "Pas de raison que je sois le seul à souffrir !"
            "Il me prend par la main et me tire dehors."
            "Je n'ai plus trop le choix..."
    l "Elusia nous attend déjà sur place."
    scene gymnaseout with fade
    show ryou sad at left
    show laura normal at right
    show elusia normal sport
    e "On joue ?"
    show laura angry
    l "Hey ! On s'est pas échauffé nous, tricheuse !!"
    show ryou angry
    r "T'façons, on n'a même pas fait les équipes..."
    e "OK, OK, je vous laisse le temps de vous échauffer."
    e "Et puis on va laisser le choix des équipes au nouveau !"
    e "Avec qui veux tu jouer en double ?"
    play music (thinking1) fadein 4
    "Voyons voir..."
label day7_choix: # TODO imagemap
    m"Qui choisir..."
    menu:
        "Elusia...":
            "Elusia..."
            "C'est une sportive."
            "Qui fait régulièrement du tennis en plus..."
            "Objectivement, il y a de fortes chances qu'elle soit individuellement la meilleure."
            "On raconte qu'elle joue mal en équipe."
            "En face, Ryouzanki et Laura s'entendent plutôt bien..."
            "Et Laura aussi est compétente."
            "Elle ne veut pas perdre contre sa rivale."
            $ choix1 = 'Elusia'
        "Laura...":
            "Laura..."
            "Elle est sportive."
            "C'est une excellente leader."
            "Devant nous, on a Ryouzanki et Elusia."
            "Ryouzanki mis à part, Elusia est effrayante."
            "Elle ne veut pas perdre contre sa rivale."
            "Avec le jeu en équipe de Laura..."
            "L'obsession d'Elusia pour sa rivale peut jouer en notre faveur."
            $ choix1 = 'Laura'
        "Ryouzanki...":
            "Ryouzanki..."
            "Il n'a pas l'air d'être très sportif."
            "Mais c'est un homme alors peut être que..."
            "On sait jamais."
            "En face, Elusia et Laura."
            "Deux sportives..."
            "Mais elles ne s'entendent pas."
            "Je me demande si ça joue au tennis..."
            $ choix1= 'Ryouzanki'
    "C'est dur de prédire le résultat..."
    e "Alors ? T'as décidé ?"
    menu:
        "Oui.":
            m "Oui."
            m "J'ai choisi [choix1] !"
        "Non.":
            m"Pas encore."
            m "Une minute..."
            jump day7_choix
    m "On y va ?"
    show elusia happy sport
    e "Héhé, voilà un match qui promet d'être intéressant..."
    show ryou sad
    r "C'est toi qui le dit."
    show ryou normal
    r "Je parie sur la team [j]-[choix1]."
    l "Je commence à servir donc."
    show elusia normal sport
    e"Qui a dit ça ?"
    e"Pierre feuille ciseaux !"
    "..."
    e"J'ai gagné !"
    r "Et nous, on n'a pas le droit de servir ?"
    show elusia satisfied sport
    e"Honneur aux dames ?"
    show ryou angry
    r "OK, ça marche."
    show elusia happy sport
    e "En position !"
    play music (jeux2) fadein 4
    if choix1 == 'Elusia':
        $ rel_lulu+=10
        show elusia normal sport at left with move
        show ryou normal at Position(xpos=0.5) with move
        show laura normal at right with move
    elif choix1 == 'Laura':
        $ rel_lolo+=10
        show elusia normal sport at right with move
        show ryou normal at Position(xpos=0.5) with move
        show laura normal at left with move
    elif choix1 == 'Ryouzanki':
        $ rel_ryou+=10
        show elusia normal sport at right with move
        show ryou normal at left with move
        show laura normal at Position(xpos=0.75) with move
    else:
        "ERREUR : coéquipier non trouvé."
    show elusia happy sport
    e "Que le match commence !"
    show ryou sad
    r "Ca devait pas être un match amical ?"
    show elusia satisfied sport
    e"Un match amical ne l'est jamais vraiment..."
    call day7_normal
    "Elusia sert en première."
    "Elle prend une grande inspiration et lance la balle en l'air."
    "Sa frappe est si puissante..."
    if choix1 == 'Elusia':
        "Laura l'a touchée mais la balle a finit dans le filet."
    else:
        "[choix1] l'a touchée mais la balle a finit dans le filet."
    "Elusia est vraiment forte."
    show elusia satisfied sport
    e"15 - 0 !"
    show ryou angry
    r "T'y vas vraiment fort dès le début du match..."
    show elusia normal sport
    $ stamina = 2
    $ equipe1 = 0
    $ equipe2 = 0
    e "Quelqu'un qui ne se donne pas toujours à fond ne gagne pas..."
    show ryou sad
    r "Y'a rien a gagner..."
    e "L'équipe qui gagne se verra offrir un cocktail par la perdante."
    show laura angry
    l "Hey, il n'était pas question de ça !"
    show elusia satisfied sport
    e "Maintenant si."
    if choix1 == 'Elusia':
        jump day7_lulu
    elif choix1 == 'Laura':
        jump day7_lolo
    elif choix1 == 'Ryouzanki':
        jump day7_ryou
    else:
        "ERREUR : coéquipier non trouvé."
label day7_lulu:
    e "Je secoue un peu Ryou, sinon c'est pas fun."
    m "Ah bon ?"
    l "Ryou est un flemmard qui ne bouge que quand il y a une récompense à la clef."
    jump day7_fin_tennis
label day7_lolo:
    l "Mmmh... Elle tente de motiver Ryou..."
    m "Ah bon ?"
    l "Ryou est un flemmard qui ne bouge que quand il y a une récompense à la clef."
    jump day7_fin_tennis
label day7_ryou:
    show ryou angry
    r "Mec, me laisse pas tomber..."
    r "J'suis déjà assez fauché comme ça..."
    r "Je veux pas perdre."
    menu:
        "Mec, on va pas perdre...":
            $rel_ryou +=2
            m"Mec, on va pas perdre..."
            show ryou sad
            r "Bien sur que si..."
        "Tant pis...":
            m"Tant pis..."
            r "Nan mais sérieusement, ces deux filles m'extorquent des sous avec des paris à la con..."
    show ryou angry
    r "Et pourquoi tu t'es mis avec moi ?"
    r "On a juste aucune chance contre ces monstres !"
    menu:
        "Parce que je t'aime bien.":
            $rel_ryou +=2
            m"Parce que je t'aime bien."
            show ryou sad
            r "Désolé, mais je préfère les femmes."
        "Parce qu'on est des hommes.":
            $rel_ryou +=4
            m"Parce qu'on est des hommes."
            show ryou normal
            r "Ouais bah j'espère que t'assure !"
        "Non mais on va gagner !":
            m"Non mais on va gagner !"
            r "T'as l'air vraiment sûr de toi..."
    call day7_normal
    e"Attention, j'arrive !"
    "La balle arrive si vite que ma raquette flanche et envoie la balle dans le décor."
    show elusia satisfied sport
    e "30 - 0"
    show ryou angry
    r "D'habitude avec Alice, on séparait les deux brutes."
    menu:
        "Arrête de gémir, t'es un homme.":
            $rel_ryou -=2
            m"Arrête de gémir, t'es un homme."
            show ryou sad
            r "Vas te faire foutre..."
            r "Il faut trouver un autre moyen de gagner..."
        "T'as raison, trouvons un autre moyen de gagner.":
            $rel_ryou +=2
            m"T'as raison, trouvons un autre moyen de gagner."
            show ryou sad
            r "Clairement..."
    e "Il est finit le huddle là ?"
    r "Vas-y, je t'attends !"
    "Ryouzanki a réussit à contrer le service d'Elusia mais Laura au filet l'a contrée en volée."
    r " P'tain !"
    l "40 - 0."
    r "Nan mais les deux ensemble, c'est juste impossible..."
    r "J'ai bien une idée mais il va falloir garder ses forces."
    r "N'essaie pas d'arrêter cette balle."
    e "Essaie d'arrêter ça !"
    "La balle arrive..."
    menu:
        "Faire semblant de jouer.":
            $rel_ryou +=2
            "Je touche la balle mais la laisse partir dans le filet."
            e"Jeu !"
            e"Changement de serveur !"
        "Tenter de l'arrêter.":
            $ stamina -=1
            $rel_ryou -=2
            "J'ai réussi à l'arrêter."
            "Laura contre et l'envoie sur Ryouzanki qui la laisse passer."
            e"Jeu !"
            e"Changement de serveur !"
            menu:
                "...":
                    pass
                "T'as fait exprès de rater ?":
                    $rel_ryou -=2
                    m"T'as fait exprès de rater ?"
                    r "Bah ouais..."
                    menu:
                        "OK....":
                            m"OK...."
                        "Pour une fois qu'on renvoie une balle...":
                            $rel_ryou -=2
                            m"Pour une fois qu'on renvoie une balle..."
                            show ryou angry
                            r "T'es stupide ou quoi ?"
                            r "40-0, c'est un peu tard pour remonter ce jeu."
    r "Il faut se débrouiller pour gagner le tiens et celui de Laura et c'est gagné."
    menu:
        "OK.":
            $rel_ryou +=2
            m"OK."
        "Ce sera égalité.":
                m"Ce sera égalité."
                r "Nan, je vais gagner le mien, t'en fais pas."
        "Et le tiens ?":
                $rel_ryou -=2
                m"Et le tiens ?"
                r "Nan, je vais gagner le mien, t'en fais pas."
    show ryou normal
    r "Sert à fond sur Laura et économise des forces sur Elusia."
    r "Elusia la renverra de toutes façons."
    menu:
        "\"Quelqu'un qui ne se donne pas toujours à fond ne gagne pas...\"":
            $rel_ryou -=2
            m "\"Quelqu'un qui ne se donne pas toujours à fond ne gagne pas...\""
            show ryou angry
            r "C'est ça..."
            r "En attendant si on se donnent tous à fond sans réfléchir..."
            r "On sera crevés bien avant elles."
            r "Et on perdra à coup sûr."
            r "Fait le..."
        "OK, ça marche.":
            $rel_ryou +=2
            m "OK, ça marche."
            show ryou happy
            r "Je pense qu'on peut gagner."
    "Je dois servir sur Elusia."
    menu:
        "Servir avec un effet.":
            $rel_ryou -=2
            "Je donne un effet maximal à mon service."
            "Elusia renvoie la balle avec grande aisance."
            "Comme s'il n'y avait jamais eut d'effet."
        "Servir avec force.":
            $rel_ryou -=2
            $ stamina -= 1
            "Je frappe aussi fort que je peux."
            "Elusia renvoie la balle avec la même force."
            "Comme si elle n'était qu'un miroir."
        "Servir en économisant ses forces.":
            $rel_ryou +=2
            $ stamina += 1
            "Je frappe doucement la balle."
            "Elusia en profite pour attaquer sur Ryouzanki."
            "Il sort la balle."
    "Elle marque le point."
    show elusia satisfied sport
    $ equipe2 = 15
    e "[equipe1] - [equipe2]."
    r "Servir en mettant un effet à la balle ne sert à rien contre Elusia."
    r "Elle lit l'effet à l'avance dans le mouvement de ta raquette."
    r "Par contre, ça devrait marcher sur Laura."
    r "Continue d'économiser tes forces en même temps pour battre Elusia."
    call day7_normal
    
label day7_ryou_2:
    m "Service contre Laura."
    menu:
        "Servir avec un effet.":
            if equipe1 != 30:
                  $ equipe1 += 15
            else:
                $ equipe1 = 40
            $rel_ryou +=3
            "Je donne un effet à la balle."
            "Laura renvoie la balle mais sans attaquer."
            "Après un échange intense, nous remportons le point."
            show ryou happy
        "Servir avec force.":
            $rel_ryou -=2
            $ stamina -= 1
            "Je frappe aussi fort que je peux."
            "Laura renvoie la balle sans attaquer."
            if stamina >= 0:
                $ n = renpy.random.randint(1,3)
            else:
                $ n = renpy.random.randint(1,2)
            if n != 1:
                "Après un échange intense, nous remportons le point."
                if equipe1 != 30:
                      $ equipe1 += 15
                else:
                    $ equipe1 = 40
                show ryou happy
            else:
                "Après un échange intense, nous sortons la balle."
                show ryou angry
                if equipe2 != 30:
                      $ equipe2 += 15
                else:
                    $ equipe2 = 40
        "Servir en économisant ses forces.":
            $ stamina += 1
            "Je frappe doucement la balle."
            $ n = renpy.random.randint(1,3)
            if n == 1:
                "Après un échange intense, nous remportons le point."
                if equipe1 != 30:
                      $ equipe1 += 15
                else:
                    $ equipe1 = 40
                show ryou happy
            else:
                "Après un échange intense, nous sortons la balle."
                show ryou angry
                if equipe2 != 30:
                      $ equipe2 += 15
                else:
                    $ equipe2 = 40
    if (equipe1 != 55) and (equipe2 != 55):
        r "[equipe1] - [equipe2] !"
    else:
        jump day7_ryou_2_fin
    m "Service contre Elusia..."
    menu:
        "Servir avec un effet.":
            $rel_ryou -=2
            "Je donne un effet maximal à mon service."
            "Elusia renvoie la balle avec grande aisance."
            "Comme s'il n'y avait jamais eut d'effet."
            $ n = renpy.random.randint(1,4)
            if n == 1:
                "Après un échange intense, nous remportons le point."
                if equipe1 != 30:
                      $ equipe1 += 15
                else:
                    $ equipe1 = 40
                show ryou happy
            else:
                "Après un échange intense, nous sortons la balle."
                show ryou angry
                if equipe2 != 30:
                      $ equipe2 += 15
                else:
                    $ equipe2 = 40
        "Servir avec force.":
            $rel_ryou +=2
            $ stamina -= 1
            "Je frappe aussi fort que je peux."
            "Elusia renvoie la balle sans attaquer."
            if stamina >= 0:
                $ n = renpy.random.randint(1,3)
            else:
                $ n = 0
            if n != 1:
                if equipe1 != 30:
                      $ equipe1 += 15
                else:
                    $ equipe1 = 40
                "Après un échange intense, nous marquons un point."
                show ryou happy
            else:
                "Après un échange intense, nous sortons la balle."
                if equipe2 != 30:
                      $ equipe2 += 15
                else:
                    $ equipe2 = 40
                show ryou angry
        "Servir en économisant ses forces.":
            $ stamina += 1
            "Je frappe doucement la balle."
            $ n = renpy.random.randint(1,4)
            if n == 1:
                "Après un échange intense, nous remportons le point."
                if equipe1 != 30:
                      $ equipe1 += 15
                else:
                    $ equipe1 = 40
                show ryou happy
            else:
                "Après un échange intense, nous sortons la balle."
                if equipe2 != 30:
                      $ equipe2 += 15
                else:
                    $ equipe2 = 40
                show ryou angry
    if (equipe1 != 55) and (equipe2 != 55):
        r "[equipe1] - [equipe2] !"
        jump day7_ryou_2
    else:
        jump day7_ryou_2_fin
        
label day7_ryou_2_fin :
    if equipe1 == 55:
        show ryou happy
        r "Un jeu pour nous !"
        show elusia satisfied sport
        e "Ca ne se passera pas comme ça !"
        show laura sad
        l "Ryou va encore choisir les trucs les plus chers..."
        show elusia surprised sport
        e "Hey ! On a pas encore perdu !"
        $ jeu = 1
        show ryou angry
        r "Ca vient, ça vient..."
    else:
        show elusia satisfied sport
        e "Un jeu de plus pour nous."
        show ryou angry
        r "Ca ne se passera pas comme ça !"
        show ryou sad
        r "Mec, fais quelque chose, encore un jeu et on est finit..."
        $ jeu = 0
    $ equipe1 = 0
    $ equipe2 = 0
label day7_ryou_3:
    "C'est au tour de Laura de servir."
    
    jump day7_fin_tennis
label day7_fin_tennis:
    return 
label day7_normal:
    show ryou normal
    show elusia normal sport
    show laura normal
    return
