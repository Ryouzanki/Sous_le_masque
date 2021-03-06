label day2:
    scene reveil with fade
    play sound "sound/clock.mp3"
    m "..."
    m "J'ai pu récupérer un peu de sommeil..."
    stop sound
    play music (joueur1) fadein 2
    m "Allons, c'est l'heure !"
    
    if rel_ryou >= 5:
        jump day2_ER
    else:
        jump day2_autre
        
label day2_autre:
    "Mes préparatifs terminés, je sors."
    play sound "sound/doorclose.mp3"
    scene couloir with fade
    "C'est ennuyeux d'y aller seul."
    scene street with fade
    "Ryouzanki m'aborde."
    "Ils étaient juste derrière moi."
    jump route_d2
        
label day2_ER:
    play sound "sound/bell.mp3"
    pause(1)
    play sound "sound/dooropen.mp3"
    scene couloir with fade
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
        show ryou surprised
        r "Je suis Dieu voyons, je sais tout !"
        show elusia geez
        e "Dieu, il a quand même oublié de se lever..."
        show ryou normal
        menu:
            m "Le club de science..."
            "Je vais essayer de m'y inscrire aujourd'hui.":
                # $ renpy.block_rollback()
                show elusia normal
                show ryou normal
                m "Je vais essayer de m'y inscrire aujourd'hui."
                r "Oh, c'est bien !"
                r "Y'a rien a foutre dans cette petite ville."
                r "Il faut trouver de quoi s'occuper."
                e "Le club de robotique à une très bonne réputation !"
                show elusia satisfied
                e "Je viendrais pour vérifier que tu ne manques pas à ta parole !"
                show elusia sad
                e "Nous devrions y aller avant d'être en retard !"
            "Je ne risque pas d'y revenir...":
                # $ renpy.block_rollback()
                m "Je ne risque pas d'y revenir..."
                show ryou sad
                r "Dommage, c'est pourtant un excellent club, avec une bonne ambiance."
                show ryou happy
                r "Et une présidente plutot craquante !"
                show elusia geez
                e "Misère..."
                show elusia sad
                e "Non, vraiment [j], tu devrais songer à intégrer un club."
                show elusia normal
                e "Je vais t'accompagner pour en chercher un qui te convienne."
                r "Clair, c'est une petite ville ici."
                r "Il n'y a rien de bien passionant à faire."
                show elusia satisfied
                e "Le club de robotique à une très bonne réputation !"
                show elusia sad
                e "Nous devrions y aller avant d'être en retard !"
        jump day2_matin
    elif aller_art == 1:
        r "Alors, t'as fait la rencontre de ce cher Valeth ?"
        m "Comment tu sais ?"
        show ryou surprised
        r "Je suis Dieu, je sais tout..."
        show elusia satisfied
        e "Ce n'est pas ce que prouvent tes notes..."
        show ryou angry
        r "Je ne fais que m'abaisser au niveau des mortels !"
        show ryou surprised
        r "As tu joué aux échecs contre lui ?"
        menu:
            "J'ai perdu.":
                # $ renpy.block_rollback()
                m "J'ai perdu."
                show ryou happy
                r "C'est pas grave, tu n'as qu'à retenter ce soir !"
                e "Oui, c'est ouvert tous les soirs."
                show elusia geez
                e "Et c'est plus sain que les jeux vidéos..."
                show elusia sad
                show ryou normal
                r "Pourquoi tu me regardes ainsi ?"
                show elusia normal
                e "Rien rien... Allons voir [j] jouer ce soir..."
                r "D'accord."
            "J'ai gagné...":
                # $ renpy.block_rollback()
                m "J'ai gagné..."
                show ryou happy
                show elusia surprised
                r "Quoi ? Sérieusement ?"
                e "Wouah, tu es vraiment très impressionant[ter] !"
                r "Je suis libre ce soir, je viendrais constater que ce n'était pas de la chance !"
                e "Je viendrais aussi, si ça ne dérange personne."
                "Heu..."
            "Je n'ai pas joué contre lui.":
                # $ renpy.block_rollback()
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
        r "Quoi, qu'est-ce qui te fait dire ça ?"
        show elusia geez
        e "Tu as des cernes si marquées qu'on dirait du maquillage..."
        show ryou normal
        show elusia sad
        r "Mais non. Demande à [j] !"
        e "[j] ?"
        m "Je suis rentré[ter] tôt."
        show elusia geez
        e "Donc tu as bien joué tout seul toute la nuit puisque j'entendais du bruit..."
        show elusia sad
        show ryou angry
        r "Traître !"
        e "Tes notes ne sont plus extras, il faudrait te mettre à travailler."
        r "Pourquoi ? Si j'ai mon semestre, c'est l'essentiel non ?"
        show elusia geez
        e "Si tu l'as..."
        show elusia normal
        e "Qu'importe. [j], ne deviens pas comme lui."
        e "Inscris toi à un club."
        m "Lequel ?"
        show elusia happy
        e "Peu importe."
        show elusia normal
        e "Bon, on devrait commencer à marcher en discutant ou on sera en retard."
        jump day2_matin
        
    elif sport != 'aucun':
        r "Alors le [sport], c'était comment ?"
        show elusia sad
        e "Mais... D'où tu sors ça ?"
        show ryou surprised
        r "J'ai des informateurs..."
        m "C'était assez fun mais je n'ai pas fait de sport depuis un bout de temps..."
        show ryou happy
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
        show elusia geez
        e "Dis celui qui passe son temps sur les consoles !"
        show ryou angry
        show elusia normal
        r "Hey, c'est pas vrai !"
        e "[j], tu devrais songer à participer à la vie associative de l'école."
        show elusia satisfied
        e "Tu verra, c'est très plaisant !"
        show elusia normal
        e "Bon, on devrait commencer à marcher en discutant ou on sera en retard."
        jump day2_matin
        
label day2_matin:
    scene street with fade
    scene classroom with fade
    "Encore un cours à suivre avec Elusia pendant que Ryouzanki dort."
label day2_midi:
    play music (matin1) fadein 2
    scene classroom 
    show ryou sad:
        left
    show elusia normal:
        right
    with fade
    r "Bon ! J'ai faim !"
    e "Oui, moi aussi. On va acheter des sandwichs ?"
    r "Bien sûr ! Tu viens [j] ?"
    menu:
        "Bien entendu !":
            # $ renpy.block_rollback()
            m "Bien entendu !"
            show ryou happy at left
            show elusia happy at right
            r "C'est réglé alors !"
            r "Amène toi !"
            if rel_lloy >= 5:
                show lloyd normal with easeinleft
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
                        # $ renpy.block_rollback()
                        m "Il y avait de quoi..."
                        $ rel_lloy += 2
                        show lloyd happy
                        y "C'est exact."
                        y "Madame la présidente sera là cet après midi si tu veux."
                    "T'en fais pas.":
                        # $ renpy.block_rollback()
                        m "T'en fais pas."
                        
                y "Je vais rentrer chez moi déjeuner."
                y "A plus tard !"
                m "Bon appétit !"
                hide lloyd with easeoutright
            $ rel_lulu += 4
            $ rel_ryou += 4
            scene parc
            show elusia happy:
                right
            show ryou happy:
                left
            with fade
            "Nous sommes allés au parc."
            "Il faisait beau et nous avons mangé nos sandwichs en papotant, assis dans l'herbe."
            "Ils m'ont surtout parlé de cette école."
            if rel_lloy >= 5:
                "J'en sais un peu plus sur Lloyd."
                "Il n'est pas très apprécié car il a un air hautain."
            "C'était très agréable."
            "Ryouzanki est rentré chez lui prendre ses affaires."
            hide ryou with easeoutright
            e "Va directement en cours. Je m'en voudrais si tu arrivais en retard."
            "Elusia est partie l'accompagner."
            hide elusia with easeoutright
            "Ces deux là s'entendent bien."
            jump day2_cours2
        "Nan, je vais au self aujourd'hui.":
            # $ renpy.block_rollback()
            r "Ok, bah à plus !"
            e "On se voit plus tard !"
            hide ryou
            hide elusia
            with easeoutright
            if rel_lloy >= 5:
                show lloyd normal with easeinleft
                y "Bonjour !"
                m "Salut !"
                y "Pardonnes moi d'avoir été désagréable hier."
                y "Je n'étais pas dans mon assiette."
                menu:
                    "Il y avait de quoi...":
                        # $ renpy.block_rollback()
                        m "Il y avait de quoi..."
                        $ rel_lloy += 2
                        show lloyd happy
                        y "C'est exact."
                        y "Madame la présidente sera là cet après midi si tu veux."
                    "T'en fais pas.":
                        # $ renpy.block_rollback()
                        m "T'en fais pas."
                        
                y "Je vais rentrer chez moi déjeuner."
                y "A plus tard !"
                m "Bon appétit !"
                hide lloyd with easeoutright
            m "..."
            show valeth normal:
                left
            show laura normal:
                right
            with easeinleft
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
                v "Plutot que de manger seul[ter]."
                v "Tu veux te joindre à nous [j] ?"
            elif en == 'Jeune fille' and valou == 'Valeth':
                v "Salut [j] !"
                m "Bonjour Valeth !"
                v "Je te présente Laura !"
                $ en = 'Laura'
                l "Yo !"
                v "Plutot que de manger seul[ter]."
                v "Tu veux te joindre à nous [j] ?"
            else:
                v "Salut !"
                l "[j] ! Tu viens manger avec nous ?"
                
            menu:
                  "Refuser":
                      # $ renpy.block_rollback()
                      m "Non merci, je préfère rester seul."
                      $rel_val -=1
                      $ rel_lolo -= 2
                      v "Ah... Bon bah, à tout à l'heure."
                      l "..."
                      scene ru with fade
                      "Pourquoi est-ce que j'ai refusé d'ailleurs..."
                      jump day2_cours2
                  "Accepter":
                      # $ renpy.block_rollback()
                      $rel_val +=5
                      $ rel_lolo += 5
                      mh "OK."
                      v "Très bien."
                      l "Allons y !"
                      scene ru
                      show valeth normal:
                          left
                      show laura normal:
                          right
                      with fade
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
                      hide valeth with easeoutright
                      l "Je dois passer à la poste acheter des timbres"
                      l "Tu devrais aller en cours tout de suite."
                      hide laura with easeoutright

                      jump day2_cours2
                          
                          
label day2_cours2:
    play music (jour1) fadein 2
    scene black with fade
    "La pause de midi est terminée."
    "Il faut retourner en cours..."
    scene classroom with fade
    "Des visages familiers..."
    menu:
        "Et si j'allais voir..."
        "Ryouzanki et Elusia.":
                # $ renpy.block_rollback()
                show ryou sad at left
                show elusia normal at right
                "Le cours a été suivit en silence."
                "Il est rare de voir Ryouzanki suivre un cours avec une telle attention..."
                $ rel_lulu += 2
                $ rel_ryou += 2
                jump day2_cours3
        "Lloyd."if rel_lloy >= 5:
            # $ renpy.block_rollback()
            show lloyd normal
            m "Re !"
            y "Re-bonjour [j]."
            show lloyd angry
            $ rel_lloy +=3
            "Lloyd n'est pas très causant."
            "Il suit le cours et regarde d'un air menaçant ceux qui parlent."
            jump day2_cours3
            
        "Laura et Valeth."if en != 'Jeune fille' and valou != 'Jeune homme':
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
            jump day2_cours3
    
label day2_cours3:
    scene classroom with fade
    play music (prof1) fadein 2
    show prof normal with easeinleft
    p "[j]..."
    p "Hier j'ai oublier de vous dire que les clubs sont ouvert tous les jours."
    p "Sauf le sport qui n'est ouvert que lundi et jeudi."
    "Ces choses sont marquées sur des panneaux en face des bâtiments en questions."
    p "Sur ce, bonne journée."
    hide prof with easeoutright
    "Tout le monde est parti."
    if sport == 'aucun':
        show prof normal with easeinright
        p "J'oubliais..."
        p "Vous n'êtes pas allé[ter] en sport hier."
        p "Il faut vous inscrire le plus tôt possible."
        p "C'est à dire jeudi dans notre cas."
        p "Je n'ai pas l'intention de vous fliquer."
        p "Vous êtes censé[ter] être assez grand[ter] pour y aller avant d'avoir 0."
        m "Oui monsieur."
        hide prof with easeoutright
    play music (jour1) fadein 2
    "Que faire...."
label day2_passport:
    window hide None
    call screen demo_imagemap
    window show None
        
    if _return == "gymnase":
        # $ renpy.block_rollback()
        "Il n'y a pas sport aujourd'hui..."
        jump day2_passport
    
    elif _return == "science":
        # $ renpy.block_rollback()
        if aller_science == 1:
            "Allons nous inscire..."
        else:
            "J'ai cru voir de l'agitation dans le bâtiment des sciences."
            "Il y a peut être des clubs là bas..."
        call labo
        
    elif _return == "art":
        # $ renpy.block_rollback()
        if aller_art == 1:
            "Allons tenter de battre Valeth !"
        else:
            "Et si j'allais faire un tour au bâtiments des clubs..."
        call club

    elif _return == "rentrer":
        # $ renpy.block_rollback()
        
        "Je crois que je vais rentrer."
        call go_home
        
        
label day2_fin:
    play music (joueur1) fadein 2
    scene couloir with fade
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    "2 eme jour fini."
    scene chambre m with fade
    play sound "sound/doorclose.mp3"
    "Je vais dormir tôt."
    stop music
    return
    
