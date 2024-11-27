import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import pygame
import os
import random
import webbrowser
import cv2  # Для работы с видео

# Инициализация pygame для воспроизведения музыки
pygame.mixer.init()
try:
    pygame.mixer.music.load("Data/SFX/1-01 - Inside the Wall.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
except pygame.error:
    print("Music file not found!")

# Создание главного окна
window = tk.Tk()
window.title("Cargo")
window.geometry("1450x900")
window.resizable(False, False)
icon = tk.PhotoImage(file='Data/Images/Icon.png') 
window.iconphoto(True, icon)

# Подготовка видео
video_path = "Earth Rotation Loop.mp4"  # Укажите путь к видео
cap = cv2.VideoCapture(video_path)

def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (1450, 900))  # Подгонка под размеры окна
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Преобразование BGR -> RGB
        img = ImageTk.PhotoImage(image=Image.fromarray(frame))
        video_label.config(image=img)
        video_label.image = img
        video_label.after(33, play_video)  # Обновление кадра через 33 мс (30 FPS)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Сброс видео к началу
        play_video()

# Использование шрифта Courier (стандартный моноширинный шрифт)
pixel_font = font.Font(family="Courier", size=20)

# Функция для изменения цвета текста в зависимости от положения курсора
def on_enter(event, label):
    label.config(fg="yellow", height=2)

def on_enter3(event, label):
    label.config(fg="purple")
def on_leave(event, label):
    label.config(fg="white", width=0, height=0)

# Функция для действия при нажатии на "кнопку"
def action1(event):
    pygame.mixer.music.stop()
    window.destroy()
    os.system("python Precious_Cargo.pyw")
    
def update_quote():
    new_quote = random.choice(quotes)
    quote_label.config(text=new_quote)
    window.after(5000, update_quote)  # Обновляет цитату каждые 5 секунд

def action2(event):
    window.destroy()

def action3(event):
    webbrowser.open_new_tab("https://github.com/KIRALAINEisSTUPID/Undertale-pygame")

# Добавление видео в качестве фона
video_label = tk.Label(window)
video_label.place(relwidth=1, relheight=1)

# Цитаты
quotes = [
    "Game for fun, not for money.",
    "Stay determined.",
    "Its writed on Vscode.",
    "It's a beautiful day outside... birds are singing...",
    "2+2=5",
    "has bugs which bigger than galactic",
    "did you your homewroks?",
    "when C++?",
    "windows sucks",
    "PDP academy's wifi pasword?",
]

# Цитата
quote_label = tk.Label(window, text=random.choice(quotes), bg="black", fg="white", font=pixel_font)
quote_label.place(x=0, y=0)

# Создание меток, которые будут работать как кнопки
label1 = tk.Label(window, text="Play", bg="black", fg="white", font=pixel_font, cursor="hand2")
label1.place(x=300, y=350)
label1.bind("<Enter>", lambda e: on_enter(e, label1))
label1.bind("<Leave>", lambda e: on_leave(e, label1))
label1.bind("<Button-1>", action1)

label2 = tk.Label(window, text="Quit", bg="black", fg="white", font=pixel_font, cursor="hand2")
label2.place(x=1050, y=350)
label2.bind("<Enter>", lambda e: on_enter(e, label2))
label2.bind("<Leave>", lambda e: on_leave(e, label2))
label2.bind("<Button-1>", action2)

label3 = tk.Label(window, text="View code on Github♡", bg="black", fg="white", font=pixel_font, cursor="hand2")
label3.place(x=500, y=860)
label3.bind("<Enter>", lambda e: on_enter3(e, label3))
label3.bind("<Leave>", lambda e: on_leave(e, label3))
label3.bind("<Button-1>", action3)

# Запуск воспроизведения видео и цитат
play_video()
update_quote()
window.mainloop()
