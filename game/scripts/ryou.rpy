# TODO easin + easeout
#            # $ renpy.block_rollback()

label ryou:
    define e = Character('Elusia', color="#FF69B4", show_two_window=True)
    define l = Character('Laura', color="#8B0000", show_two_window=True)
    define v = Character('Valeth', color="#800080", show_two_window=True)
    define y = Character('Lloyd', color="#FF8C00", show_two_window=True)
    define a =  Character('Alice', color="#228B22", show_two_window=True)
    define p = Character('Vincent', color="#2b2a64", show_two_window=True)
    define n = Character('Néphénie', color="#fd5f6e", show_two_window=True)
    define m = Character('Labrys', color="#58D3F7", show_two_window=True)
    define r = Character('Ryouzanki',
                 color="#58D3F7",
                 window_left_padding=160,
                 show_side_image=Image("test.jpg", xalign=0.03, yalign=0.97), show_two_window=True)
    define s = Character('Shadow',
                 color="#778899",
                 window_left_padding=160,
                 show_side_image=Image("test.jpg", xalign=0.03, yalign=0.97), show_two_window=True)

    
    $ weekday2='Dimanche'
    $ day2='19'
    $ month2='Mars'
label ryou_d1:
    scene black with dissolve
    play music (balombre) fadein 3
    p "Alors, Shadow ?"
    scene classroom
    show prof dark
    with fade
    p "Tu prends racine ?"
    p "Cet échiquier va prendre la poussière..."
    s "La ferme !"
    s "Je vérifiais juste que mon plan est parfait."
    s "S'il l'est, je devrais pouvoir m'emparer de ta dame en moins de 4 tours."
    "Je déplace mon cavalier."
    show prof naughty with dissolve
    p "Allons bon..."
    p "Rien de ce qui n'émane d'un humain ne peut être parfait."
    "Il ne déplace pas sa dame malgré ma mise en garde."
    s "Ne me mets pas dans le même bac que tes élèves !"
    s "Ne mêlange pas le joueur et ses pièces."
    p "Ses pièces ?"
    "Il déplace encore une autre pièce que sa dame."
    s "Oui, ta classe n'est qu'un échiquier géant pour moi..."
    p "Tu \"es\" dans ma classe."
    p "Tu fais donc partie de mes pions."
    s "Je ne suis pas un mouton !"
    p "Hooo ?"
    p "Alors tu te prétends loup ?"
    s "Je le suis."
    p "En attendant, je crois que tu n'as pas compris le but de ce jeu."
    "Il déplace sa tour et annonce :"
    show prof dark with dissolve
    p "Echec et mat."
    p "Tu confonds objectifs et moyens."
    p "Prendre ma dame en 4 tours ?"
    p "Mais je te l'offre !"
    p "Je la sacrifie pour me donner le temps de gagner la partie."
    p "Pour réussir, il faut parfois sacrifier des choses."
    s "Tsss..."
    s "Et maintenant, tu me fais la leçon..."
    show prof happy with dissolve
    p "Tu es mon élève."
    s "..."
    "Je pris sa dame dans ma main"
    s "Comment puis-je obtenir la dame ?"
    show prof naughty
    p "Si tu n'as pas une pièce de puissance équivalente à offrir en retour..."
    p "Tu peux faire en sorte qu'elle vienne à toi."
    "Incroyable... Il n'a même pas eut besoin de réfléchir pour comprendre..."
    "Je parlais bien de la classe et d'Elusia..."
    "Ca fait depuis le début de l'année que j'essaie de mettre la main dessus."
    "Mais à chaque fois, elle est si imprévisible..."
    p "Je te trouve bien perplexe..."
    s "Un pion de même équivalence, c'est quoi pour toi ?"
    p "Une marionnette parfaite qui la poussera vers toi..."
    p "Et pour ce qui est de la faire venir vers toi..."
    p "Elle est très sensible, alors détruit sa vie depuis les ombres."
    p "Elle se jettera dans tes bras réconfortants..."
    s "Je comprends... Maître."
    show prof dark with dissolve
    p "En parlant de pion parfait..."
    p "La nouvelle est arrivée samedi."
    p "D'après son dossier, elle habite dans ton immeuble."
    p "Tu sais ce qu'il te reste à faire !"
    s "L'isoler... La rendre indépendante de moi..."
    s "Tu vas m'aider ?"
    show prof annoyed with dissolve
    p "Quoi ?"
    p "Je t'ai suffisemment aidé comme ça..."
    p "Je ne peux que t'échanger des infos contre des rapports de la situation."
    p "Je n'agirais jamais sauf pour t'achever."
    s "M'achever ?"
    p "Oui, tu as parfaitement entendu."
    p "Je pense que tu vas perdre."
    p "Et je n'ai que faire des jouets cassés..."
    show prof naughty
    p "Sur ce..."
    p "Je retourne vous observez depuis mon trône dans les ténèbres."
    p "Je ne suis qu'un observateur, offrez moi un beau spectacle les enfants !"
    stop music fadeout 5
    scene black with dissolve
    pause 1
    scene couloir with dissolve
    "C'est quoi ce bruit ?"
    "C'est à cette heure ci qu'elle déballe ses cartons ?"
    "Quelle stupidité..."
    "Elle doit se lever tôt le lendemain en plus..."
    "Enfin bon, à cette heure-ci, Elusia aussi est éveilée alors pourquoi pas..."
    "Sonnons, portons le masque du gentil voisin accueillant."
    "N'est-ce pas Ryouzanki ?"
    play music (shadow1) fadeout 1.0
    r "Pfff..."
    play sound "sound/bell.mp3"
    r "Amène toi, j'ai pas que ça à foutre..."
    r "Je ne sais pas qui tu es mais tu m'énerves déjà..."
    "Je frappais mon poing contre la porte lorsqu'elle ouvrit..."
    play sound "sound/dooropen.mp3"
    "Quel timing..."
    "Improvise un truc, vite !"
    r "Merde !"
    r "Moi qui voulais tomber sur une jolie demoiselle en petite tenue..."
    "Quelle première rencontre avec mon futur tremplin..."
    "Pour qu'elle me serve, il faut la rapprocher d'Elusia..."
    "Chaque chose en son temps..."
    "J'ai encore un semestre..."
    stop music fadeout 1.0
    window hide
    hide screen button
    python:
        renpy.pause(1.0)
        renpy.scene()
        renpy.show('black')
        date_manager = date_manager.next_day(3)
        renpy.show('calendar', what=CalendarWidget(date_manager))
        renpy.with_statement(Fade(0.5, 0.0, 0.5))
        renpy.pause(8.0)
    window show
    show screen button
    $weekday2 = 'Lundi'
    $ day2 = date_manager.datetime.day
    $month2 = 'Mars'
    play music (shadow1) fadeout 1.0
    scene classroom
    show elusia happy at left
    e "Hey, pour ce midi, j'ai une superbe idée !"
    "T'as toujours des idées de merde..."
    r "Balance !"
    e "Et si aujourd'hui, on allait manger avec les autres au self pour les présenter à Labrys ?"
    e "Après tout, elle n'a pas encore rencontré tout le monde !"
    "Non mais non !!"
    r "Mouais... OK..."
    e "Alice ! Alice !"
    show alice normal at Position(xpos=0.4) with easeinleft
    a "Qu... Quoi ?"
    e "Et si on allait manger tous ensemble ?"
    show alice sad
    a "T... Tous ?"
    a "Tu veux dire... Toi, moi, baka-powa et Labrys ?"
    r "Baka powa ?"
    "Appelle moi encore une fois comme ça..."
    "Et je m'arrange pour que ton projet pour le gala foire."
    e "Non, plus de gens que ça !"
    e "Lloyd ! Tu veux bien déjeuner avec nous pour une fois ?"
    "Elle invite tous les gens chiants ou quoi ?"
    show lloyd normal at Position(xpos=0.65) with easeinright
    hide alice
    show alice sad at Position(xpos=0.4)
    y "En quel honneur ?"
    e "Mmmh... l'arrivée de Labrys !"
    y "Labrys est arrivée depuis 3 jours déjà."
    show elusia geez
    e "Misère, ce n'est pas une raison !"
    show alice geez
    a "Allons bon... Nous vous laisserons le siège d'honneur en boût de table, Sir."
    y "Non merci. Cela ne m'intéresse guère."
    y "Je rentre manger, mais j'apprécie l'intention."
    "C'est ça, casse toi."
    y "Au revoir et bon appétit."
    hide lloyd with easeoutright
    e "Tant pis."
    r "On vient de rater monsieur le vice président de l'Association des Elèves."
    a "Messire Lloyd Baptiste Reeds de Bellato."
    a "Alias Lloyd pour les intimes."
    "J'en ai marre d'entendre vos radots de jeunes écervellées..."
    "Je me casse."
    r "Bon, je vais chercher Valeth."
    stop music fadeout 1.0
    scene classroom with fade
    play music (balombre) fadein 3
    s "Hey, l'observateur !"
    show prof annoyed with easeinleft
    p "Ne m'appellez pas comme ça dans l'enceinte de l'école."
    s "Bien Pro-fe-sseur La-roi-je-se-a !"
    p "Que voulez vous ?"
    s "La dame a emené mon pion rencontrer d'autre pions."
    show prof naughty
    p "C'est mauvais pour toi."
    p "Mais je ne te conseillerai pas, débrouille toi."
    s "Je voulais juste te le dire, pour te \"vendre\" des infos."
    s "C'est ce que tu veux non ?"
    p "C'est rien ça."
    p "Tu me dira quand y'aura des disputes ou des rendez-vous galant."
    s "Entre deux filles ?"
    p "C'est encore mieux !"
    
label test:
    "position"
    show shadow ombre:
        left
    show alice normal:
        right
    with easeinleft
    "fin du test"
    a "le journal va etre incrementé"
    $ unlocked_journal_pages += 3
    menu:
        "A":
            $testjournal="A"
        "B":
            $testjournal="B"
    r "journal incrémenté"
    play music (joueur1) fadein 2
    m "Je suis un homme !"
    $rel_lulu +=10
    $ rel_ryou -=10
    e "Ryou, je t'aime !"
    # $ renpy.block_rollback()
    l "test"
    v "test"
    y "test"
    s "Je suis le maitre ici !"
    s "On va gagner elusia"
    $ persistent.route = max(persistent.route, 1)
    s "On a gagner elusia"
    s "On va gagner alice"
    $ persistent.route = max(persistent.route, 2)
    s "On a gagner alice"
