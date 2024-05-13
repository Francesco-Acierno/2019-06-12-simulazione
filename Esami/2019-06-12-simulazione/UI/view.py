import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._txtCalorie = None
        self._btnIngredienti = None
        self._ddIngrediente = None
        self._btnDieta = None
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
        self._title = ft.Text("ESAME 12/06/2019 - simulazione", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW1
        self._txtCalorie = ft.TextField(label="Calorie")
        self._btnIngredienti = ft.ElevatedButton(text="Ingredienti",
                                                 on_click=self._controller.handle_ingredienti)
        row1 = ft.Row([
            ft.Container(self._txtCalorie, width=300),
            ft.Container(self._btnIngredienti, width=300)
        ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW2
        self._ddIngrediente = ft.Dropdown(label="Ingrediente")
        self._btnDieta = ft.ElevatedButton(text="Dieta equilibrata",
                                           on_click=self._controller.handle_dieta)

        row2 = ft.Row([
            ft.Container(self._ddIngrediente, width=300),
            ft.Container(self._btnDieta, width=300)
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
