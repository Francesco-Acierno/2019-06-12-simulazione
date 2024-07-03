import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddAnno = None
        self._btnAvvistamenti = None
        self._ddStato = None
        self._btnAnalizza = None
        self._btnSequenzaAvvistamenti = None
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
        self._title = ft.Text("Ufo sightings (simulazione d'esame 11/06/2018", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._ddAnno = ft.Dropdown(label="Anno")
        self._btnAvvistamenti = ft.ElevatedButton(text="Avvistamenti",
                                                  on_click=self._controller.handleAvvistamenti)
        self._controller.fillDDAnno()
        row1 = ft.Row([
            ft.Container(self._ddAnno, width=300),
            ft.Container(self._btnAvvistamenti, width=300),
            ft.Container(None, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._ddStato = ft.Dropdown(label="Stato")
        self._btnAnalizza = ft.ElevatedButton(text="Analizza",
                                              on_click=self._controller.handleAnalizza)
        self._btnSequenzaAvvistamenti = ft.ElevatedButton(text="Sequenza avvistamenti",
                                                          on_click=self._controller.handleSequenzaAvvistamenti)

        row2 = ft.Row([
            ft.Container(self._ddStato, width=300),
            ft.Container(self._btnAnalizza, width=300),
            ft.Container(self._btnSequenzaAvvistamenti, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

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
