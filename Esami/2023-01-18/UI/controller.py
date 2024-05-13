import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceProvider = None

    def fillDDProvider(self):
        provider = self._model.getProvider()
        providerDD = [ft.dropdown.Option(x) for x in provider]
        self._view._ddProvider.options = providerDD
        self._view.update_page()

    def handleCreaGrafo(self, e):
        dist = self._view._txtDistanza.value

        if dist is None:
            self._view.create_alert("Inserire una distanza e un provider")
            return
        try:
            dist_float = float(dist)
        except ValueError:
            self._view.create_alert("Inserire un valore valido nel campo distanza")
            return
        self._model.buildGraph(self._choiceProvider, dist_float)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {len(self._model._grafo.edges)}"))

        location = self._model._grafo.nodes
        locationDD = [ft.dropdown.Option(x) for x in location]
        self._view._ddTarget.options = locationDD
        self._view.update_page()

    def handleAnalisiGrafo(self, e):
        self._view.txt_result.controls.append(ft.Text("Vertici con più vicini:"))
        dizionario = self._model.getAnalisi()
        for l in dizionario:
            self._view.txt_result.controls.append(ft.Text(f"- {l}, #vicini = {dizionario[l]}"))
        self._view.update_page()

    def handleCalcolaPercorso(self, e):
        stringa = self._view._txtStringa.value
        if stringa is None:
            self._view.create_alert("inserire una stringa")
            return
        target = self._view._ddTarget.value
        if target is None:
            self._view.create_alert("inserire un target")
            return
        stringa_maiuscola = stringa.upper()
        cammino, peso = self._model.getCamminoOttimo(target, stringa_maiuscola)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il miglior cammino ha lunghezza: {peso}"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"{c}"))
        self._view.update_page()

    def getSelectedProvider(self, e):
        self._choiceProvider = e.control.value
