label day0:

    $ renpy.music.play("music/joueur.ogg", fadein=2)
    scene chambre m_cartons with dissolve
    m "Fiou..."
    m "J'ai bientôt fini de déballer mes affaires."
    m "Il était temps, on dépasse minuit..."
    "Mon regard se fige sur mes cartons."
    m "C'est difficile de déménager en pleine année scolaire..."
    m "En plus, ces cartons ne sont pas légers... Les porter au 3ème ne fut pas une mince affaire !"
    "Je réfléchis."
    "Je repense à mon ancienne école."
    "Il n'y a aucun bon souvenir qui s'y attache."
    stop music fadeout 1.0
    play sound "sound/bell.mp3"
    "Je secoue ma tête, balayant mes songes."
    m "J'arrive, j'arrive !"
    "Qui peut bien venir sonner à une heure pareille ?"
    play sound "sound/dooropen.mp3"
    scene couloir with dissolve
    $ renpy.music.play("music/ryouzanki.ogg", fadein=1)
    show ryou angry
    "J'ouvre la porte et vois un jeune homme sur le palier."
    "Il me dévisagea, les yeux plissés."
    "Soudain, il baisse la tête et frappe doucement du poing sur le cadrant de ma porte."
    r "Merde !"
    m " Quoi ?"
    show ryou sad
    r "Moi qui voulait tomber sur une jolie demoiselle en petite tenue..."
label choix_sexe:
    menu:
        "Perdu, je suis un homme, un vrai ! Pour la petite tenue, revient plus tard !":
            m "Perdu, je suis un homme, un vrai ! Pour la petite tenue, revient plus tard !"
            show ryou happy
            r "Ha ha ! Ouais mais... Nan merci !"
            $ sexe = 'il'
            $ bite = True
            $ ter = ''
        "Tssss ! Heureuse de constater que certaines choses sont immuables !":
            centered "Attention, la route \"Fille\" comporte quelques problèmes scénaristique."
            centered "Voulez vous vraiment continuer ?"
            menu:
                "Oui.":
                    pass
                "Non.":
                    jump choix_sexe
            m "Tssss ! Heureuse de constater que certaines choses sont immuables !"
            show ryou happy
            r "Oh ça va, je plaisantais ! Ne le prends pas aussi mal !"
            $bite = False
            $ ter ='e'
            $sexe='elle'
    m "Et en fait... T'es qui toi ?"
    show ryou angry
    r "Hey ! C'est MA question !"
    m "Quoi ?"
    if bite:
        r "Espèce de voleur de question !"
        m "Tu viens de sonner chez moi quand même..."
        show ryou happy
        r "Héhé, et alors ?"
        m "Alors que j'allais sonner chez toi !"
        m "Chacun son tour !"
    else:
        r "Espèce de voleuse de question !"
        m "Tu viens de sonner chez moi quand même..."
        show ryou normal
        r "La galanterie m'oblige à laisser l'initiative aux dames !"
        m "Oui, merci. Donc, j'ai pris l'initiative et je t'ai posé la question en première !"
        show ryou happy
        r "Pas faux..."
        
    show ryou sad
    r "OK ! Moi, c'est Ryouzanki !"
    $ inc = 'Ryouzanki'
    show ryou normal
    r "J'suis ton voisin ! J'habite l'appart' just' à côté !"
    r "J'entendais du bruit alors je suis venu te souhaiter la bienvenu !"
    r "Et toi, c'est comment ?"
    m "C'est marqué au dessus de la sonnette..."
    m "Enfin je crois..."
    "Je me penchais en dehors afin de vérifier moi même."
label sonnette:
    if bite:
       $ j = renpy.input("Il y avait bien mon prénom :", "Minato", length=15) or "Minato"
    else:
        $ j = renpy.input("Il y avait bien mon prénom :", "Hamuko", length=15) or "Hamuko"
    r "[j], c'est ça ?"
    menu:
        "Ah, c'est bien, tu sais lire !":
            m "Ah, c'est bien, tu sais lire !"
        "Mais non... Retourne en primaire !":
            show ryou sad
            m "Mais non... Retourne en primaire !"
            "Dans le doute, je regarde une fois de plus."
            show ryou normal
            jump sonnette
            
    show ryou happy
    r "Sympa comme prénom !"
    m "Merci..."
    show ryou normal
    r "T'es étudiant[ter] ?"    
    m "Bien sur !"
    m "Je vais à l'école juste à côté !"
    m " Enfin d'après googlemap..."
    m "Mais je ne sais pas vraiment encore comment m'y rendre..."
    show ryou angry
    r "Sérieusement ?"
    show ryou happy
    r "Moi aussi j'y suis !"
    r "Et la voisine du dessous aussi !"
    show ryou normal
    r "T'es en GTR ?"
    m "Ouep."
    r "Idem. On pourra venir te chercher le matin si tu veux !"
    show ryou happy
    if bite:
        r "Tu verra, la voisine, elle est mignonne et gentille."
    else :
        r "Il est de mon devoir de chevalier de t'accompagner à l'école !"
        
    menu :
        "Oui, je veux bien !":
            m "Oui, je veux bien !"
            $ rel_ryou += 5
            jump accompagner_matin
        "Non merci, ça ira...":
            m "Non merci, ça ira..."
            show ryou angry
            r "..."
            r "Bon OK. Bah, à demain !"
            hide ryou
            stop music
            return
            
label accompagner_matin:
    r "Cool !"
    show ryou normal
    r "Tant qu'à faire, tu veux qu'on aille te présenter à la voisine ?"
    menu:
        "Oui, pourquoi pas...":
            m "Oui, pourquoi pas..."
            jump rencontre_elusia
        "C'est pas un peu tard là ?":
            m "C'est pas un peu tard là ?"
            jump rencontre_tard
            
label rencontre_tard:
    show ryou sad
    r "Mmmh... C'est pas faux."
    show ryou normal
    r "Bon bah, je vais te laisser finir tes cartons !"
    m "Oui..."
    r "Bonne nuit et à demain !"
    m "Toi aussi, à demain !"
    stop music
    hide ryou
    return
    
label rencontre_elusia:
    "Nous descendîme d'un étage."
    scene couloir with fade
    show ryou happy
    r "Voila on y est !"
    r "Pile en dessous de chez toi !"
    show ryou normal
    "Ryouzanki s'avança et sonna."
    play sound "sound/bell.mp3"
    stop music fadeout 1.0
    "Il a directement sonné sans hésiter..."
    play sound "sound/dooropen.mp3"
    $ renpy.music.play("music/elusia.ogg", fadein=2)
    show ryou normal at left with move
    show elusia angry at right
    e "Ryou ?!"
    e "Qu'est ce qu'il te prend de venir sonner à une heure pareille ?"
    "Elle me remarqua enfin."
    show elusia normal at right
    e "Oh ! Bonsoir !"
    e "A qui ai-je l'honneur ?"
    show ryou happy at left
    if bite:
        r "Je te présente mon frère : [j] !"
    else:
        r "Je te présente ma soeur : [j] !"
        
    e "très drôle !"
    e "Depuis le temps que je te connais..."
    e "Je sais que tu es fils unique."
    e "Et donc, toi tu es... [j], c'est ça ?"
    m "Oui."
    e "Enchantée [j], moi, c'est Elusia !"
    $ fille = 'Elusia'
    $ rel_lulu += 5
    e "Bon, vu que personne ne semble vouloir aller se coucher tout de suite..."
    e "Voulez vous venir prendre le thé ?"
    r "Nan, je préfère le café, c'est un truc d'homme !"
    if bite:
        menu:
            "Prendre un café.":
                $ rel_ryou += 2
                m "Oui, moi aussi je prendrais bien un café si possible."
                show ryou happy at left
                m "J'ai encore une longue nuit devant moi !"
                r "On est des hommes, des vrais !"
                show elusia sad at right
                e "Lui, je ne sais pas. Mais toi, Ryou, sûrement pas !"
            "Prendre un thé.":
                $ rel_lulu += 2
                m "Un thé me conviendra parfaitement !"
                show ryou angry at left
                "Ryouzanki s'éloigne de moi."
                show elusia sad at right
                e "Tu sais Ryou, il avait de très grand samouraïs qui ne buvaient que ça !"
                r "... Pas faux."
                show ryou happy at left
                r "Je m'en contenterais !"
    else:
        menu:
            "Prendre un café.":
                $ rel_ryou += 2
                m "Je prendrais aussi un café si ça ne te gêne pas."
                show ryou angry at left
                "Ryouzanki s'éloigna"
                e "Non, ça ne me gêne aucunement !"
                show elusia happy at right
                e "Je crois que son stéréotype de la virilité s'est éffondré !"
            "Prendre un thé.":
                $ rel_lulu += 2
                m "Un thé me conviendra parfaitement !"
                show elusia happy
                e "Oui !"
                e "Laissons ce primate avec son café !"
                e "Qu'il ne s'étonne pas de rester éveillé toute la nuit après !"
                
    scene chambre e with dissolve
    hide ryou
    hide elusia
    "Nous avons discuté très tard dans la nuit...."
    "C'était agréable."
    "Puis, je les ai salués et j'ai continué de déballer mes affaires."
    "Avant d'aller me coucher, à bout de force."
    scene black with dissolve
    stop music
    
    return
