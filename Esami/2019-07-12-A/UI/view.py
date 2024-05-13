import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.txt_result = None
        self._txtK = None
        self._btnSimula = None
        self._ddCibo = None
        self._btnCalorie = None
        self._btnAnalisi = None
        self._txtPorzioni = None
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
        self._title = ft.Text("Esame 12/07/2019 - A", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._txtPorzioni = ft.TextField(label="Porzioni")
        self._btnAnalisi = ft.ElevatedButton(text="Analisi",
                                             on_click=self._controller.handleAnalisi)
        row1 = ft.Row([
            ft.Container(self._txtPorzioni, width=300),
            ft.Container(self._btnAnalisi, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._btnCalorie = ft.ElevatedButton(text="Calorie",
                                             on_click=self._controller.handleCalorie)
        row2 = ft.Row([
            ft.Container(None, width=300),
            ft.Container(self._btnCalorie, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._ddCibo = ft.Dropdown(label="Cibo")
        self._btnSimula = ft.ElevatedButton(text="Simula",
                                            on_click=self._controller.handleSimula)
        row3 = ft.Row([
            ft.Container(self._ddCibo, width=300),
            ft.Container(self._btnSimula, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW4
        self._txtK = ft.TextField(label="K")

        row4 = ft.Row([
            ft.Container(self._txtK, width=300),
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
