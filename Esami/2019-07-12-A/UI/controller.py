import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._choiceCibo = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalisi(self, e):
        soglia = self._view._txtPorzioni.value
        try:
            sogliaInt = int(soglia)
        except ValueError:
            self._view.create_alert('Errore inserire un numero intero di porzioni')
        self._view.txt_result.controls.clear()
        grafo = self._model.buildGraph(sogliaInt)
        ingredienti = grafo.nodes
        ingredientiDD = map(lambda x: ft.dropdown.Option(
            data=x,
            text=x.display_name,
            on_click=self.getSelectedCibo), ingredienti)
        self._view._ddCibo.options = ingredientiDD
        self._view.txt_result.controls.append(ft.Text('Grafo correttamente creato'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {len(grafo.nodes)}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di archi: {len(grafo.edges)}'))
        self._view.update_page()

    def handleCalorie(self, e):
        if self._choiceCibo is None:
            self._view.create_alert("Selezionare un cibo dal menu a tendina")
            return
        massime = self._model.getMax(self._choiceCibo)
        self._view.txt_result.controls.append(ft.Text(f"I cibi che hanno calorie congiunte al cibo {self._choiceCibo.display_name} sono:"))
        for c in massime:
            self._view.txt_result.controls.append(ft.Text(f'{c[0].display_name}, calorie = {c[1]}'))
        self._view.update_page()



    def handleSimula(self, e):
        pass

    def getSelectedCibo(self, e):
        if e.control.data is None:
            self._choiceCibo = None
        else:
            self._choiceCibo = e.control.data
