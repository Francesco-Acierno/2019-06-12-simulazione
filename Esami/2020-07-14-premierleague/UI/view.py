import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.txt_result = None
        self._txtSogliaCritica = None
        self._btnCollegamento = None
        self._txtN = None
        self._btnClassifica = None
        self._ddSquadra = None
        self._btnCreaGrafo = None
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
        self._title = ft.Text("ESAME 14/07/2019-PremierLeague", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(None, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._ddSquadra = ft.Dropdown(label="Squadra")
        self._btnClassifica = ft.ElevatedButton(text="Classifica squadra",
                                                    on_click=self._controller.handleClassifica)

        row2 = ft.Row([
            ft.Container(self._ddSquadra, width=300),
            ft.Container(self._btnClassifica, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)


        # ROW3
        self._txtN = ft.TextField(label="N")
        self._btnCollegamento = ft.ElevatedButton(text="Collegamento",
                                                  on_click=self._controller.handleCollegamento)
        row3 = ft.Row([
            ft.Container(self._txtN, width=300),
            ft.Container(self._btnCollegamento, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW4
        self._txtSogliaCritica = ft.TextField(label="Soglia critica (x)")
        row4 = ft.Row([
            ft.Container(self._txtSogliaCritica, width=300),
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
