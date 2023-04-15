import customtkinter
import subprocess
from tkinter import *
from PIL import Image, ImageTk

def abrir_arq(arq):
    subprocess.run(['python', arq])
    return True


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('theme/light.json')

index = customtkinter.CTk()
index.title("Departamento de Compras")

index.geometry('450x300+500+200')
index.config(bg='#f0f0f0')
icon_docx = PhotoImage(file="img/oficio_icon.png")

icon_oficio = customtkinter.CTkImage(light_image=Image.open("img/oficio_icon.png"),
                                  dark_image=Image.open("img/oficio_icon.png"),
                                  size=(40, 40))
botao_oficios = customtkinter.CTkButton(index,corner_radius=3, image=icon_oficio, height=40, width=80, text="Oficios",font=('Goldplay semibold', 14,),  compound="top", )
botao_oficios.grid(column=0, row = 1, padx = (30, 0), pady=30, )
botao_oficios.bind("<Button-1>", lambda event: abrir_arq('oficios1.py'))


icon_oficio = customtkinter.CTkImage(light_image=Image.open("img/oficio_icon.png"),
                                  dark_image=Image.open("img/oficio_icon.png"),
                                  size=(40, 40))
botao_agua = customtkinter.CTkButton(index,corner_radius=3, image=icon_oficio, height=40, width=80, text="Água",font=('Goldplay semibold', 14,),  compound="top", )
botao_agua.grid(column=1, row = 1, padx = (30, 0), pady=30, )
botao_agua.bind("<Button-1>", lambda event: abrir_arq('requisicao_agua.py'))


index.mainloop()

