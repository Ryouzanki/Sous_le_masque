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
    scene classroom with fade
    play music (matin1) fadein 2
    
                                        # TODO
    
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
