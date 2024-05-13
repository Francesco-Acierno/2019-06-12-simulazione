import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selectedAlbum = None
        self._selectedAlbum2 = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_graph(self, e):
        numeroCanzoni = self._view.txtNCanzoni.value
        numeroCanzoniT = 0
        try:
            numeroCanzoniT = int(numeroCanzoni)
        except ValueError:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Inserire un numero intero positivo"))
            self._view.update_page()
        self._model.buildGraph(numeroCanzoniT)
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di nodi: {len(self._model._graph.nodes)}"))
        self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {len(self._model._graph.edges)}"))
        self._view.update_page()
        for a in self._model._graph.nodes:
            self._view.ddAlbum_a1.options.append(ft.dropdown.Option(data=a, text=a.Title, on_click=self.readDDAlbum))
            self._view.ddAlbum_a2.options.append(ft.dropdown.Option(data=a, text=a.Title, on_click=self.readDDAlbum2))
        self._view.update_page()

    def readDDAlbum(self, e):
        if e.control.data is None:
            self._selectedAlbum = None
        else:
            self._selectedAlbum = e.control.data

    def readDDAlbum2(self, e):
        if e.control.data is None:
            self._selectedAlbum2 = None
        else:
            self._selectedAlbum2 = e.control.data

    def handle_adiacenti(self, e):
        a1 = self._selectedAlbum
        if a1 is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Selezionare un album"))
            self._view.update_page()
        self._view.txtOut.controls.clear()
        vicini_dizionario = self._model.getVicini(a1)
        for a in vicini_dizionario:
            self._view.txtOut.controls.append(ft.Text(f"{a[0].Title}, bilancio:{a[1]}"))
        self._view.update_page()

    def handle_percorso(self, e):
        soglia = self._view.txtSoglia.value
        sogliaT = 0
        s = self._selectedAlbum
        a = self._selectedAlbum2
        try:
            sogliaT = int(soglia)
        except ValueError:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Inserire un numero intero positivo"))
            self._view.update_page()
        if s is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Selezionare un album"))
            self._view.update_page()
        if a is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Selezionare un album"))
            self._view.update_page()

        self._view.txtOut.controls.clear()
        path = self._model.getCamminoOttimo(s, a, sogliaT)
        self._view.txtOut.controls.append(ft.Text(f"Il percorso ottimo tra {s} e {a}"))
        for p in path:
            self._view.txtOut.controls.append(ft.Text(f"{p}"))
        self._view.update_page()



