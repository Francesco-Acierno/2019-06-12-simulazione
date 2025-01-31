import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddAnno = None
        self._btnCreaGrafo = None
        self._ddMetodo = None
        self._btnCalcolaProdotti = None
        self._txtSoglia = None
        self._btnCalcolaCammino = None
        self.txt_result = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 24/01/2024 - Turno unico", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 1
        self._ddAnno = ft.Dropdown(label="Anno (a)")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)

        row1 = ft.Row([
            ft.Container(self._ddAnno, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._ddMetodo = ft.Dropdown(label="Metodo")
        self._btnCalcolaProdotti = ft.ElevatedButton(text="Calcola prodotti redditizi",
                                                     on_click=self._controller.handleCalcolaProdotti)

        row2 = ft.Row([
            ft.Container(self._ddMetodo, width=300),
            ft.Container(self._btnCalcolaProdotti, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self._controller.fillDD()

        # ROW 3
        self._txtSoglia = ft.TextField(label="Soglia")
        self._btnCalcolaCammino = ft.ElevatedButton(text="Calcola cammino",
                                                    on_click=self._controller.handleCalcolaCammino)
        row3 = ft.Row([
            ft.Container(self._txtSoglia, width=300),
            ft.Container(self._btnCalcolaCammino, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW5
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
