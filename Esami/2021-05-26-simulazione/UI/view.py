import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.txt_result = None
        self._txtSoglia = None
        self._btnCalcolaPercorso = None
        self._ddLocale = None
        self._btnLocaleMigliore = None
        self._ddAnno = None
        self._btnCreaGrafo = None
        self._ddCitta = None
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
        self._title = ft.Text("Simulazione d'esame 26/05/2021", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._ddCitta = ft.Dropdown(label="Città")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self._ddCitta, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._ddAnno = ft.Dropdown(label="Anno (a)")
        self._btnLocaleMigliore = ft.ElevatedButton(text="Locale Migliore",
                                                    on_click=self._controller.handleLocaleMigliore)

        row2 = ft.Row([
            ft.Container(self._ddAnno, width=300),
            ft.Container(self._btnLocaleMigliore, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self._controller.fillDD()

        # ROW3
        self._ddLocale = ft.Dropdown(label="Locale")
        self._btnCalcolaPercorso = ft.ElevatedButton(text="Calcola Percorso",
                                                     on_click=self._controller.handleCalcolaPercorso)
        row3 = ft.Row([
            ft.Container(self._ddLocale, width=300),
            ft.Container(self._btnCalcolaPercorso, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW 4
        self._txtSoglia = ft.TextField(label="Soglia")

        row4 = ft.Row([
            ft.Container(self._txtSoglia, width=300),
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
