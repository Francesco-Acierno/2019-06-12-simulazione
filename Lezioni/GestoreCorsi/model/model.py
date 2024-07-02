from database.corso_dao import CorsoDao

class Model:

    def __init__(self):
        self.corsi = CorsoDao.get_all_corsi()


    def get_corsi_periodo(self, pd):
        #soluzione programmatica
        result = []

        for corso in self.corsi:
            if corso.pd == int(pd):
                result.append(corso)
        return result

        #soluzione da DAO
        # return CorsoDao.get_corsi_periodo(pd)

    def get_studenti_periodo(self, pd):
        #soluzione con join da SQL
        # matricole = CorsoDao.get_studenti_periodo(pd)
        # return len(matricole)

        #soluzione con mappa relazioni
        matricole = set()
        for corso in self.corsi:
            if corso.pd == int(pd):
                # chiedo al corso i suoi iscritti
                matricole_corso = corso.get_studenti()
                # se il corso non sa i suoi iscritti, li chiedo al DAO
                # e li inserisco nel corso
                if matricole_corso is None:
                    corso.studenti = CorsoDao.get_studenti_singolo_corso(corso.codins)
                    matricole_corso = corso.studenti
                #calcolo l'unione degli iscritti
                matricole = matricole.union(matricole_corso)
        return len(matricole)