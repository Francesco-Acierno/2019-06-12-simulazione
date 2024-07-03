import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddSquadra = None
        self._btnCreaGrafo = None
        self._ddAnno = None
        self._btnDettagli = None
        self._txtTifosi = None
        self._btnSimula = None
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
        self._title = ft.Text("ESAME 30/06/2023 -Turno A", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._ddSquadra = ft.Dropdown(label="Squadra")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self._ddSquadra, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._controller.fillDDSquadre()

        # ROW2
        self._ddAnno = ft.Dropdown(label="Anno (a)")
        self._btnDettagli = ft.ElevatedButton(text="Dettagli",
                                              on_click=self._controller.handleDettagli)

        row2 = ft.Row([
            ft.Container(self._ddAnno, width=300),
            ft.Container(self._btnDettagli, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)


        # ROW3
        self._txtTifosi = ft.TextField(label="Tifosi")
        self._btnSimula = ft.ElevatedButton(text="Simula",
                                            on_click=self._controller.handleSimula)
        row3 = ft.Row([
            ft.Container(self._txtTifosi, width=300),
            ft.Container(self._btnSimula, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

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
