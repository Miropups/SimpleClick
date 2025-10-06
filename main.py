import flet as ft
import time
import random



notes = []
with open("NotesFile.txt", 'r') as file:
    for line in file:
        notes.append(line.strip())


def main(page: ft.Page):

    page.fonts= {
        "pixelFont": "fonts/Comic Sans MS Pixel.ttf"  # Путь к файлу шрифта
    }

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
    page.window.top = 680

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
        size = 20, 
        color="black",
        overflow=ft.TextOverflow.ELLIPSIS,
        max_lines=3,
        font_family="pixelFont"   )  
    image = ft.Image(
        src=animation_frames[0],
         #320x320
        width=120,
        height=120
            
        )
    text_background = ft.Container(
        margin=ft.margin.only(top=50),
        content=text,
        bgcolor="#FBF2BE",
        padding=5,
        border_radius=10,
        opacity=0
        
        
    )
    wrapper = ft.Row(
        [text_background],
        width = 300,  # ⬅️ ограничение максимальной ширины
        wrap=True,  # разрешаем перенос строк в Row
        alignment=ft.MainAxisAlignment.END
    )
    image_container = ft.Container(
                content=image,
                alignment=ft.alignment.center_right,         
            )          
    container = ft.Row(
        controls=[
            wrapper,
            image_container   
        ],
        
        alignment=ft.MainAxisAlignment.END,  # Картинка прижата к правому краю
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True,
    )
    def Animation():
        frame_time = 0.1
        nonlocal text
        global notes
        
        while True:
            
            time.sleep(5)
            text.value = ''
            text_background.opacity = 0
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
            
            
            index = random.randint(0, len(notes)-1)
            text_background.opacity = 1
            text.value = notes[index]
            page.update()         
    page.add(
        
        container
    )
    Animation()


def test(page:ft.Page):
    page.title = "Адаптивная ширина текста"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Сам "пузырёк" с текстом
    text_box = ft.Container(
        content=ft.Text(
            "1.",
            color=ft.Colors.WHITE,
            no_wrap=False,    # разрешаем перенос строк
            selectable=True,
            max_lines=None,
        ),
        bgcolor=ft.Colors.BLUE_700,
        padding=ft.padding.all(12),
        border_radius=ft.border_radius.all(10),
        margin=ft.margin.all(10),
        expand=False,       # не растягиваем контейнер
    )

    # Обёртка, которая задаёт максимум
    wrapper = ft.Row(
        [text_box],
        alignment=ft.MainAxisAlignment.START,
        width=400,  # ⬅️ ограничение максимальной ширины
        wrap=True,  # разрешаем перенос строк в Row
    )

    page.add(wrapper)

ft.app(target=main)