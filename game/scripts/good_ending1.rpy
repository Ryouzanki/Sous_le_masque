# Minato est sur le toit
# paralysée d'une façon qui reste a discuter.
label ending:
    "Ou... Ou suis-je..."
    "Ouah, je suis complètement sonné..."
    "Quand est-ce que j'ai pris une cuite ?"
    "Mon portable est devant moi..."
    "?!"
    "Je n'arrive pas à l'atteindre..."
    "C'est comme si quelque chose me retenait..."
    
    $ choix1 = True
    $ choix2 = True
    $ choix3 = True
    $ choix4 = False
    $ choix5 = False
    $ choix6 = False
    $ choix7 = False
    $ choix8 = False
    $ choix9 = False
    
    $ choix10 = True
    $ choix11 = False
    $ choix12 = False
    $ choix13 = False
    $ choix14 = False
    
    menu:
        "Regarder derrière.":
            "Je me retourne lentement et j'aperçois Ryouzanki souriant."
            "Il regarde loin devant lui en souriant avant de baisser les yeux sur moi."
            "Il me tient solidement le bras gauche."
        "Tenter de tendre le bras plus loin.":
            "Je reçois un violent coup de pied dans les côtes et roule un peu."
            "En me retournant, je vois Ryouzanki riant."
            "Puis il s'approche de moi."
    menu:
        "C'est toi le responsable de tout, Shadow ?":
            m "Alors c'est toi le responsable de tout : Shadow..."
            s "Bravo Sherlock !"
            s "Est-ce que t'as trouvé tout seul ou est-ce que Watson t'a aidé ?"
        "Qu'est-ce qui se passe ici ?":
            m "Qu'est-ce qui se passe ici ?"
            "Il me frappe au sol."
            s "C'est assez clair comme réponse ? Je suis Shadow !"
            s "Tu te mets en travers de mon chemin, je punis."
            s "C'est la loi de mon monde !"
    s "Aller, on va jouer sur le toit."
    "Il me porte et me lance sur le bord du toit."
    "Puis, il pose son pied sur moi, menaçant de me faire tomber."
    "Il soupire puis me regarde"
    s "Je suis étonné que tu te sois réveillé."
    s "J'ai pourtant mis une sacrée dose de somniphère..."
    m "..."
    "Cela explique donc pourquoi mon corps est si lourd..."
    s "T'endors pas ! Tu vas gâcher ma scène finale !"
    "Il craque le cou et donne de petits coups de pieds pour me pousser vers le bord."
    "J'en profite pour faire tomber mon portable discrètement en bas."
    "Merde, j'espère que quelqu'un va le voir..."
    "En attendant, il faut que je gagne du temps..."
label answer:
    menu:
        "Pourquoi tu fais ça ?" if choix1:
            $ choix1 = False
            m "Shadow... Mais pourquoi tu fais ça ? Dans quel but ?"
            s "Pourquoi ? Dans quel but ?" 
            s "Mmmh... Je n'ai pas vraiment de but."
            s "Je l'ai fait parce que je pouvais et parce que c'était amusant."
            $ choix6 = True
            $ choix9 = True
        "C'est amusant de jouer avec les gens ?" if choix2:
            $ choix2 = False
            m "C'est amusant de jouer avec les gens ?"
            s "c'est amusant de jouer les petits détectives ?"
            s "Tu as mieux à faire que d'aller fouiner partout nan ?"
            s "A quoi ça rime tout ça ?"
            menu:
                "C'est ma justice.":
                    m "C'est ma justice."
                    s "Gahahaha !"
                    s "Mon cul, ouais..."
                    s "Je parie que tu voulais juste pimenter ta misérable existence..."
                    s "En quoi es-tu différent d'un meurtrier qui aime tuer ?"
                    s "On est pareil tous les deux !"
                    s "Tu me pourchasses pour rendre ta pitoyable vie excitante !"
                "J'aide mes amis.":
                    m "J'aide mes amis."
                    s "Aider tes amis ?"
                    s "\"Nous allons attraper le coupable, je vous le promets !!\""
                    s "Ha ha ha ! C'est si gênant !"
                    s "J'en ai mal aux côtes !"
                    $ choix4 = True
        "Tu as détruit des gens qui t'aimaient." if choix3:
            $ choix3 = False
            m "Tu as détruit des gens qui t'aimaient."
            s "Et alors ?"
            s "Ce monde n'est pas régit par des gens naïfs comme vous."
            s "Mais par des gens comme moi."
            s "Autrefois, c'était la loi du plus fort, puis celle du pur sang."
            s "Maintenant c'est celle du plus rusé."
            $ choix4 = True
            $ choix5 = True
        "Tu n'as plus d'ami..." if choix4:
            $ choix4 = False
            m "Tu n'as plus d'ami..."
            s "Les amis ? Ca me sert à rien ce truc..."
            s "Sans eux, tu es si faible, regardes toi !"
            "Il me frappe pour appuyer ses propos."
            $ choix7 = True
        "Tu te prends pour un être supérieur ?" if choix5:
            $ choix5 = False
            m "Tu te prends pour un être supérieur ?"
            s "Tu ne sais pas quand t'arrêter hein, avec tes questions débiles..."
            s "Je ne suis pas vraiment un être supérieur."
            s "Je dirais plutôt que je suis un être adapté à ce monde."
            s "La gentillesse ne nourira pas ta famille, tu sais..."
        "Et tu ne regrettes aucun de tes actes ?" if choix6:
            $ choix6 = False
            m "Et tu ne regrettes aucun de tes actes ?"
            s "Peu importe à présent..."
            s "Tout ce qui est fait, ne peut être défait."
            s "Pleurer ne fera pas reculer les choses..."
            s "Les morts ne reviennent pas à la vie."
            s "En fait si, je regrette de t'avoir laisser trainer trop longtemps avec Elusia."
            s "J'avais sous-estimé votre relation..."
        "Avec mes amis, nous sommes plus forts que toi." if choix7:
            $ choix7 = False
            m "Avec mes amis, nous sommes plus forts que toi."
            s "Ah ouais ?"
            s "Mais dis moi... Ou sont-ils maintenant que t'as besoin d'eux ?"
            s "Les études sont plus importantes non ?"
            s "Alors travailles bien, trouve une épouse charmante et fonde un foyer."
            s "A l'école, joue avec tes amis tant que c'est possible."
            s "Puis jettes les lorsqu'ils deviennent obsolètes !"
            m "Ca ne sert à rien de discuter avec toi, des amis, tu n'en as plus."
            $ choix8 = True
        "Comment peux tu comprendre alors que tu es seul..." if choix8:
            $ choix8 = False
            m "Comment peux tu comprendre alors que tu es seul..."
            s "Tu t'es vu ? Monsieur le héros solitaire !!"
            m "Qui est solitaire ici ?"
            s "Qu- Quoi ?!"
            s "Espèce d'enfoiré arrogant !"
            s "Et puis tu n'es qu'un étudiant non ?"
            s"Tu ne fais que flaner autour de l'école et jouer aux devinettes."
        "Pourquoi avoir détruit l'associatif ?"if choix9:
            $ choix9 = False
            m "Pourquoi avoir détruit l'associatif ?"
            s "T'es stupide ou quoi ?"
            "Il me frappe encore et encore..."
            s "Je t'ai déjà dit que c'était pour me divertir !"
        "J'en ai d'entendre tes conneries...":
            m "J'en ai d'entendre tes conneries..."
            s "..."
            jump answer2
    jump answer
label answer2:
    menu:
        "J'ai juste pitié de toi." if choix10:
            $ choix10 = False
            m "J'ai juste pitié de toi."
            s "Hey ? Les gens naïfs comme toi m'emmerdent !"
            s "Leur existence même m'emmerde !!"
            s "Je n'ai pas besoin de pauvres merdes comme toi dans mon monde !"
            "Il exprime sa colère sur mes côtes meurtries."
            "J'en tousse..."
            $ choix11 = True
        "Il n'y a pas que ton monde qui existe." if choix11:
            $ choix11 = False
            m "Il n'y a pas que ton monde qui existe."
            s "Il n'y a rien d'intéressant dans ce monde terne et ennuyeux."
            s "Je n'ai rien à gagner à le préserver."
            s "Alors que c'est amusant de jouer avec, puis de le détruire."
            s "Mais il n'y a que moi qui joue et c'est tant mieux."
            s "Personne ne s'en rend compte."
            s "Il sont juste tous coincés parce qu'ils ne peuvent pas nier qu'en fait..."
            s "Ceux qui réussissent réellement dans la vie sont ceux qui sont nés avec un ticket magique nommé \"talent\""
            s "Ces gens dont un représentant est dressé devant toi."
            s "Tu es voué à l'échec."
            s "Une fois que tu réalises ça, c'est le désespoir."
            s "L'ultime \"GAME OVER\""
            s"Donc il vaut mieux ignorer la réalité non ?"
            $ choix12 = True
            $ choix13 = True
        "La réalité n'est pas un jeu !" if choix12:
            $ choix12 = False
            m "La réalité n'est pas un jeu !"
            s "..."
            s "Putain... Je pensais que tu comprendrais mais en fait t'es juste trop con !"
            s "Peu importe ce que tu fais, rien ne changera."
            s "Tu aurais du arrêter pendant qu'il en était encore temps."
            s "Tu n'obtiendra rien en affrontant la réalité et impossible de la changer non plus."
            s "Alors il vaut mieux l'ignorer et croire que tu vis pleinement ta vie."
            s "C'est pas plus facile comme ça ?"
            s "Ce serait génial si la vie pouvait être aussi simple."
            $ choix14 =True
        "Je vais changer cette réalité, tu verra !" if choix14:
            $ choix14 = False
            m "Je vais changer cette réalité, tu verra !"
            s "C'est de la stupidité ou du troll ?"
            s "Pourquoi essayer de changer des choses fixées ?"
            s "Lloyd est déjà mort, l'associatif aussi."
            s "T'as rien de mieux à faire ?"
            










#arrivage porte défoncée

e "Tu as joué avec mon amour."
l "Tu as joué avec ma compassion."
v "Tu as joué avec ma fierté."



s "Un jour vous verrez."
s "Vous serez confronté à l'ennuyante réalité qui vous confine."
s"Honnêtement, on n'en a pas besoin."
a "Arrete tes conneries !!"
a "Si tu n'acceptes pas la réalité, laisse nous le faire au moins !"
s "Les gosses comme vous sont si naïfs..."
s"Je vois dans vos yeux cette peur de l'avenir..."
s "Vous dissimulez vos angoisses..."
s "Mais ce que je dis est basé sur mes propres expériences !"
s "Je suis devenu insensible à ce monde pitoyable."
s "C'est plutôt agréable en fait..."
s "Etudier, sa marier, travailler, consommer, mourir..."
s "C'est si ennuyeux..."

s"Combien de personne ont déjà réfléchit à la réalité ou à ce qui est bien ou mal ?"
s"Pas grand monde en fait..."
s "Ce monde pourri ne vaut rien et vivre ne sert à rien."
s"La voilà, la vérité que tu as toujours cherché..."
m"Ce n'est pas cette vérité là !"
s "Ola ola, je viens de te dire tout ce qu'il y a à savoir !"
s "C'est cette stupide ignorance que vous appelez espoir qui vous rend tous si ennuyants !"
s "L'espoir qui entraîne le desespoir..."
m "Arrêtes tes conneries !"
m "T'as même pas les couilles de me pousser !"
s "Hein ?"
m "J'en ai marre de t'entendre gémir !"
m "Peu importe ce que tu diras, tu ne t'en tirera pas comme ça !"
m "Tes péchers te suivront toujours !!"
m "La voilà, la vérité !!"
a "Ta logique tordue est celle d'un gamin égoiste et immature !"
a "On ne peut pas vivre seul !"
a "Si tu t'isoles et que tu coupes tes liens avec la société, il deviendra naturellement difficile d'y vivre."
s "Qu'est ce que des pourris gâtés comme vous en savent ?!"
a "C'est toi le pourri gâté !"
a "Affronter la réalité est trop dur pour toi alors tu veux empêcher les autres de le faire ?"
a "Bien sur que personne ne te comprend !"
a "Tu piques une crise comme un sale gosse !"
s "La ferme !!"
a "Je vais te dire franchement !"
a "Favorisé par le monde, mon cul !"
a "T'es juste un lâche !!"
a "Nous, on se bat pour ce qu'on aime !"
s "Ta gueule ! Ta gueule ! Ta gueule !"
s "Vous... Vous ne devriez pas être aussi confiants !!"
s "A moins de nier en bloc tout ce que je viens de dire !!"
a "Nous avons vu la vérité dans des choses que nous avons toujours refusé de voir."
s"Va te faire foutre !"
s"Un pauvre naïf comme toi ne peut pas comprendre !"
s"As tu seulement une idée de tout ce que j'ai enduré ?!"
m "Shadow, tu n'es pas le seul à souffrir..."
s "Je... Je ne peux pas perdre !"
s "Pas contre toi !!"
"Il sort un couteau et me fonce dessus."
"Elusia s'interpose, et bloque immédiatement son poignet."
"Puis, elle donna un coup sec dans son plexus, lui coupant la respiration."
m"Fais face à la vérité !!"
"Habilement, elle le maitrise et le mets au sol et lui brise le bras."
"Il hurle et se tortille au sol pendant qu'elle s'éloigne."
s "Ha ha ha... Bah quoi... C'est quoi cette merde..."
s "C'est si ennuyant... J'ai... Vraiment perdu..."

