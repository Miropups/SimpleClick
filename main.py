import flet as ft
def main(page: ft.Page):
    page.bgcolor = "transparent"
    page.window.bgcolor = "transparent"
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.always_on_top = True
    page.window.ignore_mouse_events = True
    
    page.window.width = 200
    page.window.height = 200
    page.padding = 0
    page.spacing=0

    page.window.left = 1120
    page.window.top = 720
    

    page.add(
        ft.Image(
            src="1.png", #320x320
            width=120,
            height=120,
            
            
        )
    )

ft.app(target=main)