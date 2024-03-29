from time import sleep

import flet as ft


def main(page: ft.Page):
    txtIn = ft.Text(value="Buongiorno TdP 2024!", color="red")
    page.controls.append(txtIn)
    page.update()

    # txtOut = ft.Text(value="Counter: ", color="red")
    # page.add(txtOut)  # è una shortcut ed equivale alle righe 8 e 9

    # for i in range(1, 100):
    #    txtOut.value = "Counter: " + str(i)
    #    txtOut.update()
    #    sleep(1)

    # def handleBottone(e):
    #   txtOut.value = ""
    #   page.update()
    #   sleep(1)
    #   txtOut.value = "Pulsante cliccato!"
    #   page.update()

    def handleBottone(e):
        lv.controls.append(ft.Text("Tasto Cliccato!"))
        lv.update()

    txt1 = ft.Text(value="Colonna 1", color="red")
    txt2 = ft.Text(value="Colonna 2", color="blue")
    btn = ft.ElevatedButton(text="Premi qui!", on_click=handleBottone)
    row1 = ft.Row([txt1, txt2, btn])
    txtOut = ft.Text(value="", color="red", size=24)
    page.add(row1, txtOut)
    page.update()

    lv = ft.ListView(expand=1, spacing=16, padding=26, auto_scroll=True)
    page.add(lv)


ft.app(target=main)  # view = ft.AppView.WEB_BROWSER apre una pagina web
# view = ft.AppView.FLET_APP (default) apre un'istanza locale
