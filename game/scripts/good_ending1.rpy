# Minato est sur le toit
# paralysée d'une façon qui reste a discuter.
label ending:
    scene black
    stop music
    "Ou... Ou suis-je..."
    "Ouah, je suis complètement sonné..."
    scene toit with fade
    "Quand est-ce que j'ai pris une cuite ?"
    "Je suis allongé par terre et ma tête tourne..."
    "Mon portable est devant moi..."
    "?!"
    "Je n'arrive pas à l'atteindre..."
    "C'est comme si quelque chose me retenait..."
    
    $ sha = "Shadow"
    
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
    
    $ choix15 = True
    $ choix16 = True
    $ choix17 = True
    $ choix18 = True
    $ choix19 = True
    $ choix20 = True
    $ choix21 = True
    
    $ choix22 = False
    $ choix23 = False
    $ choix24 = False
    $ choix25 = False
    $ choix26 = True
    $ choix27 = False
    $ choix28 = False
    $ choix29 = False
    $ choix30 = False
    
    
    menu:
        "Regarder derrière.":
            show shadow afk
            play music (shadow3)
            "Je me retourne lentement et j'aperçois Ryouzanki souriant."
            "Il me tient solidement le bras gauche."
            "Il regarde loin devant lui en souriant avant de baisser les yeux sur moi."
            show shadow normal
            r "Mmmh ?"
        "Tenter de tendre le bras plus loin.":
            $ renpy.play('sound/punch.mp3')
            with hpunch
            "Je reçois un violent coup de pied dans les côtes et roule un peu."
            play music (shadow3)
            show shadow smirk
            "En me retournant, je vois Ryouzanki riant."
            "Puis il s'approche de moi."
    menu:
        "C'est toi le responsable de tout, Shadow ?":
            ma "Alors c'est toi le responsable de tout : Shadow..."
            show shadow pity
            s "Bravo Sherlock !"
            s "Est-ce que t'as trouvé tout seul ou est-ce que Watson t'a aidé ?"
        "Qu'est-ce qui se passe ici ?":
            ma "Qu'est-ce qui se passe ici ?"
            $ renpy.play('sound/punch.mp3')
            with hpunch
            "Il me frappe au sol."
            show shadow surprised
            s "C'est assez clair comme réponse ? Je suis Shadow !"
            show shadow pity
            s "Tu te mets en travers de mon chemin, je punis."
            s "C'est la loi de mon monde !"
    s "Aller, on va jouer sur le toit."
    "Il me porte et me lance sur le bord du toit."
    "Puis, il pose son pied sur moi, menaçant de me faire tomber."
    "Il soupire puis me regarde."
    show shadow surprised
    s "Je suis étonné que tu te sois réveillé."
    s "J'ai pourtant mis une sacrée dose de somniphère..."
    ma "..."
    "Cela explique donc pourquoi mon corps est si lourd..."
    show shadow pity
    s "T'endors pas ! Tu vas gâcher ma scène finale !"
    "Il fait craquer son cou et donne des coups de pieds pour me pousser vers le bord."
    $ renpy.play('sound/punch.mp3')
    with hpunch
    $ renpy.play('sound/punch.mp3')
    with hpunch
    "J'en profite pour faire tomber le portable de Shadow discrètement en bas."
    "Merde, j'espère que quelqu'un va le voir..."
    "En attendant, il faut que je gagne du temps..."
label answer:
    menu:
        "Pourquoi t'as fait tout ça ?" if choix1:
            $ choix1 = False
            ma "Shadow... Mais pourquoi t'as fait tout ça ? Dans quel but ?"
            show shadow normal
            s "Pourquoi ? Dans quel but ?" 
            s "Mmmh... Je n'ai pas vraiment de but."
            show shadow pity
            s "Je l'ai fait parce que je pouvais et parce que c'était amusant."
            $ choix6 = True
            $ choix9 = True
        "C'est amusant de jouer avec les gens ?" if choix2:
            $ choix2 = False
            ma "C'est amusant de jouer avec les gens ?"
            show shadow smirk
            s "C'est amusant de jouer les petits détectives ?"
            s "Tu as mieux à faire que d'aller fouiner partout nan ?"
            s "A quoi ça rime tout ça ?"
            menu:
                "C'est ma justice.":
                    ma "C'est ma justice."
                    show shadow pity
                    s "Gahahaha !"
                    s "Mon cul, ouais..."
                    show shadow smirk
                    s "Je parie que tu voulais juste pimenter ta misérable existence..."
                    s "En quoi es-tu différent d'un meurtrier qui aime tuer ?"
                    s "On est pareil tous les deux !"
                    s "Tu me pourchasses pour rendre ta pitoyable vie excitante !"
                "J'aide mes amis.":
                    ma "J'aide mes amis."
                    show shadow surprised
                    s "Aider tes amis ?"
                    show shadow pity
                    s "\"Nous allons attraper le coupable, je vous le promets !!\""
                    s "Ha ha ha ! C'est si gênant !"
                    show shadow smirk
                    s "J'en ai mal aux côtes !"
                    $ choix4 = True
        "Tu as détruit des gens qui t'aimaient." if choix3:
            $ choix3 = False
            ma "Tu as détruit des gens qui t'aimaient."
            show shadow normal
            s "Et alors ?"
            s "Ce monde n'est pas régit par des gens naïfs comme vous."
            show shadow surprised
            s "Mais par des gens comme moi."
            s "Autrefois, c'était la loi du plus fort, puis celle du pur sang."
            s "Maintenant c'est celle du plus rusé."
            $ choix4 = True
            $ choix5 = True
        "Tu n'as plus d'ami..." if choix4:
            $ choix4 = False
            ma "Tu n'as plus d'ami..."
            show shadow pity
            s "Les amis ? Ca me sert à rien ce truc..."
            s "Sans eux, tu es si faible, regardes toi !"
            $ renpy.play('sound/punch.mp3')
            with hpunch
            "Il me frappe pour appuyer ses propos."
            $ choix7 = True
        "Tu te prends pour un être supérieur ?" if choix5:
            $ choix5 = False
            ma "Tu te prends pour un être supérieur ?"
            s "Tu ne sais pas quand t'arrêter hein, avec tes questions débiles..."
            show shadow contraried
            s "Je ne suis pas vraiment un être supérieur."
            s "Je dirais plutôt que je suis un être adapté à ce monde."
            show shadow normal
            s "La gentillesse ne nourira pas ta famille, tu sais..."
        "Et tu ne regrettes aucun de tes actes ?" if choix6:
            $ choix6 = False
            ma "Et tu ne regrettes aucun de tes actes ?"
            show shadow normal
            s "Peu importe à présent..."
            s "Tout ce qui est fait, ne peut être défait."
            s "Pleurer ne fera pas reculer les choses..."
            s "Les morts ne reviennent pas à la vie."
            show shadow contraried
            s "En fait si, je regrette de t'avoir laisser trainer trop longtemps avec Elusia."
            s "J'avais sous-estimé votre relation..."
        "Avec mes amis, nous sommes plus forts que toi." if choix7:
            $ choix7 = False
            ma "Avec mes amis, nous sommes plus forts que toi."
            show shadow pity
            s "Ah ouais ?"
            s "Mais dis moi... Ou sont-ils maintenant que t'as besoin d'eux ?"
            show shadow smirk
            s "Les études sont plus importantes non ?"
            s "Alors travailles bien, trouve une épouse charmante et fonde un foyer."
            s "A l'école, joue avec tes amis tant que c'est possible."
            s "Puis jettes les lorsqu'ils deviennent obsolètes !"
            ma "Ca ne sert à rien de discuter avec toi, des amis, tu n'en as plus."
            $ choix8 = True
        "Comment peux tu comprendre alors que tu es seul..." if choix8:
            $ choix8 = False
            ma "Comment peux tu comprendre alors que tu es seul..."
            show shadow pity
            s "Tu t'es vu ? Monsieur le héros solitaire !!"
            ma "Qui est solitaire ici ?"
            show shadow contraried
            s "Qu- Quoi ?!"
            s "Espèce d'enfoiré arrogant !"
            s "Et puis tu n'es qu'un étudiant non ?"
            s"Tu ne fais que flaner autour de l'école et jouer aux devinettes."
        "Pourquoi avoir détruit l'associatif ?"if choix9:
            $ choix9 = False
            ma "Pourquoi avoir détruit l'associatif ?"
            show shadow smirk
            s "T'es stupide ou quoi ?"
            $ renpy.play('sound/punch.mp3')
            with hpunch
            $ renpy.play('sound/punch.mp3')
            with hpunch
            "Il me frappe encore et encore..."
            s "Je t'ai déjà dit que c'était pour me divertir !"
        "J'en ai assez d'entendre tes conneries...":
            ma "J'en ai assez d'entendre tes conneries..."
            show shadow normal
            s "..."
            jump answer2
    jump answer
label answer2:
    menu:
        "Pourquoi avoir tué Lloyd ?" if choix15:
            $choix15 = False
            ma "Pourquoi avoir tué Lloyd ?"
            show shadow surprised
            s "Tuer Lloyd ?"
            s "Je ne l'ai pas vraiment tué..."
            s "Je n'avais même pas prévu qu'il meurt !"
            s "Je pensais qu'il allait tout simplement déménager comme Néphénie."
            s "Je voulais juste m'en débarasser."
            $ choix22 = True
            $ choix23 = True
        "Pourquoi vouloir éliminer Lloyd ?" if choix22:
            $ choix22 = False
            ma "Pourquoi vouloir éliminer Lloyd ?"
            show shadow smirk
            s "Ceux qui s'opposent à moi, je les élimine !"
            s "Il n'arrêtait pas de se mettre contre moi lors des conseils étudiants !"
            s "En plus, il se doutait de quelque chose pour Néphénie..."
            s "Alors, je voulais qu'il dégage !"
        "Ca ne te fais rien que Lloyd soit mort ?" if choix23:
            $ choix23 = False
            ma "Ca ne te fais rien que Lloyd soit mort ?"
            show shadow normal
            s "Je n'avais pas prévu que cela arrive."
            show shadow pity
            s "Mais en fait, c'était plutôt marrant."
            show shadow smirk
            s "Je ne savais pas qu'il était aussi faible."
            s "Je voulais voir comme il était facile de manipuler l'opinion publique."
            s "C'était un cobaye de qualité !"
        "Pourquoi avoir fait arrêté Laura ?" if choix16:
            $choix16 = False
            ma "Pourquoi avoir fait arrêté Laura ?"
            s "Je ne l'ai pas fait arrêtée."
            s "Je ne suis jamais allé voir la police."
            $ choix24 = True
        "Alors pourquoi on a arrêté Laura ?" if choix24:
            $ choix24 = False
            ma "Alors pourquoi on a arrêté Laura ?"
            show shadow surprised
            s "Parce qu'elle s'est rendue !"
            show shadow surprised
            s "Je n'ai jamais contacté les autorité."
            show shadow pity
            s "Je n'ai fait que lui mettre la pression !"
            $ choix25 = True
        "Qu'as tu fait à Laura ?" if choix25:
            $ choix25 = False
            ma "Qu'as tu fait à Laura ?"
            show shadow surprised
            s "Je ne voulais pas que la police remonte jusqu'à moi."
            s "La seule faille dans mon plan était ma complice."
            s "Il fallait que je la fasse croire qu'elle était entièrement coupable."
            s "Pour qu'elle évite de parler."
            show shadow pity
            s "Et cette idiote y a tellement cru qu'elle s'est rendue à la police !"
        "Pourquoi avoir pourri Nephenie ?" if choix17:
            $choix17 = False
            ma "Pourquoi avoir pourri Nephenie ?"
            show shadow contraried
            s "T'es vraiment trop con..."
            show shadow pity
            s "Pour son poste bien évidemment !"
            s "Personne ne l'aime, c'est le maillon faible à remplacer !"
        "Aimais tu vraiment Elusia ?" if choix18:
            $choix18 = False
            ma "Aimais tu vraiment Elusia ?"
            show shadow normal
            s "Je ne sais pas."
            s "Elle est si faible..."
            show shadow smirk
            s "J'aurais pu en faire le pion parfait !"
            s "Et puis l'amour..."
            show shadow pity
            s "C'est juste le plus gros mensonge de l'humanité mon pauvre..."
            s "\"Regarde moi, reste auprès de moi !\"..."
            s "Il ne s'agit que de désir et de besoin de réconfort."
        "Pourquoi avoir diffamé Alice ?" if choix19:
            $choix19 = False
            ma "Pourquoi avoir diffamé Alice ?"
            show shadow smirk
            s "Pour le plaisir !"
        "Pourquoi avoir diffamé Valeth ?" if choix20:
            $choix20 = False
            ma "Pourquoi avoir diffamé Valeth ?"
            show shadow smirk
            s "Pour le plaisir !"
        "Quelle relation as-tu avec Salazard ?" if choix21:
            $choix21 = False
            ma "Quelle relation as-tu avec Salazard ?"
            show shadow normal
            s "Je lui propose des petites commission payées."
            show shadow pity
            s "Ce type aime vraiment l'argent !"
            s "Tout ça pour sauver des gens à qui il ne doit rien..."
            s "Des gens qui ne lui sont d'aucune utilité !"
        "T'es vraiment qu'un salop, je ne veux pas en entendre plus...":
            ma "T'es vraiment qu'un salop, je ne veux pas en entendre plus..."
            show shadow smirk
            s "Comme tu voudra !"
            "La lumière des escaliers vient de s'allumer..."
            jump answer3
    jump answer2
label answer3:
    
    menu:
        "Au fond de moi, je te comprends..." if choix26 :
            $ choix26 = False
            m "Au fond de moi, je te comprends..."
            show shadow surprised
            s "On va peut être faire quelque chose de toi..."
            show shadow smirk
            s "Je pense qu'on peut faire des choses intéressantes à deux !"
            $ choix27 = True
            $ choix28 = True
        "J'étais comme toi avant." if choix27:
            $ choix27 = False
            $ choix28 = False
            ma "J'étais comme toi avant."
            show shadow surprised
            s "Avant ?"
            ma "Oui. Mais j'ai rencontré des gens."
            ma "Ces rencontres m'ont changés."
            ma "Tu devrais aussi t'ouvrir aux autres et tu comprendrais."
            show shadow contraried
            s "Comprendre quoi ?"
            s "Que les sentiments c'est pour les faibles ?"
            s "Que se reposer sur les autres c'est bien ?"
        "Je pense comme toi." if choix28:
            $ choix27 = False
            $ choix28 = False
            m "Je pense comme toi."
            show shadow surprised
            s "..."
            "Il me tend une main pour m'aider à me relever."
            "Puis il la retire avant que je ne la prenne."
            show shadow contraried
            s "Qu'est ce qui me prouve que tu dis vrai ?"
            $ choix29 = True
        "Les autres vont arriver, détruisons les ensemble." if choix29:
            $ choix29 = False
            mh "Les autres vont arriver, détruisons les ensemble."
            show shadow surprised
            s "Comment ?"
            m "J'ai laissé tombé ton portable en bas. Ils vont venir."
            show shadow pity
            s "Pas mal..."
            show shadow smirk
            s "Ca marche !"
            jump answer5
        "J'ai juste pitié de toi." if choix10:
            $ choix10 = False
            ma "J'ai juste pitié de toi."
            show shadow contraried
            s "Hey ? Les gens naïfs comme toi m'emmerdent !"
            s "Leur existence même m'emmerde !!"
            s "Je n'ai pas besoin de pauvres merdes comme toi dans mon monde !"
            $ renpy.play('sound/punch.mp3')
            with hpunch
            $ renpy.play('sound/punch.mp3')
            with hpunch
            "Il exprime sa colère sur mes côtes meurtries."
            "J'en tousse..."
            $ choix11 = True
        "Il n'y a pas que ton monde qui existe." if choix11:
            $ choix11 = False
            ma "Il n'y a pas que ton monde qui existe."
            show shadow normal
            s "Il n'y a rien d'intéressant dans ce monde terne et ennuyeux."
            s "Je n'ai rien à gagner à le préserver."
            show shadow smirk
            s "Alors que c'est amusant de jouer avec, puis de le détruire."
            s "Mais il n'y a que moi qui joue et c'est tant mieux."
            s "Personne ne s'en rend compte."
            s "Il sont juste tous coincés parce qu'ils ne peuvent pas nier qu'en fait..."
            show shadow surprised
            s "Ceux qui réussissent réellement dans la vie sont ceux qui sont nés avec un ticket magique nommé \"talent\"."
            s "Ces gens dont un représentant est dressé devant toi."
            s "Tu es voué à l'échec."
            s "Une fois que tu réalises ça, c'est le désespoir."
            s "L'ultime \"GAME OVER\" !"
            show shadow pity
            s"Donc il vaut mieux ignorer la réalité non ?"
            $ choix12 = True
            $ choix13 = True
        "La réalité n'est pas un jeu !" if choix12:
            $ choix12 = False
            ma "La réalité n'est pas un jeu !"
            show shadow hate
            s "..."
            s "Putain... Je pensais que tu comprendrais mais en fait t'es juste trop con !"
            s "Peu importe ce que tu fais, rien ne changera."
            s "Tu aurais du arrêter pendant qu'il en était encore temps."
            s "Tu n'obtiendra rien en affrontant la réalité et impossible de la changer non plus."
            s "Alors il vaut mieux l'ignorer et croire que tu vis pleinement ta vie."
            show shadow pity
            s "C'est pas plus facile comme ça ?"
            show shadow smirk
            s "Ce serait génial si la vie pouvait être aussi simple."
            $ choix14 = True
        "Ignorer la réalité, c'est lâche." if choix13:
            $ choix13 = False
            ma "Ignorer la réalité, c'est lâche."
            show shadow contraried
            s "Lâche ?"
            show shadow pity
            s "Dans ce monde, les lâches survivent bien souvent !"
        "Je vais changer cette réalité, tu verra !" if choix14:
            $ choix14 = False
            ma "Je vais changer cette réalité, tu verra !"
            show shadow pity
            s "C'est de la stupidité ou du troll ?"
            s "Pourquoi essayer de changer des choses fixées ?"
            show shadow smirk
            s "Lloyd est déjà mort, l'associatif aussi."
            s "Rends toi à l'évidence !"
            s "T'as rien de mieux à faire ?"
            s "J'ai déjà gagné !!"
            jump answer4
    jump answer3
label answer4:
    stop music fadeout 3.0
    "Quelqu'un vient d'essayer d'ouvrir la porte."
    show shadow contraried
    s "Alors les voilà..."
    s "Toutes ces questions pour gagner du temps..."
    m "Oui. C'est fini."
    m "Maintenant, ils savent la vérité."
    show shadow normal
    s "Dis moi [j]..."
    s "Combien de personne ont déjà réfléchit à la réalité ou à ce qui est bien ou mal ?"
    m "..."
    s"Pas grand monde en fait..."
    s "Ce monde pourri ne vaut rien et vivre ne sert à rien."
    s"La voilà, la vérité que toi, tu as toujours cherché..."
    "La porte cède et mes amis entrent."
    play music (verite)
    show elusia sad at left
    #show laura sad at Position(xpos=0.375)
    show shadow normal 
    #show valeth angry at Position(xpos=0.625)
    show alice angry at right
    
    "Shadow se tourne vers eux."
    show shadow surprised
    s "Un jour vous verrez."
    s "Vous serez confronté à l'ennuyante réalité qui vous confine."
    s"Honnêtement, on n'en a pas besoin."
    a "Arrete tes conneries !!"
    a "Si tu n'acceptes pas la réalité, laisse nous le faire au moins !"
    show shadow smirk
    s "Les gosses comme vous sont si naïfs..."
    s"Je vois dans vos yeux cette peur de l'avenir..."
    s "Vous dissimulez vos angoisses..."
    show shadow pity
    s "Mais ce que je dis est basé sur mes propres expériences !"
    s "Je suis devenu insensible à ce monde pitoyable."
    s "C'est plutôt agréable en fait..."
    show shadow contraried
    s "Etudier, se marier, travailler, consommer, mourir..."
    s "C'est si ennuyeux..."
    ma "Nous on y trouve du plaisir."
    ma "C'est toi, tu t'es perdu tout seul !"
    show shadow pity
    s "Ola ola, je viens de te dire tout ce qu'il y a à savoir !"
    s "C'est cette stupide ignorance que vous appelez espoir qui vous rend tous si ennuyants !"
    show shadow smirk
    s "Cet espoir qui entraîne le desespoir..."
    ma "Arrêtes tes conneries !"
    ma "T'as même pas les couilles de me pousser !"
    show shadow surprised
    s "Hein ?"
    ma "J'en ai marre de t'entendre gémir !"
    ma "Peu importe ce que tu diras, tu ne t'en tirera pas comme ça !"
    "J'attrape sa cheville."
    s "Guh..."
    "Il secoue la jambe et je lâche prise mais il recule."
    ma "Tes péchers te suivront toujours !!"
    "Malgré mon corps engourdi, je me relève."
    ma "La voilà, la vérité !!"
    a "Cette logique tordue est celle d'un gamin égoiste et immature !"
    a "On ne peut pas vivre seul !"
    a "Si tu t'isoles et que tu coupes tes liens avec la société, il deviendra naturellement difficile d'y vivre."
    show shadow hate
    s "Qu'est ce que des pourris gâtés comme vous en savent ?!"
    e "C'est toi le pourri gâté !"
    e "Affronter la réalité est trop dur pour toi alors tu veux empêcher les autres de le faire ?"
    e "Vivre, c'est trop dur mais tu ne veux pas mourir ?"
    e "Bien sur que personne ne te comprend !"
    e "Tu piques une crise comme un sale gosse !"
    
    s "La ferme !!"
    v "Je vais te dire franchement !"
    v "Favorisé par le monde, mon cul !"
    v "T'es juste un lâche !!"
    v "Nous, on se bat pour ce qu'on aime !"
    
    s "Ta gueule ! Ta gueule ! Ta gueule !"
    s "Vous... Vous ne devriez pas être aussi confiants !!"
    s "A moins de nier en bloc tout ce que je viens de dire !!"
    
    e "Nous avons vu la vérité dans des choses que nous avons toujours refusé de voir."
    s "Va te faire foutre !"
    s "Une pauvre naïve comme toi ne peut pas comprendre !"
    s "As tu seulement une idée de tout ce que j'ai enduré ?!"
    m "Shadow, tu n'es pas le seul à souffrir..."
    s "Je... Je ne peux pas perdre !"
    s "Pas contre toi !!"
    "Il sort un couteau et me fonce dessus."
    "Elusia s'interpose, et bloque immédiatement son poignet."
    e "Fais face à la vérité !!"
    "Puis, elle donna un coup sec dans son plexus, lui coupant la respiration."
    "Habilement, elle le maitrise et le mets au sol et lui brise le bras."
    "Il hurle et se tortille au sol pendant qu'elle s'éloigne."
    s "Ha ha ha... Bah quoi... C'est quoi cette merde..."
    s "C'est si ennuyant... J'ai... Vraiment perdu..."
label answer5:
        "..."
        # todo bad end shadow
