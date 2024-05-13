import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.txt_result = None
        self._btnCalcolaPercorso = None
        self._txtArtistiId = None
        self._btnArtistiConnessi = None
        self._btnCreaGrafo = None
        self._ddRuolo = None
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
        self._title = ft.Text("ESAME 20/01/2020", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._ddRuolo = ft.Dropdown(label="Ruolo")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea grafo",
                                               on_click=self._controller.handleCreaGrafo)
        self._controller.fillDD()
        row1 = ft.Row([
            ft.Container(self._ddRuolo, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._btnArtistiConnessi = ft.ElevatedButton(text="Artisti connessi",
                                                     on_click=self._controller.handleArtistiConnessi)

        row2 = ft.Row([
            ft.Container(None, width=300),
            ft.Container(self._btnArtistiConnessi, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW3
        self._txtArtistiId = ft.TextField(label="Artisti (id)")
        self._btnCalcolaPercorso = ft.ElevatedButton(text="Calcolo percorso",
                                                     on_click=self._controller.handleCalcolaPercorso)
        row3 = ft.Row([
            ft.Container(self._txtArtistiId, width=300),
            ft.Container(self._btnCalcolaPercorso, width=300)
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
