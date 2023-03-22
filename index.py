from tkinter import filedialog
import sqlite3
import tkinter
import customtkinter
import subprocess
from tkinter import *
from PIL import Image, ImageTk


def importar_pdf():
    file_location = filedialog.askopenfilename(title="Selecione o arquivo MAPA PDF",
                                          filetypes= (("pdf files","*.pdf"),
                                          ))
    return file_location



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



