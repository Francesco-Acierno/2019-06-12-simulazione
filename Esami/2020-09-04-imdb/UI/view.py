import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_rank = None
        self.btn_film = None
        self.btn_Cammino = None
        self.btn_graph = None
        self.ddFilm = None
        self.txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("ESAME 04/09/2020 IMDB", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.txt_rank = ft.TextField(label="Rank (r)")

        # button for the "creat graph" reply
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self.txt_rank, self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.btn_film = ft.ElevatedButton(text="Film di Grado Massimo", on_click=self._controller.handle_film)

        row2 = ft.Row([self.btn_film],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.ddFilm = ft.Dropdown(label="Film")
        self.btn_Cammino = ft.ElevatedButton(text="Cammino incremento", on_click=self._controller.handle_cammino)
        row3 = ft.Row([self.ddFilm, self.btn_Cammino],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self._controller.fillDD()

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
