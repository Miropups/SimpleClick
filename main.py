import flet as ft
import time
import random

def main(page: ft.Page):
    page.bgcolor = "transparent"
    page.window.bgcolor = "transparent"
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.always_on_top = True
    page.window.ignore_mouse_events = True
    
    page.window.width = 450
    page.window.height = 200
    page.padding = 0
    page.spacing=0

    page.window.left = 920
    page.window.top = 720

    animation_frames = [
        "animation/1.png",
        "animation/2.png",
        "animation/3.png",
        "animation/4.png",
        "animation/5.png",
        "animation/6.png",
    ]
    
    text = ft.Text(
        "", 
        size = 15, 
        color="white",
        overflow=ft.TextOverflow.ELLIPSIS,
        max_lines=3,

        )
    
    image = ft.Image(
        src=animation_frames[0],
         #320x320
        width=120,
        height=120
            
        )
   
    container = ft.Stack(
        controls=[
            # Текст прижат к левому краю
            ft.Container(
                border_radius=15,
                content=text,
                alignment=ft.alignment.center_right,
                left = 10,
                bgcolor=ft.Colors.BLACK26,
                padding=10,
                width=300
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
        nonlocal text
        
        while True:
            
            time.sleep(5)
            text.value = ''
            page.update()
            for id in range(len(animation_frames)):
                image.src = animation_frames[id]
                
                page.update()
                time.sleep(frame_time)
            time.sleep(1)
            for id in range(len(animation_frames)-1, -1, -1):
                image.src = animation_frames[id]
                page.update()
                time.sleep(frame_time)
            
            notes = [
                'а ты не плох',
                'как же твой код хорош',
                'МОЙ СОЗДАТЕЛЬ - ДУРАК, не учится нифига, фигней страдает',
                'кастую автомат на сессию'
            ]
            index = random.randint(0, len(notes)-1)
            text.value = notes[index]
            page.update()
            
            
    page.add(
        
        container
    )
    Animation()
    


ft.app(target=main)