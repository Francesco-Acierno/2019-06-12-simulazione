import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddGenere = None
        self._btnCreaGrafo = None
        self._btnDeltaMassimo = None
        self._ddCanzone = None
        self._btnCreaLista = None
        self._txtMemoria = None
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
        self._title = ft.Text("Simulazione d'esame 24/05/2022 iTunes", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._ddGenere = ft.Dropdown(label="Genere")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self._ddGenere, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._controller.fillDD()

        # ROW2
        self._btnDeltaMassimo = ft.ElevatedButton(text="Delta Massimo",
                                                  on_click=self._controller.handleDeltaMassimo)

        row2 = ft.Row([
            ft.Container(None, width=300),
            ft.Container(self._btnDeltaMassimo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._ddCanzone = ft.Dropdown(label="Canzone")
        self._btnCreaLista = ft.ElevatedButton(text="Crea Lista",
                                               on_click=self._controller.handleCreaLista)
        row3 = ft.Row([
            ft.Container(self._ddCanzone, width=300),
            ft.Container(self._btnCreaLista, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW4
        self._txtMemoria = ft.TextField(label="Memoria")
        row4 = ft.Row([
            ft.Container(self._txtMemoria, width=300),
            ft.Container(None, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        # List View where the reply is printed
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
