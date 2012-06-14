label labo:
    
    $ renpy.music.play("music/club.ogg", fadein=2)
    scene labo with dissolve
    
    if aller_science == 0:
        jump science_0
    elif aller_science == 1 and ali =='Alice':
        jump science_02
    elif aller_science ==1:
        jump science_1
        
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
        "Ici, c'est...?" if choix_1 :
            $ choix_1 = False
            m "Ici, c'est...?"
            y "Le club des sciences."
            y "Informatique et robotique."
            y "Mais je n'en fais pas partie."
            y "Que désires tu ?"
            menu:
                "Non, je demandais juste..."if choix_2 == False:
                    m "Non, je demandais juste..."
                    y "Je vois."
                    jump lloyd_menu_1
                "Moi ? Rien de spécial." if choix_2:
                    m "Moi ? Rien de spécial."
                    show lloyd angry
                    m "Je ne faisais que passer."
                    y "Alors passe."
                    m "Je vois qu'on ne veut pas de moi ici..."
                    "Est-ce possible d'être aussi désagréable ?"
                    "Maintenant je sais que oui."
                    return
                "Je peux m'inscrire ?":
                    m "Je peux m'inscrire ?"
                    show lloyd angry
                    y "Je viens de te dire que je ne fais pas partie du club !"
                    y "La responsable de ce club s'est absentée."
                    y "Et je dois la remplacer pendant ce temps."
                    y "Quel manque de responsabilité n'est-ce pas ?"
                    menu:
                        "Effectivement.":
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
                            m "Honnêtement, on s'en fiche."
                            y "Non, c'est important !"
                            y "S'il y a de la casse, qui va assumer les conséquences ?"
                            y "C'est elle. Alors qu'elle n'y pouvait rien !"
                            m "Oui."
                    jump lloyd_menu_1
        "Je suis [j]. Et toi ?" if choix_2 :
            $ choix_2 = False
            m "Je suis [j]. Et toi ?"
            y "Classe ?"
            menu:
                "J'ai posé une question avant toi...":
                    m "J'ai posé une question avant toi..."
                    show lloyd happy
                    y "C'est vrai !"
                    show lloyd normal
                    y "Excuse moi, je suis un peu sur les nerfs."
                    y "Je suis Lloyd Baptiste Reeds de Bellato"
                    $ noble = 'Lloyd'
                    y "Mais c'est un peu long alors appelles moi Lloyd."
                    y "Et tu es en quelle classe [j] ?"
                    m "GTR !"
                    show lloyd happy
                    y "Oh milles pardons, je ne t'avais pas reconnu[ter] !"
                    y "Nous sommes donc dans la même promotion !"
                    show lloyd normal
                    m "C'est pas grave, je viens d'arriver."
                    $ rel_lloy += 5
                "Je suis en GTR.":
                    m "Je suis en GTR."
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
            m "Au revoir !"
            if choix_2 == False:
                y "Au revoir [j]."
                y "Et à demain."
            else:
                y "Au revoir."
            if choix_1 == False:
                y "Ah, et... Reviens demain si tu veux t'inscrire."
                m "D'accord, merci !"
        
            hide lloyd
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
            m "Je préfère parler peu mais bien."
            a "Vraiment... Tant mieux alors..."
            a "Le sage parle parce qu'il a quelque chose à dire."
            a "Et le fou parle parce qu'il veut dire quelque chose..."
            a "Je suppose..."
            $ rel_ali +=5
        "Comme tous les geeks.":
            m "Comme tous les geeks."
            show alice geez
            a "Pfff... Encore un imbécile ancré dans les stéréotypes."
            a "Je ne suis pas la présidente parce que je suis la plus compétente."
            a "Je le suis parce que je suis douée en communication, coordination."
            a "Du moins... Parmis les membres du club.."
            show alice sad
            a "Ce n'est qu'un titre honorifique."
        "Je n'ai rien dit !":
            $ rel_ali +=2
            m "Je n'ai rien dit !"
            a "Ne pas dire des choses ne signifie pas ne pas les penser."
            m "Je n'ai rien penser non plus..."
            a "Ne rien penser, c'est ne pas exister."
            
label science_02:
    show alice geez
    a "Désolée mais je vais être directe !"
    show alice sad
    a "Es tu venu t'inscrire oui ou non ?"
    menu :
        m "Je crois bien que..."
        "J'ai bien réfléchit, je ne veux pas m'inscrire.":
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
            m "Je vais encore y réfléchir."
            show alice normal
            a "Ma question est binaire."
            a "Elle ne comportait que 2 réponses possibles."
            a "Oui, ou non."
            a "Je réitère donc ma question. Oui ou non ?"
            menu:
                "Oui.":
                    m "Oui."
                    a "Et bah voilà."
                    a "La prochaine fois, clarifie donc tes objectifs avant d'agir."
                "Non.":
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
            $ rel_ali += 3
            $ aller_science += 1
            m "Oui, je veux venir."
            show alice happy
            a "Bienvenu[ter] parmis nous !"
            show alice geez at left with move
            a "Que faîtes vous ici Sir Lloyd ?"
            show lloyd normal at right
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
            hide lloyd
            show alice sad at center with move
            a "L'aristo a encore brisé un moment d'émotion."
            menu:
                "N'exagérons rien.":
                    m "N'exagérons rien."
                    a "Oui..."
                "(Rire)":
                    $ rel_ali += 3
                    m "Haha..."
                    show alice happy
                    a "Ce sera la même chose à chacune de ses apparitions."
                    a "A chaque réaction son produit."
                "Oui, c'est vrai.":
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
            a "Il m'arrive aussi de mettre main à la patte dans un des projets s'il m'intéresse."
            a "Un club en particulier t'intéresse ?"
            m "Vous avez quoi déjà ?"
            a "Chimie, robotique ou informatique."
            menu:
                m "Je vais prendre..."
                "Chimie.":
                    m "Chimie."
                    $ club = 'chimie'
                "Robotique.":
                    m "Robotique."
                    $ club = 'robot'
                "Informatique.":
                    m "Informatique."
                    $ club = 'info'
                    
            show alice happy
            a "Club [club] donc..."
            m "Oui, c'est ça."
            show alice sad at left with move
            e "Hello ! Je suis en retard ?"
            show elusia normal 
            a "Bonjour Lulu."
            e "Alice, tu vas bien ?"
            show lloyd angry at right
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
            e "A plus tard !"
            hide elusia
            hide lloyd
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
            
