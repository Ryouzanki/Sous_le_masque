label day11:
    if (rel_lulu < 50) or (rel_ryou < 50):
        jump day11_classe
    scene reveil with fade
    play sound "sound/clock.mp3"
    ma "Mince, j'ai oublié de reculer mon réveil..."
    stop sound
    play music (joueur1) fadein 2
    play sound "sound/dooropen.mp3"
    scene couloir
    show ryou sad
    with fade
    r "Yo !"
    m "Qu'est-ce que tu fiches ici ?"
    show ryou surprised
    r "C'est ma question ça !"
    r "Tu me voles encore ma question !"
    m "Ca va, ça va..."
    show ryou normal
    r "Je suis juste venu te réveiller au cas où."
    r "Et faire un boût de chemin avec toi pour aller acheter des bougies."
    r "C'est plus discret et rapide. Je ferais ma part, t'en fais pas."
    m "OK."
    scene street
    show ryou normal
    with fade
    r "Bon, la meilleure pâtisserie de la ville est au boût de cette rue."
    r "La supérette est de l'autre côté."
    r "A plus !"
    show ryou happy
    r "Et silence sur toute la ligne hein !"
    m "Oui, je saurais tenir ma langue."
    hide ryou with easeoutleft
    scene street with fade
    "La voilà."
    "C'est un établissement plutôt modeste mais la vitrine est alléchante."
    "J'entre."
    "Il n'y a qu'une personne à l'intérieur."
    play music (nephie1) fadein 2
    scene boulangere with fade
    "Sauf elle."
    "Cette boulangère là."
    "Mais... Mais !"
label day11_nephie:
    menu:
        "Qu'est-ce que tu fais là, Elusia ?":
            # $ renpy.block_rollback()
            m "Qu'est-ce que tu fais là, Elusia ?"
            scene boulangerie
            show nephie normal
            with fade
            n "M~... Moi ?"
            n "Et bien je travaille et toi ?"
            n "Il faut bien payer le loyer !"
            menu:
                "Attends une minute...":
                    # $ renpy.block_rollback()
                    ma "Attends une minute..."
                    ma "Tu n'es pas Elusia ?"
                    show nephie vhappy
                    n "Eh non !"
                    n "Mais tu n'es pas passé loin !"
                    n "Tu es venu[ter] chercher un gâteau n'est-ce pas ?"
                    m "Comment~..."
                "Je suis passé[ter] par hasard.":
                    # $ renpy.block_rollback()
                    m "Je suis passé[ter] par hasard."
                    show nephie happy
                    n "Je ne crois pas à ce hasard."
                    n "Tu es venu[ter] m'acheter quelque chose n'est-ce pas ?"
                    n "Au hasard... Un gâteau ?"
                    menu:
                        "Pas vraiment non.":
                            # $ renpy.block_rollback()
                            ma "Pas vraiment non."
                            show nephie sad
                            n "Ewwww..."
                            n "Vraiment ?"
                            m "Je dois aller en cours."
                            m "Tu devrais y aller aussi. Ryouzanki doit t'attendre."
                            n "Tu fais erreur, je ne suis pas Elusia."
                            n "Donc tu ne veux rien acheter ?"
                            n "Sûr de sûr ?"
                            menu:
                                "Oui.":
                                    # $ renpy.block_rollback()
                                    ma "Oui."
                                    n "Sûr de sûr de sûr ?"
                                    menu:
                                        "(Partir)":
                                            # $ renpy.block_rollback()
                                            "Je sors de la boutique."
                                            "Elle me regarde partir en silence."
                                            "J'ai un très mauvais pressentiment."
                                            "Je devrais revenir sur mes pas."
                                            "Mais je n'ai plus vraiment le temps."
                                            jump day11_bad
                                        "(Faire un achat)":
                                            # $ renpy.block_rollback()
                                            m "Bon d'accord, je vais acheter quelque chose avant de partir."
                                            show nephie normal
                                            n "Un gâteau alors ?"
                                "Je peux bien acheter quelque chose en route.":
                                    # $ renpy.block_rollback()
                                    m "Je peux bien acheter quelque chose en route."
                        "Oui, c'est exact.":
                            # $ renpy.block_rollback()
                            m "Oui, c'est exact."
                "Je suis venu[ter] acheter quelque chose.":
                    # $ renpy.block_rollback()
                    m "Je suis venu[ter] acheter quelque chose."

        "(Ressortir discrètement.)":
            # $ renpy.block_rollback()
            m "..."
            scene boulangerie
            show nephie angry
            with fade
            n "Hey !"
            n "On ne t'a pas appris à dire bonjour aux gens toi ?"
            "Mince... Que faire ?"
            menu:
                "(S'enfuir en courant.)":
                    # $ renpy.block_rollback()
                    show nephie sad
                    n "Mais attends !"
                    n "Je mords pas les gens !"
                    jump day11_bad
                "Acheter quelque chose.":
                    # $ renpy.block_rollback()
                    m "Bonjour !"
                    m "Excusez moi, j'étais ailleurs."
                    show nephie normal
                    m "..."
                    n ".......... Oui ?"
                    m "Rien."
                    "Elle ne me reconnait pas. Ce n'est pas Elusia."
                    m "Je prendrais ce gâteau au chocolat."
                    show nephie happy
                    n "Excellent choix. Probablement le meilleur rapport qualité prix de la boutique."
                    show nephie vhappy
                    n "Et le voilà !"
                    m "Merci, au revoir."
                    jump day11_like_a_boss
    show nephie vhappy
    n "Tu vois ce gâteau aux fraises ?"
    m "Il est un peu cher pour un[ter] étudiant[ter]..."
    show nephie normal
    n "Pas si je te le fais à moitié prix."
    m "Pourquoi tu ferais ça ?"
    n "Je le fais si tu réponds à une question."
    n "En fonction de la réponse, je te le fais à moitié prix."
    m "Heu... D'accord..."
    "J'ai des mauvais souvenirs à cause de Laroijesea..."
    n "Pour qui est ce gâteau ?"
    n "Il est pour Elusia non ?"
    m "..."
    show nephie happy
    n "Tu m'as appelé Elusia donc tu la connais."
    n "Et venir acheter un gâteau pile le jour de son anniversaire, c'est suspect."
    m "Tu gardera le secret ?"
    n "Oh et bien si tu l'achètes !"
    m "Bien entendu."
    n "Merci... [j]."
    m "..."
    n "Sais-tu qui je suis ?"
    menu:
        "Sa mère.":
            # $ renpy.block_rollback()
            m "Sa mère ?"
            show nephie surprised
            n "Heyyyyy ?"
            show nephie sad
            n "J'ai l'air si vieille que ça ?"
            n "Nous n'avons pourtant que 6 ans de différence..."
            n "Je suis sa grande soeur !"
        "Sa soeur.":
            # $ renpy.block_rollback()
            m "Sa soeur ?"
            show nephie surprised
            n "Bien joué !"
            show nephie vhappy
            n "Pas trop dur, on dit souvent qu'on se ressemble."
            n "On a pourtant 6 ans de différence..."
        "Une amie.":
            # $ renpy.block_rollback()
            m "Une amie ?"
            show nephie happy
            n "Perdu."
            n "Je suis sa grande soeur !"
            n "Je suis plus agée de 6 ans."
        "Sa marraine.":
            # $ renpy.block_rollback()
            m "Sa marraine ?"
            show nephie happy
            n "Perdu. On est athées."
            n "Je suis sa grande soeur !"
            n "Je suis plus agée de 6 ans."
    n "Je suis Néphénie Hrist, pour vous servir !"
    $ boul = 'Néphénie'
    show nephie vhappy
    n "Bref, voilà ton gâteau. Amusez vous bien !"
    mh "Merci, au revoir !"
label day11_like_a_boss:
    # AWESOME CAKE
    # boul == 'Néphénie'   <==>    AWESOME CAKE
    # Else : Cake normal
label day11_bad:
    # label ou on a pas buy le cake D:
label day11_classe:
    # label ou l'anniv d'elusia n'a pas lieu
    # EH et RZ lachent Minato qui se retrouve avec Laura
    # Laura mange avec lui et lui explique pourquoi ils sont seuls
