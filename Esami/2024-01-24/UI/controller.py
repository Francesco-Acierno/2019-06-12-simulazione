import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        for a in range(2015, 2019):
            self._view._ddAnno.options.append(ft.dropdown.Option(a))
        metodi = self._model.getMetodi()
        for m in metodi:
            self._view._ddMetodo.options.append(
                ft.dropdown.Option(data=m, text=m.Order_method_type, on_click=self.readDDMetodo))
        self._view.update_page()

    def readDDMetodo(self, e):
        if e.control.data is None:
            self._selectedMetodo = None
        else:
            self._selectedMetodo = e.control.data

    def handleCreaGrafo(self, e):
        anno = int(self._view._ddAnno.value)

        if anno is None:
            self._view.create_alert("Selezionare un anno dal menù a tendina")
            return

        if self._selectedMetodo is None:
            self._view.create_alert("Selezionare un anno dal menù a tendina")
            return

        soglia = self._view._txtSoglia.value
        try:
            soglia_int = float(soglia)
        except ValueError:
            self._view.create_alert("Inserire un numero")
        if soglia_int<=0:
            self._view.create_alert("Inserire un numero maggiore di zero")


        self._model.buildGraph(anno, self._selectedMetodo.Order_method_code, soglia_int)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {len(self._model._grafo.edges)}"))
        self._view.update_page()

    def handleCalcolaProdotti(self, e):
        top5 = self._model.getAnalisi()
        self._view.txt_result.controls.append(ft.Text("I prodotti piu redditizi sono:"))
        for p in top5:
            self._view.txt_result.controls.append(ft.Text(f"Prodotto {p[0]}  Archi entranti {p[1]}  ricavi = {p[2]}"))
        self._view.update_page()

    def handleCalcolaCammino(self, e):
        self._view.txt_result.controls.clear()
        cammino, peso = self._model.getBestPath()
        self._view.txt_result.controls.append(ft.Text(f"Il percorso semplice di lunghezza massima ha peso: {peso}"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"Prodotto {c.Product_number}, ricavi = {c.ricavo}"))
        self._view.update_page()
