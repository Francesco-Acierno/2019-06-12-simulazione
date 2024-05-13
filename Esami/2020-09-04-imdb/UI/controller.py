import time

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.choicefilm = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        for m in self._model._grafo.nodes:
            self._view.ddFilm.options.append(ft.dropdown.Option(data=m, text=m.name, on_click=self.readData))

    def readData(self, e):
        if e.control.data is None:
            self.choicefilm = None
        else:
            self.choicefilm = e.control.data

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        rank = self._view.txt_rank.value
        if rank is None or rank == "":
            self._view.create_alert("Inserire il rank")
            self._view.update_page()
            return
        try:
            rank_int = float(rank)
        except ValueError:
            self._view.create_alert("Il rank inserito è una stringa")
            self._view.update_page()
            return
        if (0.0 < rank_int < 10.0) is False:
            self._view.create_alert("Rank inserito errato!!")
            self._view.update_page()
            return
        self._model.buildGraph(rank_int)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text('Grafo correttamente creato!!!'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di vertici: {len(self._model._grafo.nodes)}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di archi: {len(self._model._grafo.edges)}'))
        self.fillDD()
        self._view.update_page()


    def handle_film(self, e):
        self._view.txt_result.controls.clear()
        nodo, grado = self._model.getGradoMax()
        self._view.txt_result.controls.append(ft.Text(f"Film grado MASSIMO:"))
        self._view.txt_result.controls.append(ft.Text(f"{nodo.id} - {nodo.name}({grado})"))
        self._view.update_page()

    def handle_cammino(self, e):
        self._view.txt_result.controls.clear()
        cammino = self._model.searchPath(self.choicefilm)
        self._view.txt_result.controls.append(ft.Text(f"Il miglior cammino ha lunghezza: {len(cammino)}"))
        for n in cammino:
            self._view.txt_result.controls.append(ft.Text(f'{n[0].name} --> {n[1].name}'))
        self._view.update_page()
