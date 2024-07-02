import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.valore_int = 0
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleContaArchi(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))
        self._view.txt_result.controls.append(ft.Text(f"Peso minimo = {self._model.minimo}, peso massimo = {self._model.massimo}"))
        valore = self._view._txtSoglia.value
        try:
            self.valore_int = int(valore)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("valore errato, inserisci un valore intero"))
            self._view.update_page()
            return
        minimo = self._model.minimo
        massimo = self._model.massimo
        if minimo < self.valore_int < massimo is False:
            self._view.txt_result2.controls.append(ft.Text("il valore inserito non è corretto"))
            self._view.update_page()
            return
        min, max = self._model.contaArchi(self.valore_int)
        self._view.txt_result.controls.append(ft.Text(f"numero archi con peso maggiore della soglia: {max}"))
        self._view.txt_result.controls.append(ft.Text(f"numero archi con peso maggiore della soglia: {min}"))
        self._view.update_page()
        self._view.update_page()

    def handleRicercaCromosomi(self, e):
        self._view.txt_result.controls.clear()
        path, val = self._model.getCamminoOttimo(self.valore_int)
        self._view.txt_result.controls.append(ft.Text(f"Peso cammino massimo: {val}"))
        for p in path:
            self._view.txt_result.controls.append(
                ft.Text(f"{p[0]} --> {p[1]}: {self._model.grafo[p[0]][p[1]]['weight']}"))
        self._view.update_page()

