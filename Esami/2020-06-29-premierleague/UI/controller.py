import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.dizionario_mesi = {1: "gennaio", 2: "febbraio", 3: "marzo", 4: "aprile", 5: "maggio", 6: "giugno",
                                7: "luglio", 8: "agosto", 9: "settembre", 10: "ottobre", 11: "novembre", 12: "dicembre"}

    def fillDDMese(self):
        for m in self.dizionario_mesi:
            self._view._ddMese.options.append(ft.dropdown.Option(data=m, text=self.dizionario_mesi[m]))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        mese = self._view._ddMese.value
        for m in self.dizionario_mesi:
            if self.dizionario_mesi[m] == mese:
                meseDD = int(m)
        min = self._view._txtMin.value
        try:
            min_int = int(min)
        except ValueError:
            self._view.create_alert("Errore: inserire minuti in formato corretto")
            return
        if min_int < 0:
            self._view.create_alert("Errore: inserire un tempo corretto")
            return
        self._model.buildGraph(meseDD, min_int)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"#NODI: {len(self._model.grafo.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"#ARCHI: {len(self._model.grafo.edges)}"))
        partite = self._model.grafo.nodes
        for p in partite:
            self._view._ddm1.options.append(ft.dropdown.Option(data=p, text=p.MatchID))
            self._view._ddm2.options.append(ft.dropdown.Option(data=p, text=p.MatchID))
        self._view.update_page()

    def handleConnessioneMax(self, e):
        self._view.txt_result.controls.clear()
        archi, peso = self._model.getGradoMax()
        self._view.txt_result.controls.append(ft.Text("Coppie con connessione massima:"))
        for a in archi:
            self._view.txt_result.controls.append(ft.Text(f"[{a[0].MatchID}]-[{a[1].MatchID}] {peso}"))
        self._view.update_page()


    def handleCollegamento(self, e):
        m1 = self._view._ddm1.value
        m2 = self._view._ddm2.value
        if m1 is None or m2 is None:
            self._view.create_alert("Errore: inserire le partite")
            return
        self._view.txt_result.controls.clear()
        print(m1, m2)
        cammino, peso = self._model.getCamminoOttimo(m1, m2)
        self._view.txt_result.controls.append(ft.Text(f"Il percorso migliore ha peso massimo: {peso}"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"[{c.MatchID}]"))
        self._view.update_page()
