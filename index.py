from logging import root
from tkinter import filedialog
import sqlite3
import tkinter
import customtkinter
import subprocess
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd





file_location = filedialog.askopenfilename(title="Selecione o arquivo XLS",
                                          filetypes= (("xls files","*.xls"),
                                          ))
print(file_location)
file = xlrd.open_workbook(file_location)
print(file)
plan = file.sheet_by_name('dados')
print(plan)

x = plan.col.value(0)
y = plan.col.value(1)

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
        tkinter.messagebox.showinfo('Sistema Python', "Bem-vindo!")
        return True
    else:
        tkinter.messagebox.showinfo('Sistema Python', "Usuário ou senha incorretos.")
        return False

    conexao.commit()
    conexao.close()

    user.delete(0, "end")
    senha.delete(0, "end")


def cadastro():
    index.destroy()
    subprocess.run(['python', 'cadastro.py'])


customtkinter.set_appearance_mode("light")

TEMA = "theme/light.json"
customtkinter.set_default_color_theme(TEMA)

index = customtkinter.CTk()
index.title("Sistema Python")

largura_tela = index.winfo_screenwidth()
altura_tela = index.winfo_screenheight()

index.geometry("{0}x{1}+0+0".format(largura_tela, altura_tela))


menu_abas = customtkinter.CTkFrame(index, bg_color="gray50", width= largura_tela, height= 120)
menu_abas.grid(column=0, row=0,padx=0, pady=0 )



texto = customtkinter.CTkLabel(index, text="Area de Trabalho:",
                               font=('poppins medium', 25),
                               text_color="#3F84CB",
                               compound='left')
texto.grid(column=1, row=1, rowspan=1, padx=10, pady=0, sticky=W, )

# usertitle = customtkinter.CTkLabel(index, text="Email",
#                                    font=('poppins medium', 15),
#                                    text_color="#3F84CB",
#                                    )
#
# usertitle.place(x=420, y=70)

user = customtkinter.CTkEntry(index, placeholder_text="Seu Email",
                              width=200, height=40,
                              border_width=2,
                              border_color='#dddddd',
                              corner_radius=10,
                              )

user.grid(column=1, row=2, padx=10, pady=0)
#
# senhatitle = customtkinter.CTkLabel(index, text="Senha",
#                                     font=('poppins medium', 15),
#                                     text_color="#3F84CB",
#                                     compound='bottom')
#
# senhatitle.place(x=420, y=150)

senha = customtkinter.CTkEntry(index, placeholder_text="Sua Senha", show="*",
                               width=200, height=40,
                               border_width=2,
                               border_color='#dddddd',
                               corner_radius=10)

senha.grid(column=1, row=4, padx=10, pady=0)

botao_login = customtkinter.CTkButton(index, text="Login", command=fazer_login, width=200, height=30,
                                      fg_color="#0A50FF")
botao_login.grid(column=1, row=6, padx=0, pady=0)

texto_cadastro = customtkinter.CTkLabel(index, text="     É novo por aqui?",
                                        font=('poppins medium', 12),
                                        text_color="gray50",
                                        fg_color="white",
                                        )
texto_cadastro.grid(column=1, row=7, padx=0, pady=0, sticky=W)

botao_cadastro = customtkinter.CTkButton(index, text="Cadastre-se      ", command=openFile,
                                         width=60,
                                         height=10,
                                         font=('poppins medium', 12),
                                         text_color="#3F84CB",
                                         fg_color="white",
                                         hover_color="white"
                                         )
botao_cadastro.grid(column=0, row=0, padx=0, pady=0, sticky=E)
menu_abas = customtkinter.CTkFrame(index, bg_color="gray50", width= largura_tela, height= 120)
menu_abas.place(x=50, y=50 )

img = customtkinter.CTkImage(Image.open("img/login.png"), size=(largura_tela, (altura_tela-100)))
button = customtkinter.CTkLabel(master=index, image=img, text="", )
button.place(x=100, y=100)

index.mainloop()
