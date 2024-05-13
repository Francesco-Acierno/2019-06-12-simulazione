import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._selectedArtista = None

    def fillDDGeneri(self):
        generi = self._model.getGeneri()
        generiDD = map(lambda x: ft.dropdown.Option(x), generi)
        self._view._ddGenere.options.extend(generiDD)
        self._view.update_page()

    def handleCreaGrafo(self, e):
        genere = self._view._ddGenere.value
        if genere is None:
            self._view.create_alert("Errore: inserire un genere")
            return

        self._model.buildGraph(genere)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))

        attori = self._model.grafo.nodes
        attoriDD = map(lambda x: ft.dropdown.Option(data=x, text=x, on_click=self.readDDArtista), attori)
        self._view._ddAttore.options.extend(attoriDD)
        self._view.update_page()

    def handleAttoriSimili(self, e):
        attore = self._selectedArtista
        if attore is None:
            self._view.create_alert("Errore: selezionare un attore")
            return
        simili = self._model.getSimili(attore)
        self._view.txt_result.controls.append(ft.Text(f"Attori simili a: {attore}"))
        for a in simili:
            self._view.txt_result.controls.append(ft.Text(a))
        self._view.update_page()


    def handleSimulazione(self, e):
        pass

    def readDDArtista(self, e):
        if e.control.data is None:
            self._selectedArtista = None
        else:
            self._selectedArtista = e.control.data

