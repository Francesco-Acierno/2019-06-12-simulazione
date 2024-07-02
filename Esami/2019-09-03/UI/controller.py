import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selectedTipo = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analisi(self, e):
        cal = self._view._txtCalorie.value
        try:
            cal_int = int(cal)
        except ValueError:
            self._view.create_alert("Errore: inserire calorie in formato corretto")
            return
        self._model.buildGraph(cal)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model._grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model._grafo.edges)}"))
        tipiPorzione = self._model._grafo.nodes
        for n in tipiPorzione:
            self._view._ddPorzione.options.append(ft.dropdown.Option(n, on_click=self.readDDTipo))
        self._view.update_page()

    def handle_correlate(self, e):
        tipo = self._view._ddPorzione.value
        if tipo is None:
            self._view.create_alert("Errore: scegliere una tipologia")
            return
        self._view.txt_result.controls.append(ft.Text(f"Le tipologie di porzione correlate a {tipo} sono:"))
        connesse = self._model.getConnesse(tipo)
        for n in connesse:
            self._view.txt_result.controls.append(ft.Text(n))
        self._view.update_page()

    def handle_cammino(self, e):
        massimo = self._view._txtPassi.value
        try:
            massimo_int = int(massimo)
        except ValueError:
            self._view.create_alert("Errore: inserire #passi in formato corretto")
            return
        percorso, peso = self._model.getBestPath(massimo_int, self._view._ddPorzione.value)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Il cammino semplice di peso massimo ha peso {peso} ed è composto da:"))
        for p in percorso:
            self._view.txt_result.controls.append(ft.Text(f"{p}"))
        self._view.update_page()

    def readDDTipo(self, e):
        if e.control.data is None:
            self._selectedTipo = None
        else:
            self._selectedTipo = e.control.data
