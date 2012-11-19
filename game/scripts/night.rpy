init python:
    class CalendarWidget(renpy.Displayable):
        def __init__(self, date_manager, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)

            old_date = date_manager.previous
            new_date = date_manager.datetime

            # Allow flashbacks!
            min_date = min(old_date, new_date)
            max_date = max(old_date, new_date)

            nb_days = (max_date - min_date).days

            # Days part of the view: they must cover the whole change
            days = [(min_date + timedelta(i)) for i in xrange(-1, 5 + nb_days)]

            self.start_index = days.index(old_date)
            self.stop_index = days.index(new_date)

            config = {'substitute': False, 'xalign': 0.5,
                      'color': '#121212', 'bold': False, 'size': 120}

            self.month_text = Text(DateManager.MONTHS[old_date.month-1],
                                   **config)
            self.month_text2 = Text(DateManager.MONTHS[new_date.month-1],
                                    **config)

            config['size'] = 400
            self.day_text = Text('%d' % old_date.day, **config)
            self.day_text2 = Text('%d' % new_date.day, **config)
            self.background = renpy.displayable('UI/calendar.png')
            self.days_widgets = [DayWidget(day, date_manager.get_meteo(day))
                                    for day in days]

            self.width, self.height = 800, 600



        def render(self, width, height, st, at):
            duration = 1.
            render = renpy.Render(self.width, self.height)
            time = min(max(0., st - 2.), duration)

            t = Transform(child=self.month_text, alpha=(1. - time))
            month_render = renpy.render(t, width, height, st, at)
            render.blit(month_render, (30, 40))

            t = Transform(child=self.month_text2, alpha=time)
            month_render = renpy.render(t, width, height, st, at)
            render.blit(month_render, (30, 40))

            t = Transform(child=self.day_text, alpha=(1. - time))
            day_render = renpy.render(t, width, height, st, at)
            w, h = day_render.get_size()
            render.blit(day_render, (self.width - w - 20, 90))

            t = Transform(child=self.day_text2, alpha=time)
            day_render = renpy.render(t, width, height, st, at)
            w, h = day_render.get_size()
            render.blit(day_render, (self.width - w - 20, 90))

            back_render = renpy.render(self.background, width, height, st, at)
            render.blit(back_render, (0, 0))

            dest_x = 120
            for i, day in enumerate(self.days_widgets):
                x = 150 * (i - self.start_index - (self.stop_index - self.start_index) * time / duration) + dest_x
                alpha = max(0.65, 1. - abs(x - dest_x) / 200.)
                t = Transform(child=day, alpha=alpha)
                day_render = renpy.render(t, width, height, st, at)
                render.blit(day_render, (x, 400))

            renpy.redraw(self, 1./60.) # Smooth animation

            return render


        def visit(self):
            return self.days_widgets + [self.month_text, self.day_text,
                                        self.background]




    class DayWidget(renpy.Displayable):
        def __init__(self, date=None, meteo=None, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)

            date = date or datetime(2012, 1, 1)
            text = '%s\n%02d' % (DateManager.WEEKDAYS_SHORT[date.weekday()],date.day)
            self.text = Text(text, slow=False,
                             substitute = False,
                             color='#f2f2f2',
                             xalign=0.5,
                             bold=False,
                             size=24,
                             text_align=0.5)
            meteo = meteo or 'thunder'
            self.meteo = renpy.displayable('UI/%s.png' % meteo)
            self.width, self.height = 0, 0


        def render(self, width, height, st, at):
            text_render = renpy.render(self.text, width, height, st, at)
            meteo_render = renpy.render(self.meteo, width, height, st, at)

            twidth, theight = text_render.get_size()
            mwidth, mheight = meteo_render.get_size()

            self.width = max(twidth, mwidth)
            self.height = theight + 10 + mheight

            render = renpy.Render(self.width, self.height)
            render.blit(text_render, ((self.width - twidth) // 2, 0))
            render.blit(meteo_render, (0, theight + 10))
            return render


        def visit(self):
            return [self.text, self.meteo]



label night:
    scene black
    "..."
    play music (shadow1) fadeout 1.0
    if date_manager.get_day() == 3:
        jump night4
    elif date_manager.get_day() == 7:
        jump night8
    else:
        jump fin_night

label night4:
    show shadow ombre with fade
    s "Je n'arrive pas à dormir..."
    s "Des nouveaux visages..."
    s "Je déteste ça !"
    s "De nouveaux paramètres inconnus dans l'équation..."
    s "[j], [j]..."
    s "As tu vraiment l'intention de devenir ami[ter] avec toutes ces personnes ?"
    s "Peux tu seulement le faire..."
    s "Avant qu'il ne soit trop tard..."
    hide shadow with fade
    jump fin_night
label night8:
    show shadow ombre with fade
    s "Pourquoi j'y suis allé[ter] ?"
    s "Je ne suis pas un pion, ni une pièce de rechange..."
    s "Je les déteste !"
    s "Je vais les briser en miette un à un..."
    hide shadow with fade
    jump fin_night

label fin_night:
    # $ dayyy = date_manager.datetime.day
    # $ monthh = date_manager.datetime.month
    # $ jourrr = date_manager.datetime.weekday()
    # "[jourrr] [dayyy] [monthh]"
    # # weekday est un int de 0 à 6
    
    stop music fadeout 1.0
    window hide
    hide screen button
    python:
        renpy.pause(1.0)
        renpy.scene()
        renpy.show('black')
        date_manager = date_manager.next_day()
        # date_manager = date_manager.next_day(4)
        renpy.show('calendar', what=CalendarWidget(date_manager))
        renpy.with_statement(Fade(0.5, 0.0, 0.5))
        renpy.pause(8.0)
    window show
    show screen button
    $ weekday2 = date_manager.datetime.weekday()
    if weekday2 == 0:
        $weekday2 = 'Lundi'
    if weekday2 == 1:
        $weekday2 = 'Mardi'
    if weekday2 == 2:
       $ weekday2 = 'Mercredi'
    if weekday2 == 3:
        $weekday2 = 'Jeudi'
    if weekday2 == 4:
        $weekday2 = 'Vendredi'
    if weekday2 == 5:
        $weekday2 = 'Samedi'
    if weekday2 ==6:
        $weekday2 = 'Dimanche'
        
    
    $ day2 = date_manager.datetime.day
    
    $ month2 =  date_manager.datetime.month
    if month2 ==3:
        $month2 = 'Mars'
    return
