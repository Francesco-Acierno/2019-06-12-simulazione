import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDSquadre(self):
        squadre = self._model.getSquadre()
        for s in squadre:
            self._view._ddSquadra.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        squadra = self._view._ddSquadra.value

        if squadra is None:
            self._view.create_alert("Selezionare una squadra dal menu a tendina")
            return
        self._model.buildGraph(squadra)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {len(self._model.grafo.edges)}"))
        anni = self._model.grafo.nodes
        for a in anni:
            self._view._ddAnno.options.append(
                ft.dropdown.Option(data=a, text=a, on_click=self.readDDAnno))
        self._view.update_page()

    def readDDAnno(self, e):
        if e.control.data is None:
            self._selectedAnno = None
        else:
            self._selectedAnno = e.control.data

    def handleDettagli(self, e):
        if self._selectedAnno is None:
            self._view.create_alert("Selezionare un anno dal menu a tendina")
            return
        vicini = self._model.getAdiacenti(self._selectedAnno)
        self._view.txt_result.controls.append(ft.Text(f"I nodi adiacenti al nodo {self._selectedAnno} sono:"))
        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{v[0]}, peso = {v[1]}"))
        self._view.update_page()


    def handleSimula(self, e):
        pass