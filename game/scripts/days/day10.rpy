# choix6 va de 0 à 3
# dans j10, P propose a E de sécher ses cours et de lui envoyer les poly
# a cause du divorce de ses parents, si E a besoin de calme.
# E refuse car elle a besoin de penser a autre chose.
# P est gentil avec E pas parce qu'il l'aime mais pârce qu'il veut bien se 
# faire voir de sa soeur
label day10:
    scene reveil with fade
    play sound "sound/clock.mp3"
    ma "C'est aujourd'hui qu'on nous rend le premier contrôle..."
    stop sound
    play music (joueur1) fadein 2
    play sound "sound/bell.mp3"
    play sound "sound/dooropen.mp3"
    scene couloir
    show ryou sad:
        left
    show elusia normal:
        right
    with fade
    r "Yo !"
    e "Salutations !"
    scene street
    show ryou sad:
        left
    show elusia normal:
        right
    with fade
    pause(1)
    play music (matin1) fadein 2
    scene classroom with fade
    $ pnjj = 'Professeur'
    pnj "Je vous rends les contrôles par ordre croissant des notes."
    if choix6 == 0:
        "Le professeur se tourne vers moi..."
        "Il me tend ma copie. Je suis donc dernier[ter] de la promotion..."
        "Quelle honte..."
        "Elusia ne me regarde pas et Ryouzanki roule des yeux."
        "Laura hausse les épaules et Valeth est ailleurs."
        "Je me fait tout[ter] petit[ter] et ne fais plus attention aux notes des autres."
    elif choix6 == 1:
        "Le professeur distribue quelques copies puis se tourne vers moi."
        "Il me tend ma copie."
        "Elusia fait la moue et Ryouzanki sourit en secouant la tête."
        "Laura hausse les épaules et Valeth est ailleurs."
        "Je me fait tout[ter] petit[ter] et ne fais plus attention aux notes des autres."
    elif choix6 == 2:
        "Le professeur a distribué plus de la moitié des copies."
        "Valeth a déjà reçu la sienne et n'y prête aucune attention."
        "Puis le professeur continue."
        "Il donne la sienne à Ryouzanki qui tapote son front contre sa table."
        "Puis vient la mienne."
        "Un score respectable."
        "Elusia et Laura me regardent en souriant."
        "Ryouzanki ne bouge plus, la tête sur la table."
        "Valeth est toujours ailleurs."
        "Laura obtient sa copie peu après, suivie d'Elusia."
        "Lloyd a la meilleure note de la classe."
        "J'ai cru comprendre que ça n'étonnait personne."
    elif choix6 == 3:
        "Le professeur a distribué plus de la moitié des copies."
        "Valeth a déjà reçu la sienne et n'y prête aucune attention."
        "Puis le professeur continue."
        "Il donne la sienne à Ryouzanki qui tapote son front contre sa table."
        "Arrive le tour de Laura qui semble plutôt satisfaite et se relit."
        "Puis mon propre tour."
        "Suivi juste après d'Elusia."
        "Laura me regarde avec un pouce levé tandis qu'Elusia relit sa copie avec un grand sourire."
        "Ryouzanki et Valeth sont ailleurs."
        "Lloyd a la meilleure note de la classe."
        "J'ai cru comprendre que ça n'étonnait personne."
    else :
        "ERROR"
    "A chaque travail sa récompense je suppose."
    "Allons manger !"
    scene parc
    show elusia geez at left
    show ryou happy
    show laura normal at right 
    with fade
    r "J'ai plus de la moyenne c'est déjà ça !"
    e "Misère, tu manques d'ambition, mon pauvre..."
    show ryou surprised
    r "Nan, avoir la moyenne c'est suffisant."
    menu:
        "Je pense que...":
            # $ renpy.block_rollback()
            $ rel_lolo += 3
            menu:
                m "Je pense que..."
                "Avoir la moyenne, c'est suffisant.":
                    # $ renpy.block_rollback()
                    $ rel_ryou += 3
                    mh "Avoir la moyenne, c'est suffisant."
                    m "Ce qui compte, c'est d'avoir son diplôme après tout."
                    m "Le classement n'est pas écrit dessus."
                    e "Misère..."
                    e "Principe de la démocratie, je me tais..."
                "Être dans les premiers, c'est mieux.":
                    # $ renpy.block_rollback()
                    $ rel_lulu += 3
                    mh "Être dans les premiers, c'est mieux."
                    show ryou sad
                    r "Ca sert à rien..."
                    r "Ton futur employeur ne va pas forcément éplucher tes bulletins de note..."
                    show elusia normal
                    e "Et s'il le fait ?"
                    show ryou normal
                    r "Lol."
                    show ryou happy
                    r "Il verra que mes notes sont pile ce qu'il faut et se doutera de ma puissancecachée !"
                    show elusia geez
                    e "C'est ça..."
        "...":
            # $ renpy.block_rollback()
            pass
    show elusia surprised
    e "D'ailleurs, où est Valou ?"
    l "Je crois qu'il avait un conseil de guerre avec ses sous-respo."
    show elusia sad
    e "Oh, encore ce problème de pénurie de membre..."
    show ryou sad
    r "Il faudrait vraiment faire quelque chose..."
    l "Bon, il faudrait retourner en cours."
    show elusia geez
    e "J'aime pas la physique..."
    show ryou happy
    r "T'aime pas la physique ou Laroi ?"
    show laura happy
    l "L'un n'excluant pas l'autre !"
    play music (prof1) fadein 2
    scene classroom with fade
    p "Et donc, la réponse n'est pas aussi simple que ça."
    p "Sinon, je ne serais pas payé une fortune pour trainer avec des moldus de la physique comme vous."
    p "..."
    p "Mademoiselle Hrist et sa suite, je veux vous voir après le cours."
    p "Chacun votre tour en privé."
    "Je crois que j'étais inclus[ter]..."
    "Cette soudaine demande fait l'office de tous les chuchots..."
    scene classroom
    show ryou normal at left
    with fade
    "Ryouzanki, entré en premier en est ressortit en souriant."
    "Il s'est fait sermonné par Laroijesea à cause des plaintes des autres profs."
    "Lorsqu'il ne connait pas la réponse, Ryouzanki marque des âneries."
    "Elusia, entrée en second vient de ressortir."
    show elusia sad at right with easeinright
    r "Alors ?"
    e "Hum... Affaire personnelle."
    show ryou surprised
    r "Vraiment ?"
    r "Aller, crache le morceau !"
    r "Il t'a fait des avances ?"
    show elusia embarassed
    e "Pas... Pas du tout !!"
    e "Arrête de raconter n'importe quoi !"
    show elusia shy
    e "Je vois mal quelqu'un comme lui tomber amoureux de qui que ce soit..."
    r "Raconte !"
    show elusia timid
    e "Mais nan !"
    menu:
        "Insister.":
            # $ renpy.block_rollback()
            $ rel_ryou += 4
            $ rel_lulu -= 2
            mh "Aller, raconte nous !"
            show elusia angry
            e "Mais nan ! Tu vas pas t'y mettre toi aussi !"
            e "Je ne veux vraiment pas en parler !"
            show ryou sad
            r "OK, comme tu voudra..."
        "Ne pas agir.":
            # $ renpy.block_rollback()
            $ rel_ryou -= 2
            "Il y eut un petit silence."
            show elusia geez
            e "[j], à ton tour..."
        "Défendre Elusia.":
            # $ renpy.block_rollback()
            $ rel_lulu += 4
            m "Si elle ne veut pas nous le dire, c'est pas si grave."
            show elusia geez
            show ryou normal
            r "OK. Désolé..."
    m "Bon et bien, j'y vais..."
    scene classroom
    show prof annoyed
    with fade
    m "Vous m'avez demandé ?"
    show prof normal
    p "Oui..."
    show prof happy
    p "Je voulais vous poser une petite question."
    p "Puis-je ?"
    "J'ai pas envie !"
    m "Bien sur."
    stop music fadeout 3.0
    p "Vous êtes dans une gare..."
    p "Un train arrive à toute vitesse sur une voie où il y a 5 personnes."
    p "Vous avez devant vous un levier qui déviera le train."
    p "La voie sur laquelle il sera dévié est traversée par une unique personne."
    p "Que choisissez-vous de faire ?"
label day10q:
    menu:
        m "Je..."
        "Je désire ne pas répondre.":
            # $ renpy.block_rollback()
            ma "Je désire ne pas répondre."
            show prof annoyed
            p "Oh mais vous ne partirez pas d'ici sans !"
            p "Je vis seul, j'ai tout mon temps !"
            jump day10q
        "J'enclenche le levier...":
            # $ renpy.block_rollback()
            m "J'enclenche le levier."
            m "Il faut parfois sacrifier une vie pour en sauver plus."
            m "Objectivement parlant, j'en sacrifie une pour en sauver cinq."
            m "C'est la même réponse qu'à votre question d'avant-hier."
            show prof dark with dissolve
            play music (prof2) fadein 2
            p "Hahaha !"
            p "Intéressant... Très intéressant !!"
            show prof happy with dissolve
            p "C'est ce que disent tous les héros naïfs !"
            show prof naughty
            p "Mais pourriez vous ensuite réellement encaisser les plaintes de la famille du défunt ?"
            p "\"Objectivement parlant\", c'est vous qui l'avez tué !"
            p "Vous aurez sa mort sur la conscience !"
            show prof annoyed
            p "Voyez vous, j'aime les héros naïfs."
            p "Lorsqu'ils sont confrontés à la réalité, ils deviennent imprévisibles."
            p "Offrez moi donc du spectacle !"
            menu:
                "Ce n'est pas naïf mais réaliste !":
                    # $ renpy.block_rollback()
                    ma "Ce n'est pas naïf mais réaliste !"
                    show prof happy
                    p "C'est la raison pour laquelle les scientifques ne dirigent pas notre pays."
                    p "Parce que les humains, nos victimes ici, ne sont pas que des variables chiffrées."
                    p "Parce que les humains, vous ici, n'êtes pas un algorithme sans coeur."
                    p "Le jour où ça arrivera, je vous souhaite de faire un choix que vous ne regretterez pas."
                "C'est le meilleur choix possible !":
                    # $ renpy.block_rollback()
                    ma "C'est le meilleur choix possible !"
                    p "Meilleur ?"
                    p "C'est très subjectif ça."
                    p "Si vous considérez que c'est le meilleur choix, alors je vous souhaite bien du courage."
                    show prof naughty
                    p "Le courage de faire face à vos actes devant une famille éplorée."
        "Je n'enclenche pas le levier...":
            # $ renpy.block_rollback()
            m "Je n'enclenche pas le levier..."
            m "Je refuse d'être responsable de la mort d'une personne."
            play music (prof2) fadein 2
            show prof dark with dissolve
            p "Vraiment ?"
            p "Le problème peut se résumer à la question suivante :"
            p "\"Suis-je prêt à tuer une personne pour en sauver 5 ?\""
            show prof annoyed with dissolve
            p "Avant-hier, vous m'aviez répondu que c'était évident."
            p "Que vous étiez prêt à tuer une personne pour en sauver 5."
            show prof naughty
            p "Voilà que vous revenez sur votre parole !"
            m "Les conditions ne sont pas les mêmes !"
            show prof happy
            p "En quoi sont-elles différentes ?"
            menu:
                ma "Je n'avais pas le choix avant-hier !"
                "Je ne veux tuer personne !":
                    # $ renpy.block_rollback()
                    ma "Je ne veux tuer personne !"
                    ma "Avant-hier, je devais obligatoirement tuer des gens !"
                    ma "Alors autant en tuer le moins possible !"
                    show prof dark with dissolve
                    p "Hahaha !"
                    p "De plus en plus intéressant."
                    p "Dans ce cas, vous soutenez que..."
                    show prof naughty with dissolve
                    p "Tant que ce n'est pas vous qui les tuez, la mort des gens vous importe peu ?"
                    p "Quel choix égoiste..."
                    p "Après tout, c'est dans la nature humaine que de se protéger soi d'abord..."
                "Je ne veux pas de problème !":
                    # $ renpy.block_rollback()
                    ma "Je ne veux pas de problème !"
                    ma "Avant-hier, j'allais déjà tuer des gens alors autant faire le moins de mort possible."
                    ma "Là, je vais avoir des problèmes parce que je suis totalement responsable de la mort d'une personne."
                    show prof normal
                    p "Hum..."
                    p "C'est de loin la réponse la plus honnête que j'ai pu entendre."
                    show prof annoyed
                    p "Dîtes moi... Êtes-vous toujours honnête comme ça ?"
                    m "Oui."
                    show prof happy
                    p "J'espère que ça ne vous attirera pas trop d'ennuis."
                    p "Les gens comme vous sont si rares..."
    show prof happy    
    p "Aller, vous pouvez disposer."
    scene classroom
    show ryou normal at left
    show elusia sad at right
    with fade
    e "Alors ?"
    m "Et bien..."
    menu:
        m "Il m'a posé des questions..."
        "Assez bizarres...":
            # $ renpy.block_rollback()
            extend "Assez bizarres..."
        "Scolaires, rien d'intéressants.":
            # $ renpy.block_rollback()
            extend "Scolaires, rien d'intéressants."
         
label day10_fin:
    play music (joueur1) fadein 2
    scene couloir with fade
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    "9 eme jour fini."
    scene chambre m with fade
    play sound "sound/doorclose.mp3"
    "Je vais dormir tôt."
    stop music
    return
