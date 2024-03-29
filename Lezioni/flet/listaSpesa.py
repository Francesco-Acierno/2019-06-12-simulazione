import flet as ft


def main(page: ft.Page):
    def addCheckBox(e):
        strToAdd = txtIn.value
        txtIn.value = ""
        if strToAdd == '':
            return

        page.add(ft.Checkbox(label=strToAdd, value=False))

    # Row 1
    txtIn = ft.TextField(label="Aggiungi un elemento.")
    btnAdd = ft.CupertinoButton(text="Add", on_click=addCheckBox)
    row1 = ft.Row([txtIn, btnAdd], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row1)


ft.app(target=main)
