import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.valore_int = 0
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo Creato"))
        self._model.buildGraph()
        nNodes, nEdges = self._model.getCaratteristiche()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi e {nEdges} vertici"))
        minimo, massimo = self._model.getMaxEMin()
        self._view.txt_result.controls.append(ft.Text(f"Valore minimo: {minimo} e  valore massimo: {massimo}"))
        self._view.update_page()

    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()
        valore = self._view.txt_name.value
        try:
            self.valore_int = int(valore)
        except ValueError:
            self._view.txt_result2.controls.append(ft.Text("valore errato, inserisci un valore intero"))
            self._view.update_page()
            return
        minimo, massimo = self._model.getMaxEMin()
        if minimo < self.valore_int < massimo is False:
            self._view.txt_result2.controls.append(ft.Text("il valore inserito non è corretto"))
            self._view.update_page()
            return
        min, max = self._model.count(self.valore_int)
        self._view.txt_result2.controls.append(ft.Text(f"numero archi con peso maggiore della soglia: {max}"))
        self._view.txt_result2.controls.append(ft.Text(f"numero archi con peso maggiore della soglia: {min}"))
        self._view.update_page()

    def handle_search(self, e):
        self._view.txt_result3.controls.clear()
        path, val = self._model.getCamminoOttimo(self.valore_int)
        self._view.txt_result3.controls.append(ft.Text(f"Peso cammino massimo: {val}"))
        for p in path:
            self._view.txt_result3.controls.append(ft.Text(f"{p[0]} --> {p[1]}: {self._model._grafo[p[0]][p[1]]['weight']}"))
        self._view.update_page()
