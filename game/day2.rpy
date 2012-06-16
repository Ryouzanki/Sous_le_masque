label day2:
    scene reveil with dissolve
    play sound "sound/clock.mp3"
    m "..."
    m "J'ai pu récupérer un peu de sommeil..."
    stop sound
    $ renpy.music.play("music/joueur.ogg", fadein=2)
    m "Allons, c'est l'heure !"
    
    if rel_ryou >= 5:
        jump day2_ER
    else:
        jump day2_autre
        
label day2_autre:
    "Mes préparatifs terminés, je sors."
    play sound "sound/doorclose.mp3"
    scene black with dissolve
    scene couloir with dissolve
    "C'est ennuyeux d'y aller seul."
    scene street with dissolve
    "Ryouzanki m'aborder."
    "Ils étaient juste derrière moi."
    jump route_d2
        
label day2_ER:
    play sound "sound/bell.mp3"
    pause(1)
    play sound "sound/dooropen.mp3"
    scene black with dissolve
    scene couloir with dissolve
label route_d2:
    show ryou normal at left
    show elusia normal at right
    r "Yo !"
    e "Salutations !"
    r "T'en as mis du temps à sortir !"
    "Je crois que maintenant, ils vont venir me chercher tous les jours..."
    if aller_science == 1:
        r "Alors le club des grosses têtes, c'était comment ?"
        m "De quoi ?"
        r "Le club de science ! Tu y es allé[ter] hier non ?"
        m "Comment tu sais ?"
        show ryou happy
        r "Je suis Dieu voyons, je sais tout !"
        show elusia sad
        e "Dieu, il a quand même oublié de se lever..."
        menu:
            m "Le club de science..."
            "Je vais essayer de m'y inscrire aujourd'hui.":
                show elusia normal
                show ryou normal
                m "Je vais essayer de m'y inscrire aujourd'hui."
                r "Oh, c'est bien !"
                r "Y'a rien a foutre dans cette petite ville."
                r "Il faut trouver de quoi s'occuper."
                e "Le club de robotique à une très bonne réputation !"
                show elusia happy
                e "Je viendrais pour vérifier que tu ne manques pas à ta parole !"
                e "Nous devrions y aller avant d'être en retard !"
            "Je ne risque pas d'y revenir...":
                m "Je ne risque pas d'y revenir..."
                show ryou sad
                r "Dommage, c'est pourtant un excellent club, avec une bonne ambiance."
                show ryou happy
                r "Et une présidente plutot craquante !"
                e "Misère..."
                e "Non, vraiment [j], tu devrais songer à intégrer un club."
                e "Je vais t'accompagner pour en chercher un qui te convienne."
                r "Clair, c'est une petite ville ici."
                r "Il n'y a rien de bien passionant à faire."
                show elusia normal
                e "Le club de robotique à une très bonne réputation !"
                e "Nous devrions y aller avant d'être en retard !"
        jump day2_matin
    elif aller_art == 1:
        r "Alors, t'as fait la rencontre de ce cher Valeth ?"
        m "Comment tu sais ?"
        show ryou happy
        r "Je suis Dieu, je sais tout..."
        show elusia happy
        e "Ce n'est pas ce que prouvent tes notes..."
        show ryou angry
        r "Je ne fais que m'abaisser au niveau des mortels !"
        r "As tu joué aux échecs contre lui ?"
        menu:
            "J'ai perdu.":
                m "J'ai perdu."
                show ryou happy
                r "C'est pas grave, tu n'as qu'à retenter ce soir !"
                e "Oui, c'est ouvert tous les soirs."
                show elusia sad
                e "Et c'est plus sain que les jeux vidéos..."
                show ryou normal
                r "Pourquoi tu me regardes ainsi ?"
                e "Rien rien... Allons voir [j] jouer ce soir..."
                r "D'accord."
            "J'ai gagné...":
                m "J'ai gagné..."
                show ryou happy
                show elusia happy
                r "Quoi ? Sérieusement ?"
                e "Wouah, tu es vraiment très impressionant[ter] !"
                r "Je suis libre ce soir, je viendrais constater que ce n'était pas de la chance !"
                e "Je viendrais aussi, si ça ne dérange personne."
                "Heu..."
            "Je n'ai pas joué contre lui.":
                m "Je n'ai pas joué contre lui."
                r "Dommage."
                e "C'est son jeu favori et il est vraiment très très fort."
                r "Le numéro uno de l'école !"
                r "Tu devrais essayer pour voir."
                r "Ce soir je suis libre, je viendrais te voir perdre."
                e "C'est pas gentil de dire ça !"
                r "Valeth n'a jamais perdu. C'est simplement la vérité."
                
        e "Bon, on devrait commencer à marcher en discutant ou on sera en retard."
        jump day2_matin
                
    elif aller_home == 1:
        show elusia sad
        e "Vous n'auriez pas jouer à la console toute la nuit hier quand même ?"
        show ryou happy
        r "Quoi, qu'est-ce qui te fais dire ça ?"
        e "Tu as des cernes si marquées qu'on dirait du maquillage..."
        show ryou normal
        r "Mais non. Demande à [j] !"
        e "[j] ?"
        m "Je suis rentré[ter] tôt."
        e "Donc tu as joué toute la nuit..."
        show ryou angry
        r "Traître !"
        e "Tes notes ne sont plus extras, il faudrait te mettre à travailler."
        r "Pourquoi ? Si j'ai mon semestre, c'est l'essentiel non ?"
        e "Si tu l'as..."
        show elusia normal
        e "Qu'importe. [j], ne deviens pas comme lui."
        e "Inscrit toi à un club."
        m "Lequel ?"
        e "Peu importe."
        e "Bon, on devrait commencer à marcher en discutant ou on sera en retard."
        jump day2_matin
        
    elif sport != 'aucun':
        r "Alors le [sport], c'était comment ?"
        show elusia sad
        e "Mais... D'où tu sors ça ?"
        show ryou happy
        r "J'ai des informateurs..."
        m "C'était assez fun mais je n'ai pas fait de sport depuis un bout de temps..."
        r "Dur la reprise hein..."
        show elusia happy
        e "Dit celui qui séche tous les cours de sport..."
        show ryou happy
        r "Je sèche pas, je reste chez moi, à l'ombre !"
        show elusia normal
        e "C'est la même chose."
        e "Bon, on devrait commencer à marcher en discutant ou on sera en retard."
        jump day2_matin
        
    else:
        r "Bon..."
        r "Il va falloir que tu t'intègres vite !"
        show elusia happy
        e "Dis celui qui passe son temps sur les consoles !"
        show ryou angry
        r "Hey, c'est pas vrai !"
        e "[j], tu devrais songer à participer à la vie associative de l'école."
        e "Tu verra, c'est très plaisant !"
        show elusia normal
        e "Bon, on devrait commencer à marcher en discutant ou on sera en retard."
        jump day2_matin
        
label day2_matin:
    scene street with dissolve
    pause(1)
    scene black with dissolve
    scene classroom with dissolve
    hide ryou
    hide elusia
    "Encore un cours à suivre avec Elusia pendant que Ryouzanki dors."
label day2_midi:
    scene black with dissolve
    pause(1)
    scene classroom with dissolve
    $ renpy.music.play("music/matin.ogg", fadein=2)
    show ryou sad at left
    show elusia normal at right
    r "Bon ! J'ai faim !"
    e "Oui, moi aussi. On va acheter des sandwichs ?"
    r "Bien sûr ! Tu viens [j] ?"
    menu:
        "Bien entendu !":
            m "Bien entendu !"
            show ryou happy at left
            show elusia happy at right
            r "C'est réglé alors !"
            r "Amène toi !"
            if rel_lloy >= 5:
                show lloyd normal
                show elusia normal
                show ryou normal
                y "Bonjour !"
                e "Bonjour Lloyd."
                r "Yo !"
                m "Salut !"
                y "Pardonnes moi d'avoir été désagréable hier."
                y "Je n'étais pas dans mon assiette."
                menu:
                    "Il y avait de quoi...":
                        m "Il y avait de quoi..."
                        $ rel_lloy += 2
                        show lloyd happy
                        y "C'est exact."
                        y "Madame la présidente sera là cet après midi si tu veux."
                    "T'en fais pas":
                        m "T'en fais pas"
                        
                y "Je vais rentrer chez moi déjeuner."
                y "A plus tard !"
                m "Bon appétit !"
                hide lloyd
            $ rel_lulu += 4
            $ rel_ryou += 4
            scene parc with dissolve
            show elusia happy at right
            show ryou happy at left
            "Nous sommes allés au parc."
            "Il faisait beau et nous avons mangé nos sandwichs en papotant, assis dans l'herbe."
            "Ils m'ont surtout posé des questions sur l'endroit d'où je viens."
            if rel_lloy >= 5:
                "J'en sais un peu plus sur Lloyd."
                "Il n'est pas très apprécié car il a un air hautain."
            "C'était très agréable."
            "Ryouzanki est rentré chez lui prendre ses affaires."
            hide ryou
            e "Va directement en cours. Je m'en voudrais si tu arrivais en retard."
            "Elusia est partie l'accompagner."
            hide elusia
            "Ces deux là s'entendent bien."
            jump day2_cours2
        "Nan, je vais au RU aujourd'hui.":
            r "Ok, bah à plus !"
            e "On se voit plus tard !"
            hide ryou
            hide elusia
            if rel_lloy >= 5:
                show lloyd normal
                y "Bonjour !"
                m "Salut !"
                y "Pardonnes moi d'avoir été désagréable hier."
                y "Je n'étais pas dans mon assiette."
                menu:
                    "Il y avait de quoi...":
                        m "Il y avait de quoi..."
                        $ rel_lloy += 2
                        show lloyd happy
                        y "C'est exact."
                        y "Madame la présidente sera là cet après midi si tu veux."
                    "T'en fais pas":
                        m "T'en fais pas"
                        
                y "Je vais rentrer chez moi déjeuner."
                y "A plus tard !"
                m "Bon appétit !"
                hide lloyd
                    
            show valeth normal at left
            show laura normal at right
            if en == 'Jeune fille' and valou == 'Jeune homme':
                v "Hey ! Salut !"
                v "Moi c'est Valeth !"
                $ valou = 'Valeth'
                l "Et moi Laura !"
                $ en = 'Laura'
                v "Plutot que de manger seul[ter]"
                v "Tu veux te joindre à nous [j] ?"
                m "Comment vous..."
                show laura happy
                l "Ton nom était sur la feuille d'appel."
                show laura normal
            elif en == 'Laura' and valou == 'Jeune homme':
                l "Salut [j] !"
                m "Bonjour Laura !"
                l "Je te présente Valeth !"
                $ valou = 'Valeth'
                v "Yo !"
                v "Plutot que de manger seul[ter]"
                v "Tu veux te joindre à nous [j] ?"
            elif en == 'Jeune fille' and valou == 'Valeth':
                v "Salut [j] !"
                m "Bonjour Valeth !"
                v "Je te présente Laura !"
                $ en = 'Laura'
                l "Yo !"
                v "Plutot que de manger seul[ter]"
                v "Tu veux te joindre à nous [j] ?"
            else:
                v "Salut !"
                l "[j] ! Tu viens manger avec nous ?"
                
            menu:
                  "Refuser":
                      m "Non merci, je préfère rester seul."
                      $rel_val -=1
                      $ rel_lolo -= 2
                      v "Ah... Bon bah, à tout à l'heure."
                      l "..."
                      hide laura
                      hide valeth
                      scene ru with dissolve
                      "Pourquoi est-ce que j'ai refusé d'ailleurs..."
                      jump day2_cours2
                  "Accepter":
                      $rel_val +=5
                      $ rel_lolo += 5
                      m "OK."
                      v "Très bien."
                      l "Allons y !"
                      scene ru with dissolve
                      show valeth normal at left
                      show laura normal at right
                      if rel_lloy >= 5:
                          v "D'ailleurs, on a vu Lloyd venir vers toi."
                          m "Heu... C'est si spécial ?"
                          l "D'habitude, il ne nous parle pas à nous, roturiers !"
                          v "Il t'a dit quoi ?"
                          m "Il est juste venu s'excuser."
                          l "Oh, pas très fréquent de sa part..."
                          v "Oui, ce n'est pas courant."
                          "Nous avons passé le reste du repas à parler de Lloyd."
                          "Laura médit sur lui pendant que Valeth essaie de la tempérer."
                      else:
                          "J'ai passé tout le repas à les écouter se chamailler."
                          "Laura médit sur les profs pendant que Valeth essaie de la tempérer."
                      "C'était divertissant."
                      v "Bon, j'ai des affaires à régler pour le club d'art."
                      v "Si vous voulez bien m'excusez !"
                      hide valeth
                      l "Je dois passer à la poste acheter des timbres"
                      l "Tu devrais aller en cours tout de suite."
                      hide laura

                      jump day2_cours2
                          
                          
label day2_cours2:
    $ renpy.music.play("music/jour.ogg", fadein=2)
    scene black with dissolve
    "La pause de midi est terminée."
    "Il faut retourner en cours..."
    scene classroom with dissolve
    "Des visages familiers..."
    menu:
        "Et si j'allais voir..."
        "Ryouzanki et Elusia.":
                show ryou sad at left
                show elusia normal at right
                "Le premier rang n'est pas aussi désagréable que ça..."
                "C'est amusant d'empêcher Ryouzanki de dormir en lui pinçant les côte..."
                hide elusia
                hide ryou
                $ rel_lulu += 2
                $ rel_ryou += 2
                jump day2_cours3
        "Lloyd." if rel_lloy >= 5:
            show lloyd normal
            m "Re !"
            y "Re-bonjour [j]."
            show lloyd angry
            $ rel_lloy +=3
            "Lloyd n'est pas très causant."
            "Il suit le cours et regarde d'un air menaçant ceux qui parlent."
            hide lloyd
            jump day2_cours3
            
        "Laura et Valeth." if en != 'Jeune fille' and valou != 'Jeune homme':
            show valeth normal at left
            show laura normal at right
            "Toujours à se chamailler ces deux là."
            if noble == 'Lloyd':
                "Laura qui dit du mal de Lloyd"
            else:
                "Laura qui dit du mal d'un certain Lloyd"
            "A propos d'air supérieur et ce genre de chose."
            "Et Valeth qui la calme."
            $ rel_lolo += 2
            $ rel_val += 2
            hide valeth
            hide laura
            jump day2_cours3
    
label day2_cours3:
    show prof normal
    "A la fin de cours, le prof m'a encore retenu[ter]."
    "Cette fois pour me dire que les clubs sont ouvert tous les jours."
    "Sauf le sport qui n'est ouvert que lundi et jeudi."
    "Des choses qui sont marquées sur des panneaux en face des bâtiments en questions."
    hide prof
    "Tout le monde est parti."
    "A croire qu'il le fait exprès."
label day2_passport:
    window hide None
    call screen demo_imagemap
    window show None
        
    if _return == "swimming":
        "Il n'y a pas sport aujourd'hui..."
        jump day2_passport
    
    elif _return == "science":
        if aller_science == 1:
            "Allons nous inscire..."
        else:
            "J'ai cru voir de l'agitation dans le bâtiment des sciences."
            "Il y a peut être des clubs là bas..."
        call labo
        
    elif _return == "art":
        if aller_art == 1:
            "Allons tenter de battre Valeth !"
        else:
            "Et si j'allais faire un tour au bâtiments des clubs..."
        call club

    elif _return == "go home":
        
        "Je crois que je vais rentrer."
        call go_home
        
        
label day2_fin:
    $ renpy.music.play("music/joueur.ogg", fadein=2)
    scene couloir with dissolve
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    "2 eme jour fini."
    scene chambre m with dissolve
    play sound "sound/doorclose.mp3"
    "Je crois que je vais dormir."
    stop music
    return
    
