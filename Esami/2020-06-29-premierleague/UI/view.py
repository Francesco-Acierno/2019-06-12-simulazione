import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.txt_result = None
        self._ddm2 = None
        self._btnCollegamento = None
        self._ddm1 = None
        self._btnConnessioneMax = None
        self._ddMese = None
        self._btnCreaGrafo = None
        self._txtMin = None
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
        self._title = ft.Text("ESAME 29/06/2020-PremierLeague", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._txtMin = ft.TextField(label="Min")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo",
                                               on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([
            ft.Container(self._txtMin, width=300),
            ft.Container(self._btnCreaGrafo, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._ddMese = ft.Dropdown(label="Mese")
        self._btnConnessioneMax = ft.ElevatedButton(text="Connessione Max",
                                                    on_click=self._controller.handleConnessioneMax)

        row2 = ft.Row([
            ft.Container(self._ddMese, width=300),
            ft.Container(self._btnConnessioneMax, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._controller.fillDDMese()


        # ROW3
        self._ddm1 = ft.Dropdown(label="m1")
        self._btnCollegamento = ft.ElevatedButton(text="Collegamento",
                                                  on_click=self._controller.handleCollegamento)
        row3 = ft.Row([
            ft.Container(self._ddm1, width=300),
            ft.Container(self._btnCollegamento, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # ROW4
        self._ddm2 = ft.Dropdown(label="m2")
        row4 = ft.Row([
            ft.Container(self._ddm2, width=300),
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
