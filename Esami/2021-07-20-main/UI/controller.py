import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDanno(self):
        for n in range(2005, 2014):
            self._view._ddAnno.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        rec = self._view._txtRecensioni.value
        try:
            rec_int = int(rec)
        except ValueError:
            self._view.create_alert("Errore: inserire un numero intero")
            return
        anno = self._view._ddAnno.value
        try:
            anno_int = int(anno)
        except ValueError:
            self._view.create_alert("Errore: inserire un anno in formato AAAA")
            return
        if 2005 > anno_int > 2013:
            self._view.create_alert("Errore: inserire un anno compreso tra il 2005 e il 2013")
            return
        self._model.buildGraph(rec_int, anno_int)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {len(self._model._grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {len(self._model._grafo.edges)}"))
        self._view.update_page()

    def handleGetUtenteSimile(self, e):
        pass

    def handleSimula(self, e):
        pass
