import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for i in range(2015, 2019):
            self._view.ddyear.options.append(ft.dropdown.Option(f"{i}"))
        countries = self._model.getNazioni()
        for coun in countries:
            self._view.ddcountry.options.append(ft.dropdown.Option(f"{coun}"))

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        nazione = self._view.ddcountry.value
        anno = self._view.ddyear.value
        if nazione is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare una nazione"))
            return
        if anno is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare un anno"))
            return
        self._model.buildGraph(nazione, anno)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di vertici: {self._model.getNumNodes()} Numero di Archi: {self._model.getNumEdges()}"))
        self._view.update_page()

    def handle_volume(self, e):
        self._view.txtOut2.controls.clear()
        volumi = self._model.getVolumeVendite()
        ordinato = dict(sorted(volumi.items(), key=lambda item: item[1], reverse=True))
        for (key, value) in ordinato.items():
            self._view.txtOut2.controls.append(ft.Text(f"{key} --> {value}"))
        self._view.update_page()

    def handle_path(self, e):
        max_archi = self._view.txtN.value
        self._view.txtOut3.controls.clear()
        try:
            tInt = int(max_archi)
            if tInt < 2:
                self._view.txtOut3.controls.clear()
                self._view.txtOut3.controls.append(ft.Text("Il valore inserito deve essere minimo 2"))
                self._view.update_page()
        except ValueError:
            self._view.txtOut3.controls.clear()
            self._view.txtOut3.controls.append(ft.Text("Il valore inserito non è un numero"))
            self._view.update_page()

        path, value = self._model.getCamminoOttimo(tInt)
        self._view.txtOut3.controls.append(ft.Text(f"Peso cammino massimo: {value}"))
        for cm in range(len(path) - 1):
            self._view.txtOut3.controls.append(ft.Text(
                f"{path[cm].Retailer_name} --> {path[cm + 1].Retailer_name}: {self._model._graph[path[cm]][path[cm + 1]]['weight']}"))

        self._view.update_page()
