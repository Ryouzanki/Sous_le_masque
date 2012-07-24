init python:
    tutorials = [
        ("tuto_lulu", "Relations sociales", "v1"),
        ("tuto_val", "L'interface de jeu", "v1"),
        ("tuto_lolo", "Les commandes", "v1"),
        ("tuto_ali", "Les statistiques", "v1"),
        ("tuto_sha", "Fin du jeu et bonus", "v1"),

        ]
screen tutorials:

    side "c r":
        area (250, 40, 548, 400)
        
        viewport:
            yadjustment adj
            mousewheel True
            
            vbox:
                for label, name, ver in tutorials:
                    button:
                        action Return(label)
                        left_padding 20
                        xfill True
                        
                        hbox:
                            text name style "button_text" min_width 420
                            text ver style "button_text"
                            
                null height 20

                textbutton "J'ai tout ce que je voulais savoir.":
                    xfill True
                    action Return(False) 
                
        bar adjustment adj style "vscrollbar" 
label tuto:
    play music (thinking1) fadein 2
    define e = Character('Elusia', color="#FF69B4", show_two_window=True)
    define r = Character('Ryouzanki', color="#4169E1", show_two_window=True)
    define l = Character('Laura', color="#8B0000", show_two_window=True)
    define v = Character('Valeth', color="#800080", show_two_window=True)
    define y = Character('Lloyd', color="#FF8C00", show_two_window=True)
    define a =  Character('Alice', color="#228B22", show_two_window=True)
    define s = Character('Shadow', color="#778899", show_two_window=True)
    window show
    show ryou angry with easeinright
    r "Heu... Où est-ce que je suis là..."
    show ryou happy
    r "Ah tiens ! Un nouveau visage !"
    show ryou normal
    r "Je suppose que t'es là pour apprendre à jouer..."

    $ tutorials_adjustment = ui.adjustment()
    $ tutorials_first_time = True
    
    while True:
        show ryou normal at left with easeinleft
        with move

        if tutorials_first_time:
            $ r("Que veux tu savoir ?", interact=False) 
        else:
            $ r("Tu veux savoir autre chose ?", interact=False) 

        $ tutorials_first_time = False

        call screen tutorials(adj=tutorials_adjustment)
        
        show ryou normal at center
        with move

        if _return is False:
            jump end_tuto

        call expression _return
label end_tuto:
    show ryou happy
    r "Voilà, j'ai fini mon travail."
    r "Bon jeu !"
    return
label tuto_lulu :
    show ryou sad
    r "J'suis nul en relations humaines..."
    r "Elusia ! Viens me remplacer..."
    hide ryou with easeoutleft
    show elusia geez with easeinright
    e "Misère... Ryou, espèce de bras-cassés..."
    show elusia normal
    e "Les relations sociales sont un élément important du jeu."
    e "Elles sont représentées par des nombres."
    show elusia satisfied
    e "Plus le nombre est grand, plus la personne concernée t'adore."
    show elusia normal
    e "Les choix dans ce jeu feront grimper ou descendre ces nombres."
    e "Ca commence à 0 et ça ne peut pas passer dans le négatif."
    e "Des amis auront tendance à t'aider plus souvent ou à sortir avec toi."
    e "Certaines actions nécessitent qu'une personne t'apprécie."
    show elusia satisfied
    e "Voilà, je crois avoir tout dit."
    show elusia happy
    e "Ryou, je te rends la main !"
    hide elusia with easeoutright
    return
label tuto_val :
    show ryou angry
    r "L'interface de jeu ?"
    r "Je suis un personnage du jeu..."
    r "Je ne la vois pas l'interface..."
    v "Place ! Place !"
    hide ryou with easeoutleft
    show valeth happy with easeinright
    v "L'interface de jeu..."
    show valeth normal
    v "Tout d'abord, le \"QuickMenu\"..."
    v "C'est le machin en bas à droite de la boite de dialogue."
    v "Il contient 6 options."
    v "Les 2 premières servent à effectuer et charger des mini-sauvegardes."
    v "\"Q.Load\" t'amènera à la dernière fois que tu as cliqué sur \"Q.Save\"."
    v "\"Sauvegarde\" te donne accès aux vrais sauvegardes."
    v "Tu peux aussi accéder aux anciennes \"Q.Save\"."
    v "\"Avance rapide\" permet de jouer en accéléré."
    v "L'accélération cessera au premier choix rencontré ou si tu cliques."
    v "\"Auto\" fera défiler le texte automatiquement."
    v "\"Auto\" s'arrêtera aux même condition qu'\"Avance rapide\"."
    v "Enfin, \"paramètres\" contient divers options sur \"Avance rapide\" et \"auto\"."
    v "Il contient aussi le réglage volume."
    show valeth happy
    v "Maintenant on passe au plus intéressant !"
    v "Les boutons du jeu !"
    show valeth normal
    v "\"Stats\" te permets de voir tes compétences."
    v "Alice t'expliquera mieux ce genre de chose."
    v "\"Relations\" permet de voir comment tu t'entends avec les 8 personnages du jeu."
    v "Sous forme de chiffre et de barre. Une barre remplie est très difficile à avoir."
    show shadow ombre at left with easeinleft
    s "Voire impossible."
    show valeth angry
    v "On t'as pas sonné toi !"
    s"..."
    hide shadow with easeoutleft
    show valeth normal
    v "Ne cherches pas à avoir une barre à 100\%."
    v "Essaie de les équilibrer."
    v "\"Records\" te permet de voir tes meilleures barres de relations."
    v "Toutes parties confondues."
    v "\"Résumé\" contient divers informations sur ta santé et autres."
    v "Il contient aussi un \"journal\" intime qui sert de synopsis."
    show valeth happy
    v "Voilà, c'est tout !"
    v "Ryou, reprends ta place !"
    hide valeth with easeoutright
    return
label tuto_lolo :
    show ryou sad
    r "Les commandes..."
    r "Je sais plus moi..."
    r "Laura ?"
    hide ryou with easeoutleft
    show laura sad with easeinright
    l "Pourquoi il faut que ça soit moi ?"
    show laura normal
    l "Soit !"
    l "Je ne t'explique pas le clic-droit et clic-central, tu n'as qu'à essayer."
    l "Le droit ouvre le menu des sauvegardes."
    l "Echap aussi."
    l "La molette sert à retourner en arrière et revenir en avant."
    l "Pour ce qui est du clavier..."
    show laura happy
    l "A vos crayons les enfants !"
    l "S (Screenshot) : Capture d'écran."
    l "F (Fullscreen) : Plein écran - Fenêtré."
    l "F11 marche aussi."
    l "H (Hide) : Cache tous les boutons et les dialogues."
    l "Utile pour admirer le paysage."
    l "Tab : Active - Désactive l'avance rapide."
    l "Ctrl : Avance rapide tant que la touche est appuyée."
    if config.developer:
        l "Il semblerait que l'outil de la Dev Team soit actif."
        l "Shift + > : Sauter tous les textes jusqu'au prochain choix."
        l "Shift + D : Accès au menu développeur dont le visionneur de variable."
        l "Shift + R : Recharger le jeu."
        l "Shift + I : Inspecte les box et layout."
        l "Shift + G : Change de carte graphique ou de moteur."
    show laura sad
    l "Voilà, je ne trouve rien d'autre à dire."
    l "C'est déjà pas mal, je pense."
    hide laura with easeoutright
    return
label tuto_sha :
    show ryou angry
    r "Oh nan..."
    hide ryou with easeoutleft
    show shadow ombre with easeinleft
    s "Héhéhé..."
    s "A peine le jeu commencé et ça parle de finir le jeu ?"
    s "Le jeu comporte 0 fin et 8 à venir."
    s "2 très bonne, 2 bonnes et 4 mauvaises."
    s "Voir des CG et entendres des musiques les débloque dans la galerie (à faire)."
    s "Les très bonnes fins débloquent une route mirroir ou le personnage principal ne sera pas le même."
    s "Gagner le jeu avec une bonne fin ou plus débloque un set de graphisme \"amélioré\"."
    s "Je ne vois rien d'autre à ajouter."
    s "Tu verra quand tu me battra..."
    s "A suppose que cela soit possible..."
    hide shadow with easeoutleft
    return
label tuto_ali :
    show ryou angry
    r "Ah nan... Trop de chiffres pour moi !"
    r "Professeur Alice ?"
    hide ryou with easeoutleft
    show alice angry with easeinright
    a "Je ne suis pas ton chien !"
    show alice geez
    a "Des chiffres..."
    show alice normal
    a "D'abord, il y a les niveaux de relation."
    a "Selon les choix, ils montent ou descendent de 5 pour les choix importants."
    a "2 ou 3 pour les choix de répliques."
    show alice happy
    a "Et cas exceptionnel, certains choix donnent 10."
    show alice normal
    a "Les stats..."
    a "Il y en a 3."
    a "1 qui monte avec les études ou les jeux intellectuels."
    a "Les deux autres avec le sport."
    a "De manière générale, ça monte par tranche de 2."
    a "Sauf pour les mini-events."
    show ryou happy at left with easeinleft
    r "Comme courir pour arriver à l'heure en cours ?"
    hide ryou with easeoutleft
    show alice angry
    a "Oui, c'est ça..."
    show alice normal
    a "Si tu es fatigué ou malade, les stats montent moins vite voir pas du tout selon les cas."
    a "La vigueur est un chiffre qui représente l'énergie en surplus que tu peux dépenser en faisant du sport ou en travaillant."
    a "A chaque activité de ce type, elle baissera."
    a "Quand tu dors tôt ou fait la grasse matinée, elle remonte."
    a "Lorsqu'elle est négative, tu peux tomber malade."
    a "Tes stats montent moins vite ou pas du tout."
    a "Certains events seront cachés."
    show alice sad
    a "Des questions ?"
    show alice satisfied
    a "Bien sûr que non, ma présentation était parfaite !"
    hide alice with easeoutright
    return
    
    
