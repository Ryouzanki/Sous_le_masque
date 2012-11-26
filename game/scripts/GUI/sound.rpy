# TODO rebouclage et beauté et scroll

init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("music/Game.ogg", always_unlocked=True)
    mr.add("music/verite.mp3")
    mr.add("music/prof2.mp3")
    mr.add("music/elusia1.mp3")
    mr.add("music/ryouzanki1.mp3")
    mr.add("music/alice1.mp3")
    mr.add("music/joueur1.mp3")
    mr.add("music/shadow1.wav")
    mr.add("music/bal des ombres.wav")
    mr.add("music/shadow end.mp3")
    mr.add("music/prof1.mp3")
    mr.add("music/prof2.mp3")
    mr.add("music/prof3.mp3")
    mr.add("music/laura1.mp3")
    # Thème autres
    mr.add("music/matin1.mp3")
    mr.add("music/jour1.ogg")
    mr.add("music/club1.mp3")
    mr.add("music/game.ogg")
    mr.add("music/weekend1.mp3")
    mr.add("music/jeux1.wav")
    mr.add("music/jeux2.mp3")
    mr.add("music/thinking1.wav")
    mr.add("music/thinking2.wav")
    mr.add("music/verite.mp3")
    mr.add("music/bar.mp3")
    mr.add("music/credit.mp3")
# Step 3. Create the music room screen.
screen music_room:

    tag menu

    add "start"
    
    hbox:
        xmaximum 380
        grid 2 2:
            frame:
                style_group "pref"
                has vbox
                # The buttons that play each track.
                textbutton "Un nouveau départ" action mr.Play("music/Game.ogg")
                
                textbutton "Le vagabond" action mr.Play("music/joueur1.mp3")
                textbutton "Sympathie" action mr.Play("music/ryouzanki1.mp3")
                textbutton "Amitié sincère" action mr.Play("music/elusia1.mp3")
                textbutton "Vérité éclatante" action mr.Play("music/verite.mp3")
                textbutton "Le tyran bienveillant" action mr.Play("music/alice1.mp3")
                textbutton "Prestance" action mr.Play("music/laura1.mp3")
                textbutton "Le témoin passif" action mr.Play("music/prof1.mp3")
                textbutton "L'observateur silencieux" action mr.Play("music/prof2.mp3")
                textbutton "L'arbitre suprême" action mr.Play("music/prof3.mp3")
                textbutton "Mal en patience" action mr.Play("music/shadow1.wav")
                textbutton "Sous le masque" action mr.Play("music/shadow end.mp3")
                textbutton "Innocentes occupations" action mr.Play("music/club1.mp3")
                textbutton "Détente méritée" action mr.Play("music/bar.mp3")
                textbutton "Dissipation" action mr.Play("music/jeux1.wav")
                
            frame:
                style_group "pref"
                has vbox
                textbutton "Action" action mr.Play("music/jeux2.mp3")
                textbutton "Méditation" action mr.Play("music/thinking1.wav")
                textbutton "Réflexion intense" action mr.Play("music/thinking2.wav")
                textbutton "Le bal des ombres" action mr.Play("music/bal des ombres.wav")
                
                textbutton "Démarrage en douceur" action mr.Play("music/matin1.mp3")
                textbutton "Temps libre" action mr.Play("music/jour1.ogg")
                textbutton "Journée de repos" action mr.Play("music/weekend1.mp3")
                textbutton "Futur rayonnant" action mr.Play("music/credit.mp3")
            frame:
                style_group "pref"
                has vbox
                # Buttons that let us advance tracks.
                textbutton "Suivante" action mr.Next()
                textbutton "Précédente" action mr.Previous()
            frame:
                style_group "pref"
                has vbox
            # The button that lets the user exit the music room.
                textbutton "Menu principal" action ShowMenu("main_menu")
                label _("Volume musique ")
                bar value Preference("music volume")

    # Start the music playing on entry to the music room.
    on "replace" action mr.Stop()
    
    # Restore the main menu music upon leaving.
    on "replaced" action mr.Play("music/Game.ogg")
