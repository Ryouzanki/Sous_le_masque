label day4:
    scene reveil with dissolve
    play sound "sound/clock.mp3"
    m "..."
    m "Quand c'est l'heure..."
    stop sound
    $ renpy.music.play("music/joueur.ogg", fadein=2)
    m "Je suis prêt[ter] !"
    play sound "sound/bell.mp3"
    m "Toujours aussi ponctuels ces deux là..."
    play sound "sound/dooropen.mp3"
    scene couloir with fade
    show ryou normal at left
    show elusia normal at right
    r "Yo !"
    e "Salutations !"
    scene street with dissolve
    show ryou normal at left
    show elusia normal at right
    pause(1)
    if choix1 and aller_science > 1:
        r "Alors comme ça t'as décidé d'aider Alice ?"
        menu:
            "Oui":
                m "Oui."
                $ rel_ryou +=2
                $ rel_lulu += 2
                r "C'est gentil de ta part."
                r "J'aide le secrétaire de l'association des élèves à gérer les papiers."
                r "Donc, je ne peux pas venir régulièrement."
                show elusia sad
                e "Je voudrais bien aider, mais a part faire les courses, je ne sers à rien d'autre."
                r "C'est déjà ça, ça leur évite de perdre du temps pour aller chercher le matos."
                e "Oui... Mais j'aimerais vraiment être plus utile."
                r "Chacun fait ce qu'il peut."
                show elusia normal
            "On m'y a contraint...":
                m "On m'y a contraint..."
                show ryou sad
                r "C'est pas son genre à Alice..."
                r "Ca veut dire qu'elle est vraiment sous pression."
                e "Et qu'elle est en retard..."
                show ryou normal
                r "Moi, j'aide le secrétaire de l'association des élèves à gérer les papiers."
                r "Donc, je ne peux pas venir régulièrement."
                show elusia sad
                e "Je voudrais bien aider, mais a part faire les courses, je ne sers à rien d'autre."
                r "C'est déjà ça, ça leur évite de perdre du temps pour aller chercher le matos."
                e "Oui... Mais j'aimerais vraiment être plus utile."
                r "Chacun fait ce qu'il peut."
    else:
        r "Alice t'avais demandé de venir la voir hier je crois."
        r "Elle était vraiment pas contente que tu lui fausses compagnie."
        e "Tu as vraiment fait ça ?"
        menu:
            "Je n'aime pas qu'on me force la main.":
                m "Je n'aime pas qu'on me force la main."
                $ rel_ryou -= 1
                $ rel_lulu -= 3
                r "C'est pas son genre à Alice..."
                r "Ca veut dire qu'elle est vraiment sous pression."
                e "Et qu'elle est en retard..."
                r "Tâches d'y aller aujourd'hui..."
                m "Si j'oublie pas..."
            "J'ai oublié.":
                m "J'ai oublié."
                $ rel_ryou -= 3
                $ rel_lulu -= 1
                show ryou angry
                show elusia sad
                r "Ah bon... Vraiment ?"
                e "Tant pis. On te le rappellera ce soir alors."
        
    scene classroom with fade
    "Encore un cours à suivre avec Elusia pendant que Ryouzanki dors."
    scene classroom with fade
    $ renpy.music.play("music/matin.ogg", fadein=2)
    show ryou sad at left
    show elusia normal at right
    e "On va voir comment va Alice ?"
    show ryou normal
    r "Pourquoi pas..."
    r "[j], tu viens avec nous."
    m "OK..."
    call day4_labo
    jump day4_cours
    
label day4_labo:
    scene labo with dissolve
    show ryou normal at left
    show elusia normal at center
    if choix1 and aller_science > 1:
        show alice normal at right
        a "Oh, que faites vous là ?"
        a "Vous n'allez pas manger au parc ?"
        e "On allait voir comment ça allait de ton côté."
        show alice geez
        a "Ah... Tout va mal... Je suppose..."
        a "Je viens de trouver les papiers des feux d'artifices pour la mairie."
        show elusia sad
        e "Misère... Cela veut dire qu'on ne les a pas encore envoyé ?"
        show ryou angry
        r "Je vais m'en charger ce soir dans ce cas."
        show alice sad
        a "D'accord, je compte sur toi Ryou."
        show elusia normal
        e "Tu viens manger avec nous ?"
        e "Il faut savoir décompresser."
        show alice angry
        a "Décompresser ? Décompresser ?"
        a "C'est tellement facile à dire."
        a "Désolée, mais je n'ai pas le temps d'aller glander en ville."
        menu:
            "Intervenir.":
                $ rel_ali += 2
                $ rel_lulu += 4
                $ rel_ryou += 2
                m "Hey, c'est bon, elle ne te voulait pas de mal !"
                m "Tu n'as pas besoin de l'agresser !"
                show alice geez
                a "Oui... Excuse moi Elusia, je suis sur les nerfs."
                e "C'est pas grave..."
            "Laisser passer.":
                m "..."
                r "Hey, c'est bon, elle ne te voulait pas de mal !"
                r "Tu n'as pas besoin de l'agresser !"
                show alice geez
                a "Oui... Excuse moi Elusia, je suis sur les nerfs."
                e "C'est pas grave..."
        show alice sad
        a "Désolée, mais je vais rester là."
        a "Si vous voulez m'aider, vous pourriez me rapporter un sandwich ?"
        e "Bien sur !"
        scene street
        show ryou normal at left
        show elusia normal at right
        "Nous sommes allés acheter des sandwichs."
        "Après en avoir apporté un à Alice, nous sommes allés au parc."
        scene parc with dissolve
        show elusia happy at right
        show ryou happy at left
        r "Alice n'est pas méchante, loin de là."
        r "Si elle a été aussi agressive c'est vraiment que ça va mal."
        m "Je comprends."
        "Nous avons parlé d'Alice jusqu'à la fin de la pause."
        "C'est quelqu'un de très sérieux."
        "Ryouzanki et elle se sont connus au collège et se sont retrouvés par hasard."
        "De nature timide, elle s'enflamme vite."
    else:
        show alice angry at right
        a "Ah, mais qui voilà !"
        a "J'ai perdu beaucoup de temps à t'attendre hier !"
        a "Je ne pensais pas que tu oserais venir te présenter devant moi tout naturellement le lendemain !"
        menu:
            "S'excuser.":
                m "Excuse moi..."
                $ rel_ali += 2
                a "Des excuses..."
                a "Je préfère de la présence."
                a "Je veux que tu viennes ce soir."
            "Ne rien dire.":
                m "..."
                $ rel_ali -= 2
                show alice geez
                a "Dis quelque chose au moins..."
                a "Par exemple que tu viendra ce soir..."
        a "Bon, j'ai énormément de travail."
        a "Allez manger sans moi."
        scene parc with dissolve
        show elusia sad at right
        show ryou sad at left
        r "Il faudrait vraiment l'aider..."
        e "Oui..."
        "Nous avons passé le repas en silence."
return

label day4_cours:
    $ renpy.music.play("music/jour.ogg", fadein=2)
    scene black with dissolve
    "La pause de midi est terminée."
    "Il faut retourner en cours..."
    scene classroom with dissolve
    "Comme toujours, Ryouzanki et Elusia se sont mis au premier rang."
    "Laura et Valeth sont au dernier rang."
    menu:
        "J'irais bien au premier rang...":
                show ryou sad at left
                show elusia normal at right
                "Le premier rang n'est pas aussi désagréable que ça..."
                "C'est amusant d'empêcher Ryouzanki de dormir en lui pinçant les côte..."
                $ rel_lulu += 2
                $ rel_ryou += 2
                "A la fin du cours, Alice est venue me voir."
                call day4_labo2
                r "Ce fut bref..."
                r "Je dois aussi assister à cette réunion."
                r "A plus !"
                hide ryou
                e "Je dois aussi te laisser, je dois rentrer chez moi récupérer mes affaires de sport."
                hide elusia
                jump day4_apres
        "J'irais bien au dernier rang...":
            show valeth normal at left
            show laura sad at right
            "Valeth passe son temps à dessiner en relevant la tête parfois pour suivre le cours."
            "Laura est très perplexe. On dirait qu'elle est ailleurs."
            $ rel_val += 2
            $ rel_lolo += 2
            "A la fin du cours, Alice est venue me voir."
            call day4_labo2
            v "C'était rapide."
            v "Je dois aussi aller ouvrir le club pour les autres."
            hide valeth
            l "Et moi je dois aller chercher mes affaires de sport."
            hide laura
            jump day4_apres
            
label day4_labo2:
    if aller_science == 3:
        show alice normal
        a "[j] ! Je voulais te voir."
        a "On a une réunion très importante avec des employers municipaux."
        a "Le club sera fermé donc aujourd'hui, repose toi bien."
        a "Je vais être en retard, à la prochaine !"
        hide alice
        return
    else:
        show alice sad
        a "[j] ! Je vais au labo."
        a "Tu es libre ? On y va maintenant ?"
        m "Oui, pas de souci."
        a "Je te laisse prendre tes affaires."
        a "Je t'attends dans le couloir."
        hide alice
        return
    
label day4_apres:
    if aller_science < 3:
        scene classroom with fade
        show alice normal
        a "Allons-y..."
        hide alice
        call labo
    else:        
        window hide None
        call screen demo_imagemap
        window show None
            
        if _return == "swimming":
            "Si j'en profitais pour faire du sport..."
            call sport
        
        elif _return == "science":
            "Les locaux sont fermés."
            "Il n'y a personne."
            jump day4_apres
            
        elif _return == "art":
            if aller_art >= 1:
                "Allons tenter de battre Valeth !"
            else:
                "Et si j'allais faire un tour au bâtiments des clubs..."
            call club
    
        elif _return == "go home":
            "Je crois que je vais rentrer."
            scene street with dissolve
            "Ah oui, Ryouzanki est allé à la réunion lui aussi..."

    $ renpy.music.play("music/joueur.ogg", fadein=2)
    scene couloir with dissolve
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    if aller_science == 3:
        "Maintenant, je me suis engagé à venir les aider pour le gala..."
        "Ou plutôt j'ai été forcé[ter]..."
    "3 eme jour fini."
    scene chambre m with dissolve
    play sound "sound/doorclose.mp3"
    "Je crois que je vais dormir."
    stop music
    return
