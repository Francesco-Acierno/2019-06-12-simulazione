from Lezioni.libretto_voti.UI.view import View
from Lezioni.libretto_voti.modello.voto import Libretto, Voto
import flet as ft


class Controller(object):
    def __init__(self, view: View, libretto: Libretto):
        self._view = view
        self._model = libretto
        self.startupLibretto()

    def handleAdd(self, e):

        nameEsame = self._view._txtIn.value
        if nameEsame == "":
            self._view._lvOut.controls.append(ft.Text("Il campo nome non può essere vuoto!",
                                                      color="red"))
            self._view.update()
            return

        strCfu = self._view._txtCFU.value

        try:
            intCfu = int(strCfu)
        except ValueError:
            self._view._lvOut.controls.append((ft.Text("Il campo CFU deve essere un intero.",
                                                       color="red")))
            self._view.update()
            return

        punteggio = self._view._ddVoto.value

        if punteggio == None:
            self._view._lvOut.controls.append((ft.Text("Il campo punteggio va selezionato.",
                                                       color="red")))
            self._view.update()
            return

        if punteggio == "30L":
            punteggio = 30
            lode = True
        else:
            punteggio = int(punteggio)
            lode = False

        data = self._view._datePicker.value
        if data is None:
            self._view._lvOut.controls.append((ft.Text("Seleziona una data.",
                                                       color="red")))
            self._view.update()
            return

        self._model.append(Voto(nameEsame, intCfu, punteggio, lode,
                                f"{data.year}-{data.month}-{data.day}"))
        self._view._lvOut.controls.append(ft.Text("Voto correttamente aggiunto.",
                                                  color="green"))
        self._view.update()
        #     esame: str
        #     cfu: int
        #     punteggio: int
        #     lode: bool
        #     data: str

    def handlePrint(self, e):
        outList = self._model.stampaGUI()
        for elem in outList:
            self._view._lvOut.controls.append(ft.Text(elem))
        self._view.update()

    def startupLibretto(self):
        self._model.append(Voto("Fisica I", 10, 25, False, '2022-07-12'))
        self._model.append(Voto("Analisi II", 8, 30, True, '2023-02-15'))
        self._model.append(Voto("Analisi 1", 10, 18, False, '2020-01-01'))
        self._model.append(Voto("Chimica", 8, 30, False, '2020-01-02'))
        self._model.append(Voto("Informatica", 8, 30, True, '2020-01-03'))
        self._model.append(Voto("Algebra Lineare", 10, 24, False, '2020-06-01'))
        self._model.append(Voto("Fisica 1", 10, 21, False, '2020-06-02'))
