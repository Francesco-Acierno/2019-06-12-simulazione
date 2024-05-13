import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDanno(self):
        for n in range(2005, 2019):
            self._view._ddAnno.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillDDBrand(self):
        for b in self._model.getBrand():
            self._view._ddBrand.options.append(ft.dropdown.Option(b))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        brand = self._view._ddBrand.value
        if brand is None:
            self._view.create_alert("Errore: selezionare un brand")
            self._view.update_page()
        anno = self._view._ddAnno.value
        if anno is None:
            self._view.create_alert("Errore: selezionare un anno")
            self._view.update_page()
        self._model.buildGraph(brand, anno)
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result1.controls.append(ft.Text(f"numero di vertici: {len(self._model.grafo.nodes)}"))
        self._view.txt_result1.controls.append(ft.Text(f"numero di archi: {len(self._model.grafo.edges)}"))
        archi = self._model.getGradoMax()
        self._view.txt_result1.controls.append(ft.Text("Top 3 archi:"))
        for a in archi:
            self._view.txt_result1.controls.append(
                ft.Text(f"Arco da {a[0][0].Product_number} a {a[0][1].Product_number} {a[1]}"))
        ripetuti = self._model.ripetuti()
        self._view.txt_result1.controls.append(ft.Text("Nodi che compaiono almeno due volte:"))
        for r in ripetuti:
            self._view.txt_result1.controls.append(ft.Text(f"Product_number: {r.Product_number} "))
        for p in self._model.grafo.nodes:
            self._view._ddProdotto.options.append(ft.dropdown.Option(data=p, text=p.Product_number))
        self._view.update_page()

    def handlePercorso(self, e):
        prodotto = self._view._ddProdotto.value
        if prodotto is None:
            self._view.create_alert("Errore: selezionare un prodotto")
            self._view.update_page()
        cammino = self._model.searchPath(prodotto)
        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(ft.Text(f"Percorso piu lungo: {len(cammino)}"))
        for c in cammino:
            print(c)
            self._view.txt_result2.controls.append(ft.Text(f"{c[0].Product}-->{c[1].Product}"))
        self._view.update_page()
