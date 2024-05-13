import time

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        ruoli = self._model.getRuoli()
        ruoliDD = map(lambda x: ft.dropdown.Option(x), ruoli)
        self._view._ddRuolo.options = ruoliDD
        self._view.update_page()

    def handleCreaGrafo(self, e):
        ruolo = self._view._ddRuolo.value
        if ruolo is None:
            self._view.create_alert("Errore: selezionare un ruolo dal menu a tendina")
            return
        self._model.buildGraph(ruolo)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))
        self._view.update_page()

    def handleArtistiConnessi(self, e):
        self._view.txt_result.controls.append(ft.Text("Le coppie di artisti che hanno esposto almeno un'opera insieme "
                                                      "sono:"))
        lista = self._model.artistiConnessi()
        for a in lista:
            self._view.txt_result.controls.append(ft.Text(f"{a[0].name} - {a[1].name}, esposizioni comuni = {a[2]['weight']}"))
        self._view.update_page()


    def handleCalcolaPercorso(self, e):
        artista = self._view._txtArtistiId.value
        try:
            artista_int = int(artista)
        except ValueError:
            self._view.create_alert("Inserire un id valido")
            return
        tic = time.time()
        self._view.txt_result.controls.clear()
        path, val = self._model.searchPath(artista_int)
        self._view.txt_result.controls.append(ft.Text(f"Peso cammino massimo: {val}"))
        for p in path:
            self._view.txt_result.controls.append(ft.Text(f"{p[0].name} --> {p[1].name}, esposizioni comuni: {p[2]['weight']}"))
        self._view.txt_result.controls.append(ft.Text(f"{time.time() - tic}s"))
        self._view.update_page()
