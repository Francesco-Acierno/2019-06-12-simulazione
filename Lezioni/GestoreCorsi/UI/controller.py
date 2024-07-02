import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._pd = None

    def get_corsi_periodo(self, e):
        if self._pd is None:
            self._view.create_alert("selezionare un periodo didattico")
            return
        corsi = self._model.get_corsi_periodo(self._pd)
        self._view.lst_result.controls.clear()
        for corso in corsi:
            self._view.lst_result.controls.append(ft.Text(corso))
        self._view.update_page()


    def get_studenti_periodo(self, e):
        if self._pd is None:
            self._view.create_alert("selezionare un periodo didattico")
            return
        numero_studenti = self._model.get_studenti_periodo(self._pd)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"gli studenti iscritti ai corsi del periodo didattico {self._pd} sono {numero_studenti}"))
        self._view.update_page()


    def get_studenti_corso(self, e):
        pass

    def get_dettaglio_corso(self,e):
        pass

    def leggi_tendina(self, e):
        self._pd = self._view.dd_periodo.value

