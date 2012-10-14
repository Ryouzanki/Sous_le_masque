# TODO :
# remise au max des relations
# rééquilibrage relationnel
# ending bar

label day7:
    scene reveil2 with fade
    play sound "sound/bell.mp3"
    m "..."
    ma "Un dimanche matin...?"
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
    e "As tu fais tes devoirs ?"
    e "Est-ce que tu veux les miens ?"
    menu:
        "OK.":
            # $ renpy.block_rollback()
            m "OK."
            show elusia happy
            e "Tiens, les voila !"
        "En quel honneur ?":
            # $ renpy.block_rollback()
            $ rel_lulu +=3
            m "En quel honneur ?"
            show elusia satisfied
            e "Comme ça, par gentillesse..."
        "Non merci.":
            # $ renpy.block_rollback()
            $ rel_lulu+=1
            m "Non merci."
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
            # $ renpy.block_rollback()
            m"D'accord, je vais essayer."
            show elusia satisfied
            e "Je savais qu'on pouvait compter sur toi."
            show elusia happy
            e "Rendez vous au gymnase d'à côté à 16h !"
            e "A plus !"
            $ rel_lulu+=5
            hide elusia with easeoutright
        "Je ne suis pas un bouche trou...":
            # $ renpy.block_rollback()
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
                    # $ renpy.block_rollback()
                    $ action_soir = 'd'
                "Non, ça ira...":
                    # $ renpy.block_rollback()
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
        scene couloir 
        show ryou sad:
            left
        show laura happy:
            right
        with fade
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
        ma "Elle est revenue ?"
        play sound "sound/dooropen.mp3"
        scene couloir
        show ryou sad :
            left
        show laura normal:
            right
        with fade
        r "Comment qu'[sexe] se la coule douce !"
        l "Salut !"
        l "On est venu te chercher au cas où tu trouves pas le chemin !"
        ma "Nan mais en fait..."
        if action_aprem == 't':
            ma "J'allais travailler là..."
            show laura sad
            l"Ah bon... Je croyais qu'Elusia t'avait donné les devoirs..."
            show ryou angry
            r "C'est quoi cette histoire ?"
            r "Donc tu viens !"
        else:
            ma "J'allais jouer là..."
            show ryou angry
            r "Sérieusement ?"
            l "Avec ce temps superbe ?"
            show ryou happy
            r "T'façons, il va y avoir une coupure d'électricité donc amène toi !"
    r "Pas de raison que je sois le seul à souffrir !"
    "Il me prend par la main et me tire dehors."
    "Je n'ai plus trop le choix..."
    l "Elusia nous attend déjà sur place."
    scene gymnaseout
    show ryou sad:
        left
    show laura normal:
        right
    show elusia normal sport:
        center
    with fade
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
    m "Qui choisir..."
    menu:
        "Elusia...":
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
            m "Oui."
            mh "J'ai choisi [choix1] !"
        "Non.":
            # $ renpy.block_rollback()
            m "Pas encore."
            m "Une minute..."
            jump day7_choix
    m "On y va ?"
    show elusia happy sport
    e "Héhé, voilà un match qui promet d'être intéressant..."
    show ryou sad
    r "C'est toi qui le dit."
    show ryou normal
    r "Je parie sur la team [j]-[choix1]."
    show elusia normal sport
    e "On fait en 4 jeux."
    e "Chacun servira pendant un jeu."
    e "En cas d'égalité, on fera un 5ème jeu en tie-break."
    l "Je commence à servir donc."
    show elusia satisfied sport
    e "Bien essayé..."
    e "Pierre feuille ciseaux !"
    "..."
    e"J'ai gagné !"
    r "Et moi, j'ai pas le droit de servir ?"
    show elusia satisfied sport
    e "Honneur aux dames ?"
    show ryou angry
    r "OK, ça marche."
    show ryou happy
    "Ryouzanki me regarde en souriant."
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
    e "Un match amical ne l'est jamais vraiment..."
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
    show elusia happy sport
    e "Je secoue un peu Ryou, sinon c'est pas fun."
    m "Ah bon ?"
    l "Ryou est un flemmard qui ne bouge que quand il y a une récompense à la clef."
    show elusia normal sport
    e "Et bien maintenant, nous sommes alliés pour cette bataille !"
    e "Tâchons de les écraser !"
    menu:
        "T'en fais pas un peu trop ?":
            # $ renpy.block_rollback()
            m "T'en fais pas un peu trop ?"
            $ rel_lulu -= 2
            show elusia surprised sport
            e "Tu trouves ?"
            show elusia normal sport
            e "Les sports de compétition comme le tennis..."
            show elusia satisfied sport
            e "Ont pour principe qu'une équipe gagne car elle a surpassé l'équipe adverse !"
            show elusia sad sport
            e "Je trouve dommage que tu ne comprennes pas cela."
        "Oui...":
            # $ renpy.block_rollback()
            m "Oui..."
            show elusia surprised sport
            e "Hey ! Tu pourrais être un peu plus motivé[ter] !"
            menu:
                "Je vais essayer.":
                    # $ renpy.block_rollback()
                    $ rel_lulu += 3
                    m "Je vais essayer."
                    show elusia normal sport
                    e "C'est mieux !"
                    e "Partir avec un bon moral, c'est avoir la victoire à portée de main."
                "Non.":
                    # $ renpy.block_rollback()
                    $ rel_lulu -= 3
                    m "Non."
                    show elusia sad sport
                    e "T'es pas cool..."
                    e "Moi qui me faisait une joie de jouer avec toi..."
        "C'est comme si c'était fait !":
            # $ renpy.block_rollback()
            $ rel_lulu += 5
            mh "C'est comme si c'était fait !"
            show elusia happy sport
            e "Super !"
            e "J'aime cet état d'esprit !"
            show elusia normal sport
            e "Partir avec un bon moral, c'est avoir la victoire à portée de main."
    show elusia normal sport
    e "Sinon, simple curiosité..."
    e "Pourquoi moi ?"
    menu:
        m "Et bien..."
        "Tu es la plus forte non ?":
            # $ renpy.block_rollback()
            m "Tu es la plus forte non ?"
            $ rel_lulu += 5
            show elusia satisfied sport
            e "Tu as parfaitement raison."
            show elusia happy sport
            e "Excellent choix !"
        "Tu es la plus jolie.":
            # $ renpy.block_rollback()
            mh "Tu es la plus jolie."
            $ rel_lulu += 3
            show elusia shy sport
            e "P...Pardon ?!"
            menu:
                "Ca va, je plaisante...":
                    # $ renpy.block_rollback()
                    mh "Ca va, je plaisante..."
                    show elusia timid sport
                    e "Si possible, j'aimerais que tu évites ce genre de plaisanterie..."
                    menu:
                        "Oui, désolé.":
                            # $ renpy.block_rollback()
                            $ rel_lulu -= 1
                            m "Oui, désolé."
                            show elusia sad sport
                            e "C'est pas bien grave..."
                        "Nan, t'es mignonne quand tu rougis.":
                            # $ renpy.block_rollback()
                            $ rel_lulu += 2
                            mh "Nan, t'es mignonne quand tu rougis."
                            show elusia embarassed sport
                            e "Mais qu'est ce qui te prends de dire des trucs pareils !"
                            e "C'est pas le moment de me déconcentrer !"
                            show elusia timid sport                    
                "Bah oui, c'est vrai quoi...":
                    # $ renpy.block_rollback()
                    $ rel_lulu += 4
                    m "Bah oui, c'est vrai quoi..."
                    show elusia embarassed sport
                    e "Mais qu'est ce qui te prends de dire des trucs pareils !"
                    e "C'est pas le moment de me déconcentrer !"
                    show elusia timid sport
                "Je t'aime, Elusia...":
                    # $ renpy.block_rollback()
                    mh "Je t'aime, Elusia..."
                    show elusia embarassed sport
                    e "C'est pas un peu tôt pour ce genre de chose ?"
                    show elusia timid sport
                    e "Tu me connais à peine..."
        "Tu es la plus sympa.":
            # $ renpy.block_rollback()
            mh "Tu es la plus sympa."
            e "Ah bon..."
            show elusia happy sport
            e "Tant mieux alors !"
    show ryou angry
    r "Mais qu'est-ce qu'ils font ?"
    show laura happy
    l "Ils se glissent des mots doux !"
    show ryou sad
    r "Très marrant."
    r "Bon, il arrive ce service ?"
    e "On continue ?"
    m "Bien sûr."
    "..."
    "Elusia est vraiment très forte."
    "A elle seule, elle a remporté le jeu."
    $ jeu = 1
    jump day7_elu
label day7_elu:
    call day7_normal
    show elusia satisfied sport
    e "Et voilà !"
    e "1 jeu à 0 !"
    show ryou sad
    r "Tu m'étonnes..."
    show laura sad
    l "..."
    menu:
        "T'es vraiment forte !":
            # $ renpy.block_rollback()
            $ rel_lulu += 3
            mh "T'es vraiment forte !"
            show elusia happy sport
            e "Merci, espérons que tu fasses aussi bien !"
        "Je vais faire mieux !":
            # $ renpy.block_rollback()
            mh "Je vais faire mieux !"
            show elusia normal sport
            e "Ah bon... Nous verrons."
    e "Ne les sous estimes pas !"
    e "Laura est plutôt adroite."
    e "Et Ryou n'en a pas l'air mais il est précis et fourbe."
    m "OK."
    "C'est à Laura de servir."
    "Elle sert sur Elusia."
    "Son service est mou et sans effet."
    "Elusia attaque sur le service et marque le point."
    show elusia normal sport
    e "Hé...."
    show laura happy
    l "0 - 15."
    show laura normal
    "Elle va servir."
    menu:
        "Attaquer sur le service.":
            # $ renpy.block_rollback()
            $ rel_lulu -= 2
            "Je décide d'attaquer sur son service."
            "Elle frappe."
            "La balle va bien plus vite que prévu."
            "En la heurtant, ma raquette dévie !"
            "La balle fini dans le filet."
            show laura happy
            l "15 A !"
        "Défendre sur le service.":
            # $ renpy.block_rollback()
            "Je décide de défendre sur son service."
            "Elle frappe."
            "La balle va bien plus vite que prévu."
            "Adoptant une attitude défensive, j'arrive à renvoyer la balle."
            "Ryouzanki au filet intercepte immédiatement la balle et me la renvoie dessus."
            "Je l'avais oublié lui..."
            "De si près, il m'est impossible de l'arrêter."
            "L'équipe adverse marque le point."
            show ryou happy
            r "15 A !"
    show elusia sad sport
    e "..."
    $ choix1 = True
label day7_elu_2:
    menu:
        "Désolé[ter].":
            # $ renpy.block_rollback()
            $ rel_lulu += 2
            m "Désolé[ter]."
            e "Tu fais ce que tu peux hein..."
            e "Je t'avais prévenu qu'ils étaient forts."
            menu:
                "Je n'ai pas été assez prudent[ter].":
                    # $ renpy.block_rollback()
                    $ rel_lulu += 2
                    m "Je n'ai pas été assez prudent[ter]."
                    e "Je vois ça."
                "Oui je sais merci.":
                    # $ renpy.block_rollback()
                    ma "Oui je sais merci."
                    e "C'est juste vrai."
            show elusia geez sport
            e "Espérons que cela ne se reproduise pas."
        "Ils sont fourbes !":
            # $ renpy.block_rollback()
            m "Ils sont fourbes !"
            show elusia normal sport
            e "Que veux tu dire ?"
            menu:
                m "Et bien..."
                "Ils cachent bien leur jeu...":
                    # $ renpy.block_rollback()
                    $ rel_lulu -= 2
                    m "Ils cachent bien leur jeu..."
                    show elusia geez sport
                    e "Je t'avais prévenu qu'ils étaient forts."
                    e "Espérons que cela ne se reproduise pas."
                "Ils me visent intentionnellement...":
                    # $ renpy.block_rollback()
                    $ rel_lulu -= 4
                    m "Ils me visent intentionnellement..."
                    show elusia geez sport
                    e "Tu ne serais pas un peu parano sur les bords ?"
        "..." if choix1:
            # $ renpy.block_rollback()
            $ rel_lulu -= 2
            $ choix1 = False
            m "..."
            e "Tu n'as donc rien à me dire ?"
            jump day7_elu_2
        "Je n'ai rien à te dire." if not choix1:
            # $ renpy.block_rollback()
            $ rel_lulu -= 4
            m "Je n'ai rien à te dire."
            show elusia angry sport
            e "Ah..."
    l "J'arrive !"
    "Laura sert de nouveau sur Elusia."
    "C'est assez visible, Laura \"donne\" le service."
    "Elusia marque le point."
    "Ryouzanki paraît inactif. Il suivait à peine la balle du regard."
    show elusia happy
    e "15 - 30 !"
    "Laura doit servir sur moi."
    "Elle se concentre."
    "Je regarde Ryouzanki furtivement."
    "Il est concentré, les yeux rivés sur le tamis de ma raquette."
    "Laura sert."
    $ equipe1 = 15
    $ equipe2 = 30
    $ choix1 = True
label day7_elu_3:
    menu:
        "Que faire ?"
        "Défendre.":
            # $ renpy.block_rollback()
            "En jouant défensif, je renvoie aisément la balle."
            "Celle-ci atterrit entre les deux."
            l "Ryou !"
            r "Arg !"
            "Ryouzanki la frappe de justesse mais perd l'équilibre."
            "Elusia l'attaque en retour et déséquilibré, il sort la balle."
            $ equipe2 = 40
        "Attaquer sur Ryouzanki.":
            # $ renpy.block_rollback()
            "J'attaque sur Ryouzanki."
            "Force contre force, je n'ai pas pu envoyer une attaque digne de ce nom."
            "Il smash aux pieds d'Elusia qui, à cette distance ne peux pas contrer."
            $ equipe1 = 30
        "Attaquer sur Laura." if choix1:
            # $ renpy.block_rollback()
            "J'attaque sur Laura."
            "Force contre force, je n'ai pas pu envoyer une attaque digne de ce nom."
            "Laura attaque de nouveau sur moi."
            $ choix1 = False
            jump day7_elu_3
        "Encore attaquer Laura" if not choix1:
            # $ renpy.block_rollback()
            "J'attaque encore sur Laura."
            "Laura renvoie encore la balle sur moi."
            "Cette fois, je la rate."
            $ equipe1 = 30
    menu:
        "Ils me visent intentionnellement !":
            # $ renpy.block_rollback()
            ma "Ils me visent intentionnellement !"
        "Elusia, tu ne remarques rien d'anormal ?":
            # $ renpy.block_rollback()
            $ rel_lulu +=3
            m "Elusia, tu ne remarques rien d'anormal ?"
    show elusia sad sport
    e "Désolée... Je ne voulais pas y croire."
    show elusia geez sport
    e "Ca ressemble à un stratagème de Ryou tout craché..."
    e "Exceptionnellement, je vais t'aider."
    menu:
        "Tu es censée m'aider, on est une équipe...":
            # $ renpy.block_rollback()
            $ rel_lulu -= 4
            m "Tu es censée m'aider, on est une équipe..."
            show elusia normal sport
            e "Possible..."
            e "Mais tu es censé[ter] être assez compétent[ter] pour ne pas avoir besoin de moi."
        "Pourquoi exceptionnellement ?":
            # $ renpy.block_rollback()
            m "Pourquoi exceptionnellement ?"
            show elusia normal sport
            e "Parce que je veux gagner face à Laura sur son terrain."
        "D'accord, merci !":
            # $ renpy.block_rollback()
            $ rel_lulu += 2
            m "D'accord, merci !"
            show elusia normal sport
            e "Maintenant, ensemble, gagnons cette partie !"
    "J'ai fait de mon mieux pour renvoyer les balles et Elusia a été très agressive."
    "Après plusieurs échanges, notre dur labeur est récompensé."
    show ryouzanki angry
    show laura sad
    show elusia happy sport
    e "Yes !"
    show elusia normal sport
    e "2 jeux à 0 donc !"
    r  "Tss !"
    l "..."
    "Par la suite, l'équipe adverse a perdu toute volonté de jouer."
    "Ils étaient mous et sans énergie."
    "Ils nous ont \"offert\" la victoire."
    show elusia happy sport
    show laura sad
    show ryou sad
    e "Et c'est la victoire !"
    show elusia satisfied sport
    e "Une écrasante victoire 4-0 !"
    e "Vous savez ce qu'il vous reste à faire !"
    r "Hum... Se mettre à genou ?"
    show elusia happy sport
    e "Bien tenté mais non..."
    show elusia sad sport
    e "Faites pas ces têtes là, je gagne."
    show elusia normal sport
    e "Je m'octroie donc le droit d'annuler le gage !"
    call day7_normal
    l "Ca ne te ressemble pas..."
    e "Je sais que Ryou touche le fond et je pense que tu ne nous aurais pas fait payer."
    e "Parce que [j] joue pour la première fois avec nous."
    show laura happy
    l "Oui..."
    r "Merci."
    show ryou normal
    r "Par contre, j'irais quand même au bar, j'ai soif..."
    show elusia happy sport
    e "D'où l'intérêt d'apporter une bouteille d'eau..."
    show laura normal
    l "Oui enfin autant finir la journée ensemble."
    show laura happy
    l "Je suis partante !"
    jump day7_pari
label day7_lolo:
    l "Mmmh... Elle tente de motiver Ryou..."
    m "Ah bon ?"
    l "Ryou est un flemmard qui ne bouge que quand il y a une récompense à la clef."
    menu:
        m "Ce pari..."
        "C'est une bonne idée...":
            # $ renpy.block_rollback()
            $ rel_lolo += 2
            mh "C'est une bonne idée..."
            l "Tu trouves ?"
        "Je ne veux pas être impliqué[ter].":
            # $ renpy.block_rollback()
            $ rel_lolo += 4
            ma "Je ne veux pas être impliqué[ter]."
            l "Bah... Moi non plus..."
            l "Mais ne t'en fais pas."
        "...":
            # $ renpy.block_rollback()
            m "..."
            l "Qu'y a t'il ?"
            l "Le pari te dérange, c'est ça ?"
    l "De toutes façons, je ne crois pas qu'Elusia te fasse payer."
    l "Je pense que ce sont juste des paroles en l'air."
    menu:
        "OK":
            # $ renpy.block_rollback()
            m "OK."
        "Ca me rassure.":
            # $ renpy.block_rollback()
            $ rel_lolo += 2
            m "Ca me rassure."
            show laura happy
            l "A ce point là ?"
            l "Tu vas pouvoir jouer l'esprit tranquille !"
        "Dommage.":
            # $ renpy.block_rollback()
            $ rel_lolo += 4
            m "Dommage."
            l "Tout à fait."
            l "Rien ne t'empêches de payer ma part si on perd !"
            mh "Tu pourrais faire exprès de perdre !"
            l "Mince !"
    l "Commençons la partie alors !"
    show ryou angry
    r "Mais qu'est-ce qu'ils font ?"
    show elusia geez sport
    e "Ils se glissent des mots doux !"
    show ryou sad
    r "Très marrant."
    r "Bon, sert leur dessus !"
    "Elusia sert sur Laura."
    l "Tu rêves !"
    "Laura renvoie la balle sur Ryouzanki."
    "Ce dernier attaque sur moi."
    "J'entends Laura crier \"J'ai !\""
    menu:
        "Laisser passer.":
            # $ renpy.block_rollback()
            $ rel_lolo += 4
            "Je laisse passer la balle."
            "J'entends une frappe derrière moi et la balle va rebondir dans un coin du camp adverse."
            "Laura vient de marquer le point."
            l "Bravo partenaire !"
            menu:
                "Bravo à toi !":
                    # $ renpy.block_rollback()
                    $ rel_lolo += 2
                    m "Bravo à toi !"
                    show laura sad
                    l "Non..."
                    l "C'est du travail d'équipe !"
                "Excellent travail d'équipe.":
                    # $ renpy.block_rollback()
                    $ rel_lolo += 4
                    m "Excellent travail d'équipe."
                    show laura happy
                    l "Exactement !"
                "J'ai rien fait...":
                    # $ renpy.block_rollback()
                    m "J'ai rien fait..."
                    show laura sad
                    l "Mais si..."
                    l "C'était du travail d'équipe !"
            show laura happy
            l "Une chose qu'en face, ils ne connaissent pas !"
            l "C'est pourquoi on devrait gagner !"
            l "Tu as eut confiance en moi."
        "Attaquer.":
            # $ renpy.block_rollback()
            $ rel_lolo -= 2
            "Je décide d'attaquer sur Ryouzanki."
            "Il me renvoie une balle molle."
            l "N'attaque surtout pas !"
            menu:
                "Rattaquer.":
                    # $ renpy.block_rollback()
                    $ rel_lolo -= 4
                    "Laura ne chercherait pas à prendre mon moment de gloire ?"
                    "Je rattaque."
                    "Grave erreur, c'était un effet très bien placé et je touche le filet."
                "Défendre.":
                    # $ renpy.block_rollback()
                    $ rel_lolo -= 2
                    "Je défends."
                    "C'était une bonne idée."
                    "La balle possédait un effet monstrueux."
                    "Elusia attaque sur moi et je n'ai pas la force de renvoyer la balle."
                "Laisser passer.":
                    # $ renpy.block_rollback()
                    "Je laisse passer la balle."
                    "Laura la frappe."
                    "Mais elle n'attaque pas."
                    "Elusia attaque en retour sur moi."
                    "Je n'ai pas le force de contrer ce coup et la balle passe."
            show ryou happy
            r "Héhéhé... Point pour nous !"
            e "Effectivement !"
            e "Il est où le travail d'équipe ?"
            show laura sad
            l "Très drôle..."
            l "[j]... Si tu ne me fais pas confiance, nous ne gagnerons pas."
    show laura normal
    l "J'ai l'habitude de jouer contre eux avec Alice alors je les connais comme ma poche."
    l "Normalement, avec Alice..."
    show laura sad
    l "..."
    menu:
        "Tu préfères jouer avec Alice ?":
            # $ renpy.block_rollback()
            $ rel_lolo += 4
            m "Tu préfères jouer avec Alice ?"
            show laura sad
            l "Pas vraiment non..."
            show laura happy
            l "En fait non."
            l "Elle est meilleure que toi mais c'est ennuyeux de jouer ave elle."
            menu:
                "Parce qu'elle est trop forte ?":
                    # $ renpy.block_rollback()
                    m "Parce qu'elle est trop forte ?"
                    show laura normal
                    l "Non, pas plus que ça..."
                    l "Juste qu'on ne se déteste pas mais..."
                    l "On ne se connait pas non plus."
                    l "Et nos centres d'intérêts sont trop distants."
                "Parce que c'est une geek ?":
                    # $ renpy.block_rollback()
                    $ rel_lolo += 4
                    m "Parce que c'est une geek ?"
                    l "... Ha ha !"
                    show laura normal
                    l "Peut être que c'est ça..."
                    l "En fait, c'est surtout parce qu'elle ne parle pas du tout."
                    l "Du coup, les parties muettes sont si ennuyantes..."
        "Quelque chose te tracasse ?":
            # $ renpy.block_rollback()
            m "Quelque chose te tracasse ?"
            show laura normal
            l "Non non..."
            l "Rien du tout."
    scene gymnaseout with fade
    call day7_normal
    "Malgré ma faiblesse, nous avons réussi à leur tenir tête grâce au travail d'équipe."
    "Laura a été très attentive et gentille avec moi."
    show elusia satisfied sport
    show ryou happy
    "Nous avons perdu de peu au tie-break."
    e "Je dois vous féliciter."
    e "Je ne m'attendais pas à une telle résistance de votre part !"
    r "Dommage..."
    show elusia normal sport
    e "Pour vous remercier de cette superbe partie, je lève le gage."
    l "Merci."
    r "Par contre, j'ai soif. On va quand même au bar ?"
    show elusia happt sport
    e "D'où l'intérêt d'apporter une bouteille d'eau..."
    l "Ca va ?"
    m "Oui."
    l "Fait pas cette tête, c'est pas grave !"
    show laura happy
    l "Tu as fait un coéquipier formidable !"
    l "Je suis vraiment contente d'avoir pu jouer avec toi."
    l "On les aura la prochaine fois !"
    jump day7_pari
label day7_ryou:
    show ryou angry
    r "Mec, me laisse pas tomber..."
    r "J'suis déjà assez fauché comme ça..."
    r "Je veux pas perdre."
    menu:
        "Mec, on va pas perdre...":
            # $ renpy.block_rollback()
            $rel_ryou +=2
            m "Mec, on va pas perdre..."
            show ryou sad
            r "Bien sur que si..."
        "Tant pis...":
            # $ renpy.block_rollback()
            m "Tant pis..."
            r "Nan mais sérieusement, ces deux filles m'extorquent des sous avec des paris à la con..."
    show ryou angry
    r "Et pourquoi tu t'es mis avec moi ?"
    r "On a juste aucune chance contre ces monstres !"
    menu:
        "Parce que je t'aime bien.":
            # $ renpy.block_rollback()
            $rel_ryou +=2
            m "Parce que je t'aime bien."
            show ryou sad
            r "Désolé, mais je préfère les femmes."
        "Parce qu'on est des hommes.":
            # $ renpy.block_rollback()
            $rel_ryou +=4
            m "Parce qu'on est des hommes."
            show ryou normal
            r "Ouais bah j'espère que t'assure !"
        "Non mais on va gagner !":
            # $ renpy.block_rollback()
            m "Non mais on va gagner !"
            r "T'as l'air vraiment sûr de toi..."
    call day7_normal
    e "Attention, j'arrive !"
    "La balle arrive si vite que ma raquette flanche et envoie la balle dans le décor."
    show elusia satisfied sport
    e "30 - 0"
    show ryou angry
    r "D'habitude avec Alice, on séparait les deux brutes."
    menu:
        "Arrête de gémir, t'es un homme.":
            # $ renpy.block_rollback()
            $rel_ryou -=2
            m "Arrête de gémir, t'es un homme."
            show ryou sad
            r "Vas te faire foutre..."
            r "Il faut trouver un autre moyen de gagner..."
        "T'as raison, trouvons un autre moyen de gagner.":
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
            $rel_ryou +=2
            "Je touche la balle mais la laisse partir dans le filet."
            e"Jeu !"
            e"Changement de serveur !"
        "Tenter de l'arrêter.":
            # $ renpy.block_rollback()
            $ stamina -=1
            $rel_ryou -=2
            "J'ai réussi à l'arrêter."
            "Laura contre et l'envoie sur Ryouzanki qui la laisse passer."
            e "Jeu !"
            e "Changement de serveur !"
            menu:
                "...":
                    # $ renpy.block_rollback()
                    pass
                "T'as fait exprès de rater ?":
                    # $ renpy.block_rollback()
                    $rel_ryou -=2
                    ma "T'as fait exprès de rater ?"
                    r "Bah ouais..."
                    menu:
                        "OK....":
                            # $ renpy.block_rollback()
                            m"OK...."
                        "Pour une fois qu'on renvoie une balle...":
                            # $ renpy.block_rollback()
                            $rel_ryou -=2
                            ma "Pour une fois qu'on renvoie une balle..."
                            show ryou angry
                            r "T'es stupide ou quoi ?"
                            r "40-0, c'est un peu tard pour remonter ce jeu."
    r "Il faut se débrouiller pour gagner le tiens et celui de Laura et c'est gagné."
    menu:
        "OK.":
            # $ renpy.block_rollback()
            $rel_ryou +=2
            m "OK."
        "Ce sera égalité.":
                # $ renpy.block_rollback()
                m "Ce sera égalité."
                r "Nan, je vais gagner le mien, t'en fais pas."
        "Et le tiens ?":
                # $ renpy.block_rollback()
                $rel_ryou -=2
                m "Et le tiens ?"
                r "Nan, je vais gagner le mien, t'en fais pas."
    show ryou normal
    r "Sert à fond sur Laura et économise des forces sur Elusia."
    r "Elusia la renverra de toutes façons."
    menu:
        "\"Quelqu'un qui ne se donne pas toujours à fond ne gagne pas...\"":
            # $ renpy.block_rollback()
            $rel_ryou -=2
            m "\"Quelqu'un qui ne se donne pas toujours à fond ne gagne pas...\""
            show ryou angry
            r "C'est ça..."
            r "En attendant si on se donnent tous à fond sans réfléchir..."
            r "On sera crevés bien avant elles."
            r "Et on perdra à coup sûr."
            r "Fait le..."
        "OK, ça marche.":
            # $ renpy.block_rollback()
            $rel_ryou +=2
            m "OK, ça marche."
            show ryou happy
            r "Je pense qu'on peut gagner."
    "Je dois servir sur Elusia."
    menu:
        "Servir avec un effet.":
            # $ renpy.block_rollback()
            $rel_ryou -=2
            "Je donne un effet maximal à mon service."
            "Elusia renvoie la balle avec grande aisance."
            "Comme s'il n'y avait jamais eut d'effet."
        "Servir avec force.":
            # $ renpy.block_rollback()
            $rel_ryou -=2
            $ stamina -= 1
            "Je frappe aussi fort que je peux."
            "Elusia renvoie la balle avec la même force."
            "Comme si elle n'était qu'un miroir."
        "Servir en économisant ses forces.":
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
            ma "C'est pas très cool ça..."
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
            # $ renpy.block_rollback()
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
                # $ renpy.block_rollback()
                $ rel_ryou -= 4
                ma "Il n'y a pas que gagner qui compte..."
                show ryou angry
                r "..."
            "Bah tant pis...":
                # $ renpy.block_rollback()
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
    ma "C'est pas un peu kamikaze ?"
    r  "Nan, t'en fais pas..."
    menu:
        "Je vais essayer.":
            # $ renpy.block_rollback()
            m "Je vais essayer."
            $ rel_ryou += 3
            "Nous tirons tous les deux au milieu."
            "Nous gagnons des points faciles car aucune ne bouge."
        "Non, c'est stupide.":
            # $ renpy.block_rollback()
            ma "Non, c'est stupide."
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
            # $ renpy.block_rollback()
            m "C'est pas la peine de vous disputer !"
            show ryou happy
            r "Après, tout, vous avez déjà perdu."
            m "C'était pas vraiment ce que je voulais dire..."
            menu:
                "En fait, si.":
                    # $ renpy.block_rollback()
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
                    # $ renpy.block_rollback()
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
                            # $ renpy.block_rollback()
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
                            # $ renpy.block_rollback()
                            m "Non, finissons."
                            r "Oui, chef !"
                            show elusia sad sport
                            e "Bon OK..."
                            $ rel_ryou += 3
                            jump day7_ryou5
                "Vous êtes toutes les deux en tort.":
                    # $ renpy.block_rollback()
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
               # $ renpy.block_rollback()
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
                # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
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
label day7_ryou_lose_end:
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
            # $ renpy.block_rollback()
            m "Je vais payer la mienne."
            $ rel_lulu += 3
            $ rel_lolo += 3
        "Il reste juste la mienne.":
            # $ renpy.block_rollback()
            m "Il reste juste la mienne."
    r "Heu... Oui..."
    r "On y va ? j'ai soif..."
    e "D'où l'intérêt d'apporter une bouteille d'eau..."
label day7_pari:
    
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
