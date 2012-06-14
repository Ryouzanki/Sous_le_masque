screen demo_imagemap:
    imagemap:
        auto "imagemap_%s.jpg"

        hotspot (8, 200, 78, 78) action Return("swimming")
        hotspot (204, 50, 78, 78) action Return("science")
        hotspot (452, 79, 78, 78) action Return("art")
        hotspot (602, 316, 78, 78) action Return("go home")


label day1:
    
    scene reveil with dissolve
    play sound "sound/clock.mp3"
    m "Argh !"
    m "Maudit réveil !!"
    m "Se lever à 7h après s'être couché aussi tard, c'est dur..."
    stop sound
    $ renpy.music.play("music/joueur.ogg", fadein=2)
    m "Il est déjà si tard..."
    
    if rel_ryou == 0:
        jump oo
    elif rel_lulu == 0:
        jump os
    else:
        jump ss
        
label oo:
    "Mes préparatifs terminés, je sors."
    play sound "sound/doorclose.mp3"
    scene black with dissolve
    scene couloir with dissolve
    "Je ne sais pas où aller."
    scene street with dissolve
    "J'ai une idée géniale : Suivre le flux d'étudiants"
    "Un peu plus loin, j'aperçois une silhouette familière."
    "Ryouzanki est devant moi, accompagné d'une jeune fille."
    "Je suis sur la bonne voie."
    "Et maintenant ?"
    menu:
        "Les aborder.":
            show ryou normal at left
            show elusia normal at right
            m "Salut !"
            r "Hey ! Salut !"
            r "T'as trouvé le chemin !"
            m "Oui, j'ai suivi des jeunes au pif."
            r "Pas mal !"
            r "[j], je te présente ta voisine du dessous : Elusia !"
            r "Elusia, [j] !"
            r "[j], Elusia !"
            r "Elusia~"
            $ fille = 'Elusia'
            show elusia sad at right
            e "Oui, c'est bon, on a compris !"
            show elusia normal at right
            e "Enchantée [j] !"
            e "On ferait mieux de se dépêcher, les retards ne sont pas bien vus ici."
            hide ryou
            hide elusia
            scene black with dissolve
            scene classroom with dissolve
            "On s'est mis au premier rang."
            "Le cour était vraiment ennuyeux."
            "Mais c'est rassurant."
            "Je n'ai pas accumulé énormément de retard lors de mon transfert."
            $ rel_ryou += 2
            $ rel_lulu += 2
            jump day1_matin
        "Les suivre.":
            "Je les suis jusqu'en classe."
            scene black with dissolve
            scene classroom with dissolve
            show ryou normal
            r "Hey ! Salut !"
            r "T'as trouvé le chemin !"
            m "Oui, j'ai suivi des jeunes au pif."
            show ryou sad
            r "Mmh... Elusia est partie se mettre au premier rang..."
            r "Tu viens avec nous ?"
            menu:
                "Aller au premier rang.":
                    m "Oui, pourquoi pas."
                    show ryou normal
                    hide ryou
                    "On s'est mis au premier rang."
                    "Le cour était vraiment ennuyeux."
                    "Mais c'est rassurant."
                    "Je n'ai pas accumulé énormément de retard lors de mon transfert."
                    $ rel_ryou += 2
                    jump day1_matin
                "Aller au fond.":
                    m "Non merci, je préfère être au fond."
                    show ryou normal
                    r "Ah... Bah, à plus tard !"
                    hide ryou
                    "Le cour était vraiment ennuyeux."
                    "Mais c'est rassurant."
                    "Je n'ai pas accumulé énormément de retard lors de mon transfert."
                    jump day1_matin
        
label os:
    play sound "sound/bell.mp3"
    pause(1)
    play sound "sound/dooropen.mp3"
    scene black with dissolve
    scene couloir with dissolve
    show ryou normal at left
    show elusia normal at right
    r "Yo !"
    e "Salutations !"
    e "Enchantée de faire ta connaissance [j] !"
    e "Je me nomme Elusia !"
    $ fille = 'Elusia'
    m "Salut !"
    show elusia sad at right
    "..."
    e "Bref, allons-y avant d'être en retard..."
    show elusia normal at right
    jump route1
    
label ss:
    play sound "sound/bell.mp3"
    pause(1)
    play sound "sound/dooropen.mp3"
    scene black with dissolve
    scene couloir with dissolve
    show ryou normal at left
    show elusia normal at right
    r "Yo !"
    e "Salutations !"
    e "Bien dormi ?"
    m "Oui mais pas assez !"
    if rel_ryou == 7:
        show elusia happy at right
        e "Il ne fallait pas prendre de café..."
        e "Ca t'apprendra !"
    else:
        show ryou happy at left
        r "Pourtant, [sexe] a pris un thé."
        show elusia angry at right
        e "A force de te gorger de caféine, tu y es immunisé."
        show ryou normal at left
        
    show elusia normal at right
    e "Bref, allons-y avant d'être en retard..."
    jump route1
    
label route1:
    scene street with dissolve
    "L'école est toute proche."
    scene black with dissolve
    scene classroom with dissolve
    hide ryou
    hide elusia
    "On s'est mis au premier rang."
    "Le cour était vraiment ennuyeux."
    "Mais c'est rassurant."
    "Je n'ai pas accumulé énormément de retard lors de mon transfert."
    jump day1_matin
    
label day1_matin:
    
    "Etre au premier rang n'empêcha pas Ryouzanki de dormir."
    "Elusia a cependant l'air plus sérieuse."
    scene black with dissolve
    pause(1)
    scene classroom with dissolve
    $ renpy.music.play("music/matin.ogg", fadein=2)
    "Pendant que je range mes affaires à la fin du cours, ils viennent devant la table."
    show ryou normal at left
    show elusia normal at right
    r "Tu fais quoi pour la pause de midi ?"
    m "Je vais au RU."
    m "Comme tout le monde non ?"
    show ryou sad at left
    r "Bah..."
    show elusia happy at right
    e "Pas nous !"
    r "Il y a toujours une queue immense."
    e "Nous, on préfère acheter des sandwichs et aller déjeuner dans le parc."
    e "C'est nettement plus agréable !"
    if fille =='Jeune fille':
        show elusia normal at right
        e "Au fait, moi c'est Elusia !"
        $ fille = 'Elusia'
        e "Et toi ?"
        m "[j] !"
        e "Enchantée de faire ta connaissance [j] !"
        e "Je suis la voisine du dessous !"
    show ryou normal at left
    r "Tu veux venir manger avec nous ?"
    menu:
        "D'accord, ça m'a l'air sympa !":
            m "D'accord, ça m'a l'air sympa !"
            show ryou happy at left
            show elusia happy at right
            r "C'est réglé alors !"
            r "Amène toi !"
            $ rel_lulu += 6
            $ rel_ryou += 6
            jump manger_dehors
        "Heu, je suis un peu à sec en ce moment...":
            m "Heu, je suis un peu à sec en ce moment..."
            show ryou sad at left
            r "Ah..."
            if rel_lulu >= 5:
                show elusia sad at right
                e "Ah mais si c'est simplement une question d'argent..."
                e "Je peux t'avancer !"
                menu:
                    "Refuser poliment":
                        m "Non merci, c'est vraiment gentil."
                        m "Mais je ne peux pas accepter."
                        e "Ah... Dommage."
                        r "Bon bah tant pis. On se voit après la pause !"
                        hide ryou
                        e "Bon appétit !"
                        hide elusia
                        m "Merci !"
                        jump RU
                    "Accepter l'avance d'Elusia":
                        m "Oh vraiment, merci !"
                        e "Tout le plaisir est pour moi voyons !"
                        show ryou happy at left
                        r "Ah ouais ? Tu veux bien payer pour moi aussi ?"
                        show elusia angry at right
                        e "Même pas en rêve !"
                        $ rel_lulu += 2
                        $ rel_ryou +=5
                        jump manger_dehors
                    "Accepter de venir mais payer.":
                        m "Oh, vraiment, merci !"
                        m "Je vais venir mais je ne veux pas que tu m'avances."
                        show elusia happy at right
                        e "Comme tu voudra !"
                        show ryou happy at left
                        r "Moi je veux bien que~"
                        show elusia angry at right
                        e "Même pas en rêve !"
                        $ rel_lulu += 5
                        $ rel_ryou += 5
                        jump manger_dehors
            else:
                e "Ah... Dommage."
                r "Bon bah tant pis. On se voit après la pause !"
                hide ryou
                e "Bon appétit !"
                hide elusia
                m "Merci !"
                jump RU
                
label manger_dehors:
    scene parc with dissolve
    show elusia happy at right
    show ryou happy at left
    "Nous sommes allés au parc."
    "Il faisait beau et nous avons mangé nos sandwichs en papotant, assis dans l'herbe."
    "Ils m'ont surtout posé des questions sur l'endroit d'où je viens."
    "C'était très agréable."
    jump cours22
    
label RU:
    scene ru with dissolve
    "Comme pour venir, je suivis les flux d'étudiants pour trouver le RU."
    "Alors que je mangeais à ma table en solitaire..."
    show laura normal
    l "T'es tout seul ? On peut se mettre là ?"
    menu:
        "Oui, bien sûr !":
            m "Oui, bien sûr !"
            $ rel_lolo += 2
            jump RUU
        "Non, j'attends quelqu'un.":
            m "Non, j'attends quelqu'un."
            show laura angry
            "Elle resta devant moi un moment, sceptique."
            "Puis, rejoins par un garçon, ils partirent."
            hide laura
            jump cours2
        "Non, je préfère rester seul.":
             m "Non, je préfère rester seul."
             show laura angry
             "Elle posa son plateau."
             m "Hey !"
             l "Ce n'était pas une question !"
             m "Bien sur que si !"
             jump RUU
             
label RUU:
    show laura normal at left
    l "Valeth ! Par ici !"
    show valeth normal at right
    v "Oui, oui, j'arrive !"
    v "Salut toi !"
    v "Je suis dans ta classe, j'étais assis à l'autre boût du rang !"
    m "Ah, oui."
    v "Je m'appelle Valeth !"
    $ valou = 'Valeth'
    v "Elle, c'est Laura, la déléguée de classe !"
    show laura sad at left
    $ en = 'Laura'
    v "Et toi, c'est comment ?"
    m "Moi, c'est [j]."
    l "UNE des déléguée de classe !"
    show valeth happy at right
    v "Laura, tu ne vas pas encore piquer une crise pour ça ?"
    show laura angry at left
    l "Elle me gonfle, mais elle me gonfle celle là !!"
    m "De qui parlez vous ?"
    show valeth normal at right
    v "Laura ne s'entend pas bien avec Elusia, qui est l'autre déléguée de classe."
    l "C'est vrai quoi, elle est lourde à force avec ses 'En tant que déléguée de classe...'"
    l "Pour qui elle se prend ? Avec ses airs hautains..."
    l "Nan mais c'est vrai quoi ! Elle est chiante pas vrai ?"
    "Mince, je crois qu'elle s'adressait à moi..."
    menu:
        "Heu... Oui...":
            m "Heu... Oui..."
            show laura happy at left
            l "Ah, tu vois ? Valeth, [sexe] est d'accord avec moi !"
            v "Oui enfin, [sexe] est d'accord parce que tu l'aggresses..."
            v "Enfin, [sexe] vient d'arriver..."
            v "Laisse lui le temps de~"
            show laura angry at left
            l "Comprendre Elusia ? Il n'y a rien à comprendre."
            l "Je la hais !"
            "Je passais le reste de ma pause à entendre Laura se plaindre à propos d'Elusia."
            "C'était aussi amusant qu'embarassant."
            hide laura
            hide valeth
            $ rel_lolo += 5
            jump cours2
        "N'exagérons rien...":
            m "N'exagérons rien..."
            show laura angry at left
            l "Je n'exagère rien !"
            l "Cette manie de demander si le prof a besoin d'un coup de main..."
            l "Ca me mets hors de moi !"
            "Je passais le reste de ma pause à entendre Laura se plaindre à propos d'Elusia."
            "C'était aussi amusant qu'embarassant."
            hide laura
            hide valeth
            $ rel_lolo += 2
            jump cours2
            
label cours22:
    hide ryou
    hide elusia
    $ renpy.music.play("music/jour.ogg", fadein=2)
    scene black with dissolve
    "La pause de midi est terminée."
    "Il faut retourner en cours..."
    scene classroom with dissolve
    "Le premier rang n'est pas aussi désagréable que ça..."
    "C'est amusant d'empêcher Ryouzanki de dormir en lui pinçant les côte..."
    jump fin_cours
    
label cours2:
    $ renpy.music.play("music/jour.ogg", fadein=2)
    scene black with dissolve
    "La pause de midi est terminée."
    "Il faut retourner en cours..."
    scene classroom with dissolve
    "En entrant dans la salle, j'aperçois Ryouzanki et Elusia au premier rang."
    if rel_lolo > 0:
        "Et aussi Laura et Valeth au fond de la classe."
        "Je pourrais m'assoir avec ..."
        menu:
            "Laura et Valeth.":
                jump LV
            "Elusia et Ryouzanki.":
                jump RZ
            "Personne.":
                "Le cours est vraiment ennuyeux..."
                jump fin_cours
                
    else:
        "Je pourrais m'assoir avec eux..."
        menu:
            "Oui.":
                jump RZ
            "Non.":
                "Le cours est vraiment ennuyeux..."
                jump fin_cours

label RZ:
    show ryou sad at left
    show elusia normal at right
    r "Reuh !"
    m "Heu... Re !"
    e "Bien mangé ?"
    m "Oui, ça va, et vous ?"
    e "Perfecto !"
    show ryou happy at left
    r "Je dirais même plus, Elusia, perfectissimo !"
    "Le premier rang n'est pas aussi désagréable que ça..."
    "C'est amusant d'empêcher Ryouzanki de dormir en lui pinçant les côte..."
    hide elusia
    hide ryou
    $ rel_lulu += 2
    $ rel_ryou += 2
    jump fin_cours
    
label LV:
    show valeth happy at right
    show laura normal at left
    v "Tiens, mais qui voilà !"
    m "Salut, je peux m'assoir là ?"
    l "Bien sûr !"
    m "Merci."
    show valeth normal at right
    v "Au fait, je ne t'ai pas demandé..."
    v "As tu l'intention de joindre un club ?"
    menu :
        "Pas pour le moment non.":
            m "Pas pour le moment non."
            v "Ah... Dommage."
            v "Quand tu changera d'avis, le bâtiment des clubs, c'est le gros en rouge."
            m "D'accord."
            show valeth happy at right
            v "J'y suis presque tous les soirs."
        "Oui, le plus tôt sera la mieux !":
            m "Oui, le plus tôt sera la mieux !"
            show valeth happy at right
            v "Haha, ça fait du bien de voir des gens motivés !"
            v "Le bâtiment des clubs, c'est le gros en rouge !"
            v "Je t'y attends après les cours alors !"
            m "D'accord !"
            $ rel_val += 5
    show valeth normal at right
    show laura angry at left
    l "Ne te laisse pas embrigader par Valeth et ses clubs louches !"
    v "Pardon ?"
    show laura happy at left
    l "Valeth traîne dans les clubs d'échecs, de jeux de rôle et tout ça."
    l "Si tu veux des clubs de sport, je peux te montrer !"
    l "J'y suis tous les soir, au gymnase !"
    if rel_val == 5:
        menu:
            "Non merci, je préfère les clubs calmes":
                m "Non merci, je préfère les clubs calmes"
                show laura sad at left
                l "Tsss... Comme tu voudra !"
                $ rel_val += 2
            "Oui, je peux faire les deux.":
                m "Oui, je peux faire les deux."
                show laura normal at left
                l "Eventuellement, tu peux alterner."
                $ rel_lolo += 2
            "Ah oui, je préfère largement les clubs de sport !":
                m "Ah oui, je préfère largement les clubs de sport !"
                l "Tiens ! Dans les dents, l'intello !"
                show valeth angry at right
                v "..."
                $ rel_lolo += 5
                $ rel_val -= 3
    else:
        menu:
            "Je n'ai pas le temps pour le moment.":
                m "Je n'ai pas le temps pour le moment."
                show laura sad at left
                l "OK, tant pis."
            "Bon, va pour le sport.":
                m "Bon, va pour le sport."
                show laura happy at left
                l "Super, je t'attends ce soir pour ton inscription."
                l "Tout ce que tu veux, sauf tennis et tir à l'arc."
                show valeth happy at right
                v "Ha ha..."
                $ rel_lolo += 5
    hide valeth
    hide laura
    jump fin_cours
    
label fin_cours:
    show prof happy
    "A la fin du cours, notre professeur principal a demandé à me parler."
    "La routine."
    "Me dire qu'on ne peut choisir qu'un seul sport."
    "Il voulait aussi savoir si j'avais des difficultées à m'intégrer."
    "Demander cela dès le premier jour est assez brusque..."
    hide prof
    "..."
    "Tout le monde est parti."
    "Où pourrais-je bien aller ?"
    window hide None
    call screen demo_imagemap
    window show None
        
    if _return == "swimming":

        "Et si j'allais faire un peu de sport..."
        call sport
    
    elif _return == "science":

        "J'ai cru voir de l'agitation dans le bâtiment des sciences."
        "Il y a peut être des clubs là bas..."
        call labo
        
    elif _return == "art":

        "Et si j'allais faire un tour au bâtiments des clubs..."
        call club

    elif _return == "go home":
        
        "Je crois que je vais rentrer."
        call go_home
        
        
label day1_fin:
    $ renpy.music.play("music/joueur.ogg", fadein=2)
    scene couloir with dissolve
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    "Et ce n'est que le premier jour..."
    scene chambre m with dissolve
    play sound "sound/doorclose.mp3"
    "Je crois que je vais dormir."
    return
