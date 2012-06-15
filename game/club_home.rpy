label go_home:
    if aller_home == 0:
        jump home_0
    elif aller_home == 1:
        jump home_1
    elif aller_home == 2:
        jump home_2
        
label home_0:
    $ renpy.music.play("music/ryouzanki.ogg", fadein=2)
    scene street with dissolve
    show ryou normal at left
    r "Ah bah te voilà enfin !"
    show ryou normal at center with move
    r "Je t'attendais pour rentrer."
    m "Oh, c'est bien gentil de ta part."
    if bite:
        r "Ce serait bête que tu te perdes pour rentrer."
        m "Très drôle. Merci quand même."
        r "Ne t'en fais pas pour ça."
    else:
        r "Je ne peux pas te laisser rentrer seule."
        r "C'est contre mes principes."
        m "Oui oui..."
    
    scene couloir with dissolve
    show ryou happy
    r "Nous y voilà !"
    r "Tant qu'à faire, tu veux passer chez moi ?"
    m "Pourquoi faire ?"
    if bite:
        show ryou normal
        r "Juste récupérer les cours."
        r "'Fin après, si tu veux jouer à la console ou sortir..."
        r "C'est comme tu veux hein !"
        menu:
            "Accepter.":
                $ rel_ryou += 5
                m "Ouais, OK."
                show ryou happy
                r "Bon bah, par ici !"
                jump chez_ryou_homme
            "Refuser.":
                m "Non, ce n'est pas urgent."
                show ryou sad
                r "OK."
                r "Comme tu voudra !"
                m "Je vais me reposer."
                r "Idem. A plus !"
                $ rel_ryou -= 2
                hide ryou
                return
    else:
        show ryou angry
        r "Juste récupérer les cours."
        r "Rien de particulier hein !"
        menu:
            "Accepter.":
                $ rel_ryou += 5
                m "D'accord."
                r "Vraiment ?"
                m "Bah quoi ?"
                show ryou happy
                r "Je ne m'attendais pas à ce que tu acceptes !"
                r "Allons y!"
                jump chez_ryou_femme
            "Refuser.":
                m "Pas aujourd'hui."
                m "Je suis épuisée, désolée !"
                show ryou sad
                r "Bah, c'est pas urgent hein..."
                r "Je devrais aussi aller me reposer."
                r "A plus !"
                $ rel_ryou -= 2
                hide ryou
                return
        
label chez_ryou_homme:
    $ aller_home += 1
    play sound "sound/dooropen.mp3"
    scene chambre r with dissolve
    show ryou happy
    r "Bienvenu chez moi"
    play sound "sound/doorclose.mp3"
    show ryou sad
    r "Mmmh... J'aurais du ranger un peu..."
    r "Tiens, voilà tes cours."
    show ryou normal
    r "Et sinon, t'en penses quoi ?"
    menu:
        "De quoi ? Elusia ?":
            m "De quoi ? Elusia ?"
            r "........ Ouais !"
            m "Je crois que..."
            menu :
                "...je l'aime beaucoup !":
                    extend "je l'aime beaucoup !"
                    show ryou sad
                    r "Sérieusement ?"
                    r "Tu la cotoies depuis pas très longtemps..."
                    r "C'est un peu tôt nan ?"
                    $ rel_ryou -= 2
                "...je ne sais pas.":
                    extend "je ne sais pas."
                    m "Je ne suis ici que depuis 48h."
                    m "C'est trop tôt pour juger."
                    show ryou sad
                    r "Pas faux."
                "...elle me met mal à l'aise.":
                    extend "elle me met mal à l'aise."
                    show ryou sad
                    r "Sérieusement ?"
                    $ rel_ryou -= 4
            menu:
                "Et toi ?":
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
                    hide ryou
                    return
                "Vous vous connaissez depuis longtemps ?":
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
                    hide ryou
                    return                

            
        "De quoi ? L'école ?":
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
    scene chambre r with dissolve
    show ryou happy
    r "Bienvenu chez moi"
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
            m "Vous êtes frère et soeur ?"
            show ryou angry
            r "Nan... Tu plaisantes ?"
            r "Pas du tout nan..."
        "Vous vous connaissez depuis longtemps ?":
            m "Vous vous connaissez depuis longtemps ?"
            r "Ouep."
            $ rel_ryou +=2
        "Vous sortez ensemble ?":
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
    $ renpy.music.play("music/ryouzanki.ogg", fadein=2)
    scene street with dissolve
    show ryou normal at left
    r "Je savais que t'allais te défiler..."
    show ryou normal at center with move
    r "Tu devrais vraiment participer aux club."
    r "Et y participer activement..."
    m "Mais..."
    menu:
        "Et toi, t'es à un club peut être ?":
            $ rel_ryou -= 2
            m "Et toi, t'es à un club peut être ?"
            show ryou angry
            r "Bien sûr."
            r "Je suis dans tous les clubs en fait..."
            menu:
                "T'es pas un membre fictif par hasard ?":
                    $ rel_ryou -=2
                    m "T'es pas un membre fictif par hasard ?"
                    r "Je suis inscrit, c'est déjà ça et j'y passe de temps en temps."
                    r "Pfff, si tu veux rentrer seul[ter], il fallait le dire plus tôt..."
                    hide ryou
                    return
                "C'est si important que ça ?":
                    m "C'est si urgent que ça ?"
                    r "Bah non, pas pour moi mais quand même..."
                    r "On rentre ?"
                    r "Je voulais justement te parler."
                    jump home2
        "Je suis HS. Je vais me reposer aujourd'hui.":
            m "Je suis HS. Je vais me reposer aujourd'hui."
            show ryou sad
            r "Ah... D'accord."
            r "..."
            r "Je..."
            extend "Je voulais te parler justement."
            r "Tu as un peu de temps devant toi ?"
            menu:
                "Oui, si c'est rapide":
                    $rel_ryou +=5
                    m "Oui, si c'est rapide"
                    show ryou happy
                    r "Oui, t'inquiète !"
                    jump home2
                "Non, vraiment pas maintenant...":
                    m "Non, vraiment pas maintenant..."
                    $rel_ryou -=2
                    show ryou sad
                    r "OK..."
                    r "Repose toi bien !"
                    hide ryou
                    return
                    
label home2:  #var a changer car ambigue
    play sound "sound/dooropen.mp3"
    scene chambre r with dissolve
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
                $ rel_ryou +=2
                $ aller_home += 1
                m "Oh, tu parles de toi et~"
                show ryou happy
                r "Ta ta ta ! Pas de conclusions hative !"
                r "J'ai posé une question assez gênante..."
                show ryou sad
                r "Oh, je n'avais pas vu l'heure !"
                r "Il faut que j'aille faire ma lessive avant que ça ferme."
                r "On se voit plus tard !"
                m "Hey ! Ne t'enfuis pas !"
                scene couloir with dissolve
                show ryou happy
                r "J'y vais, à plus !"
                hide ryou
                m "Il est partit vite..."
                return
            "Bien sûr que je les aiderai.":
                $ rel_ryou +=1
                $ aller_home += 1
                m "Bien sûr que je les aiderai."
                r "OK..."
                m "..."
                show ryou happy
                r "Ta ta ta ! Pas de conclusions hative !"
                r "J'ai posé une question assez gênante..."
                show ryou sad
                r "Oh, je n'avais pas vu l'heure !"
                r "Il faut que j'aille faire ma lessive avant que ça ferme."
                r "On se voit plus tard !"
                m "Hey ! Ne t'enfuis pas !"
                scene couloir with dissolve
                show ryou happy
                r "J'y vais, à plus !"
                hide ryou
                m "Il est partit vite..."
                return
                
    else:
        "Je n'ai rien vu de très important dans ses propos."
        "Peut être qu'il hésite à en parler..."
        "Je devrais m'approcher de lui pour qu'il crache le morceau."
        $ rel_ryou += 2
        return
            
label home_2:
    $ renpy.music.play("music/ryouzanki.ogg", fadein=2)
    scene street with dissolve
    show ryou normal at left
    show ryou sad at center with move
    r "El~... Ah, c'est toi [j]."
    menu:
        "Perdu ! T'es déçu ?":
            m "Perdu ! T'es déçu ?"
            show ryou normal
            if bite :
                r "Trop marrant mec..."
            else:
                r "Funny..."
            r "En ce moment, elle me fausse souvent compagnie..."
            r "Depuis ton arrivée en fait..."
            m "Je suis là, avec toi."
            r "Oh, mais j'ai rien insinué."
        "Tu veux qu'on aille la chercher ?":
            $rel_ryou += 2
            m  "Tu veux qu'on aille la chercher ?"
            show ryou normal
            r "C'est sympa de proposer mais non."
            r "Si elle ne vient pas, c'est probablement parce qu'elle ne peut pas."
            r "On va juste la déranger en faisant ça."
    r "Je vais rentrer. Je suppose que toi aussi du coup..."
    r "Tu te plaîs ici ?"
    m "C'est pas comme si j'avais le choix !"
    r "Oui. Comment sont tes nouveaux camarades ?"
    menu:
        "Je les aime tous.":
            m "Je les aime tous."
            $ rel_ryou += 5
            r "Je vois."
            r "Content de savoir que tu t'es adapté[ter]."
        "J'en aime beaucoup.":
            m "J'en aime beaucoup."
            r "OK."
            r "C'est assez normal de ne pas tous les aimer."
        "Ils ne sont pas tous très intéressants.":
            m "Ils ne sont pas tous très intéressants."
            r "Ah bon..."
            r "Ils ont tous leur bon et mauvais côté."
            $ rel_ryou += 1
        "Ils sont ennuyeux.":
            m "Ils sont ennuyeux."
            r "Carrément..."
            r "Les types d'où tu venais étaient des anges alors."
            $ rel_ryou += 3
    scene couloir with dissolve
    show ryou sad
    r "Bon bah, on est arrivé..."
    r "A plus tard !"
    m "A plus tard."
    $ aller_home +=1
    return
