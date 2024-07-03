import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selectedLocale = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        for a in range(2005, 2014):
            self._view._ddAnno.options.append(ft.dropdown.Option(a))
        for c in self._model.getCitta():
            self._view._ddCitta.options.append(ft.dropdown.Option(c))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        citta = self._view._ddCitta.value
        if citta is None:
            self._view.create_alert("Selezionare una città dal menù a tendina")
            return

        anno = int(self._view._ddAnno.value)
        if anno is None:
            self._view.create_alert("Selezionare un anno dal menù a tendina")
            return

        self._model.buildGraph(citta, anno)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {len(self._model._grafo.edges)}"))
        locali = self._model._grafo.nodes
        for l in locali:
            self._view._ddLocale.options.append(
                ft.dropdown.Option(data=l, text=l.business_name, on_click=self.readDDLocale))
        self._view.update_page()

    def readDDLocale(self, e):
        if e.control.data is None:
            self._selectedLocale = None
        else:
            self._selectedLocale = e.control.data

    def handleLocaleMigliore(self, e):
        migliore = self._model.getMigliore()
        self._view.txt_result.controls.append(ft.Text(f"Il miglior locale in città è: {migliore[0].business_name}"))
        self._view.update_page()

    def handleCalcolaPercorso(self, e):
        if self._selectedLocale is None:
            self._view.create_alert("Selezionare un locale dal menu a tendina")
            return
        soglia = self._view._txtSoglia.value
        try:
            soglia_int = float(soglia)
        except ValueError:
            self._view.create_alert("Inserire un numero")
            return
        if soglia_int < 0 or soglia_int > 1:
            self._view.create_alert("Inserire una soglia compresa tra 0 e 1")
            return

        cammino, peso = self._model.getBestPath(self._selectedLocale, soglia_int)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il cammino migliore ha peso {peso}"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(c.business_name))
        self._view.update_page()
