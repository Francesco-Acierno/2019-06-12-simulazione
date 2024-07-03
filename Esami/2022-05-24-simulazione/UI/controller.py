import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selectedCanzone = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        generi = self._model.getGeneri()
        for g in generi:
            self._view._ddGenere.options.append(ft.dropdown.Option(g))
        self._view.update_page()


    def handleCreaGrafo(self, e):
        genere = self._view._ddGenere.value

        if genere is None:
            self._view.create_alert("Selezionare un genere dal menù a tendina")
            return
        self._model.buildGraph(genere)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {len(self._model._grafo.edges)}"))
        canzoni = self._model._grafo.nodes
        for c in canzoni:
            self._view._ddCanzone.options.append(
                ft.dropdown.Option(data=c, text=c.Name, on_click=self.readDDCanzone))
        self._view.update_page()

    def readDDCanzone(self, e):
        if e.control.data is None:
            self._selectedCanzone = None
        else:
            self._selectedCanzone = e.control.data

    def handleDeltaMassimo(self, e):
        migliori = self._model.getBest()
        self._view.txt_result.controls.append(ft.Text("Coppia canzoni con delta massimo:"))
        for m in migliori:
            self._view.txt_result.controls.append(ft.Text(f"{m[0].Name} *** {m[1].Name} --> {m[2]['weight']}"))

        self._view.update_page()

    def handleCreaLista(self, e):
        if self._selectedCanzone is None:
            self._view.create_alert("Selezionare una canzone dal menù a tendina")
            return
        memoria = self._view._txtMemoria.value
        try:
            memoria_int = int(memoria)
        except ValueError:
            self._view.create_alert("Inserire un numero di bytes valido")
        cammino, peso = self._model.getBestPath(self._selectedCanzone, memoria_int)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La soluzione migliore è composta da {peso} canzoni e sono:"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"{c.Name}"))
        self._view.update_page()
