# TODO easin + easeout
#            $ renpy.block_rollback()

label sport:
    if aller_sport == 0:
        jump sport_0
    #elif aller_sport == 1:
     #   jump sport_1
    else:
        "BUG"
        return

label sport_0:
        $ aller_sport +=1
        if rel_lulu > 2:
            scene gymnaseout with dissolve
            pause(1)
            $ fille = '???'
            scene black with dissolve
            m "Qu'est ce que..."
            "Quelqu'un m'a mis les mains devant les yeux..."
            e "Te voilà toi !"
            e "Devine qui c'est !"
            menu:
                "Elusia !":
                    m "Elusia !"
                    $ fille = 'Elusia'
                    scene gymnaseout with dissolve
                    show elusia happy sport
                    e "Bingo !"
                    $ rel_lulu += 5
                    jump lulu
                "Ryouzanki !":
                    m "Ryouzanki !"
                    $ fille = 'Elusia'
                    jump troll
                "Lloyd !" if rel_lloy >= 5:
                    m "Lloyd !"
                    $ fille = 'Elusia'
                    jump troll
                "Alice !" if rel_ali >=5:
                    m "Alice !"
                    $ fille = 'Elusia'
                    jump alice
                "Laura !"if rel_lolo >= 5:
                    m "Laura !"
                    $rel_lulu -=2
                    jump laura
                "Valeth !"if rel_lolo >= 5:
                    m "Valeth !"
                    $ fille = 'Elusia'
                    jump troll
                    
        else:
            jump lolo
label alice:
    scene gymnaseout with dissolve
    show elusia happy sport
    e "Perdu !"
    e "C'est moi ! Elusia !"
    jump lulu
            
label laura:
    e "Oh..."
    e "Tu as donc fait la connaissance de Laura..."
    $ fille = 'Elusia'
    scene gymnaseout with dissolve
    show elusia geez sport
    e "Je suppose qu'elle t'a recommandé de m'éviter et tout ça..."
    menu:
        "Oui...":
            m "Oui..."
            e "Et bien... Au revoir..."
            hide elusia
            "Elle a l'air vraiment triste..."
            $ rel_lulu -= 5
            jump lolo
        "Non.":
            m "Non."
            show elusia sad sport
            e "Je sais qu'elle l'a fait..."
            e "Elle le fait toujours..."
            show elusia geez sport
            e "Bon et bien... Au revoir..."
            hide elusia
            "Elle a l'air assez triste..."
            jump lolo
        "Je m'en fiche.":
            m "Je m'en fiche."
            show elusia sad sport
            e "Je vois..."
            jump lulu
            
label troll:
    scene gymnaseout with dissolve
    show elusia sad sport
    e "J'ai..."
    extend "J'ai une voix d'homme ?"
    menu:
        "Ouep.":
            m "Ouep."
            show elusia angry sport
            e "Pfff... Sympa..."
            e "Bon, j'ai tennis."
            e "Bye !"
            hide elusia
            "Je crois qu'elle est vexée..."
            $ rel_lulu -=5
            jump lolo
        "Mais non.":
            m "Mais non."
            m "Je plaisantais."
            e "Ah..."
            e "Navrée, je n'ai pas un sens de l'humour très développé."
            e "Et donc ?"
            jump lulu
    
label lulu:
    show elusia normal sport
    e "Que fais tu ici ?"
    e "T'es venu[ter] faire du sport ?"
    menu:
        "Oui.":
            m "Oui."
            e "Je vois."
            e "Est ce que ça t'intéresse du tennis ou du tir à l'arc ?"
            menu:
                "J'aime bien le tennis.":
                    m "J'aime bien le tennis."
                    $ sport = 'tennis'
                    $ sport2 = 'solo'
                    $ rel_lulu += 5
                    jump sport_solo         
                "Le tir à l'arc, c'est intéressant.":
                    m "Le tir à l'arc, c'est intéressant."
                    $ sport = 'tir à l\'arc'
                    $ sport2= 'solo'
                    $ rel_lulu += 5
                    jump sport_solo
                "Non merci.":
                    m "Non merci."
                    show elusia sad sport
                    e "D'accord..."
                    e "Bon, j'ai tennis."
                    show elusia normal sport
                    e "Bye !"
                    hide elusia
                    jump lolo
        "Pas vraiment non.":
            m "Pas vraiment non."
            e "Je vois."
            e "Bon, j'ai tennis."
            e "Bye !"
            hide elusia
            jump lolo
                    
label lolo:
    scene gymnase with dissolve
    show laura normal
    if en == 'Jeune fille':
        
        l "Salut !"
        l "Je t'ai aperçu vite fait ce matin, on est dans la même classe !"
        m "C'est possible."
        l "Je m'appelle Laura !"
        $ en = 'Laura'
        l "Je suis une des déléguée de ta classe."
        l "Je m'occupe aussi des clubs de sport collectif."
        l "Je ne sais pas si tu sais, mais ici, le sport est obligatoire."
        l "Puisque tu es là, on va t'inscrire tout de suite."
        l "Handball ou volley ?"
        jump sport_collectif
         
    else:
        l "Ah, je dois avouer que je ne m'attendais pas à te voir ici !"
        m "Pourtant je suis là !"
        l "Oui oui..."
        l "Et t'es vraiment venu pour faire du sport ou ...?"
        menu:
            "Je suis venu pour ça !":
                m "Je suis venu pour ça !"
                show laura happy
                l "Super !"
                l "Tu veux faire quoi ?"
                l "Handball ou Volley ?"
                $ rel_lolo += 5
                jump sport_collectif
            "Je ne faisais que passer.":
                m "Je ne faisais que~"
                show laura angry
                l "Non non non !"
                l "Le sport est obligatoire."
                l "Puisque tu es là, on va t'inscrire tout de suite."
                l "Handball ou volley ?"
                jump sport_collectif
                
label sport_collectif:
    menu:
        "Va pour le handball":
            m "Va pour le handball"
            $ sport = 'handball'
            $ sport2 = 'multi'
            jump sport_col
        "Le volley me tente bien...":
            m "Le volley me tente bien..."
            $ sport = 'volley'
            $ sport2 = 'multi'
            jump sport_col
        
label sport_col:
    
        hide laura
        if bite:
                "C'est ainsi que je me retrouvais inscrit dans l'équipe masculine de [sport]."
                "Laura est un manager impitoyable."
                "Elle ne m'a pas ménagé..."
                $ vig -= 2
        else:
                "C'est ainsi que je me retrouvais inscrite dans l'équipe féminine de [sport]."
                "J'ai joué dans l'équipe de Laura et nous avons gagné."
                "Laura est vraiment compétente !"
                $ vig -= 2
                
        "A la fin de la séance, Laura m'a indiqué le chemin pour rentrer chez moi."
        if sport == 'handball':
            if vig >=0:
                $ str_points += 2
            else:
                "J'étais trop fatigué[ter] pour être efficace."
            pass
        else:
            if vig >= 0:
                $ str_points += 1
                $ agi_points += 1
            else:
                "J'étais trop fatigué[ter] pour être efficace."
            pass
        return
        
label sport_solo:
    hide elusia
    if sport == 'tir à l\'arc':
        $ vig -= 2
        "C'est ainsi que je me retrouvais dans l'équipe de tir à l'arc de l'école."
        "Elusia est vraiment compétente."
        "Incroyablement calme, elle fait toujours mouche."
        if vig >= 0:
            $ agi_points +=2
        else:
            "J'étais trop fatigué[ter] pour être efficace."
    if sport == 'tennis':
        $ vig -= 2
        $ agi_points +=1
        $ str_points +=1
        if bite:
                "C'est ainsi que je me retrouvais inscrit dans l'équipe masculine de tennis."
                "Elusia est un manager autoritaire."
                "Je n'ai pas été ménagé..."
        else:
                "C'est ainsi que je me retrouvais inscrite dans l'équipe féminine de tennis."
                "J'ai joué contre diverse personne mais pas Elusia."
                "Heureusement, car j'aurais été ridiculisée"
        "Dur la reprise..."
        if vig >=0:
            $ agi_points +=1
            $ str_points +=1
        else:
            "J'étais trop fatigué[ter] pour être efficace."
        
    "Elusia m'a raccompagné[ter] jusqu'à l'immeuble."
    "Puis, elle est partie car elle avait des choses à faire."
    return
    