import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._txtPassi = None
        self._btnCammino = None
        self._txtCalorie = None
        self._btnAnalisi = None
        self._ddPorzione = None
        self._btnCorrelate = None
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
        self._title = ft.Text("ESAME 03/09/2019", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._txtCalorie = ft.TextField(label="Calorie")
        self._btnAnalisi = ft.ElevatedButton(text="Analisi",
                                             on_click=self._controller.handle_analisi)
        row1 = ft.Row([
            ft.Container(self._txtCalorie, width=300),
            ft.Container(self._btnAnalisi, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._ddPorzione = ft.Dropdown(label="Tipo di porzione")
        self._btnCorrelate = ft.ElevatedButton(text="Correlate",
                                               on_click=self._controller.handle_correlate)

        row2 = ft.Row([
            ft.Container(self._ddPorzione, width=300),
            ft.Container(self._btnCorrelate, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._txtPassi = ft.TextField(label="Passi")
        self._btnCammino = ft.ElevatedButton(text="Cammino",
                                             on_click=self._controller.handle_cammino)
        row3 = ft.Row([
            ft.Container(self._txtPassi, width=300),
            ft.Container(self._btnCammino, width=300)
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
