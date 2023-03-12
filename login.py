import sqlite3
import tkinter
import customtkinter
import subprocess
from tkinter import *
from PIL import Image
import ctypes



def fazer_login():
    print("Fazer Login")

    conexao = sqlite3.connect('banco_data.db')
    c = conexao.cursor()

    user1 = user.get()
    senha1 = senha.get()

    print(user1)
    print(senha1)

    cursor = c.execute("SELECT * FROM Client WHERE user = ? AND pass = ?", (user1, senha1))
    resultado = cursor.fetchall()
    print(resultado)

    if resultado:
        login.destroy()
        subprocess.run(['python', 'index.py'])
        return True
    # tkinter.messagebox.showinfo('Sistema Python', "Bem-vindo!")

    else:
        tkinter.messagebox.showinfo('Sistema Python', "Usuário ou senha incorretos.")
        return False

    conexao.commit()
    conexao.close()

    user.delete(0, "end")
    senha.delete(0, "end")

def theme():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue_dark")


def cadastro():
    login.destroy()
    subprocess.run(['python', 'cadastro.py'])


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

login = customtkinter.CTk()
login.title("Sistema Python")
login.geometry('640x360+300+200')
login.configure(background='black')
login.resizable(False, False)

img = customtkinter.CTkImage(Image.open("img/login.png"), size=(300, 300))

button = customtkinter.CTkLabel(master=login, image=img, text="", )
button.grid(column=0, row=0, rowspan=8, padx=50, pady=20)

texto = customtkinter.CTkLabel(login, text="Faça seu Login:",
                               font=('poppins medium', 25),
                               text_color="#3F84CB",
                               compound='left')
texto.grid(column=1, row=0, rowspan=1, padx=10, pady=0, sticky=W, )

usertitle = customtkinter.CTkLabel(login, text="Email",
                                   font=('poppins medium', 15),
                                   text_color="#3F84CB",
                                   )

usertitle.place(x=420, y=70)

user = customtkinter.CTkEntry(login, placeholder_text="Seu Email",
                              width=200, height=40,
                              border_width=2,
                              border_color='#dddddd',
                              corner_radius=10,
                              )

user.grid(column=1, row=2, padx=10, pady=0)

senhatitle = customtkinter.CTkLabel(login, text="Senha",
                                    font=('poppins medium', 15),
                                    text_color="#3F84CB",
                                    compound='bottom')

senhatitle.place(x=420, y=150)

senha = customtkinter.CTkEntry(login, placeholder_text="Sua Senha", show="*",
                               width=200, height=40,
                               border_width=2,
                               border_color='#dddddd',
                               corner_radius=10)

senha.grid(column=1, row=4, padx=10, pady=0)

botao_login = customtkinter.CTkButton(login, text="Login", command=fazer_login, width=200, height=30,
                                      fg_color="#0A50FF")
botao_login.grid(column=1, row=6, padx=0, pady=0)

texto_cadastro = customtkinter.CTkLabel(login, text="     É novo por aqui?",
                                        font=('poppins medium', 12),
                                        text_color="gray50",
                                        fg_color="white",
                                        )
texto_cadastro.grid(column=1, row=7, padx=0, pady=0, sticky=W)

botao_cadastro = customtkinter.CTkButton(login, text="Cadastre-se      ", command=cadastro,
                                         width=60,
                                         height=10,
                                         font=('poppins medium', 12),
                                         text_color="#3F84CB",
                                         fg_color="white",
                                         hover_color="white"
                                         )
botao_cadastro.grid(column=1, row=7, padx=0, pady=0, sticky=E)

login.mainloop()
