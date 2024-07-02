import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._txtAnno = None
        self._btnSelezionaAnno = None
        self._ddForma = None
        self._btnCreaGrafo = None
        self.txt_result = None
        self._txtAlfa = None
        self._txtT1 = None
        self._btnSimula = None
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
        self._title = ft.Text("Esame 23-07-2018 Turno B", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._txtAnno = ft.TextField(label="Anno")

        row1 = ft.Row([
            ft.Container(self._txtAnno, width=300),
            ft.Container(None, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._txtXG = ft.TextField(label="xG")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea grafo",
                                               on_click=self._controller.handleCreaGrafo)

        row2 = ft.Row([
            ft.Container(self._txtXG, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._txtT1 = ft.TextField(label="T1")

        row3 = ft.Row([
            ft.Container(self._txtT1, width=300),
            ft.Container(None, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW4
        self._txtAlfa = ft.TextField(label="Alfa")
        self._btnSimula = ft.ElevatedButton(text="Simula",
                                            on_click=self._controller.handleSimula)

        row4 = ft.Row([
            ft.Container(self._txtAlfa, width=300),
            ft.Container(self._btnSimula, width=300)
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
