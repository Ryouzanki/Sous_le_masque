# TODO club_home et club_art
# a ce stade, MC a soit lu, soit n'est pas inscrit au club science.

label day6:
    scene reveil with dissolve
    play sound "sound/vibre.ogg"
    m "..."
    m "Quoi..."
    stop sound
    m "Allo ?"
    $ ali = 'Numéro inconnu'
    a "Bonjour !"
    if aller_science == 3:
        a "C'est bien [j] ?"
        m "Oui... mais..."
        m "Qui es tu ?"
        a "Oh... Alors tu ne reconnais pas ma voix... Je suppose..."
        a "Intéressant... Devine donc !"
        menu:
            m "Je dirais..."
            "Elusia !":
                m "Elusia !"
                a "Elusia..."
                jump day6_fille
            "Ryouzanki !":
                m "Ryouzanki !"
                a "Ryouzanki..."
                jump day6_mec
            "Laura !":
                m "Laura !"
                a "Laura..."
                jump day6_fille
            "Valeth !":
                m "Valeth !"
                a "Valeth..."
                jump day6_mec
            "Alice !":
                m "Alice !"
                a "Alice..."
                a "Oh... C'est une bonne réponse !"
                $ ali = 'Alice'
                $ rel_ali += 5
                jump day6_phone
            "Lloyd !":
                m "Lloyd !"
                a "Lloyd..."
                jump day6_mec
    else:
        a "C'est bien Salazard ?"
        m "Heu, non, vous avez du vous tromper de numéro."
        a "Oops, pardon, au revoir !"
        $ ali = 'Alice'
        jump day6_plan
label day6_fille:
    $ rel_ali -= 1
    a "Je crains que ce ne soit pas la bonne réponse [j] !"
    a "C'est Alice !"
    $ ali = 'Alice'
    jump day6_phone
label day6_mec:
    $ rel_ali -=2
    a "Roooh... Je n'ai pas la voix grave au téléphone..."
    a "Tu vexes ma féminité."
    a "C'est Alice voyons !"
    $ ali = 'Alice'
    jump day6_phone
label day6_phone:
    a "Passons aux choses sérieuses."
    a "Ou pas !"
    a "Les autres membres du club disent que j'en fait trop."
    a "D'ailleurs, ouvrons une parenthèse, qu'en penses tu ?"
    a "Je suis lourde ? J'en fais trop ?"
    menu:
        "Non, pas du tout.":
            $ rel_ali += 5
            m "Non, pas du tout."
            m "Tu es passionnée. C'est une bonne chose."
            a "C'est vrai ?"
            a "Ca me fait vraiment plaisir d'entendre ça."
            a "Surtout de toi !"
        "Oui un peu.":
            $ rel_ali += 3
            m "Oui un peu. Mais c'est naturel."
            m "Ce n'est pas si dérangeant."
            a "Intéressant..."
            a "Je comprends."
            a "Ca me rassure un peu."
        "Effectivement, ils n'ont pas tort...":
            $ rel_ali -= 2
            m "Effectivement, ils n'ont pas tort..."
            m "T'abuses un peu des fois..."
            a "Je... Je comprends..."
            a "Est ce que je peux te demander pardon ?"
            m "C'est pas si grave..."
    a "Bon, fermons cette parenthèse."
    a "Je t'ai appelé pour te remercier en fait."
    a "Merci d'être venu lire ce rapport ennuyeux."
    m "Je n'ai pas finit."
    a "Tu le finira, j'ai confiance."
    a "Les autres ont dit que pour décompresser, je devais ne pas y penser samedi et faire un break."
    a "Pour ça, ils ont décidé de m'empêcher de travailler."
    a "Aujourd'hui, ils ont piqués mes clefs des locaux."
    menu:
        "(Rire)":
            $ rel_ali += 2
            m "Hahaha..."
            a "Amusant n'est-ce pas ?"
        "Ah les enfoirés...":
            m "Ah les enfoirés..."
            a "Mais non. Je ne l'ai pas mal prit."
    a "Ils me les rendront ce midi lorsqu'ils ouvriront les locaux."
    m "Je croyais que tu ne devais pas y aller ?"
    a "J'y viens, j'y viens."
    a "Ils ont l'intention de faire un petit repas d'étage entre membres du club."
    a "Je t'appelle pour t'y convier."
    a "Donc voilà, si ça t'intéresse, viens vers midi dans les locaux du club."
    m "D'accord, j'y réfléchirais."
    a "Ce sera tout... Je suppose."
    a "A tout à l'heure peut être !"
    "Bon... Il est 10h... Qu'est ce que je vais faire de ma journée..."
    call day_planner(["Matin", "Après midi", "Soir"])
