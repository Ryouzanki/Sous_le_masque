# Ce splashcreen pourra être utilisé comme OP ou trailer temporairement
# Je (Ryou) pense ensuite le muter en ending

label splashscreen:
    $ renpy.pause(0)
    play music (credit)
    scene elusia_bar
    show elusia white at left with entrerinright
    scene elusia_bar2 
    show elusia normal at left
    with Dissolve(2.5)
    scene ryou_bar
    show ryou white at right with entrerinleft
    scene ryou_bar2
    show ryou ex at right
    with Dissolve(2.5)
    scene alice_bar
    show alice white at left with entrerinright
    scene alice_bar2
    show alice normal at left
    with Dissolve(2.5)
    scene lloyd_bar
    show lloyd white at right with entrerinleft
    scene lloyd_bar2
    show lloyd ex at right
    with Dissolve(2.5)
    pause(0.5)
    scene laura_bar
    show laura white at left with entrerinright
    scene laura_bar2
    show laura ex at left
    with Dissolve(2.5)
    scene prof_bar
    show prof white at right with entrerinleft
    scene prof_bar2
    show prof ex at right
    with Dissolve(2.5)
    scene nephie_bar
    show nephie white at left with entrerinright
    scene nephie_bar2
    show nephie ex at left
    with Dissolve(2.5)
    scene valeth_bar
    show valeth white at right with entrerinleft
    scene valeth_bar2
    show valeth ex at right
    with Dissolve(2.5)
                                             
    pause(5)
    return
