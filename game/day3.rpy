label day3:
    scene reveil with dissolve
    play sound "sound/clock.mp3"
    m "..."
    m "J'ai bien dormi..."
    stop sound
    m "Allons, c'est l'heure !"
    play sound "sound/bell.mp3"
    m "Ils sont vraiment ponctuels ces deux là..."
    play sound "sound/dooropen.mp3"
    scene black with dissolve
    scene couloir with dissolve
    show ryou normal at left
    show elusia normal at right
    r "Yo !"
    e "Salutations !"
    scene street with dissolve
    pause(1)
    "Nous avons discuté des cours."
    scene black with dissolve
    scene classroom with dissolve
    hide ryou
    hide elusia
    "Encore un cours à suivre avec Elusia pendant que Ryouzanki dors."
    scene black with dissolve
    pause(1)
    scene classroom with dissolve
    $ renpy.music.play("music/matin.ogg", fadein=2)
    show ryou sad at left
    show elusia happy at right
    e "Hey, pour ce midi, j'ai une superbe idée !"
    r "Balance !"
    e "Et si aujourd'hui, on allait manger avec les autres au RU pour les présenter à [j] ?"
    e "Il n'a pas encore rencontré tout le monde !"
    r "Mouais... OK..."
    e "Alice ! Alice !"
    #show alice normal at far left
    a "Qu... Quoi ?"
