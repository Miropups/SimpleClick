import flet as ft
def main(page: ft.Page):
    page.bgcolor = "transparent"
    page.window.bgcolor = "transparent"
    page.window.title_bar_hidden = True
    #page.window.frameless = True
    page.window.always_on_top = True
    page.window.width = 250
    page.window.height = 150

    page.add(
        ft.Image(
            src="picture.webp",
            
        )
    )

ft.app(target=main)