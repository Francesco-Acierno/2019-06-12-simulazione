import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selectedStato = None
        self._selectedAnno = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDAnno(self):
        anno = self._model.getAnni()
        for a in anno:
            self._view._ddAnno.options.append(
                ft.dropdown.Option(data=a, text=a, on_click=self.readDDAnno))
        self._view.update_page()

    def readDDAnno(self, e):
        if e.control.data is None:
            self._selectedAnno = None
        else:
            self._selectedAnno = e.control.data

    def handleAvvistamenti(self, e):
        if self._selectedAnno is None:
            self._view.create_alert("Selezionare un anno dal menu a tendina")
            return
        anno = self._selectedAnno.anno

        self._view.txt_result.controls.clear()
        self._model.buildGraph(anno)
        self._view.txt_result.controls.append(ft.Text('Grafo correttamente creato'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {len(self._model.grafo.nodes)}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di archi: {len(self._model.grafo.edges)}'))
        for s in self._model.grafo.nodes:
            self._view._ddStato.options.append(
                ft.dropdown.Option(data=s, text=s.Name, on_click=self.readDDStato))
        self._view.update_page()
    
    def readDDStato(self, e):
        if e.control.data is None:
            self._selectedStato = None
        else:
            self._selectedStato = e.control.data

    def handleAnalizza(self, e):
        if self._selectedStato is None:
            self._view.create_alert("Selezionare uno stato dal menu a tendina")
            return
        self._view.txt_result.controls.append(ft.Text(f'I nodi precedenti a {self._selectedStato.Name} sono:'))
        precedenti = self._model.getPrecedenti(self._selectedStato)
        for p in precedenti:
            self._view.txt_result.controls.append(ft.Text(f'{p.Name}'))
        self._view.txt_result.controls.append(ft.Text(f'I nodi successivi a {self._selectedStato.Name} sono:'))
        successivi = self._model.getSuccessivi(self._selectedStato)
        for s in successivi:
            self._view.txt_result.controls.append(ft.Text(f'{s[1].Name}'))
        raggiungibili = self._model.getRaggiungibili(self._selectedStato)
        self._view.txt_result.controls.append(
            ft.Text(f'I nodi raggiungibili da {self._selectedStato.Name} attraversando {len(raggiungibili)} archi e sono:'))
        for r in raggiungibili:
            self._view.txt_result.controls.append(ft.Text(f'{r.Name}'))
        self._view.update_page()


    def handleSequenzaAvvistamenti(self, e):
        if self._selectedStato is None:
            self._view.create_alert("Selezionare uno stato dal menu a tendina")
            return
        self._view.txt_result.controls.clear()
        costo, cammino = self._model.getBestPath(self._selectedStato)
        self._view.txt_result.controls.append(ft.Text(f'La soluzione migliore ha peso = {costo} ed è composta da:'))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f'{c.Name}'))
        self._view.update_page()

