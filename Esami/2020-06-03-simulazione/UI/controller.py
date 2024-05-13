import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        media = self._view._txtGol.value
        try:
            media_float = float(media)
        except ValueError:
            self._view.create_alert("Errore: inserire media in formato corretto")
            return

        self._model.buildGraph(media_float)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))
        self._view.update_page()

    def handleTopPlayer(self, e):
        topPlayer, battuti = self._model.getTopPlayer()
        self._view.txt_result.controls.append(ft.Text(f"Top player: {topPlayer.PlayerID} {topPlayer.Name}"))
        self._view.txt_result.controls.append(ft.Text("Avversari battuti:"))
        for g in battuti:
            self._view.txt_result.controls.append(ft.Text(f"{g[0].PlayerID} {g[0].Name} | {g[1]}"))
        self._view.update_page()

    def handleDreamTeam(self, e):
        ngiocatori = self._view._txtGiocatori.value
        try:
            ngiocatori_int = int(ngiocatori)
        except ValueError:
            self._view.create_alert("Errore: inserire numero giocatori in formato corretto")
            return
        costo, listaNodi = self._model.getBestPath(ngiocatori_int)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La soluzione migliore ha grado di titolarità pari a {costo}"))
        for nodo in listaNodi:
            self._view.txt_result.controls.append(ft.Text(f"{nodo.Name}"))
        self._view.update_page()
