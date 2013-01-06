# TODO 
label labo:
    
    play music (club1) fadein 2
    scene labo with fade
    
    if aller_science == 0:
        jump science_0
    elif aller_science == 1 and ali =='Alice':
        jump science_02
    elif aller_science ==1:
        jump science_1
    elif aller_science == 2:
        jump science_2
    elif aller_science < 7:
        jump science_3
    elif aller_science == 7:
        jump science_4
    else:
        "Pas encore disponible"
        return
        
label science_0:
    $ aller_science += 1
    show lloyd normal
    m "Bonjour !"
    show lloyd angry
    m "Heu..."
    $ choix_1 = True
    $ choix_2 = True
    
label lloyd_menu_1:
    
    menu:
        "Ici, c'est...?"if choix_1 :
            $ renpy.block_rollback()
            $ choix_1 = False
            m "Ici, c'est...?"
            y "Le club des sciences."
            y "Informatique et robotique."
            y "Mais je n'en fais pas partie."
            y "Que désires tu ?"
            menu:
                "Non, je demandais juste..."if choix_2 == False:
                    $ renpy.block_rollback()
                    m "Non, je demandais juste..."
                    y "Je vois."
                    jump lloyd_menu_1
                "Moi ? Rien de spécial."if choix_2:
                    $ renpy.block_rollback()
                    m "Moi ? Rien de spécial."
                    show lloyd angry
                    m "Je ne faisais que passer."
                    y "Alors passe."
                    ma "Je vois qu'on ne veut pas de moi ici..."
                    "Est-ce possible d'être aussi désagréable ?"
                    "Maintenant je sais que oui."
                    return
                "Je peux m'inscrire ?":
                    $ renpy.block_rollback()
                    m "Je peux m'inscrire ?"
                    show lloyd angry
                    y "Je viens de te dire que je ne fais pas partie du club !"
                    y "La responsable de ce club s'est absentée."
                    y "Et je dois la remplacer pendant ce temps."
                    y "Quel manque de responsabilité n'est-ce pas ?"
                    menu:
                        "Effectivement.":
                            $ renpy.block_rollback()
                            m "Effectivement."
                            show lloyd happy
                            y "Ha !"
                            y "Enfin quelqu'un qui me comprend !"
                            show lloyd normal
                            y "Les gens qui obtiennent des responsabilités devraient les assumer !"
                            show lloyd angry
                            y "C'est totalement inacceptable de refuser une inscription."
                            y "Sous un prétexte aussi ridicule..."
                            $ rel_lloy += 5                            
                        "Elle a peut être des choses importantes à faire.":
                            $ renpy.block_rollback()
                            m "Elle a peut être des choses importantes à faire."
                            y "Dans ce cas, il ne fallait pas prendre ce poste."
                            m "Ah..."
                            m "Un imprévu, ça arrive des fois..."
                            y "Cela ne devrait pas se produire."
                            m "Elle t'a nommé remplaçant..."
                            $ rel_lloy += 2
                            show lloyd happy
                            y "Non ! Je suis venu de mon propre chef."
                            y "J'assume mes responsabilités de vice président du conseil des élèves !"
                            show lloyd angry
                            y "Moi, au moins..."
                        "Honnêtement, on s'en fiche.":
                            $ renpy.block_rollback()
                            m "Honnêtement, on s'en fiche."
                            y "Non, c'est important !"
                            y "S'il y a de la casse, qui va assumer les conséquences ?"
                            y "C'est elle. Alors qu'elle n'y pouvait rien !"
                            m "Oui."
                    jump lloyd_menu_1
        "Je suis [j]. Et toi ?"if choix_2 :
            $ renpy.block_rollback()
            $ choix_2 = False
            m "Je suis [j]. Et toi ?"
            y "Classe ?"
            menu:
                "J'ai posé une question avant toi...":
                    $ renpy.block_rollback()
                    ma "J'ai posé une question avant toi..."
                    show lloyd happy
                    y "C'est vrai !"
                    show lloyd normal
                    y "Excuse moi, je suis un peu sur les nerfs."
                    y "Je suis Lloyd Baptiste Reeds de Bellato."
                    $ noble = 'Lloyd'
                    y "Mais c'est un peu long alors appelles moi Lloyd."
                    y "Et tu es en quelle classe [j] ?"
                    m "Télécoms-Réseaux !"
                    show lloyd happy
                    y "Oh milles pardons, je ne t'avais pas reconnu[ter] !"
                    y "Nous sommes donc dans la même promotion !"
                    show lloyd normal
                    m "C'est pas grave, je viens d'arriver."
                    $ rel_lloy += 5
                "Je suis en Télécoms-Réseaux.":
                    $ renpy.block_rollback()
                    m "Je suis en Télécoms-Réseaux."
                    show lloyd normal
                    y  "Oh pardon, je ne t'avais pas reconnu[ter]."
                    y "Nous sommes donc dans la même promotion."
                    m "C'est pas grave, je viens d'arriver."
                    y "Je suis Lloyd Baptiste Reeds de Bellato"
                    $ noble = 'Lloyd'
                    y "Mais c'est un peu long alors appelles moi Lloyd."
                    $ rel_lloy += 2
            jump lloyd_menu_1
        "Au revoir !":
            $ renpy.block_rollback()
            m "Au revoir !"
            if choix_2 == False:
                y "Au revoir [j]."
                y "Et à demain."
            else:
                y "Au revoir."
            if choix_1 == False:
                y "Ah, et... Reviens demain si tu veux t'inscrire."
                mh "D'accord, merci !"

            "J'ai réussi à retouver le chemin de mon studio."
            return
            
label science_1:
    show alice normal
    a "Salut [j]."
    a "L'aristo m'a dit que tu voulais t'inscrire."
    show alice sad
    a "Il m'a encore sermonée pour soi-disant manquement à mes obligations."
    show alice normal
    if ali != 'Alice':
        a "Oh, je suis tête en l'air..."
        a "Je suis Alice, la présidente de tous les clubs scientifiques de cette école."
        $ noble = 'Lloyd'
        $ ali = 'Alice'
    a "Ici, si tu t'inscris, tu pourra participer à divers projets dans les clubs d'informatique, de robotique et de chimie."
    a "C'est amusant en plus d'être instructif."
    a "Par contre, tu devra venir régulièrement si tu participes à des projets."
    a "On ne compte pas les absences mais c'est par respect pour les gens qui participent à ton projet."
    a "J'ai un peu trop parlé."
    show alice sad
    a "Mais... heu... ne t'inquiète pas, je ne parle pas beaucoup d'habitude."
    menu:
        m "Mais tu sais..."
        "Je préfère parler peu mais bien.":
            $ renpy.block_rollback()
            m "Je préfère parler peu mais bien."
            a "Vraiment... Tant mieux alors..."
            a "Le sage parle parce qu'il a quelque chose à dire."
            a "Et le fou parle parce qu'il veut dire quelque chose..."
            a "Je suppose..."
            $ rel_ali +=5
        "Comme tous les geeks.":
            $ renpy.block_rollback()
            m "Comme tous les geeks."
            show alice geez
            a "Pfff... Encore un[ter] imbécile ancré[ter] dans les stéréotypes."
            a "Je ne suis pas la présidente parce que je suis la plus compétente."
            a "Je le suis parce que je suis douée en communication, coordination."
            a "Du moins... Parmis les membres du club.."
            show alice sad
            a "Ce n'est qu'un titre honorifique."
        "Je n'ai rien dit !":
            $ renpy.block_rollback()
            $ rel_ali +=2
            mh "Je n'ai rien dit !"
            a "Ne pas dire des choses ne signifie pas ne pas les penser."
            mh "Je n'ai rien penser non plus..."
            a "Ne rien penser, c'est ne pas exister."
            
label science_02:
    if science_var == 0:
        show alice geez
        a "Désolée mais je vais être directe !"
        show alice sad
        a "Je suis plutot pressée..."
        $ science_var += 1
    elif science_var == 1:
        show alice sad
        a "Je vais te le demander une seconde fois."
        $ science_var += 1
        show alice geez
    elif science_var == 2:
        show alice geez
        a "Je vais te le demander une dernière fois."
    a "Es tu venu[ter] t'inscrire oui ou non ?"
    menu :
        m "Je crois bien que..."
        "J'ai bien réfléchit, je ne veux pas m'inscrire.":
            $ renpy.block_rollback()
            m "J'ai bien réfléchit, je ne veux pas m'inscrire."
            show alice normal
            a "Donc non."
            a "Et ce secteur est réservé aux membres des clubs."
            a "Je ne veux pas prendre la responsabilité s'il t'arrive malheur."
            a "Un jet d'acide, une fusée ou un boulon, ça vole vite."
            a "Tu peux sortir, s'il te plaît ?"
            "Je ne sais vraiment pas s'il s'agit de méchanceté ou de responsabilité là..."
            hide alice
            "Quoiqu'il en soit, je suis sorti[ter] et rentré[ter] chez moi."
            return
        "Je vais encore y réfléchir.":
            $ renpy.block_rollback()
            m "Je vais encore y réfléchir."
            show alice normal
            a "Ma question est binaire."
            a "Elle ne comportait que 2 réponses possibles."
            a "Oui, ou non."
            a "Je réitère donc ma question. Oui ou non ?"
            menu:
                "Oui.":
                    $ renpy.block_rollback()
                    m "Oui."
                    a "Et bah voilà."
                    a "La prochaine fois, clarifie donc tes objectifs avant d'agir."
                    jump arrive_lloyd
                "Non.":
                    $ renpy.block_rollback()
                    m "Non."
                    a "Et bah voilà."
                    a "La prochaine fois, clarifie donc tes objectifs avant d'agir."
                    a "Et ce secteur est réservé aux membres des clubs."
                    a "Je ne veux pas prendre la responsabilité s'il t'arrive malheur."
                    a "Un jet d'acide, une fusée ou un boulon, ça vole vite."
                    a "Tu peux sortir, s'il te plaît ?"
                    "Je ne sais vraiment pas s'il s'agit de méchanceté ou de responsabilité là..."
                    "Quoiqu'il en soit, je suis sorti[ter] et rentré[ter] chez moi."
                    return
        "Oui, je veux venir.":
            $ renpy.block_rollback()
            $ rel_ali += 3
            $ aller_science += 1
            m "Oui, je veux venir."
            show alice happy
            a "Bienvenu[ter] parmis nous !"
            
label arrive_lloyd:
    
            show alice geez at left with move
            a "Que faîtes vous ici Sir Lloyd ?"
            show lloyd normal at right with easeinright
            if bite:
                y "Je suis venu vérifier que l'inscription de mon camarade de classe se déroule correctement."
            else:
                y "Je suis venu vérifier que l'inscription de ma camarade de classe se déroule correctement."
            a "Et tout est bon pour vous, Sir ?"
            y "Oui. Vous devriez prendre votre rôle plus à coeur."
            show alice sad
            a "J'y réfléchirais. Allez donc me chercher les feuilles d'inscription."
            show lloyd angry
            y "Comment ? Vous ne les avez pas ?"
            y "J'estime vous avoir prévenu suffisement à l'avance."
            show alice geez
            a "Vous savez comme je suis, Sir, toujous aussi négligeante..."
            a "Une simple roturière..."
            y "Très bien. Je reviens de suite."
            hide lloyd with easeoutright
            show alice sad at center with move
            a "L'aristo a encore brisé un moment d'émotion."
            menu:
                "N'exagérons rien.":
                    $ renpy.block_rollback()
                    m "N'exagérons rien."
                    a "Oui..."
                "(Rire)":
                    $ renpy.block_rollback()
                    $ rel_ali += 3
                    mh "Haha..."
                    show alice satisfied
                    a "Ce sera la même chose à chacune de ses apparitions."
                    a "A chaque réaction son produit."
                "Oui, c'est vrai.":
                    $ renpy.block_rollback()
                    $ rel_ali +=1
                    m "Oui, c'est vrai."
                    show alice sad
                    a "Je plaisantais hein..."
                    a "Je me réjouirais réellement lorsque tu participera activement à un projet."
                    a "Sur tous nos membres, 3/4 sont des fictifs."
            show alice normal
            a "En attendant son retour, je vais t'expliquer quelques trucs."
            a "Les clubs de sciences sont 3 avec chacun leur architecture propre."
            a "Leur propre président, leur propre secrétaire et leur propre trésorier."
            a "Je suis la coordinatrice, c'est à dire que je gère les projets en commun."
            a "Il m'arrive aussi de mettre main à la pâte dans un des projets s'il m'intéresse."
            a "Un club en particulier t'intéresse ?"
            m "Vous avez quoi déjà ?"
            a "Chimie, robotique ou informatique."
            menu:
                m "Je vais prendre..."
                "Chimie.":
                    $ renpy.block_rollback()
                    m "Chimie."
                    $ club = 'chimie'
                "Robotique.":
                    $ renpy.block_rollback()
                    m "Robotique."
                    $ club = 'robot'
                "Informatique.":
                    $ renpy.block_rollback()
                    m "Informatique."
                    $ club = 'info'
                    
            show alice happy
            a "Club [club] donc..."
            mh "Oui, c'est ça."
            show alice sad at left with move
            e "Hello ! Je suis en retard ?"
            show elusia normal with easeinright
            a "Bonjour Lulu."
            e "Alice, tu vas bien ?"
            show lloyd angry at right with easeinright
            show alice geez
            y "Voilà les papiers."
            show lloyd happy
            y "Oh ! Bonjour Elusia !"
            a "Lulu, tu n'as pas le droit d'être ici."
            show alice sad
            a "N'est ce pas Sir vice président ?"
            a "Bien qu'elle ait tant envie de rester ici..."
            show lloyd angry
            y "Heu... Oui... hum..."
            y "Elusia, tu n'as pas le droit de rester ici. Sortons tous les deux."
            hide lloyd with easeoutright
            e "A plus tard !"
            hide elusia with easeoutright
            show alice sad at center with move
            a "Action, réaction..."
            show alice geez
            a "Désolée, je n'aime pas quand le labo est bondé, ça me stress..."
            a "Tâche de remplir tout ça aussi tôt que possible."
            show alice sad
            a "J'ai à faire. A demain."
            hide alice
            "Je rentre chez moi avec les papiers administratifs."
            return

label science_2:
    show alice sad
    $ aller_science += 1 # on passe a 3
    a "Oh, te voilà [j]."
    a "Votre attention tout le monde !"
    a "Je vous présente [j] qui s'est joint[ter] à nous hier."
    a "Désormais, [sexe] travaillera avec nous dans la team [club]."
    "Ils sont tous souriants et me souhaitent la bienvenu[ter]."
    a "Mais... On n'a plus vraiment le temps de former des gens, si ?"
    show alice geez
    a "Non, effectivement, question stupide."
    show alice sad
    a "Donc, [j], voici Isaac, le président du club [club]."
    a "File lui la doc, [sexe] se débrouillera... Je suppose."
    "Isaac me donne des polycopiés."
    a "C'est un rapport de ce qui a été fait depuis le début de l'année."
    a "Il faut que tu en prennes conscience avant."
    a "Le plus tôt sera le mieux."
    a "Je te laisse lire, si tu as des questions, Isaac est là."
    a "A plus tard."
    hide alice
    "C'est un rapport sur les activités du club [club]."
    "Toutes les activités recensées dans ce cahier sont centrées autour du Grand Gala."
    "Le festival de l'école est donc très attendu."
    "Le club qui aura l'animation la plus intéressante recevra des subventions supplémentaires."
    "Les 3 clubs scientifiques se sont alliés."
    if club == 'chimie':
        "Le club où je suis s'est engagé à produire des effets spéciaux tels que des nuages de fumée colorée."
        "Il produit du parfum et des colorants."
        "Et enfin, il s'occupe des feux d'artifices."
    elif club == 'robot':
        "Le club où je suis s'est engagé s'occuper de la logistique d'un feu d'artifice."
        "Il étudie les emplacements possibles pour les poster ainsi que comment les lancer."
        "Enfin, il bricole des piédestaux pour poser les fusées et des raccordements."
    elif club == 'info':
        "Le club où je suis s'est engagé s'occuper de la logistique d'un feu d'artifice."
        "Il étudie les timings pour les lancer en synchronisant avec une musique."
        "Enfin, il s'occupe du programme de lancement quoi."
    m "Excuse moi Isaac, le club chimie produit les feux d'artifices ?"
    "Isaac secoue la tête et tapote son index sur la page suivante."
    $ pnjj = "Isaac"
    pnj "C'est juste à la page suivante, juste là !"
    m "Ah, excuse moi."
    pnj "T'en fais pas va, je suis un peu là pour ça..."
    "La fabrication des feux d'artifices est interdite dans notre pays."
    "Leur utilisation est réglementée."
    "Pour un feu d'artifice contenant uniquement des produits de catégorie C1, C2, C3, T1, K1, K2 et K3 et dont la quantité de matière active est inférieure à 35 kg..."
    "... Il faut juste une autorisation écrite de la mairie."
    "Pour un feu d'artifice contenant au moins un produit de catégorie C4, T2 ou plus de 35 kg de matière active..."
    "... Une déclaration au moins un mois avant à la mairie et à la préfecture du département est nécessaire."
    "Tout est minutieusement noté sur ce carnet."
    "Les rôles de chaque membre, les lois, l'inventaire..."
    "J'ai lu 20\%"
    show alice normal
    a "Bon, il se fait tard. On a bien travaillé aujourd'hui."
    show alice sad
    a "Heu, [j], j'ai oublié de te dire que le rapport ne dois pas quitter les locaux."
    a "Donc tu vas devoir venir à chaque fois pour le lire, désolée."
    m "D'accord."
    a "Tu n'as pas lu grand chose on dirait..."
    menu:
        "Je fais ce que je peux hein !":
            $ renpy.block_rollback()
            m "Je fais ce que je peux hein !"
            show alice normal
            a "Je plaisantais."
            $ rel_ali += 2
        "Je fais ce que je veux hein !":
            $ renpy.block_rollback()
            ma "Je fais ce que je veux hein !"
            show alice geez
            a "Mais non, mais non..."
            a "Fallait pas le prendre comme ça..."
            a "Je plaisantais."
        "Désolé[ter]":
            $ renpy.block_rollback()
            m "Désolé[ter]."
            show alice geez
            a "Mais non, mais non..."
            a "Fallait pas le prendre comme ça..."
            a "Je plaisantais."
            $ rel_ali += 5
    show alice sad
    a "Tu es là depuis peu et je te rentre déjà dans un club..."
    a "Je ne peux pas te demander la lune non plus... Je suppose."
    a "Tu sais, je me sens assez coupable de t'avoir forcé la main..."
    menu:
        "Oui tu peux...":
            $ renpy.block_rollback()
            m "Oui, tu peux..."
            show alice geez
            a "Désolée... Je suis sous pression..."
        "Non, ne t'en fais pas...":
            $ renpy.block_rollback()
            $  rel_ali += 3
            m "Non ne t'en fais pas..."
            show alice sad
            a "Oui... J'espère sincèrement que tu ne regrettera pas d'être parmi nous."
        "Je voulais venir de toutes façons.":
            $ renpy.block_rollback()
            $  rel_ali += 5
            mh "Je voulais venir de toutes façons."
            show alice geez
            a "Quel soulagement..."
            show alice sad
            a "J'ai moins l'impression d'être tyrannique."
    a "J'ai très peur de ne pas finir à temps..."
    m "Oui, je comprends."
    a "A très bientôt j'espère !"
    m "Je tâcherais de revenir."
    a "D'accord merci."
    return
label science_3:
    
label science_4:
