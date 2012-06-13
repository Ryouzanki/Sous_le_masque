label day3:
    scene reveil with dissolve
    play sound "sound/clock.mp3"
    m "..."
    m "J'ai bien dormi..."
    stop sound
    m "Allons, c'est l'heure !"
    play sound "sound/bell.mp3"
    m "Ils sont vraiment ponctuels ces deux là..."
    play sound "sound/dooropen.mp3"
    scene black with dissolve
    scene couloir with dissolve
    show ryou normal at left
    show elusia normal at right
    r "Yo !"
    e "Salutations !"
    scene street with dissolve
    pause(1)
    "Nous avons discuté des cours."
    scene black with dissolve
    scene classroom with dissolve
    hide ryou
    hide elusia
    "Encore un cours à suivre avec Elusia pendant que Ryouzanki dors."
    scene black with dissolve
    pause(1)
    scene classroom with dissolve
    $ renpy.music.play("music/matin.ogg", fadein=2)
    show ryou sad at left
    show elusia happy at right
    e "Hey, pour ce midi, j'ai une superbe idée !"
    r "Balance !"
    e "Et si aujourd'hui, on allait manger avec les autres au RU pour les présenter à [j] ?"
    e "Après tout, [sexe] n'a pas encore rencontré tout le monde !"
    r "Mouais... OK..."
    e "Alice ! Alice !"
    show alice normal at Position(xpos=0.4)
    $ ali = 'Alice'
    a "Qu... Quoi ?"
    e "Et si on allait manger tous ensemble ?"
    show alice sad
    a "T... Tous ?"
    a "Tu veux dire... Toi, moi, baka-powa et [j] ?"
    show ryou angry
    r "Baka powa ?"
    e "Non, plus de gens que ça !"
    e "Lloyd ! Tu veux bien déjeuner avec nous pour une fois ?"
    show lloyd normal at Position(xpos=0.6)
    $ noble = 'Lloyd'
    y "En quel honneur ?"
    e "Mmmh... l'arrivée de [j] !"
    y "[j] est arrivé[ter] depuis 3 jours déjà."
    show elusia normal
    e "Misère, ce n'est pas une raison !"
    show alice geez
    a "Allons bon... Nous vous laisserons le siège d'honneur en boût de table, Sir."
    y "Non merci. Cela ne m'intéresse guère."
    y "Je rentre manger, mais j'apprécie l'intention."
    $ rel_lloy += 2
    y "Au revoir et bon appétit."
    hide lloyd
    show alice sad
    e "Tant pis."
    r "On vient de rater monsieur le vice président de l'Association des Elèves."
    a "Messire Lloyd Baptiste Reeds de Bellato."
    a "Alias Lloyd pour les intimes."
    r "Bon, je vais chercher Valeth."
    hide ryou
    show alice sad at left with move
    e "[j], je te présente Alice, présidente de tous les clubs scientifiques de l'école."
    show alice geez
    a "Arrête... Tu vas me faire rougir..."
    e "Donc voilà, si tu veux t'occuper l'esprit..."
    e "Et là, à point nommé, arrive Valeth !"
    show alice normal
    show valeth normal at Position(xpos=0.4)
    $ valou = 'Valeth'
    v "Salut !"
    e "A l'instar d'Alice, c'est le responsable de tous les clubs artistiques de l'école."
    e "Que ce soit les JDR, le théâtre..."
    show alice sad
    a "Tu nous fait passer pour des rivaux..."
    v "C'est bon Elusia, [sexe] viendra me parler quand ça l'intéressera."
    v" Par contre, je ne peux pas laisser Laura seule."
    v "Ce serait vache."
    v"Donc je sais que tu ne t'entends pas bien avec elle, Elusia mais..."
    show elusia happy
    e "Ne t'en fais pas Valou, je comprends parfaitement."
    e "Après tout, elle fait partie des personnes influentes ce cette promo !"
    e "Elle est tout comme moi déléguée de cette promo."
    e "Si tu as des soucis scolaires, n'hésite pas à nous en parler !"
    e "Nous sommes aussi responsables des sections de sports."
    e "Moi les sports solos et elle les sports collectifs."
    m "C'est impressionnant qu'autant de gens influents soient dans la même promo."
    a "Je ne suis pas en GTR."
    a "Je passais par hasard."
    e "En fait, nous avons formé une liste électorale pour le bureau des élèves."
    e "Et nous avons perdu de très peu alors le président de l'autre liste a été contraint de fusionner les listes."
    e "Donc nous avons eut ces postes."
    a "D'ailleurs, il est où baka-powa ?"
    v "Il discute avec Laura je crois. Il m'a dit qu'ils nous rejoindront."
    $ en = 'Laura'
    scene ru with dissolve
    $ rel_ryou += 3
    $ rel_lulu += 3
    $ rel_val += 3
    $ rel_lolo += 3
    $ rel_ali += 3
    show elusia normal at left
    show ryou normal at Position(xpos=0.375)
    show alice normal at center
    show valeth normal at Position(xpos=0.625)
    show laura normal at right 
    "Ils se sont tous assis autour de moi."
    show alice geez
    a "Assise à côté de baka-powa..."
    show ryou angry
    r "Tu sais ce qu'il dit baka-powa à la nerd ?"
    show alice angry
    a "Je ne suis pas une nerd !"
    show valeth happy
    v "Ces deux là sont vraiment incorrigibles."
    show valeth normal
    v "Sinon [j], d'où tu viens, ils avaient une bibliothèque plus grande que la notre ?"
    m "De mémoire, la nôtre était bien plus grande."
    menu:
        v "Oh, tu lisais beaucoup ?"
        "Pas vraiment non.":
            m "Pas vraiment non."
            v "Ah, dommage."
            l "Tu faisais du sport à la place ?"
            jump d3_sport
        "Oui, je lisais pas mal.":
            $ rel_val += 2
            m "Oui, je lisais pas mal."
            show valeth happy
            v "Haha, je le savais !"
            show valeth normal
            v "Et tu lis quoi exactement comme genre ?"
            v "De la littérature classique ?"
            show ryou happy
            r "De la sci-fi !"
            r "Tous les autres genres sont obsolètes !"
            show ryou normal
            show elusia sad
            e "Ou du fantastique, c'est pas mal aussi !"
            r "Alice demande si tu lis des revues scientifiques."
            show elusia normal
            show alice normal
            a "Hey ! J'ai jamais dit ça !"
            menu:
                m "Je lisais surout..."
                "De la littérature classique.":
                    extend "De la littérature classique."
                    $ rel_val += 5
                    show valeth happy
                    v "Héhé, on pourra échanger quelques oeuvres intéressantes !"
                    r "Ouah Valeth ! Ca fait quel effet de ne plus petre seul au monde ?"
                    show valeth normal
                    v "Alice aussi en lit de temps en temps tu sais..."
                    show alice geez
                    a "Tu n'avais pas besoin de le dire..."
                    show ryou angry
                    r "Normal, entre nerd..."
                    show alice angry
                    a "Tu ne pais rien pour attendre baka-powa !"
                "De la science fiction.":
                    extend "De la science fiction."
                    $ rel_ryou += 5
                    r "Ahlala. Je vous avais prévenu. La fin des autres genres moisis approche !"
                    show alice geez
                    a "C'est toi le moisi."
                    a "Scientifiquement parlant, ces livres sont vraiment puérils."
                    show elusia sad
                    e "Pourquoi tu t'intéresses autant aux space opéra ?"
                    r "J'adore les complots et tout ça..."
                    show ryou sad
                    r "Mais bon, c'est vrai que je ne suis pas très malin et c'est plus du fantasme qu'autre chose."
                "Du fantastique.":
                    extend "Du fantastique."
                    $ rel_lulu += 5
                    show elusia happy
                    e "Je savais bien que t'étais quelqu'un de superbe !"
                    r "Du fantastique... C'est pas mal non plus."
                    show ryou sad
                    r "Mais un peu trop de princesses sauvées par des chevaliers à mon goût."
                    a "T'as des goûts de chiotte aussi..."
                    v "Respectez les goûts des autres vous deux..."
                "Des articles par ci, par là.":
                    extend "Des articles par ci, par là."
                    $ rel_ali += 5
                    v "Oh, tu dois avoir une culture générale impressionante !"
                    show alice happy
                    a "Ha ! Ainsi s'effondrent vos illusions !"
                    a "Pourquoi lire des fictions alors que notre univers recelle de merveilles ?"
                    show elusia sad
                    e "Il est bon de rêvasser de temps en temps !"
                    show ryou angry
                    r "On n'a pas encore de croiseurs interglactiques !"
                    v "Dans la litterature, il y a des romans historiques tu sais..."
                    a "Mais comme tu le dis, c'est de l'histoire ancienne, cela ne nous concerne plus."
            l "Et sinon avec ça, tu faisais du sport ?"
            jump d3_sport
label d3_sport:
        show ryou angry
        show alice normal
        r "Du quoi ?"
        show elusia normal
        e "Quelque chose que tu sèches chaque semaine Ryou."
        
        
        menu:
                    "Du sport, bah oui !":
                        m "Du sport, bah oui !"
                        m "J'aime ça."
                        e "Oh ! Et tu faisais quoi comme sport ?"
                        m "Je faisais un peu de tout."
                        m "J'aime surtout les sports..."
                        menu:
                            "Collectifs !":
                                $ rel_lolo += 5
                                $ rel_lulu += 2
                                extend "Collectifs !"
                                show laura happy
                                l "C'est bien, ça change de ce groupe d'asociaux !"
                                show elusia sad
                                e "On n'est pas asociaux, sinon,ne on serait pas tous réunis ici."
                                show laura normal
                                l "Oui, je suis très étonnée de te voir au RU."
                                e "J'ai le droit non ?"
                            "Solo !":
                                $ rel_lolo += 2
                                $ rel_lulu += 5
                                extend "Solo !"
                                show elusia happy
                                e "La compétivité est un excellent moteur !"
                                show laura sad
                                l "L'esprit d'équipe est bien plus important."
                                e "Oui mais il ne permet pas d'avancer en soi."
                                show laura angry
                                l "Bien sur que si !"
                        show ryou sad
                        r "Hey c'est bon, commencez pas vous deux."
                        show valeth normal
                        v "Les mettre le plus loin possible l'une de l'autre sur la table n'a pas suffit on dirait."
                        show alice sad
                        a "A part le sport, tu as des loisirs ?"
                        jump d3_loisir
                    "Pas trop non.":
                      m "Pas trop non."
                      show laura sad
                      l "OK."
                      show elusia normal
                      e "Il faut entretenir ton corps ou tu vas devenir un légume."
                      show alice happy
                      a "Comme baka-powa !"
                      show ryou angry
                      r "Toi..."
                      v "Et donc, que fais tu pour t'occuper ?"
                      jump d3_loisir
label d3_loisir:
    v "Je me demande si tu faisais des jeux de rôles, de plateau ou ce genre de choses."
    menu:
        "Oui, très souvent !":
            $ rel_val += 5
            m "Oui, très souvent !"
            show valeth happy
            v "Cool, au bâtiment des clubs, on a beaucoup de jeu."
            show valeth normal
            v "Plus que de joueurs d'ailleurs..."
            show alice normal
            a "On pourrait y aller tous ensemble un de ces jours."
            show ryou normal
            r "Oui, pourquoi pas."
        "Oui, ça m'arrive.":
            $ rel_val +=2
            m "Oui, ça m'arrive."
            v "Oh, on pourrait jouer de temps en temps."
            show alice normal
            a "C'est agréable de temps à autre."
            show ryou normal
            r "Ouais, on y pensera."
        "Non, pas trop.":
            m "Non pas trop."
            show laura normal
            l "Tu préfères sortir ?"
            m "Entre autre."
            v "Oh, tant pis..."
            v "Si un jour tu es tenté[ter], passe me voir."
    show elusia normal
    e "Etais-tu impliqué[ter] dans la vie associative de ton école ?"
    show alice normal
    a "Tu étais dans des clubs ?"
    menu:
        "J'étais très impliqué dans les clubs.":
            m "J'étais très impliqué dans les clubs."
            $ rel_lulu += 1
            $ rel_ali += 3
            $ rel_ali += 3
            a "Intéressant..."
            show valeth happy
            v "C'est super !"
            v "J'espère vraiment que nos clubs te plaîront alors !"
            show valeth normal
            a "Le pannel de nos clubs n'est pas bien large mais ils sont de qualité."
        "Je venais de temps en temps.":
            m "Je venais de temps en temps."
            $ rel_ali += 1
            $ rel_ali += 1
            a "Comme tous les gens normaux... Je suppose."
            v "Ca peut pas faire de mal d'avoir des membres en plus."
            a "Le pannel de nos clubs n'est pas bien large mais ils sont de qualité."
            e "J'espère que tu en trouvera un qui te convienne."
        "Les clubs ne m'ont jamais vraiment intéressé.":
            m "Les clubs ne m'ont jamais vraiment intéressé."
            r "Pourtant, je veux pas dire mais ici les clubs sont assez sympas."
            r "Tu devrais vraiment au moins les tester."
            e "C'est bien vrai."
            jump day3_cours
            
    a "Et donc ? Dans quel club étais-tu ?"
    menu:
        m "J'étais dans des clubs..."
        "... De sport":
            extend "De sport."
            e "Oh, c'est sympa ça..."
            l "Tu jouais dans l'équipe de ton école ?"
            m "Oui !"
            l "D'ailleurs, qu'est ce qui est le plus important pour toi ?"
            menu:
                l "L'esprit d'équipe ou la rivalité ?"
                "L'esprit d'équipe.":
                    m "Je pense que l'esprit d'équipe est très important."
                    l "Je le pense aussi."
                    l "Que ce soit pour gagner ou juste d'amuser."
                    $ rel_lolo += 5
                    $ rel_lulu += 2
                "La rivalité.":
                     m "Je pense que la rivalité permet de se surpasser."
                     e "Tout juste."
                     e "L'être humain peut devenir plus fort via l'esprit de compétivité !"
                     $ rel_lolo += 2
                     $ rel_lulu += 5
        "... Plutôt techniques.":
            extend "... Plutôt techniques."
            a "Très intéressant."
            a "Ton expérience m'intéresse... Je suppose."
            a "Tu devrais devenir membre régulier des clubs de science."
            show alice sad
            a "Nous avons... besoin de toute l'aide disponible."
            v "Oui, d'autant plus que ça commence à être urgent."
            show elusia happy
            e "Oh, c'est vrai ! Le grand gala approche !"
            m "C'est quoi le... Grand gala ?"
            r "Genre t'avais pas ça dans ton école..."
            e "C'est le festival de l'école. Une grande fête en quelque sorte."
            a "Nous devons produire des... animations pour le gala."
