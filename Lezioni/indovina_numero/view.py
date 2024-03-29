import flet as ft


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        #Row 1
        self._txtNmax = ft.TextField(label="N Max", width=100,
                                     disabled=True, value=self._controller.getNmax())
        self._txtMmax = ft.TextField(label="Tentativi Max", width=100,
                                     disabled=True, value=self._controller.getMmax())
        self._txtMrim = ft.TextField(label="Tentativi Rim", width=100,
                                     disabled=True, value=self._controller.getMrim())

        # row1 = ft.Row([self._txtNmax, self._txtMmax, self._txtMrim],
        #        alignment=ft.MainAxisAlignment.CENTER)

        #Row 2
        self._txtTentativo = ft.TextField(label="Tentativo", width=100,disabled=True)
        self._btnNuova = ft.ElevatedButton(text="Nuova Partita",
                                           on_click=self._controller.handleNuova)
        self._btnProva = ft.ElevatedButton(text="Prova",
                                           on_click=self._controller.handleProva,
                                           disabled=True)

        # row2 = ft.Row([self._btnNuova, self._txtTentativo, self._btnProva],
        #        alignment=ft.MainAxisAlignment.CENTER)

        #Row 3
        self._lvOut = ft.ListView()
        self._pb = ft.ProgressBar(width=400, color="amber")

        self._page.add(
            ft.Row([
                ft.Container(self._txtNmax, width=150),
                ft.Container(self._txtMmax, width=150),
                ft.Container(self._txtMrim, width=150)
            ], alignment=ft.MainAxisAlignment.CENTER),

            ft.Row([
                ft.Container(self._btnNuova, width=150),
                ft.Container(self._txtTentativo, width=150),
                ft.Container(self._btnProva, width=150),
            ], alignment=ft.MainAxisAlignment.CENTER),

            ft.Container(self._pb, alignment=ft.alignment.center),
            self._lvOut
        )

        # self._page.add(self._titolo, row1, row2, self._lvOut)

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()