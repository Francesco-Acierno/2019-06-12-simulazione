import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        anno = self._view._txtAnno.value
        try:
            anno_int = int(anno)
        except ValueError:
            self._view.create_alert("Inserire un anno nel formato corretto")
            return
        if anno_int < 1906 or anno_int > 2014:
            self._view.create_alert("Inserire un anno compreso tra il 1910 e il 2014 (estremi inclusi)")
            return

        diffGiorni = self._view._txtXG.value
        try:
            diffGiorni_int = int(diffGiorni)
        except ValueError:
            self._view.create_alert("Inserire un intervallo di giorni valido")
            return
        if diffGiorni_int < 1 or diffGiorni_int > 180:
            self._view.create_alert("Inserire un intervallo di giorni compreso tra 1 e 180 (estremi inclusi)")
            return

        self._view.txt_result.controls.clear()
        self._model.buildGraph(anno_int, diffGiorni)
        self._view.txt_result.controls.append(ft.Text('Grafo correttamente creato'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {len(self._model.grafo.nodes)}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di archi: {len(self._model.grafo.edges)}'))
        vicini = self._model.getAdiacenti()
        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f'Il peso dei vicini di {v.Name} è {vicini[v]}'))
        self._view.update_page()

    def handleSimula(self, e):
        pass
