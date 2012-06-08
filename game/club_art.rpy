label club:

    $ renpy.music.play("music/club.ogg", fadein=2)
    scene salledart with dissolve
    
    if aller_art == 0:
        jump club_0
    elif aller_art == 1:
        jump club_1
        
label club_0:
    $ aller_art += 1
    show valeth normal
    if valou == 'Jeune homme':
        v "Salut !"
        v "T'es le nouveau dans la classe de GTR avec moi non ?"
        m "Je ne sais pas..."
        m "Mais je suis bien en GTR."
        v "Oui je sais. Tu étais assis à l'autre boût du rang."
        v "Oh ! Mais je me présente : je suis Valeth !"
        $ valou = 'Valeth'
    elif rel_val >= 5:
        v "Ah ! Te voilà enfin !"
        v "Je t'attendais !"
    else:
        v "Tiens ! Je ne m'attendais pas à te voir !"
        
    v "Je suis responsable de tout ce qui est associatif !"
    v "Bienvenu dans le bâtiment des clubs !"
    v "Il n'y a aucune inscription. Aucune obligation."
    v "Tu fais ce qu'il te plaît."
    v "Mais le matériel des clubs ne doit pas sortir des locaux."
    v "Des questions ?"
    m "Non, c'est bon."
    v "Tu sais jouer aux échecs ?"
    m "Oui, bien sûr. Mais je ne suis pas très compétent !"
    v "Ce n'est pas très important."
    v "Je te défie !"
    menu:
        "Accepter.":
            m "OK, c'est partit !"
            "C'était stressant."
            "Valeth n'a pas dit grand mot de la partie."
            "Ce sourire sur de lui ne quittait pas ses lèvres."
            "Je suis suis fait[ter] ramassé[ter] en beauté."
            "Il est bien trop fort."
            "Au moment de partir, Valeth m'a montré[ter] le chemin du retour."
            $ rel_val += 5
            $ int_points += 2
        "Refuser.":
            m "Nan merci, ça ira."
            v "Ah..."
            v "Tu veux jouer à autre chose ?"
            menu:
                "Et si j'essayais un de leur jeu ?":
                    $ rel_val += 2
                    $ int_points += 1
                    m "Je crois que je vais essayer autre chose."
                    v "D'accord. On a toute une armoire de jeux !"
                    v "Je te laisse choisir."
                    "J'ai passé tout l'après midi à jouer avec Valeth à divers jeux."
                    "C'était divertissant."
                    "Au moment de partir, Valeth m'a montré[ter] le chemin du retour."
                "Non, je venais juste voir.":
                    m "Non, ça ira."
                    m "Je venais juste regarder."
                    v "Ah... Comme tu voudra..."
                    "Valeth m'a raccompagné jusqu'à la grille de l'école et m'indiqua le chemin."
    hide valeth
    return
   
label club_1:
    $ aller_art += 1
    show valeth normal
    v "Oh ! Te revoilà !"
    m "Salut !"
    show ryou angry at left
    r "Je vous attendais monsieur Bond !"
    show elusia sad at right
    e "Misère..."
    show ryou happy
    r "Bonne chance Valeth !"
    v "Hein ?"
    r "[j] est imbattable aux d'échec dans sa région !"
    r "Et oui, [sexe] ne va faire qu'une bouchée de toi !"
    e "Misère de misère..."
    e "Ryou, à quoi cela te sert-il de débiter ce genre de stupidité ?"
    show ryou normal
    r "C'est fun."
    v "Commence donc !"
    hide elusia
    hide ryou
    $ int_points += 2
    "Je joue aux échecs contre Valeth."
    "Pendant que les deux autres sont partis jouer aux cartes."
    "Il mène largement."
    "Subitement, il enchaîne les erreurs d'étourderie."
    "Je remporte la partie."
    show ryou angry at left
    show elusia happy at right
    r "Attends... Il s'est passé quoi là ?"
    e "Hi hi, tu me dois une boîte de thé !"
    r "Nan, sérieusement, Valeth, tu as..."
    r "T'as fait exprès, espèce de traitre !!"
    r "Combien est-ce que la déléguée t'a payé pour perdre ?"
    show elusia normal
    e "Misère... Je ne l'ai pas soudoyé !"
    e "Allons-y, avant que les magasins ne ferment..."
    e "Un pari est un pari !"
    show ryou sad
    r "Ouais, j'arrive..."
    hide elusia
    hide ryou
    menu:
        "Heu Valeth..."
        "Tu m'as offert la victoire n'est-ce pas ?":
            $ rel_val += 3
            m "Tu m'as offert la victoire n'est-ce pas ?"
            show valeth happy
            v "Allons, qu'est-ce qui te fais dire ça ?"
            menu:
                "Merci.":
                    m "Merci."
                    show valeth normal
                    v "Ho, c'est pas grand chose."
                "Tu n'aurais pas du...":
                    $ rel_val += 3
                    m "Tu n'aurais pas du..."
                    show valeth normal
                    v "Pourquoi cela ?"
                    m "Gagner ou perdre, ce n'est pas important pour moi."
                    m "En plus, tu méritais de gagner."
                    show valeth happy
                    v "Vraiment ? Nous sommes pareil alors..."
        "Merci pour la partie.":
            v "Oh, tout le plaisir est pour moi."
            v "J'espère pouvoir jouer de nouveau contre toi !"
            
    v "Bon, je m'en vais."
    v "Tu peux rester ici autant que tu le souhaite."
    m "Non, je vais partir aussi."
    hide valeth
    return
