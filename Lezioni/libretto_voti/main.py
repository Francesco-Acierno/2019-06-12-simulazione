import flet as ft

from Lezioni.libretto_voti.UI.controller import Controller
from Lezioni.libretto_voti.UI.view import View
from Lezioni.libretto_voti.modello.voto import Libretto


def main(page: ft.Page):
    v = View(page)
    l = Libretto()
    c = Controller(v, l)
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)
