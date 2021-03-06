# TODO 
label go_home:
    if aller_home == -1:
        scene street with fade
        m "Je rentre seul[ter] chez moi."
        return
    elif aller_home == 0:
        jump home_0
    elif aller_home == 1:
        jump home_1
    elif aller_home == 2:
        jump home_2
    elif aller_home == 3:
        jump home_3
    else:
        "Pas encore disponible"
        return
        
label home_0:
    play music (ryou1) fadein 2
    scene street with fade
    show ryou surprised at left
    r "Ah bah te voilà enfin !"
    show ryou normal at center with move
    r "Je t'attendais pour rentrer."
    mh "Oh, c'est bien gentil de ta part."
    if bite:
        r "Ce serait bête que tu te perdes pour rentrer."
        mh "Très drôle. Merci quand même."
        r "Ne t'en fais pas pour ça."
    else:
        r "Je ne peux pas te laisser rentrer seule."
        r "C'est contre mes principes."
        mh "Oui oui..."
    
    scene couloir with fade
    show ryou happy
    r "Nous y voilà !"
    r "Tant qu'à faire, tu veux passer chez moi ?"
    m "Pourquoi faire ?"
    if bite:
        show ryou surprised
        r "Juste récupérer les cours."
        show ryou happy
        r "'Fin après, si tu veux jouer à la console ou sortir..."
        r "C'est comme tu veux hein !"
        menu:
            "Accepter.":
                # $ renpy.block_rollback()
                $ rel_ryou += 5
                m "Ouais, OK."
                show ryou normal
                r "Bon bah, par ici !"
                jump chez_ryou_homme
            "Refuser.":
                # $ renpy.block_rollback()
                m "Non, ce n'est pas urgent."
                show ryou sad
                r "OK."
                r "Comme tu voudra !"
                m "Je vais me reposer."
                r "Idem. A plus !"
                $ rel_ryou -= 2
                hide ryou with easeoutright
                $ vig += 2
                return
    else:
        show ryou angry
        r "Juste récupérer les cours."
        r "Rien de particulier hein !"
        menu:
            "Accepter.":
                # $ renpy.block_rollback()
                $ rel_ryou += 5
                m "D'accord."
                show ryou surprised
                r "Vraiment ?"
                m "Bah quoi ?"
                show ryou happy
                r "Je ne m'attendais pas à ce que tu acceptes !"
                r "Allons y!"
                jump chez_ryou_femme
            "Refuser.":
                # $ renpy.block_rollback()
                m "Pas aujourd'hui."
                m "Je suis épuisée, désolée !"
                show ryou sad
                r "Bah, c'est pas urgent hein..."
                r "Je devrais aussi aller me reposer."
                r "A plus !"
                $ rel_ryou -= 2
                $ vig += 2
                hide ryou with easeoutright
                return
        
label chez_ryou_homme:
    $ aller_home += 1
    play sound "sound/dooropen.mp3"
    scene chambre r with fade
    show ryou happy
    r "Bienvenu chez moi"
    play sound "sound/doorclose.mp3"
    show ryou sad
    r "Mmmh... J'aurais du ranger un peu..."
    r "Tiens, voilà tes cours."
    show ryou surprised
    r "Et sinon, t'en penses quoi ?"
    menu:
        "De quoi ? Elusia ?":
            # $ renpy.block_rollback()
            m "De quoi ? Elusia ?"
            r "........ Ouais !"
            m "Je crois que..."
            menu :
                "...je l'aime beaucoup !":
                    # $ renpy.block_rollback()
                    extend "je l'aime beaucoup !"
                    show ryou sad
                    r "Sérieusement ?"
                    r "Tu la cotoies depuis pas très longtemps..."
                    r "C'est un peu tôt nan ?"
                    $ rel_ryou -= 2
                "...je ne sais pas.":
                    # $ renpy.block_rollback()
                    extend "je ne sais pas."
                    m "Je ne suis ici que depuis peu."
                    m "C'est trop tôt pour juger."
                    show ryou sad
                    r "Pas faux."
                "...elle me met mal à l'aise.":
                    # $ renpy.block_rollback()
                    extend "elle me met mal à l'aise."
                    show ryou sad
                    r "Sérieusement ?"
                    $ rel_ryou -= 4
            menu:
                "Et toi ?":
                    # $ renpy.block_rollback()
                    $ rel_ryou += 2
                    m "Et toi ?"
                    show ryou angry
                    r "Moi ?"
                    m "Oui toi !"
                    show ryou sad
                    r "Je..."
                    show ryou happy
                    r "Je l'aime."
                    show ryou normal
                    r "Enfin je crois..."
                    r "Qu'importe !"
                    show ryou happy
                    r "On joue ?"
                    "J'ai passé la soirée à jouer aux jeux vidéos avec Ryouzanki."
                    "Le temps est passé si vite..."
                    hide ryou with easeoutright
                    return
                "Vous vous connaissez depuis longtemps ?":
                    # $ renpy.block_rollback()
                    m "Vous vous connaissez depuis~"
                    show ryou sad
                    r "Le lycée."
                    r "Ca remonte à un petit bout de temps."
                    show ryou normal
                    r "Puis, on s'est retrouvés par hasard dans la même école."
                    r "Qu'importe !"
                    show ryou happy
                    r "On joue ?"
                    "J'ai passé la soirée à jouer aux jeux vidéos avec Ryouzanki."
                    "Le temps est passé si vite..."
                    hide ryou with easeoutright
                    return                

            
        "De quoi ? L'école ?":
            # $ renpy.block_rollback()
            m "De quoi ? L'école ?"
            r "Bah ouais..."
            r "Tu croyais quoi ? Que je te demandais d'Elusia ?"
            m "L'école m'a l'air tout à fait convenable."
            m "Ce n'est pas très différent d'où je viens."
            r "Heureux de constater qu'on est normaux !"
            r "On joue ?"
            "J'ai passé la soirée à jouer aux jeux vidéos avec Ryouzanki."
            "Le temps est passé si vite..."
            hide ryou
            return
    
label chez_ryou_femme:
    $ aller_home += 1
    play sound "sound/dooropen.mp3"
    scene chambre r with fade
    show ryou happy
    r "Bienvenu chez moi !"
    play sound "sound/doorclose.mp3"
    show ryou sad
    r "Mmmh... J'aurais du ranger un peu..."
    r "Tiens, voilà tes cours."
    show ryou normal
    r "Et sinon, t'en penses quoi ?"
    m "De quoi ? L'école ?"
    r "Bah ouais..."
    r "Tu croyais quoi ? Que je te demandais d'Elusia ?"
    m "L'école m'a l'air tout à fait convenable."
    m "Ce n'est pas très différent d'où je viens."
    r "Heureux de constater qu'on est normaux !"
    m "Maintenant que tu parles d'Elusia..."
    menu:
        "Vous êtes frère et soeur ?":
            # $ renpy.block_rollback()
            m "Vous êtes frère et soeur ?"
            show ryou angry
            r "Nan... Tu plaisantes ?"
            r "Pas du tout nan..."
        "Vous vous connaissez depuis longtemps ?":
            # $ renpy.block_rollback()
            m "Vous vous connaissez depuis longtemps ?"
            r "Ouep."
            $ rel_ryou +=2
        "Vous sortez ensemble ?":
            # $ renpy.block_rollback()
            m "Vous sortez ensemble ?"
            show ryou angry
            r "Pardon ?"
            r "Pas vraiment non."
            $ rel_ryou -= 2
            
        
    show ryou sad
    r "On se connait depuis le lycée."
    r "Ca remonte à un petit bout de temps."
    show ryou normal
    r "Puis, on s'est retrouvés par hasard dans la même école."
    r "Qu'importe !"
    show ryou happy
    r "On peut passer aux choses ennuyantes ?"
    "Ryouzanki a relu ses notes avec moi pour s'assurer que j'arrivais à le relire."
    "C'est quelqu'un de plutot attentionné."
    "Le temps est passé si vite..."
    hide ryou
    return
    
label home_1:
    play music (ryou1) fadein 2
    scene street with fade
    show ryou normal at left
    r "Je savais que t'allais te défiler..."
    show ryou normal at center with move
    r "Tu devrais vraiment participer aux club."
    r "Et y participer activement..."
    m "Mais..."
    menu:
        "Et toi, t'es à un club peut être ?":
            # $ renpy.block_rollback()
            $ rel_ryou -= 2
            ma "Et toi, t'es à un club peut être ?"
            show ryou angry
            r "Bien sûr."
            r "Je suis dans tous les clubs en fait..."
            menu:
                "T'es pas un membre fictif par hasard ?":
                    # $ renpy.block_rollback()
                    $ rel_ryou -=2
                    mh "T'es pas un membre fictif par hasard ?"
                    r "Je suis inscrit, c'est déjà ça et j'y passe de temps en temps."
                    r "Pfff, si tu veux rentrer seul[ter], il fallait le dire plus tôt..."
                    hide ryou with easeoutright
                    $vig += 2
                    return
                "C'est si important que ça ?":
                    # $ renpy.block_rollback()
                    ma "C'est si urgent que ça ?"
                    r "Bah non, pas pour moi mais quand même..."
                    r "On rentre ?"
                    r "Je voulais justement te parler."
                    jump home2
        "Je suis HS. Je vais me reposer aujourd'hui.":
            # $ renpy.block_rollback()
            m "Je suis HS. Je vais me reposer aujourd'hui."
            show ryou sad
            r "Ah... D'accord."
            r "..."
            r "Je..."
            extend "Je voulais te parler justement."
            r "Tu as un peu de temps devant toi ?"
            menu:
                "Oui, si c'est rapide":
                    # $ renpy.block_rollback()
                    $rel_ryou +=5
                    m "Oui, si c'est rapide"
                    show ryou happy
                    r "Oui, t'inquiète !"
                    jump home2
                "Non, vraiment pas maintenant...":
                    # $ renpy.block_rollback()
                    m "Non, vraiment pas maintenant..."
                    $rel_ryou -=2
                    show ryou sad
                    r "OK..."
                    r "Repose toi bien !"
                    $ vig +=2
                    hide ryou with easeoutright
                    return
                    
label home2:  #var a changer car ambigue
    play sound "sound/dooropen.mp3"
    scene chambre r with fade
    show ryou happy
    r "Bienvenu chez moi"
    play sound "sound/doorclose.mp3"
    show ryou sad
    r "Mmmh... J'ai toujours pas rangé..."
    show ryou normal
    "On a parlé de tout et de n'importe quoi."
    if rel_ryou >= 15:
        "Quand soudain, il me demande."
        r "Dis moi..."
        r "Tu aiderai deux amis à sortir ensemble ?"
        menu:
            "Oh, tu parles de toi et Elusia ?":
                # $ renpy.block_rollback()
                $ rel_ryou +=2
                $ aller_home += 1
                mh "Oh, tu parles de toi et~"
                show ryou happy
                r "Ta ta ta ! Pas de conclusions hative !"
                r "J'ai posé une question assez gênante..."
                show ryou sad
                r "Oh, je n'avais pas vu l'heure !"
                r "Il faut que j'aille faire ma lessive avant que ça ferme."
                r "On se voit plus tard !"
                mh "Hey ! Ne t'enfuis pas !"
                scene couloir with fade
                show ryou happy
                r "J'y vais, à plus !"
                hide ryou with easeoutright
                mh "Il est partit vite..."
                return
            "Bien sûr que je les aiderai.":
                # $ renpy.block_rollback()
                $ rel_ryou +=1
                $ aller_home += 1
                mh "Bien sûr que je les aiderai."
                r "OK..."
                m "..."
                show ryou happy
                r "Ta ta ta ! Pas de conclusions hative !"
                r "J'ai posé une question assez gênante..."
                show ryou sad
                r "Oh, je n'avais pas vu l'heure !"
                r "Il faut que j'aille faire ma lessive avant que ça ferme."
                r "On se voit plus tard !"
                mh "Hey ! Ne t'enfuis pas !"
                scene couloir with fade
                show ryou surprised
                r "J'y vais, à plus !"
                hide ryou with easeoutright
                mh "Il est partit vite..."
                return
                
    else:
        "Je n'ai rien vu de très important dans ses propos."
        "Peut être qu'il hésite à en parler..."
        "Je devrais m'approcher de lui pour qu'il crache le morceau."
        $ rel_ryou += 2
        return
            
label home_2:
    play music (ryou1) fadein 2
    scene street with fade
    show ryou normal at left
    show ryou sad at center with move
    r "El~... Ah, c'est toi [j]."
    menu:
        "Perdu ! T'es déçu ?":
            # $ renpy.block_rollback()
            m "Perdu ! T'es déçu ?"
            show ryou normal
            if bite :
                r "Trop marrant mec..."
            else:
                r "Funny..."
            r "En ce moment, elle me fausse souvent compagnie..."
            r "Depuis ton arrivée en fait..."
            m "Je suis là, avec toi."
            show ryou happy
            r "Oh, mais j'ai rien insinué."
        "Tu veux qu'on aille la chercher ?":
            # $ renpy.block_rollback()
            $rel_ryou += 2
            mh  "Tu veux qu'on aille la chercher ?"
            show ryou happy
            r "C'est sympa de proposer mais non."
            r "Si elle ne vient pas, c'est probablement parce qu'elle ne peut pas."
            r "On va juste la déranger en faisant ça."
    r "Je vais rentrer. Je suppose que toi aussi du coup..."
    show ryou normal
    r "Tu te plaîs ici ?"
    m "C'est pas comme si j'avais le choix !"
    r "Oui. Comment sont tes nouveaux camarades ?"
    menu:
        "Je les aime tous.":
            # $ renpy.block_rollback()
            mh "Je les aime tous."
            $ rel_ryou += 5
            r "Je vois."
            r "Content de savoir que tu t'es adapté[ter]."
        "J'en aime beaucoup.":
            # $ renpy.block_rollback()
            mh "J'en aime beaucoup."
            r "OK."
            r "C'est assez normal de ne pas tous les aimer."
        "Ils ne sont pas tous très intéressants.":
            # $ renpy.block_rollback()
            m "Ils ne sont pas tous très intéressants."
            r "Ah bon..."
            r "Ils ont tous leur bon et mauvais côté."
            $ rel_ryou += 1
        "Ils sont ennuyeux.":
            # $ renpy.block_rollback()
            ma "Ils sont ennuyeux."
            r "Carrément..."
            r "Les types d'où tu venais étaient des anges alors."
            $ rel_ryou += 3
    scene couloir with fade
    show ryou surprised
    r "Bon bah, on est arrivé..."
    show ryou happy
    r "A plus tard !"
    m "A plus tard."
    $ vig += 2
    $ aller_home +=1
    return
    
label home_3:
    $ aller_home +=1
    $ vig += 2
    play music (ryou1) fadein 2
    scene street with fade
    show ryou surprised at left
    r "Oh te voilà !"
    show ryou normal at center with move
    r "J'ai un petit détour à faire si ça ne te gêne pas..."
    menu:
        "Pas de soucis.":
            # $ renpy.block_rollback()
            m "Pas de soucis."
        "Fais le sans moi.":
            # $ renpy.block_rollback()
            $ rel_ryou -= 2
            m "Fais le sans moi."
            show ryou angry
            r "Sérieux ?"
            r "J'en ai juste pour 5 minutes à la poste !"
            menu:
                "Je n'ai pas 5 minutes à t'accorder.":
                    # $ renpy.block_rollback()
                    $ rel_ryou -= 6
                    m "Je n'ai pas 5 minutes à t'accorder."
                    r "..."
                    show ryou sad
                    r "OK, désolé pour le dérangement..."
                    r "Je ne t'attendrais plus, désormais vu que tu préfères rentrer en solo."
                    $ aller_home = -1
                    return
                "Bon OK...":
                    # $ renpy.block_rollback()
                    m "Bon OK..."
    show ryou happy
    r "On va juste faire un petit tour à la poste !"
    m "On va récupérer quoi ?"
    show ryou normal
    r "Une figurine d'anime."
    r "Aimes-tu les animes ?"
    menu:
        "Pas vraiment non.":
            # $ renpy.block_rollback()
            $ rel_ryou -= 2
            m "Pas vraiment non."
            r "Oh... Dommage"
        "Ca m'arrive d'en regarder.":
            # $ renpy.block_rollback()
            $ rel_ryou -= 1
            m "Ca m'arrive d'en regarder."
            r "Ah oui ?"
        "Oui de temps en temps.":
            # $ renpy.block_rollback()
            $ rel_ryou += 1
            m "Oui de temps en temps."
            r "Oh... Tu regardes quoi ?"
        "Oui, beaucoup.":
            # $ renpy.block_rollback()
            $ rel_ryou += 2
            m "Oui, beaucoup."
            r "Sérieux ?"
            r "Alors est-ce que tu connais..."
    hide ryou with fade
    "Ryou a passé le trajet jusqu'à la poste à me parler d'animes de mechas et de conquête spatiale."
    "Mais aussi de complots et de géo-politique."
    "Il aime beaucoup ce genre on dirait."
    show ryou happy with fade
    r "Désolé pour l'attente."
    show ryou normal
    r "Dis moi... Qu'est ce qui est important pour toi dans une série ?"
    menu:
        "Le scénario.":
            # $ renpy.block_rollback()
            $ rel_ryou += 2
            m "Le scénario."
            r "C'est vrai que le scénario est très important."
            r "Mais si les personnages le jouent mal..."
            r "Toute la série est mauvaise."
        "Les personnages.":
            # $ renpy.block_rollback()
            $ rel_ryou += 4
            m "Les personnages."
            show ryou happy
            r "Tout à fait, je pense aussi ainsi."
        "L'époque.":
            # $ renpy.block_rollback()
            $ rel_ryou -= 2
            m "L'époque."
            r "Sérieux ?"
            r "C'est assez... Superficiel comme critère de sélection..."
        "Le graphisme.":
            # $ renpy.block_rollback()
            m "Le graphisme."
            r "C'est assez... Superficiel comme critère de sélection..."
            r "Mais ça se défend."
        "Les musiques.":
            # $ renpy.block_rollback()
            m "Les musiques."
            r "C'est assez... Superficiel comme critère de sélection..."
            r "Mais bon, les musiques font l'ambiance..."
    r "Moi, il m'est difficile d'accrocher à une série avec de mauvais personnages."
    r "Je ne parle pas de m'identifier à l'un d'entre eux."
    r "J'aime voir des personnages théâtraux et charismatiques."
    r "Même si c'est souvent le méchant..."
    scene couloir
    show ryou normal
    with fade
    r "On est arrivé."
    r "Merci de m'avoir accompagné et à la prochaine !"
    m "Bye !"
    return
