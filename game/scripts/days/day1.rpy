screen demo_imagemap:
    imagemap:
        auto "UI/imagemap_%s.png"

        hotspot (8, 200, 78, 78) action Return("science")
        hotspot (204, 50, 78, 78) action Return("gymnase")
        hotspot (452, 79, 78, 78) action Return("rentrer")
        hotspot (602, 316, 78, 78) action Return("art")


label day1:
    $ unlocked_journal_pages += 1
    scene reveil with fade
    play sound "sound/clock.mp3"
    ma "Argh !"
    ma "Maudit réveil !!"
    m "Se lever à 7h après s'être couché aussi tard, c'est dur..."
    stop sound
    play music (joueur1) fadein 2
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
    scene couloir with fade
    "Je ne sais pas où aller."
    scene street with fade
    "J'ai une idée géniale : Suivre le flux d'étudiants"
    "Un peu plus loin, j'aperçois une silhouette familière."
    "Ryouzanki est devant moi, accompagné d'une jeune fille."
    "Je suis sur la bonne voie."
    "Et maintenant ?"
    menu:
        "Les aborder.":
            $ renpy.block_rollback()
            show ryou normal:
                left
            show elusia normal:
                right
            with easeinright
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
            show elusia geez
            e "Oui, c'est bon, on a compris !"
            show elusia normal
            e "Enchantée [j] !"
            show elusia sad
            e "On ferait mieux de se dépêcher, les retards ne sont pas bien vus ici."
            scene classroom with fade
            "On s'est mis au premier rang."
            "Le cour était vraiment ennuyeux."
            "Mais c'est rassurant."
            "Je n'ai pas accumulé énormément de retard lors de mon transfert."
            $ rel_ryou += 2
            $ rel_lulu += 2
            jump day1_matin
        "Les suivre.":
            $ renpy.block_rollback()
            "Je les suis jusqu'en classe."
            scene classroom with fade
            show ryou normal with easeinleft
            r "Hey ! Salut !"
            r "T'as trouvé le chemin !"
            m "Oui, j'ai suivi des jeunes au pif."
            show ryou sad
            r "Mmh... Elusia est partie se mettre au premier rang..."
            r "Tu viens avec nous ?"
            menu:
                "Aller au premier rang.":
                    $ renpy.block_rollback()
                    m "Oui, pourquoi pas."
                    hide ryou
                    "On s'est mis au premier rang."
                    "Le cour était vraiment ennuyeux."
                    "Mais c'est rassurant."
                    "Je n'ai pas accumulé énormément de retard lors de mon transfert."
                    $ rel_ryou += 2
                    jump day1_matin
                "Aller au fond.":
                    $ renpy.block_rollback()
                    m "Non merci, je préfère être au fond."
                    show ryou normal
                    r "Ah... Bah, à plus tard !"
                    hide ryou with easeoutright
                    "Le cour était vraiment ennuyeux."
                    "Mais c'est rassurant."
                    "Je n'ai pas accumulé énormément de retard lors de mon transfert."
                    jump day1_matin
        
label os:
    play sound "sound/bell.mp3"
    pause(1)
    play sound "sound/dooropen.mp3"
    scene couloir
    show ryou normal:
        left
    show elusia normal:
        right
    with fade
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
    scene couloir
    show ryou normal:
        left
    show elusia normal:
        right
    with fade
    r "Yo !"
    e "Salutations !"
    e "Bien dormi ?"
    m "Oui mais pas assez !"
    if rel_ryou == 7:
        show elusia satisfied
        e "Il ne fallait pas prendre de café..."
        e "Ca t'apprendra !"
    else:
        show ryou happy
        r "Pourtant, [sexe] a pris un thé."
        show elusia geez 
        e "A force de te gorger de caféine, tu y es immunisé."
        show ryou normal
        
    show elusia sad
    e "Bref, allons-y avant d'être en retard..."
    jump route1
    
label route1:
    scene street with fade
    "L'école est toute proche."
    scene classroom with fade
    "On s'est mis au premier rang."
    "Le cours était vraiment ennuyeux."
    "Mais c'est rassurant."
    "Je n'ai pas accumulé énormément de retard lors de mon transfert."
    
label day1_matin:
    
    "Etre au premier rang n'empêcha pas Ryouzanki de dormir."
    "Elusia a cependant l'air plus sérieuse."
    scene classroom with fade
    play music (matin1) fadein 2
    "Pendant que je range mes affaires à la fin du cours, ils viennent devant la table."
    show ryou normal at left with easeinleft
    show elusia normal at right with easeinright
    r "Tu fais quoi pour la pause de midi ?"
    m "Je vais au self."
    m "Comme tout le monde non ?"
    show ryou sad
    r "Bah..."
    show elusia satisfied
    e "Pas nous !"
    show elusia happy
    r "Il y a toujours une queue immense."
    e "Nous, on préfère acheter des sandwichs et aller déjeuner dans le parc."
    e "C'est nettement plus agréable !"
    if fille =='Jeune fille':
        show elusia normal
        e "Au fait, moi c'est Elusia !"
        $ fille = 'Elusia'
        e "Et toi ?"
        m "[j] !"
        e "Enchantée de faire ta connaissance [j] !"
        e "Je suis la voisine du dessous !"
    show ryou normal
    r "Tu veux venir manger avec nous ?"
    menu:
        "D'accord, ça m'a l'air sympa !":
            $ renpy.block_rollback()
            mh "D'accord, ça m'a l'air sympa !"
            show ryou happy
            show elusia happy
            r "C'est réglé alors !"
            r "Amène toi !"
            $ rel_lulu += 6
            $ rel_ryou += 6
            jump manger_dehors
        "Heu, je suis un peu à sec en ce moment...":
            $ renpy.block_rollback()
            ma "Heu, je suis un peu à sec en ce moment..."
            show ryou sad
            r "Ah..."
            if rel_lulu >= 5:
                show elusia sad
                e "Ah mais si c'est simplement une question d'argent..."
                e "Je peux t'avancer !"
                menu:
                    "Refuser poliment":
                        $ renpy.block_rollback()
                        m "Non merci, c'est vraiment gentil."
                        m "Mais je ne peux pas accepter."
                        show elusia geez
                        e "Ah... Dommage."
                        r "Bon bah tant pis. On se voit après la pause !"
                        hide ryou
                        show elusia sad
                        e "Bon appétit."
                        m "Merci !"
                        hide elusia
                        $ rel_lulu += 2
                        jump RU
                    "Accepter l'avance d'Elusia":
                        $ renpy.block_rollback()
                        mh "Oh vraiment, merci !"
                        show elusia satisfied
                        e "Tout le plaisir est pour moi voyons !"
                        show elusia normal
                        show ryou happy
                        r "Ah ouais ? Tu veux bien payer pour moi aussi ?"
                        show elusia geez
                        e "Même pas en rêve !"
                        $ rel_lulu += 2
                        $ rel_ryou +=5
                        jump manger_dehors
                    "Accepter de venir mais payer.":
                        $ renpy.block_rollback()
                        mh "Oh, vraiment, merci !"
                        m "Je vais venir mais je ne veux pas que tu m'avances."
                        show elusia satisfied
                        e "Comme tu voudras !"
                        show ryou happy
                        r "Moi je veux bien que~"
                        show elusia geez
                        e "Même pas en rêve !"
                        $ rel_lulu += 5
                        $ rel_ryou += 5
                        jump manger_dehors
            else:
                show elusia geez
                e "Ah... Dommage."
                r "Bon bah tant pis. On se voit après la pause !"
                hide ryou
                show elusia sad
                e "Bon appétit."
                m "Merci !"
                hide elusia
                jump RU
                
label manger_dehors:
    scene parc
    show elusia happy:
        right
    show ryou happy:
        left
    with fade
    "Nous sommes allés au parc."
    "Il faisait beau et nous avons mangé nos sandwichs en papotant, assis dans l'herbe."
    r "... C'était donc une si grande ville que ça..."
    show ryou surprised
    r "Désolé, ici c'est plutôt petit et y'a pas grand chose à faire."
    "Ils m'ont surtout posé des questions sur l'endroit d'où je viens."
    "C'était très agréable."
    jump cours22
    
label RU:
    scene ru with fade
    "Je suivis les flux d'étudiants pour trouver le self."
    "Alors que je mangeais à ma table en solitaire..."
    show laura normal with easeinleft
    l "T'es tout seul ? On peut se mettre là ?"
    menu:
        "Oui, bien sûr !":
            $ renpy.block_rollback()
            m "Oui, bien sûr !"
            $ rel_lolo += 2
            jump RUU
        "Non, j'attends quelqu'un.":
            $ renpy.block_rollback()
            m "Non, j'attends quelqu'un."
            show laura angry
            "Elle resta devant moi un moment, sceptique."
            "Puis, rejoins par un garçon, ils partirent."
            hide laura with easeoutright
            jump cours2
        "Non, je préfère rester seul[ter].":
             $ renpy.block_rollback()
             m "Non, je préfère rester seul[ter]."
             show laura angry
             "Elle pose son plateau."
             ma "Hey !"
             l "Ce n'était pas une question !"
             ma "Bien sur que si !"
             jump RUU
             
label RUU:
    show laura happy at left with move
    l "Valeth ! Par ici !"
    show valeth normal at right with easeinright
    v "Oui, oui, j'arrive !"
    v "Salut toi !"
    v "Je suis dans ta classe, j'étais assis à l'autre bout du rang !"
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
            $ renpy.block_rollback()
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
            $ rel_lolo += 5
            jump cours2
        "N'exagérons rien...":
            $ renpy.block_rollback()
            m "N'exagérons rien..."
            show laura angry at left
            l "Je n'exagère rien !"
            l "Cette manie de demander si le prof a besoin d'un coup de main..."
            l "Ca me mets hors de moi !"
            "Je passais le reste de ma pause à entendre Laura se plaindre à propos d'Elusia."
            "C'était aussi amusant qu'embarassant."
            $ rel_lolo += 2
            jump cours2
        "Je ne la connais pas.":
            $ renpy.block_rollback()
            m "Je ne la connais pas."
            show laura angry at left
            l "Quand ce sera le cas, tu comprendra !"
            v "Enfin, [sexe] vient d'arriver..."
            v "Laisse lui le temps de~"
            show laura angry at left
            l "Comprendre Elusia ? Il n'y a rien à comprendre."
            l "Je la hais !"
            "Je passais le reste de ma pause à entendre Laura se plaindre à propos d'Elusia."
            "C'était aussi amusant qu'embarassant."
            jump cours2
            
label cours22:
    play music (jour1) fadein 2
    scene black with fade
    "La pause de midi est terminée."
    "Il faut retourner en cours..."
    scene classroom with fade
    "Nous avons discrètement bavardé des plats que l'on savait cuisiner."
    jump fin_cours
    
label cours2:
    play music (jour1) fadein 2
    scene black with fade
    "La pause de midi est terminée."
    "Il faut retourner en cours..."
    scene classroom with fade
    "En entrant dans la salle, j'aperçois Ryouzanki et Elusia au premier rang."
    if rel_lolo > 0:
        "Et aussi Laura et Valeth au fond de la classe."
        "Je pourrais m'assoir avec ..."
        menu:
            "Laura et Valeth.":
                $ renpy.block_rollback()
                jump LV
            "Elusia et Ryouzanki.":
                $ renpy.block_rollback()
                jump RZ
            "Personne.":
                $ renpy.block_rollback()
                "Le cours est vraiment ennuyeux..."
                jump fin_cours
                
    else:
        "Je pourrais m'assoir avec eux..."
        menu:
            "Oui.":
                $ renpy.block_rollback()
                jump RZ
            "Non.":
                $ renpy.block_rollback()
                "Le cours est vraiment ennuyeux..."
                jump fin_cours

label RZ:
    show ryou sad at left
    show elusia normal at right
    r "Reuh !"
    m "Heu... Re !"
    e "Bien mangé ?"
    m "Oui, ça va, et vous ?"
    show elusia satisfied
    e "Perfecto !"
    show elusia normal
    show ryou happy
    r "Je dirais même plus, Elusia, perfectissimo !"
    show ryou normal
    r "Honnêtement, la prochaine fois, tu devrais venir avec nous !"
    e "D'ailleurs, on a parlé des clubs en pensant à toi."
    e "As tu songé à joindre un club ?"
    menu :
        "Pas pour le moment non.":
            $ renpy.block_rollback()
            m "Pas pour le moment non."
            e "Ah... Dommage."
            r "Quand tu changera d'avis, le bâtiment des clubs, c'est le gros en rouge."
            m "D'accord."
        "Oui, le plus tôt sera la mieux !":
            $ renpy.block_rollback()
            mh "Oui, le plus tôt sera la mieux !"
            r "Le bâtiment des clubs, c'est le gros en rouge !"
            r "Les inscriptions doivent être encore ouverte mais dépêches toi."
            m "D'accord !"
            e "Après les cours bien sur."
    show elusia satisfied
    e "Sinon, si tu veux un club de sport, je t'attends cet après-midi au gymnase."
    show ryou sad
    r "Le sport ça intéresse personne..."
    
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
            $ renpy.block_rollback()
            m "Pas pour le moment non."
            v "Ah... Dommage."
            v "Quand tu changera d'avis, le bâtiment des clubs, c'est le gros en rouge."
            m "D'accord."
            show valeth happy at right
            v "J'y suis presque tous les soirs."
        "Oui, le plus tôt sera la mieux !":
            $ renpy.block_rollback()
            mh "Oui, le plus tôt sera la mieux !"
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
                $ renpy.block_rollback()
                m "Non merci, je préfère les clubs calmes"
                show laura sad at left
                l "Tsss... Comme tu voudra !"
                $ rel_val += 2
            "Oui, je peux faire les deux.":
                $ renpy.block_rollback()
                m "Oui, je peux faire les deux."
                show laura normal at left
                l "Eventuellement, tu peux alterner."
                $ rel_lolo += 2
            "Ah oui, je préfère largement les clubs de sport !":
                $ renpy.block_rollback()
                mh "Ah oui, je préfère largement les clubs de sport !"
                l "Tiens ! Dans les dents, l'intello !"
                show valeth angry at right
                v "..."
                $ rel_lolo += 5
                $ rel_val -= 3
    else:
        menu:
            "Je n'ai pas le temps pour le moment.":
                $ renpy.block_rollback()
                m "Je n'ai pas le temps pour le moment."
                show laura sad at left
                l "OK, tant pis."
            "Bon, va pour le sport.":
                $ renpy.block_rollback()
                m "Bon, va pour le sport."
                show laura happy at left
                l "Super, je t'attends ce soir pour ton inscription."
                l "Tout ce que tu veux, sauf tennis et tir à l'arc."
                show valeth happy at right
                v "Ha ha..."
                $ rel_lolo += 5
    jump fin_cours
    
label fin_cours:
    "Le cours se déroula sans encombre."
    play music (prof1) fadein 2
    scene classroom with fade
    show prof happy with easeinleft
    "Le professeur me barre la route avant que je ne sorte de la salle."
    p "Alors [j], est-ce que tout se passe bien ?"
    p "Avez vous des difficultés à vous intégrer ?"
    m "Heu non, tout va bien..."
    "Il est débile ou quoi ?"
    "Pourquoi il me demande ça le premier jour ?"
    menu:
        "C'est pas un peu tôt pour demander ?":
            m "C'est pas un peu tôt pour demander ?"
            p "Je fais simplement mon devoir de prof."
            p "Je dois vous poser cette question."
            m "Oui mais pourquoi maintenant ?"
            p "Parce que vous ne pouvez pas me répondre que ça va mal dès le premier jour."
            m "Ah..."
        "...":
            m "..."
    p "N'oubliez pas de vous inscrire à un club de sport."
    p "On ne peut en choisir qu'un mais c'est obligatoire."
    m "Oui monsieur."
    show prof normal at left with move
    p "Vous pouvez y aller."
    m "Merci. Au revoir."
    stop music fadeout 2.0
    scene classroom with fade
    "Il est vraiment bizarre ce type..."
    "Dire que je devrais le supporter tout un semestre..."
    "..."
    play music (jour1) fadein 2
    "Tout le monde est parti."
    "Où pourrais-je bien aller ?"
    window hide None
    call screen demo_imagemap
    window show None
        
    if _return == "gymnase":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "Et si j'allais faire un peu de sport..."
        call sport
    
    elif _return == "science":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "J'ai cru voir de l'agitation dans le bâtiment des sciences."
        "Il y a peut être des clubs là bas..."
        call labo
        
    elif _return == "art":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "Et si j'allais faire un tour au bâtiments des clubs..."
        call club

    elif _return == "rentrer":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "Je crois que je vais rentrer."
        call go_home
        
        
label day1_fin:
    play music (joueur1) fadein 2
    scene couloir with fade
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    "Et ce n'est que le premier jour..."
    scene chambre m with fade
    play sound "sound/doorclose.mp3"
    "Je crois que je vais dormir."
    stop music
    return
