import flet as ft
import time

def main(page: ft.Page):
    page.bgcolor = "transparent"
    page.window.bgcolor = "transparent"
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.always_on_top = True
    page.window.ignore_mouse_events = True
    
    page.window.width = 500
    page.window.height = 200
    page.padding = 0
    page.spacing=0

    page.window.left = 720
    page.window.top = 720

    animation_frames = [
        "animation/1.png",
        "animation/2.png",
        "animation/3.png",
        "animation/4.png",
        "animation/5.png",
        "animation/6.png",
    ]
    
    text = ft.Text("1234235235ываыва ыва ыв а", size = 30, color="white")
    image = ft.Image(
            src=animation_frames[0], #320x320
            width=120,
            height=120
            
        )
   
    container = ft.Stack(
        controls=[
            # Текст прижат к левому краю
            ft.Container(
                content=text,
                alignment=ft.alignment.center_left,
                left=10,
            ),
            # Картинка прижата к правому краю
            ft.Container(
                content=image,
                alignment=ft.alignment.center_right,
                right=10,
            ),
        ],
        expand=True,
    )
    def Animation():
        frame_time = 0.15

        while True:
            
            
            for id in range(len(animation_frames)):
                image.src = animation_frames[id]
                page.update()
                time.sleep(frame_time)
            time.sleep(1)
            for id in range(len(animation_frames)-1, -1, -1):
                image.src = animation_frames[id]
                page.update()
                time.sleep(frame_time)
            time.sleep(5)
            
    page.add(
        
        container
    )
    Animation()
    


ft.app(target=main)