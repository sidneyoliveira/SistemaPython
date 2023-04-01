import tkinter as tk
from tkinter import ttk, filedialog
import os
import docx
import requests
from bs4 import BeautifulSoup
from docx import Document
from pdfminer.high_level import extract_text
from tkinter import filedialog
import customtkinter
from tkinter import *

import ctypes

global pdf_filename
id_item = 0
cnpj_list = ["", "", ""]
razao_list = ["", "", ""]
data_list =  ["", "", ""]

class TabelaApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Tabela de Dados')


        # Cria a tabela
        self.tabela = ttk.Treeview(master, columns=('CNPJ', 'Razão Social', 'Data da Coleta'))
        self.tabela.heading('#0', text='ID')
        self.tabela.heading('CNPJ', text='CNPJ')
        self.tabela.heading('Razão Social', text='Razão Social')
        self.tabela.heading('Data da Coleta', text='Data da Coleta')
        self.tabela.pack()

        # Cria o formulário de entrada de dados
        self.form = tk.Frame(master)
        self.form.pack(pady=10)

        self.cnpj_label = tk.Label(self.form, text='CNPJ:')
        self.cnpj_entry = tk.Entry(self.form)
        self.cnpj_label.grid(row=0, column=0)
        self.cnpj_entry.grid(row=0, column=1)

        self.razao_social_label = tk.Label(self.form, text='Razão Social:')
        self.razao_social_entry = tk.Entry(self.form)
        self.razao_social_label.grid(row=1, column=0)
        self.razao_social_entry.grid(row=1, column=1)

        self.data_coleta_label = tk.Label(self.form, text='Data da Coleta:')
        self.data_coleta_entry = tk.Entry(self.form)
        self.data_coleta_label.grid(row=2, column=0)
        self.data_coleta_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self.form, text='Adicionar')
        self.add_button.grid(row=3, column=1)
        self.add_button.bind("<Button-1>", input_pdf("botao_pdf"))

        self.add_button = tk.Button(self.form, text='salvar', command=self.adicionar_dados)
        self.add_button.grid(row=4, column=1)
        # Cria uma variável para gerenciar o ID dos itens da tabela
        self.item_id = 0

        # Adiciona eventos à tabela
        self.tabela.bind("<Double-1>", self.editar_item)
        self.tabela.bind("<Delete>", self.remover_item)



root = tk.Tk()
app = TabelaApp(root)
root.mainloop()
