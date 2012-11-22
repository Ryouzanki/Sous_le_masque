init python:
    from datetime import datetime, timedelta
    from random import choice

    class DateManager(object):
        WEEKDAYS = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        WEEKDAYS_SHORT = ['Lun.', 'Mar.', 'Mer.', 'Jeu.', 'Ven.', 'Sam.', 'Dim.']
        MONTHS = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
                'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
                
        def __init__(self, epoch=None, year=1939, month=3, day=19, meteo=None):
            self.meteo = meteo or [choice(['sunny', 'snowy', 'thunder', 'cloudy'])
                                    for i in xrange(365)]
            self.epoch = epoch or datetime(year, month, day)
            self.previous = datetime(year, month, day)
            self.datetime = datetime(year, month, day)


        def get_day(self, day=None):
            return ((day or self.datetime) - self.epoch).days


        def get_meteo(self, day=None):
            return self.meteo[self.get_day(day)]


        def next_day(self, nb_days=1):
            new_manager = DateManager(epoch=self.epoch, meteo=self.meteo)
            new_manager.previous = self.datetime
            new_manager.datetime = self.datetime + timedelta(nb_days)
            return new_manager


    date_manager = DateManager(meteo=['sunny', 'sunny', 'sunny', 'cloudy', 'cloudy', 
        'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny','thunder', 'thunder', 
        'thunder', 'cloudy', 'thunder', 'snowy'])
