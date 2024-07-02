import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selectedLocalizzazione = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))
        localizzazioni = self._model.grafo.nodes
        for l in localizzazioni:
            self._view._ddLocalizzazione.options.append(
                ft.dropdown.Option(data=l, text=l, on_click=self.readDDLocalizzazione))
        self._view.update_page()

    def handleStatistiche(self, e):
        if self._selectedLocalizzazione is None:
            self._view.create_alert("Selezionare una localizzazione")
            return
        connessi = self._model.getConnessi(self._selectedLocalizzazione)
        self._view.txt_result.controls.append(ft.Text(f"I geni adiacenti a {self._selectedLocalizzazione} sono:"))
        for c in connessi:
            self._view.txt_result.controls.append(ft.Text(f'{c[0]}, {c[1]}'))
        self._view.update_page()

    def readDDLocalizzazione(self, e):
        if e.control.data is None:
            self._selectedLocalizzazione = None
        else:
            self._selectedLocalizzazione = e.control.data

    def handleRicercaCammino(self, e):
        if self._selectedLocalizzazione is None:
            self._view.create_alert("Selezionare una localizzazione")
            return
        cammino, peso = self._model.searchPath(self._selectedLocalizzazione)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il cammino di lunghezza massima ha peso {peso} ed è composto da:"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"{c}"))
        self._view.update_page()
