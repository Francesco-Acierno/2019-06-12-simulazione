import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddAnno = None
        self._ddBrand = None
        self._btnCreaGrafo = None
        self.txt_result1 = None
        self._ddProdotto = None
        self._btnPercorso = None
        self.txt_result2 = None
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
        self._title = ft.Text("ESAME 17/07/2023 - TURNO B", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 1
        self._ddAnno = ft.Dropdown(label="Anno (a)")

        row1 = ft.Row([
            ft.Container(self._ddAnno, width=300),
            ft.Container(None, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._controller.fillDDanno()

        # ROW2
        self._ddBrand = ft.Dropdown(label="Brand")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row2 = ft.Row([
            ft.Container(self._ddBrand, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._controller.fillDDBrand()

        # ROW 3
        self.txt_result1 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result1)
        self._page.update()

        #ROW 4
        self._ddProdotto = ft.Dropdown(label="Prodotto")
        self._btnPercorso = ft.ElevatedButton(text="Cerca Percorso",
                                              on_click=self._controller.handlePercorso)
        row4 = ft.Row([
            ft.Container(self._ddProdotto, width=300),
            ft.Container(self._btnPercorso, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        # ROW5
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result2)
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
