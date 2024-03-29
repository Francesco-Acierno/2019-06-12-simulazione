import datetime

import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Libretto"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        self._titolo = None
        self._datePicker = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Il mio Libretto Voti ++",
                               color="blue", size=24)

        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self._page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self._titolo ],
                   alignment=ft.MainAxisAlignment.START)
        )


        # Row 1
        self._txtIn = ft.TextField(label="Nome",width=300)
        self._txtCFU = ft.TextField(label="CFU",width=100)
        self._ddVoto = ft.Dropdown(label="Voto",width=100)
        self._fillDdVoto()

        self._datePicker = ft.DatePicker(
            first_date=datetime.datetime(2022,11,1),
            last_date=datetime.datetime(2025,10,31)
        )

        self._page.overlay.append(self._datePicker)
        self._btnCalendar = ft.ElevatedButton("Pick date",
                                              icon=ft.icons.CALENDAR_MONTH,
                                              on_click=lambda _: self._datePicker.pick_date())


        row1 = ft.Row([self._txtIn, self._txtCFU, self._ddVoto, self._btnCalendar],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Row 2
        self._btnAdd = ft.ElevatedButton(text="Add", on_click=self._controller.handleAdd)
        self._btnPrint = ft.ElevatedButton(text="Print", on_click=self._controller.handlePrint)

        row2 = ft.Row([self._btnAdd, self._btnPrint],alignment=ft.MainAxisAlignment.CENTER)

        # Row 3
        self._lvOut = ft.ListView()

        self._page.add(row1, row2, self._lvOut)

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()
    def _fillDdVoto(self):
        for i in range(18,31):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self._page.theme_mode = (
            ft.ThemeMode.DARK
            if self._page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self._page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self._page.update()