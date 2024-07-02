import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddLocalizzazione = None
        self._btnStatistiche = None
        self._btnRicercaCammino = None
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
        self._title = ft.Text("Esame 30/06/2021 - pomeriggio", color="blue", size=24)
        self._page.controls.append(self._title)


        # ROW1
        self._ddLocalizzazione = ft.Dropdown(label="Localizzazione")
        self._btnStatistiche = ft.ElevatedButton(text="Statistiche",
                                                 on_click=self._controller.handleStatistiche)
        row1 = ft.Row([
            ft.Container(self._ddLocalizzazione, width=300),
            ft.Container(self._btnStatistiche, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._btnRicercaCammino = ft.ElevatedButton(text="Ricerca cammino",
                                                    on_click=self._controller.handleRicercaCammino)

        row2 = ft.Row([
            ft.Container(self._btnRicercaCammino, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._controller.handleCreaGrafo()
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
