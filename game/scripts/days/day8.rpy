    # A ce stade :
    #   Ryou    :  131
    #   Elusia   :  146
    #   Valeth  :  59
    #   Laura   :  90
    #   Lloyd    :  31
    #   Alice     : 103

label day8:
    scene reveil with fade
    play sound "sound/clock.mp3"
    mh "J'ai vraiment bien dormi après le sport !"
    m "Je devrais en faire plus souvent..."
    stop sound
    play music (joueur1) fadein 2
    m "J'espère que le contrôle va bien se passer..."
    play sound "sound/bell.mp3"
    m "Les voilà."
    play sound "sound/dooropen.mp3"
    scene couloir
    show ryou sad:
        left
    show elusia normal:
        right
    with fade
    r "Yo !"
    e "Salutations !"
    e "Prêt[ter] pour le contrôle ?"
    m "Plus ou moins..."
    e "Et toi ?"
    r "J'ai des courbatures, je peux plus tendre les bras..."
    if choix4:
        m "Moi aussi..."
        show elusia satisfied
        e "Je vous avait prévenu !"
        e "Il faut boire beaucoup d'eau et prendre une douche glacée ou un bain tiède."
        r "Un bain tiède, c'est dur dans un studio..."
        show elusia normal
        e "Ryou... Ca ne te dispense pas de la douche glacée..."
        e "Toi non plus [j]."
    else:
        m "Moi ça va..."
        show elusia satisfied
        e "Je t'avais prévenu !"
        e "Il faut boire beaucoup d'eau et prendre une douche glacée ou un bain tiède."
        r "Un bain tiède, c'est dur dans un studio..."
        show elusia normal
        e "Ryou... Ca ne te dispense pas de la douche glacée..."
    scene street
    show ryou sad:
        left
    show elusia normal:
        right
    with fade
    pause(1)
    show elusia surprised
    e "Pourquoi tu tires cette tête depuis tout à l'heure Ryou ?"
    e "Tu devrais être confiant après avoir révisé non ?"
    r "Je n'ai pas l'impression d'être prêt..."
    show elusia sad
    e "Oooh..."
    e "Ce n'est pas au dernier moment qu'il faut s'y mettre..."
    show ryou angry
    r "Oui je sais, pas besoin de me le répéter..."
    play music (thinking2) fadein 2
    scene classroom with fade
    "Le contrôle..."
    if int_points < 2:
        "C'est la débâcle !"
        "Je n'étais vraiment pas au point..."
        $ choix1 = 0
    elif int_points = 2:
        "C'était difficile mais je m'en suis sortie..."
        "Pas brillant mais pas catastrophique non plus..."
        $ choix1 = 1
    else:
        "Les doigts dans le nez."
        "Ma première note et ma première bonne note."
        $ choix1 = 2
    "La dernière question me dit quelque chose..."
    $ ans = renpy.input("Combien d'éléments y a t-il dans le sang ?", "", length=2)
    # $ renpy.block_rollback()
    if ans == 4 :
        "Mmmh... J'assure au moins les points faciles..."
        $ choix1 += 1
    else:
        "Je fais vraiment n'importe quoi."
        "Je ne suis pas sûr[ter] du tout..."
    $ pnjj = "Surveillant"
    pnj "C'est l'heure !"
    pnj "Terminez votre phrase et posez vos stylos."
    scene classroom with fade
    play music (matin1) fadein 2
    show ryou sad at left
    show elusia normal at right
    r "Et voilà..."
    show elusia surprised
    e "Encore ?"
    e "Je croyais que t'avais révisé ?"
    show ryou happy
    r "Hey, j'ai pas dit que j'allais avoir une mauvaise note."
    show ryou surprised
    r "Je voulais juste dire que je suis soulagé que ça soit passé."
    e "Et pour la note ?"
    r "Oh, ça devrait aller."
    e "Et toi [j] ?"
    menu:
        m "Oh moi.."
        "Avouer." if choix1 == 0:
            $ rel_ryou += 1
            $ rel_lulu += 1
            "Cela ne sert à rien de mentir."
            "Ils le sauront bien plus tard de toutes façons."
            m "J'ai fait n'importe quoi... Vraiment..."
            show elusia sad
            show ryou sad
            e "A ce point là ?"
            m "Je n'ai aucune bonne réponse sûre..."
            r "Aïe..."
        "Avouer." if choix1 == 1:
            $ rel_ryou += 2
            $ rel_lulu += 2
            "Cela ne sert à rien de mentir."
            "Ils le sauront bien plus tard de toutes façons."
            m "J'ai fait ce que j'ai pu."
            show elusia happy
            show ryou normal
            m "J'aurais une note pas trop mal."
            e "Tu fera mieux la prochaine fois hein !"
        "Mentir" if choix1 < 2:
            $ rel_ryou -= 2
            $ rel_lulu += 3
            "J'ai assez honte..."
            "Je préfère lâcher un petit mensonge."
            m "Moi, ça s'est assez bien passé en fait."
            show elusia satisfied
            show ryou angry
            e "Tu vois ?"
            e "Y'a quand même des gens sérieux des fois..."
            e "Espérons que l'on déteigne sur toi !"
            r "Puisque je te dis que ça va..."
        "Modestie..." if choix1 > 1:
            $ rel_ryou += 3
            $ rel_lulu +=3
            "On va éviter de les rabaisser."
            m "Moi je ne me suis pas trop mal débrouillé[ter]."
            mh "J'aurais une bonne note."
            show elusia happy
            show ryou normal
            e "Bien joué."
            r "T'as travaillé pour ça ?"
        "Franchise..." if choix1 > 1:
            $ rel_ryou -= 2
            $ rel_lulu += 2
            "Ce sont mes amis après tout."
            "Autant qu'ils apprennent à me connaître."
            mh "J'ai tout bon."
            mh "Je vous paie à boire si je suis sous la moyenne."
            show elusia satisfied
            show ryou surprised
            e "Que d'assurance..."
            r "Tu donnes des cours ?"
    show elusia surprised
    e "Oh, mais si la prochaine fois, on travaillait ensemble ?"
    show ryou normal
    r "Quoi ? Pour que tu nous mettes encore plus la pression ?"
    show elusia angry
    e "C'est pas mon but !"
    menu:
        "Accepter.":
            $ rel_lulu += 3
            mh "Personnellement, je ne vois pas de raison de refuser."
            mh "On n'a pas grand chose à perdre et on est voisin."
            show ryou sad
            r "Mouais OK, je suis."
            show elusia satisfied
            e "Super. On s'organisera pour réviser la prochaine fois alors."
        "Refuser.":
            m "Non merci."
            m "Je n'ai rien contre vous mais je travaille mieux seul[ter]."
            r "Idem."
            show ryou happy
            r "Je travaille avec ma musique dans les oreilles en mode gros associal."
            show elusia geez
            e "Tant pis..."
    show laura normal
    l "Hi !"
    l "Ne me dîtes pas que vous parlez encore du contrôle 15 min après la fin ?"
    show ryou surprised
    r "C'est pas moi ! C'est elle !!"
    show elusia normal
    e "C'est bon... On va manger ?"
    l "Je peux venir ? Il doit y avoir une sacrée queue au self..."
    show elusia happy
    e "Oui bien sûr !"
    return
