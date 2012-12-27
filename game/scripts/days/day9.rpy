label day9:
    scene reveil with fade
    play sound "sound/clock.mp3"
    ma "On est que mardi et je veux déjà un week-end..."
    stop sound
    play music (joueur1) fadein 2
    play sound "sound/bell.mp3"
    play sound "sound/dooropen.mp3"
    scene couloir
    show ryou sad:
        left
    show elusia normal:
        right
    with fade
    r "Yo !"
    e "Salutations !"
    scene street
    show ryou sad:
        left
    show elusia normal:
        right
    with fade
    pause(1)
    play music (matin1) fadein 2
    scene classroom
    show prof contraried at left
    with fade
    p "Et donc là, on obtient le bon résultat."
    p "Avec un calcul si savant que vous vous planterez tous au contrôle."
    p "Et je pourrais me délecter de vos mines décomposées devant vos notes catastrophiques."
    "Le cours continua sans encombre."
    "Maintenant, je comprends pourquoi les autres trouvent ce type bizarre."
    scene classroom 
    show elusia angry at left
    show ryou normal at right
    with fade
    e "\"Et je pourrais me délecter de vos mines décomposées devant vos notes catastrophiques.\""
    show elusia geez
    e "Misère..."
    show elusia angry
    e "Pour qui il se prend ?"
    menu:
        "Il tente de nous faire peur ?":
            m "Il tente de nous faire peur ?"
            show elusia sad
            e "Oui et non."
            r "On a tous de mauvaises notes."
            r "Mais je ne crois pas que ce soit pour ça."
        "Il note mal ?":
            m "Il note mal ?"
            r "Non, il ne note pas mal."
            show elusia sad
            e "Mais on a tous des notes médiocres."
    r "Il donne des questions tordues."
    r "Qui ont à peine un rapport avec le cours."
    e "On arrête là ?"
    r "OK, on va manger ?"
    m "Laura vient ?"
    r "Je ne sais pas, va donc lui demander."
    scene classroom
    show laura normal at left
    show valeth normal at right
    with fade
    v "Laura !"
    v "Où étais-tu hier ?"
    l "Bah... Je suis allée manger avec Elusia, [j] et Ryou..."
    v "Avec Elusia ?"
    v "Je croyais que vous ne vous entendiez pas ?"
    l "Ah bon ?"
    l "C'est parce qu'elle me parle toujours de sujets qui fâchent mais sinon je l'aime bien."
    v "Vous êtes allé manger où ?"
    l "Au parc d'Accrétia."
    v "C'est où ça ?"
    l "Tu ne sais pas où c'est ? Tu sors des fois ?"
    v "Bah oui mais pas partout..."
    v "Je peux venir avec vous ?"
    menu:
        "Bien sûr !":
            $ rel_val += 2
            $ rel_lolo += 2
            mh "Bien sûr !"
            l "Depuis quand t'es là toi ?"
            mh "Plus on est de fous plus on rit."
        "...":
            l "Je pense que personne n'y voit d'inconvénient."
    m "Laura, tu viens aussi bien sûr."
    l "Bien évidemment."
    scene parc
    show elusia happy at left
    show ryou normal at Position(xpos=0.375)
    show valeth normal at Position(xpos=0.625)
    show laura normal at right 
    with fade
    e "Plein de gens !"
    show ryou sad
    r "Il ne manque plus qu'Alice."
    r "Dommage qu'elle soit si occupée avec ses clubs."
    v "D'ailleurs en parlant de club..."
    v "J'ai quelques soucis avec le mien."
    v "Je n'ai pas beaucoup de membres."
    v "Et certains clubs vont être obligés de fermer."
    v "D'autres ne reçoivent plus de subventions."
    m "Des subventions ?"
    e "L'école investit pas mal d'argent dans ses clubs."
    e "Les clubs se battent pour avoir des inscrits parce que les subventions sont..."
    e "Proportionnelles au nombre d'actifs."
    v "Si vous pouviez vous inscrire et venir de temps en temps ce serait sympa."
    v "Les papiers sont prêts, ils n'attendent que vous dans le bâtiment des clubs."
    "Valeth a essayé de nous faire valoir ses clubs."
    "Je crois que ça m'était plus précisemment destiné."
    "Les clubs de cultures en mauvaise posture sont..."
    "\"Théâtre\" et \"Art plastique\"..."
    play music (jour1) fadein 2
    scene classroom with fade
    "Valeth était vraiment ailleurs."
    "Il n'a pas remarqué que le professeur l'interrogeait..."
    "Il s'inquiète probablement pour ses clubs."
    scene classroom with fade
    "Que pourrais-je bien faire de mon après midi..."
label day9map:
    window hide None
    call screen demo_imagemap
    window show None
        
    if _return == "gymnase":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "Il n'y a pas sport mardi."
        jump day9map
    
    elif _return == "science":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "J'irais bien voir Alice."
        call labo
        
    elif _return == "art":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "Et si j'allais voir Valeth..."
        call club

    elif _return == "rentrer":
        $ renpy.block_rollback()
        $ unlocked_journal_pages += 1
        "Je crois que je vais rentrer."
        call go_home
    
label day9_fin:
    play music (joueur1) fadein 2
    scene couloir with fade
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    "9 eme jour fini."
    scene chambre m with fade
    play sound "sound/doorclose.mp3"
    "Je vais dormir tôt."
    stop music
    return
