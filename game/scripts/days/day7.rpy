# TODO :
#            $ renpy.block_rollback()
#            tie break (day7_ryou6)
# lose, win, perfect
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
            hide elusia with easeoutright
        "Je ne suis pas un bouche trou...":
            m"Je ne suis pas un bouche trou..."
            show elusia geez
            e"Misère..."
            show elusia sad
            e "Excuse moi, ce n'était pas ce que je voulais dire..."
            e "Bon bah à 16h, tu saura où nous trouver."
            hide elusia with easeoutright
    stop music fadeout 4.0
    "Bon... Qu'est ce que je vais faire de ma journée..."
    play music (weekend1) fadein 2
    $ action_matin = None
    $ action_aprem = None
    $ action_soir = None
    call day_planner(["Matin", "Après-midi", "Soir"])
    
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
        l "On est venu te chercher au cas où tu trouves pas le chemin !"
        m "Nan mais en fait..."
        if action_aprem == 't':
            m"J'allais travailler là..."
            show laura sad
            l"Ah bon... Je croyais qu'Elusia t'avait donné les devoirs..."
            show ryou angry
            r "C'est quoi cette histoire ?"
            r "Donc tu viens !"
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
    show elusia sport normal
    e "On fait en 4 jeux."
    e "Chacun servira pendant un jeu."
    e "En cas d'égalité, on fera un 5ème jeu en tie-break."
    l "Je commence à servir donc."
    show elusia satisfied sport
    e"Bien essayé..."
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
        $ rel_lolo+=4
        $ rel_ryou-=4
        show elusia normal sport at left with move
        show ryou angry at Position(xpos=0.5) with move
        show laura normal at right with move
    elif choix1 == 'Laura':
        $ rel_lolo+=10
        $ rel_ryou+=4
        $ rel_lulu+=4
        show elusia normal sport at right with move
        show ryou normal at Position(xpos=0.5) with move
        show laura normal at left with move
    elif choix1 == 'Ryouzanki':
        $ rel_ryou+=10
        $ rel_lolo-=4
        $ rel_lulu-=4
        show elusia sad sport at right with move
        show ryou normal at left with move
        show laura sad at Position(xpos=0.75) with move
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
    show ryou angry
    r "Bon..."
    r "On tire que sur Laura..."
    r "Elle va fatiguer plus vite qu'Elusia."
    menu:
        "C'est pas très cool ça...":
            m "C'est pas très cool ça..."
            r "J'sais mais j'veux pas perdre."
            show ryou sad
            r "Je ne peux pas te forcer à faire des trucs pas cools avec moi."
            r "Si tu ne veux pas, ne le fais pas."
            m "Oui, c'est mieux."
            "..."
            "Je crois que Ryouzanki à appliqué son plan."
            "Nous avons perdu le set de très peu."
            $ rel_ryou -= 5
        "OK, ça marche...":
            m "OK, ça marche."
            show ryou happy
            r "J'savais que tu comprendrais."
            $ rel_ryou += 5
            "..."
            "Plus nous attaquons Laura et plus elle fatigue."
            "Nous avons gagné le set haut la main, grâce aux fautes de Laura."
            $ jeu += 1
    call day7_normal
    if jeu ==2:
        show ryou happy
        r "Et voilà !"
        r "2 Jeux à 1 !!"
    else:
        show ryou sad
        r "..."
        show elusia satisfied sport
        $ jeu2 = 3 - jeu
        e "[jeu2] jeux à [jeu]."
        e "Où est passé votre fierté d'homme ?"
        r "C'est finit, on ne peut plus gagner..."
        menu:
            "On peut au moins égaliser." if jeu == 1:
                $ rel_ryou += 4
                m "On peut au moins égaliser."
                show ryou sad
                r "Pas faux."
                show ryou happy
                r "On peut même gagner !"
                show ryou normal
                r "Mais avec le Tie Break, il va falloir donner..."
            "Il n'y a pas que gagner qui compte...":
                $ rel_ryou -= 4
                m "Il n'y a pas que gagner qui compte..."
                show ryou angry
                r "..."
            "Bah tant pis...":
                $ rel_ryou -= 2
                m "Bah tant pis..."
                show ryou angry
                r "..."
        if jeu == 0:
            "Nous avons déjà perdu."
            "Ryouzanki le sait, alors il joue à peine."
            jump day7_ryou_lose
label day_ryou4:
    call day7_normal
    "Il ne reste qu'un jeu."
    "Ryouzanki sert."
    "Il n'est pas très fort mais il est précis."
    r "Mec... Tire entre les deux..."
    m "Entre les deux ?"
    m "Tu veux dire, entre Elusia la gauchère à gauche et Laura la droitière à droite ?"
    m "C'est pas un peu kamikaze ?"
    r  "Nan, t'en fais pas..."
    menu:
        "Je vais essayer.":
            m "Je vais essayer."
            $ rel_ryou += 3
            "Nous tirons tous les deux au milieu."
            "Nous gagnons des points faciles car aucune ne bouge."
        "Non, c'est stupide.":
            m "Non, c'est stupide."
            $ rel_ryou -= 2
            "Ryouzanki marque des points faciles en tirant au centre car aucune ne bouge."

    show laura angry
    l "Elusia, tu pourrais bouger un peu !"
    l "Au lieu de regarder la balle passer !"
    show elusia geez sport
    e "Elle était sur ton terrain la balle..."
    l "Mon terrain ?"
    l "Tu vois bien que je suis épuisée..."
    show elusia sad sport
    e "Ce n'est pas ma faute si tu es si faible !"
    menu:
        "C'est pas la peine de vous disputer !":
            m "C'est pas la peine de vous disputer !"
            show ryou happy
            r "Après, tout, vous avez déjà perdu."
            m "C'était pas vraiment ce que je voulais dire..."
            menu:
                "En fait, si.":
                    m "En fait, si."
                    m "Vous avez perdu."
                    show elusia angry sport
                    e "Très bien."
                    e "Laura, je prends tout ce qui est à ma portée."
                    l "Bah vas-y !"
                    $ rel_ryou += 5
                    $ rel_lulu -= 3
                    $ rel_lolo -= 3
                    jump day7_ryou5
                "Le tennis, c'est qu'un jeu.":
                    $ rel_lulu += 2
                    $ rel_lolo += 4
                    m "Le tennis, c'est qu'un jeu."
                    m "Vous avez perdu de vu le but d'un jeu, on dirait..."
                    show elusia geez sport
                    e "C'est vrai..."
                    show elusia happy sport
                    e "Perso, je me suis bien amusée."
                    e "On n'arrête là ?"
                    menu:
                        "OK.":
                            m "OK."
                            m "Ryou ?"
                            show ryou sad
                            r "Je me plie à la demande de ces dames."
                            show laura happy
                            l "Allons quand même grignoter un coup."
                            $ rel_lulu += 3
                            $ rel_lolo += 3
                            jump day7_perfect
                        "Non, finissons.":
                            m "Non, finissons."
                            r "Oui, chef !"
                            show elusia sad sport
                            e "Bon OK..."
                            $ rel_ryou += 3
                            jump day7_ryou5
                "Vous êtes toutes les deux en tort.":
                    $ rel_lulu += 4
                    $ rel_lolo += 2
                    m "Vous êtes toutes les deux en tort."
                    m "Le tennis, c'est l'équilibre entre les deux."
                    m "C'est vrai, Elusia, tu devrais aider Laura."
                    m "Laura, tu devrais dire à Elusia quand tu es en difficulté."
                    show laura sad
                    l "Désolée."
                    show elusia geez sport
                    e "Bon, tâchons de jouer mieux..."
                    jump day7_ryou5
                    
        "Elusia, tu devrais jouer en équipe.":
               m "Elusia, tu devrais jouer en équipe."
               $ rel_lulu -= 4
               $ rel_lolo += 3
               show laura happy
               l "Il n'y a pas que le territoire qui compte..."
               l "Quand je suis en difficulté, tu devrais les prendre à ma place."
               l "Tu peux même attaquer..."
               show elusia angry sport
               e "Tu n'as qu'à pas être en difficulté !"
               show ryou sad
               r "On s'en fout, jouez..."
               jump day7_ryou5
        "Laura, t'es juste trop faible.":
               m "Laura, t'es juste trop faible."
               $ rel_lolo -= 4
               $ rel_lulu += 3
               show elusia satisfied sport
               e "Toujours compter sur ses coéquipiers, c'est faible..."
               e "La performance individuelle compense ce défaut."
               show laura angry
               l "Dans ce cas, à quoi ça sert de jouer en couple ?"
               show ryou sad
               r "On s'en fout, jouez..."
               jump day7_ryou5
        "Vous formez un mauvais couple.":
            m "Vous formez un mauvais couple."
            m "Vous n'êtes pas faîtes pour vous entendre."
            $ rel_lulu -= 3
            $ rel_lolo -= 3
            show laura angry
            l "Sans déconner, tu le sais et c'est un peu toi qui nous a mises ensembles..."
            show elusia sad sport
            e "J'ai juste l'impression que c'était volontaire..."
            show elusia geez sport
            e "Moi qui voulait simplement jouer avec toi pour essayer ou avec Ryou comme d'habitude..."
            show ryou sad
            r "Bon, on termine quand même hein..."
            jump day7_ryou5
label day7_ryou5:
    "Elusia a reprit du poil de la bête."
    "La détermination se lit dans ses yeux."
    "Elle a arrêté de ne contrôler que sa zone."
    "La stratégie de Ryouzanki ne fonctionne plus."
    "Mais il est trop tard."
    "Nous remportons le jeu."
    $ jeu += 1
    if jeu == 2:
        jump day7_ryou6
    elif jeu < 2:
        jump day7_ryou_lose
    else:
        jump day7_ryou_win
label day7_ryou6:
    call day7_normal
    show elusia satisfied sport
    e "Huh... Tie-Break hein..."
    show elusia normal sport
    e "Pas mal du tout..."
    show laura sad
    l "Tâchons de gagner..."
    e "Bien entendu."
    show elusia angry sport
    e "Je ne peux pas me permettre de perdre maintenant."
    e "Alors je vais aussi prendre tes balles."
    l "..."
    l "J'attendais que ça, tient..."
    "Elusia a reprit du poil de la bête."
    "La détermination se lit dans ses yeux."
    "Elle a arrêté de ne contrôler que sa zone."
    "La stratégie de Ryouzanki ne fonctionne plus."
    "Les filles gagnent de peu."
    show ryou sad
    "Ryouzanki tombe à genou, épuisé."
    jump day7_ryou_lose_end
label day7_ryou_lose:
    show elusia satisfied sport
    $ jeu2 = 4 - jeu
    e "Bon bah voilà... [jeu2] à [jeu] !"
    show ryou angry
    "Ryouzanki lance sa raquette au sol..."
label ay7_ryou_lose_end:
    show laura happy
    l "Vous savez ce qu'il vous reste à faire !"
    show ryou sad
    r "Hum... Se mettre à genou ?"
    show elusia happy sport
    e "Bien tenté mais non..."
    e "Tu dois nous inviter à boire un verre."
    l "Tu n'y échappes pas [j] !"
    show elusia normal sport
    e "Aller, je sais que tu touches un peu le fond..."
    show elusia satisfied sport
    e "Je vais me payer ma part moi même."
    show laura normal
    l "Je vais faire pareil, je n'ai jamais aimé l'idée de ce pari."
    jump day7_pari
label day7_ryou_win:
    show ryou happy
    r "Et c'est la victoire !!"
    show elusia geez sport
    e "Mince..."
    show laura sad
    l "On aura fait ce qu'on a pu..."
    show elusia angry sport
    e "..."
    show ryou normal
    r "Nan Elusia, c'est pas vraiment le moment..."
    show elusia sad sport
    e "Oui..."
    show ryou happy
    r "Aller, je suis trop gentleman pour que des filles paient ma part..."
    show elusia geez sport
    e "Tu n'as pas à faire ça..."
    l "Le pari, c'est ton idée, Elusia à la base..."
    r "Nan mais c'est bon, je vais payer juste ma part."
    menu:
        "Je vais payer la mienne.":
            m "Je vais payer la mienne."
            $ rel_lulu += 3
            $ rel_lolo += 3
        "Il reste juste la mienne.":
            m "Il reste juste la mienne."
    r "Heu... Oui..."
    r "On y va ? j'ai soif..."
    e "D'où l'intérêt d'apporter une bouteille d'eau..."
label day7_pari:
                                                                        # TODO best ending
label day7_fin_tennis:
    call save
    return
label save:
    menu:
        "Une semaine s'est écoulée, voulez vous sauvegarder ?"
        "Oui.":
              $ renpy.game_menu("save_screen")
        "Non.":
              pass
    return
label day7_normal:
    show ryou normal
    show elusia normal sport
    show laura normal
    return
