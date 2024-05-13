from datetime import datetime

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._choiceGenere = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenere(self):
        generi = self._model.getGeneri()
        generiDD = map(lambda x: ft.dropdown.Option(
            data=x,
            text=x.Name,
            on_click=self.getSelectedGenere), generi)
        self._view.dd_genere.options = generiDD
        self._view.update_page()

    def handle_grafo(self, e):
        minimo = self._view.txt_min.value
        massimo = self._view.txt_max.value
        try:
            minimo_int = int(minimo)
            massimo_int = int(massimo)
        except ValueError:
            self._view.create_alert("Errore inserire dei numeri")
            return
        min_gen = self._model.getMinMax(self._choiceGenere.GenreId)[0][0]
        max_gen = self._model.getMinMax(self._choiceGenere.GenreId)[0][1]

        if toMillisec(minimo_int) < min_gen or toMillisec(massimo_int) > max_gen:
            self._view.create_alert("Errore minimo o massimo superiori ai limiti")
            return

        if self._choiceGenere is None:
            self._view.create_alert("Scegliere un genere")
            return

        self._model.buildGraph(toMillisec(minimo_int), toMillisec(massimo_int), self._choiceGenere.GenreId)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {len(self._model.grafo.edges)}"))

        listC = self._model.getConnesse()
        for c in listC:
            self._view.txt_result.controls.append(
                ft.Text(f"Componente con {c[0]} vertici, inseriti in {c[1]} playlist"))
        self._view.update_page()

    def handle_playlist(self, e):
        dTot = self._view.txt_dtot.value
        if dTot is None:
            self._view.create_alert("Errore inserire un tempo massimo")
            return
        try:
            dTot_int = int(dTot)
        except ValueError:
            self._view.create_alert("Errore inserire un numero")
        self._view.txt_result.controls.clear()
        print("avviato")
        ini = datetime.now()
        cammino, peso = self._model.getCamminoOttimo(fromMinToMillisec(dTot_int))
        self._view.txt_result.controls.append(
            ft.Text(f"La playlist con il maggior numero di brani ha {peso} brani, ed è composta da"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"- {c}"))
        print(f"durata: {datetime.now()-ini}")
        self._view.update_page()

    def getSelectedGenere(self, e):
        if e.control.data is None:
            self._choiceGenere = None
        else:
            self._choiceGenere = e.control.data


def toMillisec(d):
    return d * 1000


def fromMinToMillisec(d):
    return d * 60 * 1000
