import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selectedSquadra = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))
        teams = self._model.grafo.nodes
        for t in teams:
            self._view._ddSquadra.options.append(ft.dropdown.Option(data=t, text=t.Name, on_click=self.readDDSquadra))
        self._view.update_page()

    def readDDSquadra(self, e):
        if e.control.data is None:
            self._selectedSquadra = None
        else:
            self._selectedSquadra = e.control.data

    def handleClassifica(self, e):
        squadra = self._selectedSquadra
        if squadra is None:
            self._view.create_alert("Scegliere una squadra")
            return
        migliori, peggiori = self._model.getClassifica(squadra.TeamID)
        self._view.txt_result.controls.append(ft.Text("SQUADRE MIGLIORI:"))
        for m in migliori:
            self._view.txt_result.controls.append(ft.Text(f"{m[0].Name} ({m[1]})"))
        self._view.txt_result.controls.append(ft.Text("SQUADRE PEGGIORI:"))
        for p in peggiori:
            self._view.txt_result.controls.append(ft.Text(f"{p[0].Name} ({p[1]})"))
        self._view.update_page()

    def handleCollegamento(self, e):
        pass
