import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._selectedGene = None

    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))
        geni = self._model.grafo.nodes
        for g in geni:
             self._view._ddGene.options.append(ft.dropdown.Option(data=g, text=g.GeneID, on_click=self.readDDGene))
        self._view.update_page()

    def readDDGene(self, e):
        if e.control.data is None:
            self._selectedGene = None
        else:
            self._selectedGene = e.control.data


    def handleGeniAdiacenti(self, e):
        if self._selectedGene is None:
            self._view.create_alert("Selezionare un gene")
            return
        vicini = self._model.getVicini(self._selectedGene)
        self._view.txt_result.controls.append(ft.Text(f"I geni adiacenti a {self._selectedGene.GeneID} sono:"))
        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f'{v[0].GeneID}, {v[1]}'))
        self._view.update_page()

    def handleSimulazione(self, e):
        pass