label day0:

    play music (joueur1) fadein 2
    scene chambre m_cartons with fade
    "Fiou..."
    "J'ai bientôt fini de déballer mes affaires."
    "Il était temps, on dépasse minuit..."
    "Mon regard se fige sur mes cartons."
    "C'est difficile de déménager en pleine année scolaire..."
    "En plus, ces cartons ne sont pas légers... Les porter au 3ème ne fut pas une mince affaire !"
    "Je réfléchis."
    "Je repense à mon ancienne école."
    "Il n'y a aucun bon souvenir qui s'y attache."
    stop music fadeout 1.0
    play sound "sound/bell.mp3"
    "Je secoue ma tête, balayant mes songes."
    "Qui peut bien venir sonner à une heure pareille ?"
    play sound "sound/dooropen.mp3"
    scene couloir
    play music (ryou1) fadein 1
    show ryou angry
    with fade
    "J'ouvre la porte et vois un jeune homme sur le palier."
    "Il me dévisagea, les yeux plissés."
    "Soudain, il baisse la tête et frappe doucement du poing sur le cadrant de ma porte."
    r "Merde !"
    "Qu'est-ce qu'il me veut ?"
    show ryou sad
    r "Moi qui voulais tomber sur une jolie demoiselle en petite tenue..."
label choix_sexe:
    menu:
        "Perdu, je suis un {b}{u}homme{/u}{/b} !":
            # $ renpy.block_rollback()
            $ m = DynamicCharacter("j",
                 color="#58D3F7",
                 window_left_padding=160,
                 show_side_image=Image("minato.png", xalign=0.03, yalign=0.97), show_two_window=True)
            $ ma = DynamicCharacter("j",
                 color="#58D3F7",
                 window_left_padding=160,
                 show_side_image=Image("minato angry.png", xalign=0.03, yalign=0.97), show_two_window=True)
            $ mh = DynamicCharacter("j",
                 color="#58D3F7",
                 window_left_padding=160,
                 show_side_image=Image("minato happy.png", xalign=0.03, yalign=0.97), show_two_window=True)

            m "Perdu, je suis un homme, un vrai ! Pour la petite tenue, reviens plus tard !"
            show ryou happy
            r "Ha ha ! Ouais mais... Nan merci !"
            $ sexe = 'il'
            $ bite = True
            $ ter = ''
        "Je suis une {b}{u}femme{/u}{/b} mais...":
            # $ renpy.block_rollback()
            $ m = DynamicCharacter("j",
                 color="#58D3F7",
                 window_left_padding=160,
                 show_side_image=Image("hamuko.png", xalign=0.03, yalign=0.97), show_two_window=True)
            $ ma = DynamicCharacter("j",
                 color="#58D3F7",
                 window_left_padding=160,
                 show_side_image=Image("hamuko angry.png", xalign=0.03, yalign=0.97), show_two_window=True)
            $ mh = DynamicCharacter("j",
                 color="#58D3F7",
                 window_left_padding=160,
                 show_side_image=Image("hamuko happy.png", xalign=0.03, yalign=0.97), show_two_window=True)
            
            ma  "Tssss ! Tant pis si je ne suis pas la femme de tes rêves !"
            show ryou happy
            r "Oh ça va, je plaisantais ! Ne le prends pas aussi mal !"
            $bite = False
            $ ter ='e'
            $sexe='elle'
    m "Et en fait... T'es qui toi ?"
    show ryou angry
    r "Hey ! C'est MA question !"
    ma "Quoi ?"
    if bite:
        r "Espèce de voleur de question !"
        ma "Tu viens de sonner chez moi quand même..."
        show ryou happy
        r "Héhé, et alors ?"
        mh "Alors que j'allais sonner chez toi !"
        mh "Chacun son tour !"
    else:
        r "Espèce de voleuse de question !"
        ma "Tu viens de sonner chez moi quand même..."
        show ryou normal
        r "La galanterie m'oblige à laisser l'initiative aux dames !"
        ma "Oui, merci. Donc, j'ai pris l'initiative et je t'ai posé la question en première !"
        show ryou happy
        r "Pas faux..."
        
    show ryou surprised
    r "OK ! Moi, c'est Ryouzanki !"
    $ inc = 'Ryouzanki'
    show ryou normal
    r "J'suis ton voisin ! J'habite l'appart' just' à côté !"
    r "J'entendais du bruit alors je suis venu te souhaiter la bienvenue !"
    r "Et toi, c'est comment ?"
    ma "C'est marqué au dessus de la sonnette..."
    m "Enfin je crois..."
    "Je me penchais en dehors afin de vérifier moi-même."
label sonnette:
    if bite:
       $ j = renpy.input("Il y avait bien mon prénom :", "Minato", length=15) or "Minato"
    else:
        $ j = renpy.input("Il y avait bien mon prénom :", "Hamuko", length=15) or "Hamuko"
    r "[j], c'est ça ?"
    if j == "Ryouzanki":
        jump end
    if j == "Shadow":
        $ j = "Minato"
        $ inc = 'Jeune homme'
        $ fille = 'Elusia'
        $ en = 'Jeune fille'
        $ valou = 'Valeth'
        $ noble = 'Jeune homme'
        $ ali = 'Alice'
        jump ending
    menu:
        "Ah, c'est bien, tu sais lire !":
            # $ renpy.block_rollback()
            ma "Ah, c'est bien, tu sais lire !"
        "Mais non... Retourne en primaire !":
            # $ renpy.block_rollback()
            show ryou sad
            ma "Mais non... Retourne en primaire !"
            "Dans le doute, je regarde une fois de plus."
            show ryou normal
            jump sonnette
            
    show ryou surprised
    r "Sympa comme prénom !"
    m "Merci..."
    show ryou normal
    r "T'es étudiant[ter] ?"   
    m "Bien sur !"
    m "Je vais à l'école juste à côté !"
    m "Enfin d'après googlemap..."
    m "Mais je ne sais pas vraiment encore comment m'y rendre..."
    show ryou angry
    r "Sérieusement ?"
    show ryou happy
    r "Moi aussi j'y suis !"
    r "Et la voisine du dessous aussi !"
    show ryou normal
    r "T'es en Télécom et Réseaux ?"
    m "Ouep."
    r "Idem. On pourra venir te chercher le matin si tu veux !"
    show ryou happy
    if bite:
        r "Tu verras, la voisine, elle est mignonne et gentille."
    else :
        r "Il est de mon devoir de chevalier de t'accompagner à l'école !"
        
    menu :
        "Oui, je veux bien !":
            # $ renpy.block_rollback()
            mh "Oui, je veux bien !"
            $ rel_ryou += 5
            jump accompagner_matin
        "Non merci, ça ira...":
            # $ renpy.block_rollback()
            m "Non merci, ça ira..."
            show ryou angry
            r "..."
            r "Bon OK. Bah, à demain !"
            $ journal1="J'ai fait la rencontre de mon stupide voisin Ryouzanki. Rien d'autre à signaler."
            hide ryou with easeoutright
            stop music
            return
            
label accompagner_matin:
    r "Cool !"
    show ryou normal
    r "Tant qu'à faire, tu veux qu'on aille te présenter à la voisine ?"
    menu:
        "Oui, pourquoi pas...":
            # $ renpy.block_rollback()
            mh "Oui, pourquoi pas..."
            jump rencontre_elusia
        "C'est pas un peu tard là ?":
            # $ renpy.block_rollback()
            ma "C'est pas un peu tard là ?"
            jump rencontre_tard
            
label rencontre_tard:
    show ryou sad
    r "Mmmh... C'est pas faux."
    show ryou normal
    r "Bon bah, je vais te laisser finir tes cartons !"
    m "Oui..."
    r "Bonne nuit et à demain !"
    mh "Toi aussi, à demain !"
    $ journal1="J'ai fait la rencontre de mon voisin Ryouzanki.\nLui et mon autre voisine que je n'ai pas vu, Elusia, vont venir me chercher chaque matin désormais."
    stop music
    hide ryou with easeoutright
    return
    
label rencontre_elusia:
    "Nous descendons d'un étage."
    scene couloir
    show ryou happy
    with fade
    r "Voila on y est !"
    r "Pile en dessous de chez toi !"
    show ryou normal
    "Ryouzanki s'avança et sonna."
    play sound "sound/bell.mp3"
    stop music fadeout 1.0
    "Il a directement sonné sans hésiter..."
    play sound "sound/dooropen.mp3"
    play music (elusia1) fadein 2
    show ryou normal at left with move
    show elusia angry at right with easeinright
    e "Ryou ?!"
    e "Qu'est ce qu'il te prend de venir sonner à une heure pareille ?"
    "Elle me remarque enfin."
    show elusia normal at right
    e "Oh ! Bonsoir !"
    e "A qui ai-je l'honneur ?"
    show ryou happy at left
    if bite:
        r "Je te présente mon frère : [j] !"
    else:
        r "Je te présente ma soeur : [j] !"
        
    show elusia geez
    e "Très drôle !"
    e "Depuis le temps que je te connais..."
    e "Je sais que tu es fils unique."
    show elusia normal
    e "Et donc, toi tu es... [j], c'est ça ?"
    mh "Oui."
    show elusia happy
    e "Enchantée [j], moi, c'est Elusia !"
    $ fille = 'Elusia'
    $ rel_lulu += 5
    show elusia normal
    e "Bon, vu que personne ne semble vouloir aller se coucher tout de suite..."
    e "Voulez-vous venir prendre le thé ?"
    r "Nan, je préfère le café, c'est un truc d'homme !"
    if bite:
        menu:
            "Prendre un café.":
                # $ renpy.block_rollback()
                $ rel_ryou += 2
                m "Oui, moi aussi je prendrais bien un café si possible."
                show ryou happy at left
                m "J'ai encore une longue nuit devant moi !"
                r "On est des hommes, des vrais !"
                show elusia satisfied at right
                e "Lui, je ne sais pas. Mais toi, Ryou, sûrement pas !"
                show elusia normal
            "Prendre un thé.":
                # $ renpy.block_rollback()
                $ rel_lulu += 2
                m "Un thé me conviendra parfaitement !"
                show ryou angry
                "Ryouzanki s'éloigne de moi."
                show elusia satisfied
                e "Tu sais Ryou, il y avait de très grand samouraïs qui ne buvaient que ça !"
                r "... Pas faux."
                show elusia normal
                show ryou happy
                r "Je m'en contenterais !"
    else:
        menu:
            "Prendre un café.":
                # $ renpy.block_rollback()
                $ rel_ryou += 2
                mh "Je prendrais aussi un café si ça ne te gêne pas."
                show ryou angry at left
                "Ryouzanki s'éloigna"
                e "Non, ça ne me gêne aucunement !"
                show elusia satisfied at right
                e "Je crois que son stéréotype de la virilité s'est éffondré !"
            "Prendre un thé.":
                # $ renpy.block_rollback()
                $ rel_lulu += 2
                mh "Un thé me conviendra parfaitement !"
                show elusia satisfied
                e "Oui !"
                e "Laissons ce primate avec son café !"
                e "Qu'il ne s'étonne pas de rester éveillé toute la nuit après !"
                
    scene chambre e with fade
    "Nous avons discuté très tard dans la nuit...."
    "C'était agréable."
    "Puis, je les ai salués et j'ai continué de déballer mes affaires."
    "Avant d'aller me coucher, à bout de force."
    scene black with fade
    $ journal1="J'ai fait la rencontre de mes voisins Elusia et Ryouzanki.\nIls vont venir me chercher chaque matin désormais."
    stop music
    
    return
