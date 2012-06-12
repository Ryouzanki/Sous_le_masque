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
    
    image rect = "CG/rect.png"


    "test position"
    # show ryou normal at left
    # show alice normal at center
    # show rect at Position(xpos = 0.75, xanchor=0, ypos=0, yanchor=0)
    # "1"
    # show rect at Position(xpos = 0.25, xanchor=0, ypos=0, yanchor=0) with move
    # "xpos --"
    # show rect at Position(xpos = 0, xanchor=0, ypos=0.75, yanchor=0)
    # "3"
    # show rect at Position(xpos = 0, xanchor=0, ypos=0.25, yanchor=0)with move
    # "ypos--"
    # show rect at Position(xpos = 0, xanchor=0.75, ypos=0, yanchor=0)
    # "1"
    # show rect at Position(xpos = 0, xanchor=0.25, ypos=0, yanchor=0) with move
    # "xanchor --"
    # show rect at Position(xpos = 0, xanchor=0, ypos=0, yanchor=0.75)
    # "3"
    # show rect at Position(xpos = 0, xanchor=0, ypos=0, yanchor=0.25)with move
    # "yanchor--"
    show rect at Position(xpos = 0.5, xanchor=0.5, ypos=1, yanchor=0)

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
