import os

import docx
import requests
from bs4 import BeautifulSoup
from docx import Document
from pdfminer.high_level import extract_text
from tkinter import filedialog
import customtkinter
from tkinter import *
from salvar_oficio import salvar_arquivo, input_pdf, on_input_change

cnpj1 = ""
cnpj2 = ""
cnpj3 = ""

global data1
global data2
global data3


class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, **kw):
        customtkinter.CTkButton.__init__(self, master=master, **kw)
    def return_value(self, value):
        self.master.return_value = value
        # self.master.destroy()

def return_value(self, value):
    self.master.return_value = value
    # self.master.destroy()

root = customtkinter.CTk()
root.geometry("600x300")
root.title("Input Demo")

input_cnpj1 = customtkinter.CTkEntry(root, placeholder_text="CNPJ",
                                     width=200, height=40,
                                     border_width=2,
                                     border_color='#dddddd',
                                     corner_radius=10, )
input_cnpj1.grid(column=1, row=1, padx=10, pady=10)
input_cnpj1.bind("<FocusOut>", on_input_change("cnpj1", input_cnpj1))

input_data1 = customtkinter.CTkEntry(root, placeholder_text="Data",
                                     width=200, height=40,
                                     border_width=2,
                                     border_color='#dddddd',
                                     corner_radius=10, )
input_data1.grid(column=2, row=1, padx=10, pady=10)
input_data1.bind("<FocusOut>", on_input_change("data1", input_data1))

input_cnpj2 = customtkinter.CTkEntry(root, placeholder_text="CNPJ",
                                     width=200, height=40,
                                     border_width=2,
                                     border_color='#dddddd',
                                     corner_radius=10, )

input_cnpj2.grid(column=1, row=2, padx=10, pady=10)
input_cnpj2.bind("<FocusOut>", on_input_change("cnpj2", input_cnpj2))

input_data2 = customtkinter.CTkEntry(root, placeholder_text="Data",
                                     width=200, height=40,
                                     border_width=2,
                                     border_color='#dddddd',
                                     corner_radius=10, )
input_data2.grid(column=2, row=2, padx=10, pady=10)
input_data2.bind("<FocusOut>", on_input_change("data2", input_data2))

input_cnpj3 = customtkinter.CTkEntry(root, placeholder_text="CNPJ",
                                     width=200, height=40,
                                     border_width=2,
                                     border_color='#dddddd',
                                     corner_radius=10, )
input_cnpj3.grid(column=1, row=3, padx=10, pady=10)
input_cnpj3.bind("<FocusOut>", on_input_change("cnpj3", input_cnpj3))

input_data3 = customtkinter.CTkEntry(root, placeholder_text="Data",
                                     width=200, height=40,
                                     border_width=2,
                                     border_color='#dddddd',
                                     corner_radius=10, )
input_data3.grid(column=2, row=3, padx=10, pady=10)
input_data3.bind("<FocusOut>", on_input_change("data3", input_data2))

# Criando a entrada e o botão personalizado
botao_pdf = CustomButton(root, text="Abrir Mapa PDF")
botao_pdf.grid(column=1, row=4, padx=10, pady=10, sticky=W)
botao_pdf.bind("<Button-1>", input_pdf("botao_pdf"))
# botao_pdf.bind("<FocusOut>", on_input_change("botao_pdf", botao_pdf))

# Criando a entrada e o botão personalizado
salvar_pdf = customtkinter.CTkButton(root, text="Salvar PDF")
salvar_pdf.grid(column=1, row=5, padx=10, pady=10, sticky=W)
salvar_pdf.bind("<FocusOut>", salvar_arquivo("botao_pdf"))

root.mainloop()

