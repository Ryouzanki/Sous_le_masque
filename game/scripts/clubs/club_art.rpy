# TODO easin + easeout
#            $ renpy.block_rollback()
# ma mh
# sexe
label club:

    play music (club1) fadein 2
    scene salledart with fade
    
    if aller_art == 0:
        jump club_0
    elif aller_art == 1:
        jump club_1
    elif aller_art == 2:
        jump club_2
    #elif aller_art == 3:
        #$ aller_art += 1
        #jump club_3
    else:
        "BUG"
        return
        
label club_0:
    $ aller_art += 1
    show valeth normal
    if valou == 'Jeune homme':
        v "Salut !"
        v "T'es le nouveau dans la classe de Télécoms-Réseaux avec moi non ?"
        m "Je ne sais pas..."
        m "Mais je suis bien en Télécoms-Réseaux."
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
    show elusia geez at right
    e "Misère..."
    show ryou happy
    r "Bonne chance Valeth !"
    v "Hein ?"
    r "[j] est imbattable aux d'échec dans sa région !"
    r "Et oui, [sexe] ne va faire qu'une bouchée de toi !"
    e "Misère de misère..."
    e "Ryou, à quoi cela te sert-il de débiter ce genre de stupidité ?"
    show ryou surprised
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
    show ryou surprised at left
    show elusia happy at right
    r "Attends... Il s'est passé quoi là ?"
    e "Hi hi, tu me dois une boîte de thé !"
    r "Nan, sérieusement, Valeth, tu as..."
    show ryou angry
    r "T'as fait exprès, espèce de traitre !!"
    r "Combien est-ce que la déléguée t'a payé pour perdre ?"
    show elusia satisfied
    e "Misère... Je ne l'ai pas soudoyé !"
    show elusia happy
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
    
label club_2:
    $ aller_art += 1
    show valeth normal
    v "Oh, bonjour [j] !"
    v "Tu es venu[ter] m'écrabouiller à nouveau ?"
    menu:
        "Je veux rejouer.":
            $ rel_val += 5
            m "Oui, je vais rejouer contre toi."
            v "Très bien. Je vais pouvoir tenter de prendre ma revanche !"
            v "Commence donc !"
            $ int_points += 2
            "Je joue aux échecs contre Valeth."
            "Je joue aussi bien que la dernière fois."
            "Voir mieux même."
            "Cette fois, Valeth n'a rien laissé au hasard et je perds."
            v "Excellent partie [j]."
            m "Tu m'avais bien laissé gagné la dernière fois."
            v "C'est possible."
            jump art3_fin
        "Non, pas cette fois.":
            m "Non, pas cette fois Valeth."
            v "Oh... Dommage."
            v "Tu veux faire un jeu de plateau à la place ?"
            menu:
                "Oui":
                    m "Oui, pourquoi pas !"
                    v "C'est partit."
                    "J'ai joué à divers jeux de réflexion avec Valeth."
                    "C'était amusant."
                    $ int_points += 1
                    $ rel_val += 2
                    jump art3_fin
                "Non":
                    m "Non, merci, une autre fois."
                    m "Je vais rentrer."
                    v "Déjà ? Tu viens juste d'arriver..."
                    v "Très bien, à la prochaine !"
                    return
label art3_fin:
            $ aller_art += 1
            v"On dirait qu'il ne reste plus que nous."
            v "Je vais rentrer donc je vais devoir fermer les locaux."
            v "Désolé de te kicker aussi brutalement !"
            m "Que veux tu que je fasses ici seul[ter] de toutes façons ?"
            v "Ouais, j'y avais pensé mais bon."
            "Il n'y a vraiment que nous."
            "Ce silence pesant n'est brisé que par Valeth qui vérouille des portes."
            "Et si j'en profitais ?"
            m "Dis moi Valeth..."
            v "Oui ?"
            menu:
                m "Que penses-tu de :"
                "Elusia ?":
                    extend "Elusia ?"
                    v "Elusia... C'est une chouette fille."
                    v "Toujours en duo inséparable avec Ryou."
                    v "Elle est plutôt sérieuse et dynamique."
                    v "Aussi serviable qu'attentionnée."
                    v "On dirait qu'elle a peur de la solitude..."
                "Ryouzanki ?":
                    extend "Ryouzanki ?"
                    v "Je ne sais pas..."
                    v "C'est quelqu'un de très gentil et de plutôt présent."
                    v "Il ne quitte jamais Elusia des yeux."
                    v "Personnellement, je l'aime bien."
                    v "Il y a quelque chose qui cloche avec lui."
                "Laura ?":
                    extend "Laura ?"
                    v "Je l'aime bien."
                    v "Même si elle paraît méchante, ce n'est pas le cas."
                    v "C'est quelqu'un de très juste et honnête."
                    v "C'est juste que c'est la déléguée malgré elle."
                    v "Alors elle ne prend pas son rôle très à coeur."
                    v "D'où cette animosité avec Elusia."
                "Lloyd ?":
                    extend "Lloyd ?"
                    v "Il est clairement issu d'un autre monde que nous celui-là."
                    v "Il est né dans un cocon loin de tous."
                    v "Entouré de domestiques toujours d'accord avec lui quoi."
                    v "Du coup il a du mal à comprendre qu'on peut ne pas être d'accord avec lui."
                    v "Mais c'est pas quelqu'un de méchant, il fait vraiment des efforts pour changer."
                "Alice ?":
                    extend "Alice ?"
                    v "Je l'aime beaucoup !"
                    v "C'est mon miroir."
                    v "Elle est très sérieuse mais très timide."
                    v "Elle ose rarement demander de l'aide."
                    v "Si tu la vois dans le besoin, n'hésite pas à lui proposer de l'aide."
                    v "Elle ne croit qu'en ce qu'elle voit."
                    v "Si je croyais au destin, je le remercirais de nous avoir mis à des postes en opposition !"
                "Moi ?":
                    extend "Moi ?"
                    $ rel_val += 2
                    v "Haha, ne t'en fais pas."
                    v "Je pense que comme moi, tout le monde t'apprécie."
                    v "Désolé si on t'agresse un peu mais on est tous très curieux !"
                "Rien, oublie...":
                    extend "Rien, oublie..."
                    show valeth happy
                    v "Hey, je mords pas tu sais !"
                    v "Personnellement, je pense que tu devrais être honnête."
                    v "Et satisfaire ta curiosité aussi ! N'hésites pas hein !"
            v "Oh pardon, je m'égare !"
            v "On a fait le tour des salles."
            v "Bon bah, à demain !"
            return
            
# label club_3:
    # # le +1 à aller_club est deja fait
    # show lloyd normal
    # "On dirait que Valeth n'est pas là..."
    # menu:
        # "Que faire..."
        # "Rentrer chez moi":
            # "Je vais rentrer chez moi."
            # return
        # "Attendre en silence.":
            # "..."
            # "Bon, et maintenant ?"
            # jump club_3
        # "Parler à Lloyd.":
            # $ rel_lloy += 5
            # m "Salut !"
            # y "Bien le bonjour [j]"
            # m "Qu'est ce que tu fais là ?"
            # y "Je suis venu jouer."
            # y "Comme tout le monde non ?"
            # m "Heu... T'as l'air"
            # 
