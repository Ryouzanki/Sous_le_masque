init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    # A button that contains an image that automatically unlocks.
    # g.button("rect")
    # g.image("rect1")
    # g.unlock("rect1")

    # This button has multiple images assocated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.
    g.button("sunny")
    g.unlock_image("classroom")
    g.unlock_image("tennis")
    g.unlock_image("ru")

    # # This button has a condition associated with it, allowing code
    # # to choose which images unlock.
    # g.button("end1")
    # g.condition("persistent.unlock_1")
    # g.image("transfer")
    # g.image("moonpic")
    # g.image("girlpic")
    # g.image("nogirlpic")
    # g.image("bad_ending")

    # g.button("end2")
    # g.condition("persistent.unlock_2")
    # g.image("library")
    # g.image("beach1 nomoon")
    # g.image("bad_ending")

    # The last image in this button has an condition associated with it,
    # so it will only unlock if the user gets both endings.
    # g.button("end3")
    # g.condition("persistent.unlock_3")
    # g.image("littlemary2")
    # g.image("littlemary")
    # g.image("good_ending")
    # g.condition("persistent.unlock_3 and persistent.unlock_4")
    
    # g.button("end4")
    # g.condition("persistent.unlock_4")
    # g.image("hospital1")
    # g.image("hospital2")
    # g.image("hospital3")
    # g.image("heaven")
    # g.image("white")
    # g.image("good_ending")
    # g.condition("persistent.unlock_3 and persistent.unlock_4")

    # The final two buttons contain images that show multiple pictures
    # at the same time. This can be used to compose character art onto
    # a background.
    g.button("elusia")
    g.unlock_image("tennis", "elusia normal")
    g.unlock_image("tennis", "elusia happy")
    g.unlock_image("tennis", "elusia sad")

    g.button("vincent")
    g.unlock_image("classroom", "prof normal")
    g.unlock_image("classroom", "prof happy")
    g.unlock_image("classroom", "prof contraried")
    
    g.button("alice")
    g.unlock_image("labo", "alice normal")
    g.unlock_image("labo", "alice happy")
    g.unlock_image("labo", "alice sad")

    g.button("shadow")
    g.unlock_image("toit", "shadow ombre")
    g.unlock_image("toit", "shadow normal")
    g.unlock_image("toit", "shadow smrik")
    
    g.button("ryou")
    g.unlock_image("couloir", "ryou normal")
    g.unlock_image("couloir", "ryou happy")
    g.unlock_image("couloir", "ryou angry")
    
    g.button("lloyd")
    g.unlock_image("bar", "lloyd normal")
    g.unlock_image("bar", "lloyd happy")
    g.unlock_image("bar", "lloyd angry")
    
    g.button("laura")
    g.unlock_image("ru", "laura normal")
    g.unlock_image("ru", "laura happy")
    g.unlock_image("ru", "laura angry")
    # The transition used when switching images.
    g.transition = dissolve

# Step 3. The gallery screen we use.
screen gallery:

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "start"

    # A grid of buttons.
    grid 3 3:

        xfill True
        yfill True

        # Call make_button to show a particular button.
        add g.make_button("sunny", "UI/cloudy.png", xalign=0.5, yalign=0.5)
        add g.make_button("vincent", "UI/vincent.png", xalign=0.5, yalign=0.5)
        add g.make_button("elusia", "UI/elusia.png", xalign=0.5, yalign=0.5)
        add g.make_button("alice", "UI/alice.png", xalign=0.5, yalign=0.5)
        add g.make_button("ryou", "UI/ryouzanki.png", xalign=0.5, yalign=0.5)
        add g.make_button("laura", "UI/laura.png", xalign=0.5, yalign=0.5)
        add g.make_button("lloyd", "UI/lloyd.png", xalign=0.5, yalign=0.5)
        add g.make_button("shadow", "UI/shadow.png", xalign=0.5, yalign=0.5)

        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.ShowMenu("stats")
        vbox xalign 0.5 yalign 0.5:
            textbutton "Retour" action Return() xalign 0.5 yalign 0.5
            textbutton "Gallerie son" action ShowMenu("music_room") xalign 0.5 yalign 0.5
