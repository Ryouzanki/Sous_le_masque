# TODO club_home et club_art
# a ce stade, MC a soit lu, soit n'est pas inscrit au club science.

label day6:
    scene reveil2 with fade
    play sound "sound/vibre.ogg"
    m "..."
    ma "Quoi..."
    stop sound
    m "Allo ?"
    $ ali = 'Numéro inconnu'
    a "Bonjour !"
    if aller_science == 3:
        a "C'est bien [j] ?"
        m "Oui... mais..."
        ma "Qui es tu ?"
        a "Oh... Alors tu ne reconnais pas ma voix... Je suppose..."
        a "Intéressant... Devine donc !"
        menu:
            m "Je dirais..."
            "Elusia !":
                # $ renpy.block_rollback()
                m "Elusia !"
                a "Elusia..."
                jump day6_fille
            "Ryouzanki !":
                # $ renpy.block_rollback()
                m "Ryouzanki !"
                a "Ryouzanki..."
                jump day6_mec
            "Laura !":
                # $ renpy.block_rollback()
                m "Laura !"
                a "Laura..."
                jump day6_fille
            "Valeth !":
                # $ renpy.block_rollback()
                m "Valeth !"
                a "Valeth..."
                jump day6_mec
            "Alice !":
                # $ renpy.block_rollback()
                m "Alice !"
                a "Alice..."
                a "Oh... C'est une bonne réponse !"
                $ ali = 'Alice'
                $ rel_ali += 5
                jump day6_phone
            "Lloyd !":
                # $ renpy.block_rollback()
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
    play music (weekend1) fadein 2
    a "Passons aux choses sérieuses."
    a "Ou pas !"
    a "Les autres membres du club disent que j'en fait trop."
    a "D'ailleurs, ouvrons une parenthèse, qu'en penses tu ?"
    a "Je suis lourde ? J'en fais trop ?"
    menu:
        "Non, pas du tout.":
            # $ renpy.block_rollback()
            $ rel_ali += 5
            m "Non, pas du tout."
            m "Tu es passionnée. C'est une bonne chose."
            a "C'est vrai ?"
            a "Ca me fait vraiment plaisir d'entendre ça."
            a "Surtout de toi !"
        "Oui un peu.":
            # $ renpy.block_rollback()
            $ rel_ali += 3
            m "Oui un peu. Mais c'est naturel."
            m "Ce n'est pas si dérangeant."
            a "Intéressant..."
            a "Je comprends."
            a "Ca me rassure un peu."
        "Effectivement, ils n'ont pas tort...":
            # $ renpy.block_rollback()
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
            # $ renpy.block_rollback()
            $ rel_ali += 2
            mh "Hahaha..."
            a "Amusant n'est-ce pas ?"
        "Ah les enfoirés...":
            # $ renpy.block_rollback()
            ma "Ah les enfoirés..."
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
    "Bon... Il est 10h... Qu'est ce que je vais faire de ma journée..."

    $ action_matin = None
    $ action_aprem = None
    $ action_soir = None
    
    if aller_science ==3:
        call day_planner(["Matin", "Après-midi", "Soir"])
    else:
        call day_planner(["Matin", "Après midi", "Soir"])
    stop music fadeout 4.0
    if action_matin == 'd':
        "Je vais me recoucher tiens..."
        "..."
        play sound "sound/bell.mp3"
        ma "Quoi encore..."
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        play music (elusia1) fadeout 2
        show elusia normal sport
        e "Salutations !"
        show elusia geez sport
        e "Misère..."
        show elusia sad sport
        e "Ne me dis pas que tu avais l'intention de dormir toute la matiné !"
        menu:
            "Mentir":
                # $ renpy.block_rollback()
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
                        # $ renpy.block_rollback()
                        m "Je vais travailler en fait."
                        show elusia geez sport
                        e "Oh... d'accord, je te laisse travailler."
                        show elusia normal sport
                        e "Je cours chaque samedi alors si tu veux venir..."
                        stop music fadeout 4.0
                        e "Bye bye !"
                        m "Bon courage !"
                        show elusia happy sport
                        e "Merci, toi aussi !"
                        play sound "sound/doorclose.mp3"
                        show elusia sad sport
                        "Elle est restée devant chez moi un petit moment sans bouger."
                        scene reveil2 with fade
                        m "Ou en étais-je..."
                        mh "Ah oui, mon oreiller."
                        $ vig += 2
                        scene black with fade
                        $ rel_lulu -= 2
                        jump day6_aprem
                    "Je préfère me reposer.":
                        # $ renpy.block_rollback()
                        m "Je préfère me reposer."
                        m "C'est tout."
                        show elusia angry sport
                        e "Tu vas devenir un légume comme Ryou."
                        show elusia geez sport
                        e "Bon et bien si tu changes d'avis..."
                        show elusia normal sport
                        stop music fadeout 4.0
                        e "Saches que je sors courir chaque samedi matin."
                        m "Amuses toi bien."
                        play sound "sound/doorclose.mp3"
                        show elusia sad sport
                        "Elle est restée devant chez moi un petit moment sans bouger."
                        scene reveil2 with fade
                        m "Ou en étais-je..."
                        mh "Ah oui, mon oreiller."
                        $ vig += 2
                        scene black with fade
                        $ rel_lulu -= 5
                        jump day6_aprem
                    "Je vais venir.":
                        # $ renpy.block_rollback()
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
                # $ renpy.block_rollback()
                ma "Oui."
                show elusia sad sport
                e "Est-ce que... Tu es fatigué[ter] ou quelque chose comme ça ?"
                menu:
                    "Oui.":
                        # $ renpy.block_rollback()
                        ma "Oui."
                        show elusia geez sport
                        e "Oh, je suis désolée de t'avoir dérangé[ter]."
                        show elusia normal sport
                        e "J'ai cru un instant que tu étais une feignasse comme ton voisin."
                        e "Bon bah écoute, repose toi bien !"
                        e "J'étais venue te chercher pour courir un peu."
                        e "Je cours chaque samedi matin."
                        e "Tu me rejoindra quand tu en aura envie."
                        stop music fadeout 4.0
                        e "Bye !"
                        play sound "sound/doorclose.mp3"
                        show elusia sad sport
                        "Elle est restée devant chez moi un petit moment sans bouger."
                        scene reveil2 with fade
                        m "Ou en étais-je..."
                        mh "Ah oui, mon oreiller."
                        $ vig += 2
                        scene black with fade
                        jump day6_aprem
                    "Non.":
                        # $ renpy.block_rollback()
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
                                # $ renpy.block_rollback()
                                m"Je préfère dormir."
                                m "C'est tout."
                                show elusia angry sport
                                e "Tu vas devenir un légume comme Ryou."
                                e "Bon et bien si tu changes d'avis..."
                                e "Saches que je sors courir chaque samedi matin."
                                stop music fadeout 4.0
                                m "Amuses toi bien."
                                play sound "sound/doorclose.mp3"
                                show elusia sad sport
                                "Elle est restée devant chez moi un petit moment sans bouger."
                                scene reveil2 with fade
                                m "Ou en étais-je..."
                                mh "Ah oui, mon oreiller."
                                $ vig += 2
                                scene black with fade
                                $ rel_lulu -= 3
                                jump day6_aprem
                            "Je vais venir.":
                                # $ renpy.block_rollback()
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
        mh "C'est partit !"
        play music (elusia1) fadeout 2
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
                # $ renpy.block_rollback()
                $ rel_lulu += 5
                m "Je ne vois pas de raison de refuser."
                e "Super !"
                e "Allons y alors !"
                call matin_sport
                jump day6_aprem
            "Refuser.":
                # $ renpy.block_rollback()
                ma "Nan, désolé, je cours seul[ter]."
                show elusia surprised sport
                m "Avec ma musique dans les oreilles."
                e "Quoi... Sérieusement ?"
                m "Oui."
                show elusia geez sport
                e "Mais dis moi..."
                show elusia sad sport
                e "Est-ce que... Tu me détestes ?"
                menu:
                    "Je ne t'aime pas, non.":
                        # $ renpy.block_rollback()
                        $ rel_lulu -= 10
                        stop music fadeout 4.0
                        ma "Je ne t'aime pas, non."
                        e "Y'a... Une raison particulière à ça ?"
                        e "Est-ce que je peux y faire quelque chose ?"
                        ma "Non. C'est comme ça."
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
                                    # $ renpy.block_rollback()
                                    $ action_soir = 'd'
                                "Non, ça ira...":
                                    # $ renpy.block_rollback()
                                    pass
                        else:
                            $  str_points += 2
                            "J'ai bien couru !"
                        jump day6_aprem
                    "Pas particulièrement.":
                        # $ renpy.block_rollback()
                        $rel_lulu -= 5
                        m "Pas particulièrement."
                        e "Alors où est le problème ?"
                        e "Laisse moi venir !"
                        e "S'il te plait !"
                        menu:
                            "Non, vraiment...":
                                # $ renpy.block_rollback()
                                $rel_lulu -= 5
                                stop music fadeout 4.0
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
                                            # $ renpy.block_rollback()
                                            $ action_soir = 'd'
                                        "Non, ça ira...":
                                            # $ renpy.block_rollback()
                                            pass
                                else:
                                    $  str_points += 2
                                    "J'ai bien couru !"
                                jump day6_aprem
                            "Bon, d'accord !":
                                # $ renpy.block_rollback()
                                mh "Bon, d'accord !"
                                show elusia happy sport
                                e "Super !"
                                show elusia satisfied sport
                                e "Je serais sage !"
                                call matin_sport
                                jump day6_aprem
                    "Mais non, je t'aime bien !":
                        # $ renpy.block_rollback()
                        mh "Mais non, je t'aime bien !"
                        show elusia geez sport
                        e "Alors..."
                        show elusia sad sport
                        e "Pourquoi est-ce que tu ne veux pas courir avec moi ?"
                        menu:
                            "Bon, d'accord, on va le faire.":
                                # $ renpy.block_rollback()
                                $ rel_lulu += 3
                                m "Bon, d'accord, on va le faire."
                                show elusia happy sport
                                e "Super !"
                                show elusia satisfied sport
                                e "Je serais sage !"
                                call matin_sport
                                jump day6_aprem
                            "J'ai mes raisons, une autre fois.":
                                # $ renpy.block_rollback()
                                $ rel_lulu += 1
                                m "J'ai mes raisons, une autre fois."
                                show elusia geez sport
                                stop music fadeout 4.0
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
                                            # $ renpy.block_rollback()
                                            $ action_soir = 'd'
                                        "Non, ça ira...":
                                            # $ renpy.block_rollback()
                                            pass
                                else:
                                    $  str_points += 2
                                    "J'ai bien couru !"
                                jump day6_aprem
    elif action_matin == 't':
        "Je vais en profiter pour travailler tiens..."
        "..."
        play sound "sound/bell.mp3"
        ma "Quoi encore..."
        play sound "sound/dooropen.mp3"
        scene couloir with fade
        play music (elusia1) fadeout 2
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
                # $ renpy.block_rollback()
                m "Je vais travailler en fait."
                show elusia geez sport
                e "Oh... d'accord, je te laisse travailler."
                show elusia normal sport
                e "Je cours chaque samedi alors si tu veux venir..."
                stop music fadeout 4.0
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
                # $ renpy.block_rollback()
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
    play music (weekend1) fadein 2
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
                # $ renpy.block_rollback()
                $ rel_ryou += 3
                m "Je joue là..."
                r "Bah, j'allais faire la même chose en fait."
                r "Je me demandais si on pouvait faire la même chose."
                r "On peut se mettre ensemble à un jeu en ligne."
                menu:
                    "Ouais, si tu veux.":
                        # $ renpy.block_rollback()
                        $ rel_ryou += 5
                        m "Ouais, si tu veux."
                        show ryou happy
                        r "Je t'ai justement apporté ce CD."
                        r "Je t'attends en ligne !"
                        scene chambre m with fade
                        "J'ai joué jusqu'au soir."
                        jump day6_soir
                    "Non, ça ira.":
                        # $ renpy.block_rollback()
                        m "Non, ça ira."
                        show ryou sad
                        r "OK, tu sais ou me trouver au pire."
                        scene chambre m with fade
                        "J'ai joué jusqu'au soir."
                        jump day6_soir
            "Je travaille là.":
                # $ renpy.block_rollback()
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
                # $ renpy.block_rollback()
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
        "Allons travailler."
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
    m "Oh, c'est vrai, Alice m'a demandé de venir..."
    m "Tant pis... Je mangerais ça ce soir."
    play sound "sound/dooropen.mp3"
    scene couloir with fade
    scene street with fade
    "J'ai acheté quelques petits trucs pour pas arriver les mains vides."
    stop music fadeout 4.0
    scene cours
    show alice geez:
        left
    show lloyd normal:
        right
    with fade
    "Arrivé[ter] sur place, j'aperçois Alice au loin avec Lloyd."
    "Ils n'ont pas l'air de s'amuser..."
    play music (alice1) fadein 10
    menu:
        "Attendre.":
            # $ renpy.block_rollback()
            $ choix1 = False
            "Je ne devrais pas me mêler de ce qui ne me regarde pas."
            "Je vais attendre que ça passe."
            "..."
            "..."
            show alice happy at center with move
            a "[j] ! Je ne pensais pas te voir !"
            a "Il faut que je remplisse de la paperasse, je reviens !"
            hide alice
            show lloyd normal at center with move
        "Aller voir.":
            # $ renpy.block_rollback()
            $ choix1 = True
            "Je vais voir de plus près ce qui se passe."
            "Ils se disputent et les autres regardent en silence."
            y "Comment ? Je crains que ce ne soit pas possible."
            show alice angry
            a "Et bien, nous allons vous montrer que c'est possible Sir !"
            y "Le réglement stipule qu'il est interdit de manger dans les locaux."
            show alice sad
            a "Nous allons faire une petite entorse au réglement."
            show lloyd angry
            y "Hors de question. Il faut la signature d'un responsable."
            y "Hors, tu n'étais toi même pas au courant de la situation !"
            show alice sad
            a "Intéressant..."
            a "Il faut donc la signature de quelqu'un... Comme toi..."
            show lloyd normal
            y"..."
            y "Je refuse de prendre la responsabilité d'un évènement aussi spontané."
            y "Il fallait se préparer et demander l'avis du président."
            show alice angry
            a "S'il faut toujours demander au président, à quoi tu sers bordel ?"
            y"Je surveille que son autorité est respectée."
            a "Et pourquoi je peux pas signer moi ?"
            y "... Tu peux."
            y "Mais tu perdra probablement ton poste."
            a "Pourquoi probablement ?"
            y "En cas de dégradation, tu perdra ton poste."
            a "Il n'y en aura pas. J'ai confiance en les membres de mon club."
            y "Très bien. Tu sais où sont les papiers."
            show alice sad at center with move
            a "[j]... Désolée, je ne voulais pas que tu assistes à ça..."
            a "Il faut que je remplisse de la paperasse, je reviens !"
            hide alice with easeoutleft
            show lloyd normal at center with move
    y "Cette fille n'a aucun sens des responsabilités..."
    if choix1:
        menu:
            "Elle en a plus que toi.":
                # $ renpy.block_rollback()
                $ rel_lloy -= 2
                m "Elle en a plus que toi."
                show lloyd angry
                y "Je te demande pardon ?"
            "Elle en a juste un différent du tien.":
                # $ renpy.block_rollback()
                $ rel_lloy += 3
                m "Elle en a juste un différent du tien."
                show lloyd angry
                y "Comment ça ?"
                m "Il n'y a pas que la hiérarchie dans la vie."
                m "Il y a aussi la confiance."
                show lloyd normal
                y "..."
            "Elle n'en a aucun, effectivement...":
                # $ renpy.block_rollback()
                $ rel_lloy += 5
                m "Elle n'en a aucun, effectivement..."
                show lloyd happy
                y "Si seulement tu étais à sa place !"
    else:
        m "Je ne sais pas. Je n'ai pas le contexte."
        y "Je te dis juste ça comme ça."
    show lloyd normal
    y "Des membres de son équipe ont abusé de sa confiance pour lui voler les clefs."
    y"Et elle refuse de découvrir les coupables."
    menu:
        "Complicité, elle défend ses amis.":
            # $ renpy.block_rollback()
            $ rel_lloy += 5
            m "Complicité, elle défend ses amis."
            show lloyd happy
            y "Exactement !"
        "En quoi est-ce important ?":
            # $ renpy.block_rollback()
            m "En quoi est-ce important ?"
            y "Elle est censée être impartiale et juste."
            y "Voler, c'est mal, peut importe la raison."
        "C'était pour la bonne cause.":
            # $ renpy.block_rollback()
            $ rel_lloy += 2
            m "C'était pour la bonne cause."
            y "C'était pour la bonne cause ?"
            y "..."
            m "Tu comprendras un jour."
    show lloyd normal at right with move
    show alice angry at left with easeinleft
    a "Les voilà tes papiers !"
    a "Maintenant, casse toi !"
    y "Non. Je vais rester pour surveiller."
    a "Surveiller quoi ? On n'est plus des gosses..."
    $ choix1 = False
    $ choix2 = False
    menu:
        "Laisses le rester.":
            # $ renpy.block_rollback()
            $ rel_lloy += 2
            $ rel_ali += 6
            m"Laisses le rester."
            show alice sad
            a "..."
            show alice geez
            a "D'accord..."
            show alice sad
            a "Tu es bien trop gentil [j]."
            a "C'est bien parce que c'est ta fête que j'accepte."
            y "Je serais discret dans un coin."
            a "..."
            y "Mais je veille sur vous."
            $ choix1= True # Lloyd est resté grace a Minato
            $ choix2= True # Lloyd est la
        "Ne rien dire.":
            # $ renpy.block_rollback()
            m"..."
            y "Je serais discret dans un coin."
            a "..."
            y "Mais je veille sur vous."
            $ choix2= True # Lloyd est la
        "Tu n'as plus rien à faire ici.":
            # $ renpy.block_rollback()
            $ rel_lloy -= 2
            $ rel_ali += 5
            m "Tu n'as plus rien à faire ici."
            show alice happy
            a "Tu vois ?"
            a "Même [j] le dit !"
            show lloyd angry
            y "Très bien, je m'en vais."
            y "Mais vous ne vous en tirerez pas ainsi."
            a "C'est ça ! Sayonara !"
    hide lloyd with easeoutright
    show alice geez at center with move
    a "Il est juste mais trop trop chiant des fois l'aristo..."
    menu:
        "C'est pas faux...":
            # $ renpy.block_rollback()
            m "C'est pas faux..."
            $ rel_ali += 5
        "N'exagérons rien...":
                # $ renpy.block_rollback()
                m"N'exagérons rien..."
                $ rel_ali += 2
                show alice sad
                a "Je n'exagère pas !"
        "Il n'a pas tout à fait tort...":
                # $ renpy.block_rollback()
                m"Il n'a pas tout à fait tort..."
                $ rel_ali -= 2
                show alice sad
                a "Tu trouves ?"
    show alice angry
    a"Juste que des fois, il fait chier pour rien..."
    a "Il est trop coincé, trop à cheval sur les règles."
    show alice sad
    a "En même temps quand tu viens d'une école privée avec que des gens comme lui..."
    a "J'ai un peu pitié de lui... J'aimerais qu'il nous comprenne..."
    a "Je crois qu'il fait des effort alors je devrais en faire aussi."
    menu:
        "C'est un peu tard pour l'inviter.":
            # $ renpy.block_rollback()
            m "C'est un peu tard pour l'inviter."
            show alice normal
            a "Il est toujours dans le coin... Je suppose..."
        "Invites le !" if choix2:
            # $ renpy.block_rollback()
            m "Invites le !"
            show alice happy
            a "Bonne idée !"
            $ rel_ali += 4
    show alice happy
    a "Heureusement que t'es là !"
    a "Du coup, ça m'évite d'y aller moi même !"
    m "Hein ?"
    play music (jeux1)
    show alice satisfied
    a "Pierre, feuille..."
    m "Quoi ?!"
    a "... Ciseaux !"
label day6_pfc:
    menu:
        "Pierre":
            # $ renpy.block_rollback()
            pass
        "Feuille":
            # $ renpy.block_rollback()
            pass
        "Ciseaux.":
            # $ renpy.block_rollback()
            pass
    $ n = renpy.random.randint(1,3)
    if n !=1:
        a "Egalité..."
        a "Pierre feuille ciseaux !"
        jump day6_pfc
    else:
        stop music fadeout 3.0
        show alice geez
        a "..."
        play music (alice1) fadein 2.0
       
        m "Je crois que t'as perdu..."
        show alice sad
        a "Oui mais je suis ta supérieure et donc tu vas y aller pour moi."
        menu:
            "Oui madame la dictatrice !":
                # $ renpy.block_rollback()
                $ rel_ali += 5
                mh "Oui madame la dictatrice !"
                show alice satisfied
                a "Merci !"
                hide alice with easeoutleft
                "Pas dur à trouver, Lloyd est resté à l'entrée les bras croisés."
                show lloyd normal with easeinright
                y "Qu'est ce qu'il y a ?"
                menu:
                    "L'inviter à venir.":
                        # $ renpy.block_rollback()
                        m "Tu viens avec nous ?"
                        y "Je ne suis plus la bienvenue."
                        menu:
                            "Tu surveillera mieux de l'intérieur.":
                                # $ renpy.block_rollback()
                                m "Tu surveillera mieux de l'intérieur."
                                y "Non... J'ai mieux à faire."
                                $ rel_lloy += 2
                            "Alice veut te voir.":
                                # $ renpy.block_rollback()
                                m "Alice veut te voir."
                                m "Elle voulait s'excuser auprès de toi."
                                y "Ce n'est pas important."
                                y "J'ai plus important à faire."
                                $ rel_ali += 2
                            "Tant pis.":
                                # $ renpy.block_rollback()
                                pass
                        y "Je vais partir."
                        y "A plus tard."
                        "Il est subitement partit..."
                    "Partir.":
                        # $ renpy.block_rollback()
                        m "Rien, je ne faisais que passer."
                        show lloyd angry
                        y "Pas de bêtises, je vous ai à l'oeil..."
                hide lloyd with easeoutright
                show alice sad with easeinleft
                a "Alors ?"
                m "Il dit qu'il ne veut pas venir."
                jump day6_postlloyd
            "C'est pas un peu de l'abus de position ?":
                # $ renpy.block_rollback()
                ma "C'est pas un peu de l'abus de position ?"
                show alice geez
                a "C'est bon, je plaisantais"
                a "J'y vais..."
                hide alice with easeoutright
                "..."
                show alice geez with easeinright
                a "Il ne veut pas venir."
                jump day6_postlloyd
label day6_postlloyd:
    show alice sad
    a "Bon bah tant pis..."
    show alice normal
    a "Allons plutot nous amuser... Je suppose..."
    scene labo with fade
    show alice happy
    "Nous mangeons des plats maison des membres dans la salle de science."
    a "Alors, ça te plait ?"
    mh "Bien sur..."
    a "Je ne sais pas pourquoi mais je suis très contente de te voir ici."
    menu:
        "C'est beau l'amour.":
            # $ renpy.block_rollback()
            $rel_ali += 3
            mh "C'est beau l'amour."
            show alice geez
            a "Le jour où je tomberais amoureuse de quelqu'un n'est pas près d'arriver."
            menu:
                "Ca va, je plaisantais.":
                    # $ renpy.block_rollback()
                    mh "Ca va, je plaisantais."
                    show alice satisfied
                    a"Je sais."
                "Pourquoi tu dis ça ?":
                    # $ renpy.block_rollback()
                    $rel_ali += 3
                    m "Pourquoi tu dis ça ?"
                    show alice sad
                    a "Disons que mon esprit scientifique ne croit pas en ce genre de chose."
                    show alice happy
                    a "Et puis il faudrait que je trouve quelqu'un de spécial."
                    a "Quelqu'un qui sache m'apprécier à ma juste valeur !"
        "En fait, j'avais rien de mieux à faire.":
            # $ renpy.block_rollback()
            m "En fait, j'avais rien de mieux à faire."
            show alice happy
            a "Hey ! C'est pas sympa !"
            show alice normal
            a"Enfin le hasard a déjà conduit à des découvertes scientifiques majeures !"
            a "Peut importe la raison, tant que tu y prends du plaisir au final... Je suppose..."
        "Je voulais m'intégrer au plus vite.":
            # $ renpy.block_rollback()
            $rel_ali += 3
            m "Je voulais m'intégrer au plus vite."
            show alice happy
            a"Excellente initiative !"
            a "C'est très facile de s'intégrer dans un club quant on a de bon résultat."
            show alice satisfied
            a "J'attends beaucoup de toi !"
            m "Tu me fais peur..."
    $ choix1 =  False
    $ choix2 =  True
    $ choix3 =  False
    $ choix4 =  True
    $ choix5 =  True
    $ choix6 =  False
label day6_q:
    menu:
        "Pourquoi tu portes une blouse ?" if choix2:
            # $ renpy.block_rollback()
            $ rel_ali += 4
            m "Pourquoi tu portes une blouse ?"
            m "Je veux dire, on est samedi..."
            show alice geez
            a"Je sais, c'est bizarre..."
            show alice sad
            a"Mais je me sens vraiment bien dans une blouse."
            show alice happy
            a "Je me sens nue sans..."
            show alice satisfied
            a "Ah mais je ne la porte pas en ville hein !"
            a"Juste au sein de l'école."
            $ choix1 = True
            $ choix2 = False
            jump day6_q
        "Est ce que tes parents sont des scientifiques ?" if choix1:
            # $ renpy.block_rollback()
            $ rel_ali += 4
            m "Est ce que tes parents sont des scientifiques ?"
            show alice angry
            a "Hey ho ! C'est quoi ces questions ?"
            a "Vive les stéréotypes !"
            show alice sad
            a "J'aimerais dire le contraire mais..."
            show alice geez
            a "Mes parents ne sont pas des scientifiques."
            $ choix1 = False
            jump day6_q
        "Comment as tu obtenu mon numéro ?" if choix4:
            # $ renpy.block_rollback()
            $ rel_ali += 2
            m "Comment as tu obtenu mon numéro ?"
            show alice satisfied
            a "Tu crois qu'elle sert à quoi ta fiche d'inscription ?"
            m "Ah oui, c'est vrai..."
            $ choix4 = False
            jump day6_q
        "Pourquoi tu tiens tant que ça à me recruter ?" if choix5:
            # $ renpy.block_rollback()
            m "Pourquoi tu tiens tant que ça à me recruter ?"
            show alice geez
            a "On n'a pas assez de membre ni assez de temps..."
            $ choix3 = True
            $ choix6 = True
            $ choix5 = False
            jump day6_q
        "Pas assez de membre... Pourquoi ?"if choix3:
            # $ renpy.block_rollback()
            $ rel_ali -= 2
            m "Pas assez de membre... Pourquoi ?"
            show alice angry
            a "Parce qu'ils veulent leur nom écrit dans la liste du staff."
            a "Mais refusent de mettre la main à la patte."
            a "\"Oh non, c'est trop de travail  !\""
            $ choix3 =  False
            jump day6_q
        "C'est pas un peu de ta faute si y'a pas grand monde ?"if choix6:
            # $ renpy.block_rollback()
            $ rel_ali -= 3
            $ choix6 = False
            m "C'est pas un peu de ta faute ?"
            show alice angry
            a "De quoi je me mêle ?"
            a "Je gère mon équipe comme je veux !"
            a "Si t'es pas content, tu peux démissionner !"
            "Quel changement brutal d'atmosphère... Je ferais bien de ne plus la titiller..."
            "Elle semble ne pas apprécier les questions sur le club et la manière dont elle le gère."
            jump day6_q
        "Ne rien demander.":
            "..."
    scene labo with fade
    show alice happy
    a"Bon ! On s'est bien amusé !"
    a"Maintenant, au travail !"
    menu:
        "J'ai l'impression de m'être fait roulé !":
            # $ renpy.block_rollback()
            $ rel_ali += 4
            mh "J'ai l'impression de m'être fait roulé !"
            show alice satisfied
            a "Tu crois ?"
        "D'accord...":
            # $ renpy.block_rollback()
            $ rel_ali += 2
            m "D'accord."
            a "J'apprécie ta bonne volonté."
        "Non, je ne suis pas venu pour ça !":
            # $ renpy.block_rollback()
            $ rel_ali -= 4
            ma "Non, je ne suis pas venu pour ça !"
            show alice sad
            a "Bon bah tant pis."
            show alice normal
            a "Bye bye !"
            jump day6_soir
    show alice normal
    a "D'ailleurs, pour vérifier que t'as bien lu..."
    a "L'autre jour, j'ai envoyé Baka-Powa à la préfecture pour le feu d'artifice."
    a "Pourtant, nous n'avons pas de feu d'articfices de grande puissance C4 ou T2."
    a "Donc, on a dépassé le seuil de matière active."
    a "Ce seuil est de combien de Kg ?"
    $ ans = renpy.input("Le seuil en Kg est de :", "", length=2)
    # $ renpy.block_rollback()
    if ans == '35':
        $ rel_ali += 8
        show alice happy
        a "Intéressant... Très impressionnant !"
        show alice satisfied
        a "On va pouvoir faire quelque chose de toi !"
    # elif ((ans - 35)*(ans-35))<=25:
        # $ rel_ali += 3
        # show alice happy
        # a "Intéressant... Presque !"
        # show alice satisfied
        # a "On va pouvoir faire quelque chose de toi !"
    else:
        show alice sad
        a"[ans]..."
        show alice geez
        a "Pas vraiment nan..."
    show alice normal
    a "Bref, voilà le rapport."
    a "Bonne lecture."
    hide alice
    "J'ai lu tout le samedi."
    "C'est long et pas toujours intéressant."
    "J'ai lu 60\%."
    $ aller_science +=2
    "J'ai beaucoup avancé et je rentre chez moi."
    jump day6_soir
label day6_salazard:
    "Je vais sortir un peu..."
    "..."
    scene street
    "..."
    scene chambre m
    "Il n'y avait rien d'intéressant à faire dehors."
    "Ryouzanki avait raison, je ferais mieux de trouver de quoi m'occuper."
    jump day6_soir
label day6_soir:
    play music (joueur1) fadeout 2
    scene chambre m
    "Je mange."
    "Puis, comme convenu..."
    if action_soir == 'd':
        extend "je me couche tôt."
        $ vig += 4
    elif action_soir == 'j':
        extend "je joue tard."
    elif action_soir == 't':
        extend "je travaille tard."
        $ vig -= 1
        if vig < 0:
            "Je suis trop fatigué pour me concentrer."
            $ int_points += 1
        else:
            "Une soirée productive."
            $ int_points += 2
    return
