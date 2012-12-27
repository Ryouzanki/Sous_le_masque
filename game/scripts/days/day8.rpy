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
    if int_points < 3:
        "C'est la débâcle !"
        "Je n'étais vraiment pas au point..."
        $ choix1 = 0
    elif int_points < 6:
        "C'était difficile mais je m'en suis sortie..."
        "Pas brillant mais pas catastrophique non plus..."
        $ choix1 = 1
    else:
        "Les doigts dans le nez."
        "Ma première note et ma première bonne note."
        $ choix1 = 2
    "La dernière question me dit quelque chose..."
    $ ans = renpy.input("Combien d'éléments y a t-il dans le sang ?", "", length=2)
    $ renpy.block_rollback()
    if ans == '4' :
        "Mmmh... J'assure au moins les points faciles..."
        $ choix1 += 1
    else:
        "Je fais vraiment n'importe quoi."
        "Je ne suis pas sûr[ter] du tout..."
    $ pnjj = "Surveillant"
    $ choix6 = choix1
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
            $ renpy.block_rollback()
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
            $ renpy.block_rollback()
            $ rel_ryou += 2
            $ rel_lulu += 2
            "Cela ne sert à rien de mentir."
            "Ils le sauront bien plus tard de toutes façons."
            m "J'ai fait ce que j'ai pu."
            show elusia happy
            show ryou normal
            m "J'aurais une note pas trop mauvaise."
            e "Tu fera mieux la prochaine fois hein !"
        "Mentir" if choix1 < 2:
            $ renpy.block_rollback()
            $ rel_ryou -= 4
            $ rel_lulu -= 6
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
            $ renpy.block_rollback()
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
            $ renpy.block_rollback()
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
            $ renpy.block_rollback()
            $ rel_lulu += 3
            mh "Personnellement, je ne vois pas de raison de refuser."
            mh "On n'a pas grand chose à perdre et on est voisin."
            show ryou sad
            r "Mouais OK, je suis."
            show elusia satisfied
            e "Super. On s'organisera pour réviser la prochaine fois alors."
        "Refuser.":
            $ renpy.block_rollback()
            m "Non merci."
            m "Je n'ai rien contre vous mais je travaille mieux seul[ter]."
            r "Idem."
            show ryou happy
            r "Je travaille avec ma musique dans les oreilles en mode gros associal."
            show elusia geez
            e "Tant pis..."
    show laura normal with easeinright
    l "Hi !"
    l "Ne me dîtes pas que vous parlez encore du contrôle 15 min après la fin ?"
    show ryou surprised
    r "C'est pas moi ! C'est elle !!"
    show elusia normal
    e "C'est bon... On va manger ?"
    l "Je peux venir ? Il doit y avoir une sacrée queue au self..."
    show elusia happy
    e "Oui bien sûr !"
    r "Allons y..."
    scene parc
    show ryou normal:
            left
    show elusia normal:
            center
    show laura normal:
            right
    with fade
    e "Valou n'est pas avec toi ?"
    l "Il devait manger avec son père qui rentre de déplacement."
    "Nous avons passé le reste du temps sans vraiment avoir de conversation."
    "Serait-ce la tension entre Elusia et Laura ?"
    scene parc
    show ryou normal:
            left
    show elusia normal:
            center
    show laura normal:
            right
    with fade
    r "Bon bah c'est l'heure..."
    show laura sad
    l "Je veux pas retourner en cours..."
    show ryou sad
    r "On a quoi déjà ?"
    l "On a Laroi..."
    show elusia geez
    e "Ce type me met mal à l'aise..."
    m "Vous voulez dire Laroijesea ?"
    r "Ouais, on parle bien de ce psycopathe..."
    m "Pourquoi tu dis ça ?"
    l "Connais tu la devinette du psycopathe ?"
    m "Heu... Ca me dit quelque chose..."
    show elusia surprised
    e "On raconte que les psys la posent à leurs patients et que la réponse indique leur état mental..."
    show elusia sad
    l "Un jeune fille va à l'enterrement de sa mère et y rencontre un inconnu très séduisant."
    l "Une semaine plus tard la jeune fille tue sa soeur."
    l "Pourquoi ?"
    r "Les réponses peuvent varier mais je connais déjà celle de Laroi..."
    show elusia geez
    e "Pose lui toi même la question à la fin du cours et tu comprendra."
    m "Heu... Je ne risque rien ?"
    show ryou sad
    r "Ca dépend. S'il a un scalpel sous la main, il risque de refaire un homicide d'élève..."
    ma "..."
    show elusia angry
    e "Misère... Ryou... T'en as pas marre de dire n'importe quoi ?"
    show ryou happy
    r "Teste et tu verra !"
    m "OK."
    stop music fadeout 2.0
    scene black with fade
    "Nous retournons en cours..."
    scene classroom with fade
    play music (prof1) fadein 2
    "Impossible de suivre faire mes exercices..."
    "A cause de notre conversation à la pause déjeuner, je passe mon temps à fixer le prof."
    "Il passe régulièrement dans les rangs."
    "Il regarde parfois les bavards mais ne leur fait aucun reproche."
    "Par contre il chuchotte de temps en temps avec ceux qui semblent travailler."
    "Mmh ?"
    "Mince, il arrive et j'ai encore rien fait !"
    menu:
        "Que faire ?"
        "Faire la statue...":
            $ renpy.block_rollback()
            "Je m'immobilise en attendant qu'il passe."
            show prof normal with easeinleft
            "C'est si stupide, qu'est ce que je suis en train de faire bon sang ?"
            hide prof with easeoutright
            "... Sérieusement ?"
            "En regardant autour de moi, je remarque qu'il ne se soucie pas de ceux qui ne travaillent pas."
            "Certains font même des mots-croisés ou des Sudoku..."
            $ choix1 = 1
        "Faire semblant d'écrire un truc.":
            $ renpy.block_rollback()
            "J'attrape mon stylo et le pose sur ma feuille."
            show prof happy with easeinleft
            "Il s'arrête pile devant moi et... Sourit ?"
            "On dirait qu'il attend quelque chose..."
            menu:
                "Ecrire des trucs au hasard.":
                    $ renpy.block_rollback()
                    p "Oh, je vois que vous avez quelques réponses."
                    p "Allez donc faire la correction au tableau."
                    m "Mais je..."
                    show prof naughty
                    p "Ne soyez pas modeste. Laissez vos camarades constater l'étandue de votre génie !"
                    scene classroom with fade
                    "Je me déplace vers le tableau mais ne peux rien y écrire."
                    p "Que vois-je ?"
                    p "Ce tableau est aussi vide que votre tête !"
                "Le regarder.":
                    $ renpy.block_rollback()
                    p "Alors [j] ? Manque d'inspiration ?"
                    m "Je..."
                    p "Je sais. Tu n'as pas compris l'exercice."
                    p "C'est normal, tu passes ton temps à me regarder."
                    "Il pose sa main sur mon épaule ?"
                    show prof naugthy
                    p "Désolé mais... j'aime déjà quelqu'un..."
            "La classe éclate de rire."
            hide prof with easeoutright
            "Je me suis rarement senti[ter] aussi humilié[ter]..."
            $ rel_ryou -= 2
            $ rel_lulu -= 3
            $ rel_lolo -= 2
            $ choix1 = 2
        "Faire semblant de réfléchir.":
            $ renpy.block_rollback()
            "La pose du Penseur de Rodin."
            show prof happy with easeinleft
            "Il se penche vers moi et me chuchotte :"
            show prof naughty
            p "Secouez la tête pour voir si ça va connecter vos deux neurones."
            hide prof with easeoutright
            "Attends... Il vient de dire quoi là ?"
            $ choix1 = 3
    scene classroom with fade
    "Enfin la fin du cours..."
    show prof normal with fade
    p "Oh, mais qui voilà ?"
    p "Que puis-je faire pour vous en tant que prof ?"
    if choix1 == 1:
        m "On m'a posé une question à mon arrivée et..."
        show prof annoyed
        p "On vous bizute ?"
        m "Non ! Juste que je ne connais pas la réponse."
        m "Et on refuse de me la donner."
        p "Je vous écoute."
    elif choix1 == 2:
        m "Vous n'aviez pas besoin de m'humilier en public..."
        show prof happy
        p "Vous n'aviez pas besoin de me fixer pendant tout le cours."
        p "J'ai horreur des gens qui font semblant de travailler."
        p "Autant être honnête et ne rien foutre."
        p "Une autre question ?"
        m "Oui."
    elif choix1 == 3:
        m "Vous n'aviez pas besoin de me dire ce genre de chose..."
        show prof happy
        p "Vous n'aviez pas besoin de me fixer pendant tout le cours."
        p "J'ai horreur des gens qui font semblant de travailler."
        p "Autant être honnête et ne rien foutre."
        p "Une autre question ?"
        m "Oui."
    else :
        "ERROR. Reportez cette erreur #81, merci."
    m "En fait, c'est une devinette."
    show prof happy
    p "Tant mieux, je commençais à m'ennuyer."
    stop music fadeout 2.0
    m "Une jeune fille va à l'enterrement de sa mère et y rencontre un inconnu très séduisant."
    m "Une semaine plus tard la jeune fille tue sa soeur."
    m "Pourquoi ?"
    show prof annoyed
    p "..."
    p "C'est tout ?"
    p "Je suis déçu."
    p "De toutes évidences, elle espère simplement revoir le bel inconnu."
    "Comment peut-il répondre ça avec tant de calme et de séreinité ?"
    "C'est assez inhumain de pouvoir penser ainsi..."
    "De pouvoir entrevoir cette possibilité non ?"
    "Je suppose que c'est la réponse d'un psycopathe..."
    menu:
        "Vous êtes monstrueux !":
            $ renpy.block_rollback()
            ma "Vous êtes monstrueux !"
            show prof happy
        "Vous êtes très intelligent...":
            $ renpy.block_rollback()
            mh "Vous êtes très intelligent..."
            show prof normal
        "OK...":
            $ renpy.block_rollback()
            m "OK..."
    play music (prof1) fadein 4
    p "Bah voyons..."
    p "Sois la devinette est nulle, soit vous racontez comme un pied."
    p "Aussi impitoyable soit-elle, cette réponse est la seule que je puisse concevoir en traitant les données que vous m'avez transmis[ter]."
    p "Enterrement = rencontre du bel inconnu."
    p "C'est stupide mais c'est ainsi."
    m "Oui, c'est une manière de voir les choses..."
    m "Je vais au club."
    p "Très bien, n'oubliez pas d'aller en sport de temps en temps."
    p "Oh ! Une seconde !"
    p "Je peux vous poser une courte question avant de vous laissez prendre congé ?"
    m "Heu... Bien sur !"
    show prof happy
    p "Vous roulez dans un camion et vos freins lâchent dans une descente."
    p "Vous devez vous encastrer dans un groupe de personne."
    p "Sur le chemin de gauche, il n'y a qu'un homme qui mourra sur le coup."
    p "Sur l'autre, il y a un groupe de 5 personnes qui eux aussi seront immédiatement tués."
    p "Que faites vous ?"
    "C'est quoi cette question moisie ?"
    "Où est le piège ?"
    ma "Il paraît logique de choisir la voie de gauche non ?"
    p "Bien sûr, vous avez tout à fait raison."
    p "Vous avez donc sacrifié une personne pour en sauver 5."
    p "Un bon choix."
    ma "C'est tout ?"
    p "Oui, c'est tout."
    p "Vous pouvez disposez."
    ma "Je vous remercie, au revoir."
    scene classroom with fade
    play music (jour1) fadein 2
    "Que faire...."
label day8_sport:
    window hide None
    call screen demo_imagemap
    window show None
        
    if _return == "gymnase":
        $ renpy.block_rollback()
        "Allons faire du sport..."
        call sport
    
    elif _return == "science":
        $ renpy.block_rollback()
        if aller_science > 0:
            "Allons voir Alice..."
        else:
            "J'ai cru voir de l'agitation dans le bâtiment des sciences."
            "Il y a peut être des clubs là bas..."
        call labo
        
    elif _return == "art":
        $ renpy.block_rollback()
        if aller_art == 1:
            "Allons tenter de battre Valeth !"
        else:
            "Et si j'allais faire un tour au bâtiments des clubs..."
        call club

    elif _return == "rentrer":
        $ renpy.block_rollback()
        "Je crois que je vais rentrer."
        call go_home
        
        
label day8_fin:
    play music (joueur1) fadein 2
    scene couloir with fade
    play sound "sound/dooropen.mp3"
    pause(1)
    "Ouf, je suis épuisé[ter]..."
    "8 eme jour fini."
    scene chambre m with fade
    play sound "sound/doorclose.mp3"
    "Je vais dormir tôt."
    stop music
    return
