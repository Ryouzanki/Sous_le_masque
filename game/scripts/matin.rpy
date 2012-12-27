label matin_sport:
    if matin_sport == 1:
        jump matin_sport1
    else:
        "ERROR"
        
label matin_sport1:
    scene parc 
    show elusia happy sport
    with fade
    "Je cours avec Elusia dans le parc."
    scene parc 
    show elusia happy sport
    with fade
    $ vig -= 2
    if vig < 0:
        $ str_points += 2
        "Je manque de sommeil ces temps ci..."
        "Je n'ai pas été très efficace."
        "Heureusement qu'Elusia était là pour me motiver."
        "Peut-être que je devrais me coucher tôt finalement aujourd'hui..."
        menu:
            "C'est une bonne idée...":
                $ renpy.block_rollback()
                $ action_soir = 'd'
            "Non, ça ira...":
                $ renpy.block_rollback()
                pass
    else:
        $ str_points += 3
        "J'ai bien couru !"
        "Je me suis surpassé."
    e "Ah ! Ca fait un bail que je ne me suis pas sentie aussi bien !"
    show elusia normal sport
    e "Est-ce que j'ai l'air d'une sportive ?"
    menu:
        "Bien sur !":
            $ renpy.block_rollback()
            $ rel_lulu += 2
            m "Bien sur !"
            show elusia happy sport
            e "Hi hi, c'est amusant parce que je ne suis pas vraiment sportive."
            show elusia normal sport
            e "Je le suis plus ou moins devenue récemment."
        "Pas vraiment.":
            $ renpy.block_rollback()
            m "Pas vraiment."
            show elusia satisfied sport
            e "Hé hé, je vois..."
            show elusia normal sport
            e "Tu as raison, je ne suis pas une sportive"
    e "Je suis tombée sur le poste de respo des sports."
    e "Et je me dois de donner le bon exemple."
    e "J'ai souvent du mal à aller en sport et à me motiver."
    show elusia happy sport
    e "Mais une fois que j'y suis, je ne regrette jamais !"
    scene couloir with fade
    show elusia normal sport
    e "Nous revoilà chez nous."
    e "Je ne sais pas pour toi mais moi, j'étais vraiment très contente d'avoir pu courir avec toi !"
    menu:
        "Le plaisir est réciproque !":
            $ renpy.block_rollback()
            $rel_lulu += 5
            mh "Le plaisir est réciproque !"
            show elusia happy sport
            e "Je suis vraiment heureuse de te l'entendre dire !"
            jump matin_sport1_hesitation
        "Oui oui...":
            $ renpy.block_rollback()
            m "Oui oui..."
            $ rel_lulu += 2
            show elusia normal sport
            e "Je suis contente de te l'entendre dire !"
            jump matin_sport1_hesitation
        "Pas moi...":
            $ renpy.block_rollback()
            m "Pas moi..."
            $ rel_lulu -= 17
            show elusia geez sport
            stop music fadeout 1.0
            e "Je vois..."
            show elusia sad sport
            e "Au moins, j'aurais fais ce que j'ai pu pour ne pas te gêner."
            e "Si c'est ce que tu veux, je ne t'approcherais plus désormais."
            e "Au revoir... [j]..."
            return
            
label matin_sport1_hesitation:
            show elusia sad sport
            e "J'avais..."
            show elusia geez sport
            extend "Vraiment peur que ma compagnie ne te soit désagréable."
            menu:
                m "Mais pourquoi..."
                "Tu manques autant de confiance en toi ?":
                    $ renpy.block_rollback()
                    $rel_lulu += 5
                    extend "Tu manques autant de confiance en toi ?"
                    m "Tu doutes toujours..."
                    show elusia sad sport
                    e "Est-ce que... Est-ce qu'on peut en parler une autre fois ?"
                    menu:
                        "Bien sur.":
                            $ renpy.block_rollback()
                            $rel_lulu += 3
                            m "Bien sur."
                            m "J'habite juste à côté, tu viens quand tu veux."
                            show elusia happy sport
                            e "Merci ! J'apprécie, vraiment !"
                            e "Je vais me changer, puis je vais me faire à manger."
                            e "Encore merci et au revoir !"
                        "Nan, je veux savoir.":
                            $ renpy.block_rollback()
                            m "Nan, je veux savoir."
                            e "Mais... C'est d'ordre privé..."
                            show elusia geez sport
                            e "Je suis désolée mais je ne me sens pas assez proche de toi pour en parler."
                            show elusia sad sport
                            e "Merci et au revoir."
                    return
                "Tu penses des trucs pareils ?":
                    $ renpy.block_rollback()
                    $ rel_lulu += 2
                    extend "Tu penses des trucs pareils ?"
                "Ta compagnie me serait désagréable ?":
                    $ renpy.block_rollback()
                    extend "Ta compagnie me serait désagréable ?"
            e "Je ne sais pas..."
            e "Je suis comme ça."
            m "Tu ne devrais pas."
            m "Tu es quelqu'un de bien alors arrêtes de te dénigrer..."
            show elusia normal sport
            e "Merci."
            e "Je vais me changer, puis je vais me faire à manger."
            e "Encore merci et au revoir !"
            return
