# TODO intégrer un "call day4_labo" et "call day4_labo2"
# 3 cas possibles : pas inscrit, lu, inscrit
label day5:
    scene reveil with dissolve
    play sound "sound/clock.mp3"
    m "..."
    m "Courage, dernier jour de la semaine..."
    stop sound
    $ renpy.music.play("music/joueur.ogg", fadein=2)
    m "Je suis prêt[ter] !"
    play sound "sound/bell.mp3"
    m "Toujours aussi ponctuels ces deux là..."
    play sound "sound/dooropen.mp3"
    scene couloir with fade
    show elusia normal at right
    extend "Ou pas..."
    e "Salutations !"
    m "Salut !"
    menu:
        "Et Ryouzanki ?":
            $ rel_lulu += 2
            m "Et Ryouzanki ?"
            show elusia sad at center with move
            e "Cet abruti ne s'est pas réveillé."
            e "Il est en train de se préparer là."
            e "Mais plutôt qu'être tous les 3 en retard, il m'a dit de partir devant."
        "On y va ?":
            m "On y va ?"
            show elusia sad at center with move
            e "Oui, allons-y."
            $ rel_lulu -= 2
            
    return
