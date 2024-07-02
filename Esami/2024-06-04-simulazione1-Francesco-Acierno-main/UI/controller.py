import time

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDDyear(self):
        for n in range(1910, 2015):
            self._view.ddyear.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillDDshape(self, e):
        self._view.ddshape.disabled = False
        anno = self._view.ddyear.value
        forme = self._model.getForme(anno)
        for f in forme:
            self._view.ddshape.options.append(ft.dropdown.Option(f))
        self._view.update_page()

    def handle_graph(self, e):
        anno = self._view.ddyear.value
        forma = self._view.ddshape.value
        if anno is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare un anno"))
            self._view.update_page()
        if forma is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare una forma"))
            self._view.update_page()
        self._model.buildGraph(anno, forma)
        self._view.txt_result.controls.clear()
        u, v = self._model.graphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi:{u}, numero archi:{v}"))
        pesiAdiacenti = self._model.getPesiAdiacenti()
        for p in pesiAdiacenti:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {p.id}, somma pesi su archi = {pesiAdiacenti[p]}"))
        self._view.update_page()

    def handle_path(self, e):
        tic = time.time()
        self._view.txtOut2.controls.clear()
        path, val = self._model.searchPath()
        self._view.txtOut2.controls.append(ft.Text(f"Peso cammino massimo: {val}"))
        for p in path:
            self._view.txtOut2.controls.append(ft.Text(f"{p[0].id} --> {p[1].id} peso: {p[2]['weight']}"
                                                       f" distanza: {self._model.getDistance(p[0], p[1])}"))
        self._view.txtOut2.controls.append(ft.Text(f"{time.time()-tic}s"))
        self._view.update_page()
