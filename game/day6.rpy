# TODO club_home et club_art
# a ce stade, MC a soit lu, soit n'est pas inscrit au club science.

label day6:
    scene reveil2 with dissolve
    play sound "sound/vibre.ogg"
    m "..."
    m "Quoi..."
    stop sound
    m "Allo ?"
    $ ali = 'Numéro inconnu'
    a "Bonjour !"
    if aller_science == 3:
        a "C'est bien [j] ?"
        m "Oui... mais..."
        m "Qui es tu ?"
        a "Oh... Alors tu ne reconnais pas ma voix... Je suppose..."
        a "Intéressant... Devine donc !"
        menu:
            m "Je dirais..."
            "Elusia !":
                m "Elusia !"
                a "Elusia..."
                jump day6_fille
            "Ryouzanki !":
                m "Ryouzanki !"
                a "Ryouzanki..."
                jump day6_mec
            "Laura !":
                m "Laura !"
                a "Laura..."
                jump day6_fille
            "Valeth !":
                m "Valeth !"
                a "Valeth..."
                jump day6_mec
            "Alice !":
                m "Alice !"
                a "Alice..."
                a "Oh... C'est une bonne réponse !"
                $ ali = 'Alice'
                $ rel_ali += 5
                jump day6_phone
            "Lloyd !":
                m "Lloyd !"
                a "Lloyd..."
                jump day6_mec
    else:
        a "C'est bien Salazard ?"
        m "Heu, non, vous avez du vous tromper de numéro."
        a "Oops, pardon, au revoir !"
        $ ali = 'Alice'
        jump day6_plan
label day6_fille:
    $ rel_ali -= 1
    a "Je crains que ce ne soit pas la bonne réponse [j] !"
    a "C'est Alice !"
    $ ali = 'Alice'
    jump day6_phone
label day6_mec:
    $ rel_ali -=2
    a "Roooh... Je n'ai pas la voix grave au téléphone..."
    a "Tu vexes ma féminité."
    a "C'est Alice voyons !"
    $ ali = 'Alice'
    jump day6_phone
label day6_phone:
    $ renpy.music.play("music/alice.ogg", fadein=2)
    a "Passons aux choses sérieuses."
    a "Ou pas !"
    a "Les autres membres du club disent que j'en fait trop."
    a "D'ailleurs, ouvrons une parenthèse, qu'en penses tu ?"
    a "Je suis lourde ? J'en fais trop ?"
    menu:
        "Non, pas du tout.":
            $ rel_ali += 5
            m "Non, pas du tout."
            m "Tu es passionnée. C'est une bonne chose."
            a "C'est vrai ?"
            a "Ca me fait vraiment plaisir d'entendre ça."
            a "Surtout de toi !"
        "Oui un peu.":
            $ rel_ali += 3
            m "Oui un peu. Mais c'est naturel."
            m "Ce n'est pas si dérangeant."
            a "Intéressant..."
            a "Je comprends."
            a "Ca me rassure un peu."
        "Effectivement, ils n'ont pas tort...":
            $ rel_ali -= 2
            m "Effectivement, ils n'ont pas tort..."
            m "T'abuses un peu des fois..."
            a "Je... Je comprends..."
            a "Est ce que je peux te demander pardon ?"
            m "C'est pas si grave..."
    a "Bon, fermons cette parenthèse."
    a "Je t'ai appelé pour te remercier en fait."
    a "Merci d'être venu lire ce rapport ennuyeux."
    m "Je n'ai pas finit."
    a "Tu le finira, j'ai confiance."
    a "Les autres ont dit que pour décompresser, je devais ne pas y penser samedi et faire un break."
    a "Pour ça, ils ont décidé de m'empêcher de travailler."
    a "Aujourd'hui, ils ont piqués mes clefs des locaux."
    menu:
        "(Rire)":
            $ rel_ali += 2
            m "Hahaha..."
            a "Amusant n'est-ce pas ?"
        "Ah les enfoirés...":
            m "Ah les enfoirés..."
            a "Mais non. Je ne l'ai pas mal prit."
    a "Ils me les rendront ce midi lorsqu'ils ouvriront les locaux."
    m "Je croyais que tu ne devais pas y aller ?"
    a "J'y viens, j'y viens."
    a "Ils ont l'intention de faire un petit repas d'étage entre membres du club."
    a "Je t'appelle pour t'y convier."
    a "Donc voilà, si ça t'intéresse, viens vers midi dans les locaux du club."
    m "D'accord, j'y réfléchirais."
    a "Ce sera tout... Je suppose."
    a "A tout à l'heure peut être !"
label day6_plan:
    $ renpy.music.play("music/weekend.ogg", fadein=2)
    "Bon... Il est 10h... Qu'est ce que je vais faire de ma journée..."
    $ action_matin = None
    $ action_aprem = None
    $ action_soir = None
    call day_planner(["Matin", "Après midi", "Soir"])
    if action_matin == 'd':
        "Je vais me recoucher tiens..."
        "..."
        play sound "sound/bell.mp3"
        m "Quoi encore..."
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        show elusia normal sport
        e "Salutations !"
        show elusia geez sport
        e "Misère..."
        show elusia sad sport
        e "Ne me dis pas que tu avais l'intention de dormir toute la matiné !"
        menu:
            "Mentir":
                m "Mais non."
                show elusia satisfied sport
                e "Me voilà rassurée !"
                e "Je pensais bien que tu ne serais pas une grosse tanche comme Ryou..."
                show elusia normal sport
                e "Tu ne voudrais pas sortir faire un peu de sport par hasard ?"
                e "J'allais courir un peu le long du canal en fait."
                e "Je me demandais si cela t'intéressait de m'accompagner."
                menu:
                    "Je vais travailler en fait.":
                        m "Je vais travailler en fait."
                        show elusia geez sport
                        e "Oh... d'accord, je te laisse travailler."
                        show elusia normal sport
                        e "Je cours chaque samedi alors si tu veux venir..."
                        e "Bye bye !"
                        m "Bon courage !"
                        show elusia happy sport
                        e "Merci, toi aussi !"
                        play sound "sound/doorclose.mp3"
                        show elusia sad sport
                        "Elle est restée devant chez moi un petit moment sans bouger."
                        scene reveil2 with fade
                        m "Ou en étais-je..."
                        m "Ah oui, mon oreiller."
                        $ vig += 2
                        scene black with fade
                        $ rel_lulu -= 2
                        jump day6_aprem
                    "Je préfère me reposer.":
                        m"Je préfère me reposer."
                        m "C'est tout."
                        show elusia angry sport
                        e "Tu vas devenir un légume comme Ryou."
                        show elusia geez sport
                        e "Bon et bien si tu changes d'avis..."
                        show elusia normal sport
                        e "Saches que je sors courir chaque samedi matin."
                        m "Amuses toi bien."
                        play sound "sound/doorclose.mp3"
                        show elusia sad sport
                        "Elle est restée devant chez moi un petit moment sans bouger."
                        scene reveil2 with fade
                        m "Ou en étais-je..."
                        m "Ah oui, mon oreiller."
                        $ vig += 2
                        scene black with fade
                        $ rel_lulu -= 5
                        jump day6_aprem
                    "Je vais venir.":
                        m "Je vais venir."
                        show elusia happy sport
                        e "Super !"
                        e "Je t'attends ici !"
                        scene chambre m with fade
                        scene couloir with fade
                        show elusia normal sport
                        e "On y va ?"
                        m "Oui."
                        call matin_sport
                        jump day6_aprem
            "Avouer":
                m "Oui."
                show elusia sad sport
                e "Est-ce que... Tu es fatigué[ter] ou quelque chose comme ça ?"
                menu:
                    "Oui.":
                        m "Oui."
                        show elusia geez sport
                        e "Oh, je suis désolée de t'avoir dérangé[ter]."
                        show elusia normal sport
                        e "J'ai cru un instant que tu étais une feignasse comme ton voisin."
                        e "Bon bah écoute, repose toi bien !"
                        e "J'étais venue te chercher pour courir un peu."
                        e "Je cours chaque samedi matin."
                        e "Tu me rejoindra quand tu en aura envie."
                        e "Bye !"
                        play sound "sound/doorclose.mp3"
                        show elusia sad sport
                        "Elle est restée devant chez moi un petit moment sans bouger."
                        scene reveil2 with fade
                        m "Ou en étais-je..."
                        m "Ah oui, mon oreiller."
                        $ vig += 2
                        scene black with fade
                        jump day6_aprem
                    "Non.":
                        m "Non."
                        show elusia geez sport
                        e "Ah..."
                        show elusia sad sport
                        e "Je ne pensais pas que tu serais une feignasse comme Ryou..."
                        show elusia normal sport
                        e "Tu ne voudrais pas sortir faire un peu de sport par hasard ?"
                        e "J'allais courir un peu le long du canal en fait."
                        e "Je me demandais si cela t'intéressait de m'accompagner."
                        menu:
                            "Je préfère dormir.":
                                m"Je préfère dormir."
                                m "C'est tout."
                                show elusia angry sport
                                e "Tu vas devenir un légume comme Ryou."
                                e "Bon et bien si tu changes d'avis..."
                                e "Saches que je sors courir chaque samedi matin."
                                m "Amuses toi bien."
                                play sound "sound/doorclose.mp3"
                                show elusia sad sport
                                "Elle est restée devant chez moi un petit moment sans bouger."
                                scene reveil2 with fade
                                m "Ou en étais-je..."
                                m "Ah oui, mon oreiller."
                                $ vig += 2
                                scene black with fade
                                $ rel_lulu -= 3
                                jump day6_aprem
                            "Je vais venir.":
                                m "Je vais venir."
                                show elusia happy sport
                                e "Super !"
                                e "Je t'attends ici !"
                                scene chambre m with fade
                                scene couloir with fade
                                show elusia normal sport
                                e "On y va ?"
                                m "Oui."
                                call matin_sport
                                jump day6_aprem
    elif action_matin == 's':
        
        "Je devrais faire un peu de sport..."
        m "C'est partit !"
        scene couloir with fade
        show elusia surprised sport
        e "Oh !"
        show elusia satisfied sport
        e "Quel heureux hasard, j'allais justement sonner chez toi."
        show elusia happy sport
        e "Tu allais courir un peu ?"
        m "Bah... Plus ou moins."
        e "C'est génial, j'allais te proposer de venir courir avec moi !"
        e "Tu veux bien ?"
        menu:
            "Accepter.":
                $ rel_lulu += 5
                m"Je ne vois pas de raison de refuser."
                e "Super !"
                e "Allons y alors !"
                call matin_sport
                jump day6_aprem
            "Refuser.":
                m"Nan, désolé, je cours seul[ter]."
                show elusia surprised sport
                m"Avec ma musique dans les oreilles."
                e "Quoi... Sérieusement ?"
                m "Oui."
                show elusia geez sport
                e "Mais dis moi..."
                show elusia sad sport
                e "Est-ce que... Tu me détestes ?"
                menu:
                    "Je ne t'aime pas, non.":
                        $ rel_lulu -= 10
                        m "Je ne t'aime pas, non."
                        e "Y'a... Une raison particulière à ça ?"
                        e "Est-ce que je peux y faire quelque chose ?"
                        m "Non. C'est comme ça."
                        e "... D'accord. Je ne t'embêterais plus..."
                        hide elusia
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
                                    $ action_soir = 'd'
                                "Non, ça ira...":
                                    pass
                        else:
                            $  str_points += 2
                            "J'ai bien couru !"
                        jump day6_aprem
                    "Pas particulièrement.":
                        $rel_lulu -= 5
                        m "Pas particulièrement."
                        e "Alors où est le problème ?"
                        e "Laisse moi venir !"
                        e "S'il te plait !"
                        menu:
                            "Non, vraiment...":
                                $rel_lulu -= 5
                                m "Non, vraiment..."
                                show elusia geez sport
                                e "..."
                                show elusia sad sport
                                e "Bon et bien... A plus tard..."
                                hide elusia
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
                                            $ action_soir = 'd'
                                        "Non, ça ira...":
                                            pass
                                else:
                                    $  str_points += 2
                                    "J'ai bien couru !"
                                jump day6_aprem
                            "Bon, d'accord !":
                                m "Bon, d'accord !"
                                show elusia happy sport
                                e "Super !"
                                show elusia satisfied sport
                                e "Je serais sage !"
                                call matin_sport
                                jump day6_aprem
                    "Mais non, je t'aime bien !":
                        m "Mais non, je t'aime bien !"
                        show elusia geez sport
                        e "Alors..."
                        show elusia sad sport
                        e "Pourquoi est-ce que tu ne veux pas courir avec moi ?"
                        menu:
                            "Bon, d'accord, on va le faire.":
                                $ rel_lulu += 3
                                m"Bon, d'accord, on va le faire."
                                show elusia happy sport
                                e "Super !"
                                show elusia satisfied sport
                                e "Je serais sage !"
                                call matin_sport
                                jump day6_aprem
                            "J'ai mes raisons, une autre fois.":
                                $ rel_lulu += 1
                                m"J'ai mes raisons, une autre fois."
                                show elusia geez sport
                                e "Très bien."
                                show elusia sad sport
                                e "Je n'insiste pas plus."
                                e "A la prochaine."
                                hide elusia
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
                                            $ action_soir = 'd'
                                        "Non, ça ira...":
                                            pass
                                else:
                                    $  str_points += 2
                                    "J'ai bien couru !"
                                jump day6_aprem
    elif action_matin == 't':
        "Je vais en profiter pour travailler tiens..."
        "..."
        play sound "sound/bell.mp3"
        m "Quoi encore..."
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        show elusia normal sport
        e "Salutations !"
        show elusia geez sport
        e "Misère..."
        show elusia sad sport
        e "Ne me dis pas que tu avais l'intention de dormir toute la matiné !"
        m "Pas vraiment...."
        show elusia satisfied sport
        e "Me voilà rassurée !"
        e "Je pensais bien que tu ne serais pas une grosse tanche comme Ryou..."
        show elusia normal sport
        e "Tu ne voudrais pas sortir faire un peu de sport par hasard ?"
        e "J'allais courir un peu le long du canal en fait."
        e "Je me demandais si cela t'intéressait de m'accompagner."
        menu:
            "Je vais travailler en fait.":
                m "Je vais travailler en fait."
                show elusia geez sport
                e "Oh... d'accord, je te laisse travailler."
                show elusia normal sport
                e "Je cours chaque samedi alors si tu veux venir..."
                e "Bye bye !"
                m "Bon courage !"
                show elusia happy sport
                e "Merci, toi aussi !"
                play sound "sound/doorclose.mp3"
                show elusia sad sport
                "Elle est restée devant chez moi un petit moment sans bouger."
                scene reveil2 with fade
                m "Ou en étais-je..."
                m "Ah oui, travailler..."
                scene black with fade
                $ vig -= 1
                if vig < 0:
                    "Je suis trop fatigué pour me concentrer."
                    $ int_points += 1
                else:
                    "Une matinée productive."
                    $ int_points += 2
                $ rel_lulu -= 1
                jump day6_aprem
            "Je vais venir.":
                m "Je vais venir."
                show elusia happy sport
                e "Super !"
                e "Je t'attends ici !"
                scene chambre m with fade
                scene couloir with fade
                show elusia normal sport
                e "On y va ?"
                m "Oui."
                call matin_sport
                jump day6_aprem
    else:
        "ERROR"
label day6_aprem:
    scene chambre m with fade
    "Je me suis fait à manger."
    "Maintenant..."
    if action_aprem == 's':
        if aller_science == 3:
            jump day6_alice
        else:
            jump day6_salazard
    elif action_aprem == 'j':
        "Allons jouer au PC."
        play sound "sound/bell.mp3"
        m "Encore..."
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        show ryou normal
        r "Salut !"
        r "Je me demandais ce que tu faisais le week-end après midi."
        menu:
            "Je joue, là...":
                $ rel_ryou += 3
                m "Je joue là..."
                r "Bah, j'allais faire la même chose en fait."
                r "Je me demandais si on pouvait faire la même chose."
                r "On peut se mettre ensemble à un jeu en ligne."
                menu:
                    "Ouais, si tu veux.":
                        $ rel_ryou += 5
                        m "Ouais, si tu veux."
                        show ryou happy
                        r "Je t'ai justement apporté ce CD."
                        r "Je t'attends en ligne !"
                        scene chambre m with fade
                        "J'ai joué jusqu'au soir."
                        jump day6_soir
                    "Non, ça ira.":
                        m "Non, ça ira."
                        show ryou sad
                        r "OK, tu sais ou me trouver au pire."
                        scene chambre m with fade
                        "J'ai joué jusqu'au soir."
                        jump day6_soir
            "Je travaille là.":
                m "Je travaille là."
                show ryou angry
                r "Ouais ouais..."
                r "On me la fait pas à moi..."
                m "Heu..."
                show ryou sad
                r "Ca va, je plaisante."
                r "Je te laisse travailler. Quand t'aura fini, tu sais où me trouver."
                scene chambre m with fade
                "J'ai joué jusqu'au soir."
                jump day6_soir
            "J'allais sortir.":
                $ rel_ryou -= 4
                m "J'allais sortir."
                show ryou angry
                r "Nan, sérieux ?"
                m "Ouais..."
                r "On me la fait pas à moi..."
                m "Heu..."
                show ryou sad
                r "Ca va, je plaisante."
                r "Je te laisse tranquille. Quand tu sera rentré, tu sais où me trouver."
                scene chambre m with fade
                "J'ai joué jusqu'au soir."
                jump day6_soir
    elif action_aprem == 't':
        "Allons jouer au PC."
        play sound "sound/bell.mp3"
        m "Encore..."
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        show ryou normal
        r "Salut !"
        r "Je me demandais ce que tu faisais le week-end après midi."
        m "Je travaille là."
        show ryou angry
        r "Ouais ouais..."
        r "On me la fait pas à moi..."
        m "Heu..."
        show ryou sad
        r "Ca va, je plaisante."
        r "Je te laisse travailler. Quand t'aura fini, tu sais où me trouver."
        scene chambre m with fade
        "J'ai travaillé jusqu'au soir."
        $ vig -= 1
                if vig < 0:
                    "Je suis trop fatigué pour me concentrer."
                    $ int_points += 1
                else:
                    "Une aprem productive."
                    $ int_points += 2
        jump day6_soir
    else:
        "ERROR"
    return
label day6_alice:
label day6_salazard:
label day6_soir:
