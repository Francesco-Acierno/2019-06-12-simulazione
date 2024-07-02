import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esericizio gestore corsi"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_periodo = None
        self.btn_corsi_periodo = None
        self.btn_studenti_periodo = None
        self.txt_codice_corso = None
        self.btn_studenti_corso = None
        self.btn_dettaglio_corso = None
        self.lst_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Gestore corsi", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with controls for periodo didattico
        self.dd_periodo = ft.Dropdown(
            label="Periodo",
            options=[ft.dropdown.Option(key="1"),
                     ft.dropdown.Option(key="2")],
            width = 200,
            hint_text="Selezionare periodo didattico",
            on_change=self._controller.leggi_tendina
        )
        self.btn_corsi_periodo = ft.ElevatedButton(text="Corsi periodo",
                                                   width=200,
                                                   tooltip="Metodo per stampare i corsi del periodo didattico",
                                                   on_click=self._controller.get_corsi_periodo)
        self.btn_studenti_periodo = ft.ElevatedButton(text="Studenti periodo",
                                                   width=200,
                                                   tooltip="Metodo per stampare gli studenti iscritti ai corsi del periodo didattico",
                                                   on_click=self._controller.get_studenti_periodo)

        row1 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[self.dd_periodo,
                                                                       self.btn_corsi_periodo,
                                                                       self.btn_studenti_periodo])
        self._page.controls.append(row1)

        # Second row with controls for codice corso
        self.txt_codice_corso = ft.TextField(label="Codice corso",
                                             hint_text="Inserire il codice di un corso",
                                             width=300)
        self.btn_studenti_corso = ft.ElevatedButton(text="Studenti corso",
                                                   width=200,
                                                   tooltip="Metodo per stampare gli studenti iscritti ad un corso",
                                                   on_click=self._controller.get_studenti_corso)
        self.btn_dettaglio_corso = ft.ElevatedButton(text="Dettaglio corso",
                                                   width=200,
                                                   tooltip="Metodo per stampare il dettaglio degli studenti iscritti ad un corso",
                                                   on_click=self._controller.get_dettaglio_corso)

        row2 = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[self.txt_codice_corso,
                                                                       self.btn_studenti_corso,
                                                                       self.btn_dettaglio_corso])
        self._page.controls.append(row2)

        # Result
        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lst_result)

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
