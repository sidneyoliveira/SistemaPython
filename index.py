from tkinter import filedialog
import sqlite3
import tkinter
import customtkinter
import subprocess
from tkinter import *
from PIL import Image, ImageTk

def botao_oficios():
    command = subprocess.run(['python', 'oficios1.py'])
    return True

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('theme/light.json')

index = customtkinter.CTk()
index.title("Sistema Python")

index.geometry('640x360+300+200')

icon_docx = PhotoImage(file="img/oficio_icon.png")

icon_oficio = customtkinter.CTkImage(light_image=Image.open("img/oficio_icon.png"),
                                  dark_image=Image.open("img/oficio_icon.png"),
                                  size=(40, 40))
botao_oficios = customtkinter.CTkButton(index,corner_radius=5, command=botao_oficios, image=icon_oficio, height=40, width=80, text="Oficios",font=('Goldplay semibold', 14,),  compound="top", )
botao_oficios.grid(column=0, row = 1, padx = 20, pady=10, )


index.mainloop()

