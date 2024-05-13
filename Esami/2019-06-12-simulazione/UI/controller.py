import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceIngrediente = None

    def handle_ingredienti(self, e):
        cal = self._view._txtCalorie.value
        try:
            calR = float(cal)
        except ValueError:
            self._view.create_alert('Errore inserire un numero di calorie reale')
        self._view.txt_result.controls.clear()
        grafo = self._model.buildGraph(cal)
        ingredienti = grafo.nodes
        ingredientiDD = map(lambda x: ft.dropdown.Option(
            data=x,
            text=x. display_name,
            on_click=self.getSelectedIngrediente), ingredienti)
        self._view._ddIngrediente.options = ingredientiDD
        self._view.txt_result.controls.append(ft.Text('Grafo correttamente creato'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {len(grafo.nodes)}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di archi: {len(grafo.edges)}'))
        ingredientimax = self._model.getIngredienti()
        for i in ingredientimax:
            self._view.txt_result.controls.append(ft.Text(f"L'ingrediente {i} contiene {ingredientimax[i][0]} calorie "
                                                          f"ed è presente in {ingredientimax[i][1]} cibi diversi"))
        self._view.update_page()

    def handle_dieta(self, e):
        ingrediente = self._view._ddIngrediente.value
        if ingrediente is None:
            self._view.create_alert("Errore: selezionare un ingrediente")
        cammino, peso = self._model.getBestPath(self._choiceIngrediente)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'La dieta con il maggior apporto calorico avrà {peso} '
                                                      f'calorie ed include i seguenti ingredienti:'))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"- {c}"))
        self._view.update_page()

    def getSelectedIngrediente(self, e):
        if e.control.data is None:
            self._choiceIngrediente = None
        else:
            self._choiceIngrediente = e.control.data
