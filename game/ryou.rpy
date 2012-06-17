label ryou:
    show image "back/start.jpg"
    menu:
        "Route bonus":
            jump ryou_confirme
        "Route classique":
            return
            
label ryou_confirme:
    define e = Character('Elusia', color="#FF69B4", show_two_window=True)
    define m = Character('Minato', color="#58D3F7", show_two_window=True)
    define r = Character('Ryouzanki', color="#4169E1", show_two_window=True)
    define l = Character('Laura', color="#8B0000", show_two_window=True)
    define v = Character('Valeth', color="#800080", show_two_window=True)
    define y = Character('Lloyd', color="#FF8C00", show_two_window=True)
    define a =  Character('Alice', color="#228B22", show_two_window=True)
    
    $ action_matin = None
    $ action_aprem = None
    $ action_soir = None
    #dp_period("matin a la con", $choix1)
    call day_planner(["Matin", "Après midi", "Soir"])
    
    "test position"
    scene RU
    show ryou normal at left
    show alice normal at right
    show lloyd normal at Position(xpos=0.40)
    show salazard evil at Position(xpos=0.60)
    "fin du test"
    a "le journal va etre incrementé"
    $ unlocked_journal_pages += 1
    r "journal incrémenté"
    m "Je suis un homme !"
    $rel_lulu +=10
    $ rel_ryou -=10
    e "Ryou, je t'aime !"
    l "test"
    v "test"
    y "test"
