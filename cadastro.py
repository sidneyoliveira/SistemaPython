import sqlite3
import tkinter
import customtkinter
import subprocess
from tkinter import *
from PIL import Image, ImageTk



def fazer_login():
    cadastro.destroy()
    subprocess.run(['python', 'login.py'])


def cadastrar():
    print("Cadastrar")
    if user.get() == senha.get():
        tkinter.messagebox.showinfo('Sistema Python', 'A senha não pode ser igual ao email, tente novamente!' )
        user.delete(0, "end")
        senha.delete(0, "end")
        return
    else:
        conexao = sqlite3.connect('banco_data.db')
        c = conexao.cursor()

        c.execute("INSERT INTO Client VALUES (:user, :senha)",
                  {
                      'user': user.get(),
                      'senha': senha.get()
                  }
                  )
        conexao.commit()
        conexao.close()
        user.delete(0, "end")
        senha.delete(0, "end")



customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("theme\light.json")

cadastro = customtkinter.CTk()
cadastro.title("Sistema Python")
cadastro.geometry('640x360+300+200')
cadastro.configure(background='black')
cadastro.resizable(False, False)

img = customtkinter.CTkImage(Image.open("img\cadastro.png"), size=(300, 300))

button = customtkinter.CTkLabel(master=cadastro, image=img, text="", )
button.grid(column=0, row=0, rowspan=8, padx=50, pady=20)

texto = customtkinter.CTkLabel(cadastro, text="Cadastre-se:",
                               font=('poppins medium', 30),
                               text_color="#3F84CB",
                               compound='left'
                               )
texto.grid(column=1, row=0, rowspan=1, padx=5, pady=0, sticky=W, )

usertitle = customtkinter.CTkLabel(cadastro, text="Email",
                                   font=('poppins medium', 15),
                                   text_color="#3F84CB",
                                   )

usertitle.place(x=420, y=70)

user = customtkinter.CTkEntry(cadastro, placeholder_text="Seu Email",
                              width=200, height=40,
                              border_width=2,
                              border_color='#dddddd',
                              corner_radius=10,
                              )

user.grid(column=1, row=2, padx=10, pady=0)

senhatitle = customtkinter.CTkLabel(cadastro, text="Senha",
                                    font=('poppins medium', 15),
                                    text_color="#3F84CB",
                                    compound='bottom')

senhatitle.place(x=420, y=150)

senha = customtkinter.CTkEntry(cadastro, placeholder_text="Sua Senha", show="*",
                               width=200, height=40,
                               border_width=2,
                               border_color='#dddddd',
                               corner_radius=10)

senha.grid(column=1, row=4, padx=10, pady=0)

botao_cadastro = customtkinter.CTkButton(cadastro, text="Cadastre-se", command=cadastrar, width=200, height=30,
                                      fg_color="#0A50FF")
botao_cadastro.grid(column=1, row=6, padx=0, pady=0)

texto_login = customtkinter.CTkLabel(cadastro, text=" Já possui um acesso?",
                                        font=('poppins medium', 12),
                                         text_color="gray50",
                                         fg_color="white",
                                         )
texto_login.grid(column=1, row=7, padx=0, pady=0, sticky=W)

botao_login = customtkinter.CTkButton(cadastro, text="Faça Login   ", command=fazer_login,
                                         width=60,
                                         height=10,
                                         font=('poppins medium', 12),
                                         text_color="#3F84CB",
                                         fg_color="white",
                                         hover_color="white"
                                         )
botao_login.grid(column=1, row=7, padx=0, pady=0, sticky=E, )

cadastro.mainloop()
