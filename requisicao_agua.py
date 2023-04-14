import os
import tkinter as tk
from tkinter import filedialog, ttk

from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import customtkinter
import ctypes
import openpyxl
import datetime
import win32com.client as win32



# Variáveis globais
global pdf_filename

id_item = 0
NUM = ''
QUANT = [0, 0, 0]
dados = [0, 0, 0, 0, 0, '','']


def on_input_change2(var_name, input_obj):
    def on_change(event):
        QUANT[var_name] = input_obj.get()
        print(QUANT[var_name])

        global dados
        dados[var_name+2] = QUANT[var_name]
        print(f'dados {dados[var_name+2]}')

    return on_change

def on_change(var_name, input_obj):
    QUANT[var_name] = input_obj.get()
    print(QUANT[var_name])

    global dados
    dados[var_name+2] = QUANT[var_name]
    print(f'dados {dados[var_name+2]}')


def exibir_alerta(titulo, mensagem, tipo_icone):
    ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, tipo_icone)


def salvar_xls():

    global dados
    workbook = openpyxl.load_workbook(filename='padraos/AGUA.xlsx')
    tabela_excel = workbook['P']

    dados[0] = tabela_excel['C11'].value


    num = int(dados[0])
    print(f'num = {num}')

    on_change(-1, setor_optionemenu)
    on_change(0, input_quant1)
    on_change(1, input_quant2)
    on_change(2, input_quant3)

    setor = dados[1]
    quant1 = dados[2]
    quant2 = dados[3]
    quant3 = dados[4]

    print(f'q1 {quant1}')
    print(f'q2 {quant2}')
    print(f'q3 {quant3}')

    tabela_excel['C11'].value = num + 1
    tabela_excel['G11'].value = setor
    tabela_excel['C19'].value = int(quant1)
    tabela_excel['C20'].value = int(quant2)
    tabela_excel['C21'].value = int(quant3)


    tabela_excel['G13'].value = datetime.datetime.now().strftime('%H:%M')
    tabela_excel['G15'].value = datetime.datetime.now().strftime('%d/%m/%Y')


    nome_do_arquivo = f'00{num+1} ABR - {setor}'
    nome_do_arquivocompleto = f'{nome_do_arquivo}.xlsx'
    diretorio = filedialog.askdirectory()
    print(diretorio)
    if diretorio:
        caminho_completo = os.path.join(diretorio, nome_do_arquivocompleto)
        print(caminho_completo)
        workbook.save(filename=caminho_completo)
        workbook = openpyxl.load_workbook(filename=caminho_completo)
        workbook.save(filename='padraos/AGUA.xlsx')
        os.startfile(caminho_completo)
        dados[5] = nome_do_arquivo
        dados[6] = f'{diretorio}/{nome_do_arquivocompleto}'

def salvar_pdf():
    global dados
    excel = win32.DispatchEx("Excel.Application")
    workbook = excel.Workbooks.Open(dados[6])
    worksheet = workbook.Worksheets[0]

    nome_arquivo_pdf = f'00{dados[0]+1} ABR - {dados[1]}.pdf'
    diretorio = filedialog.askdirectory()
    caminho_completo = os.path.join(diretorio, nome_arquivo_pdf)

    worksheet.ExportAsFixedFormat(0, caminho_completo)
    workbook.Close()
    excel.Quit()
    os.rename(f'{diretorio}/00{dados[0]+1}%20ABR%20-%20{dados[1]}.pdf', f'{diretorio}/00{dados[0]+1} ABR - {dados[1]}.pdf' )

print(id_item)

item_id = 0

class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, **kw):
        customtkinter.CTkButton.__init__(self, master=master, **kw)

    def return_value(self, value):
        self.master.return_value = value


def return_value(self, value):
    self.master.return_value = value


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('theme/light.json')

root = customtkinter.CTk()
root.geometry('450x350+450+150')
root.title("Requisição de Água - Setor de Compras")
root.config(bg='#fafafa')
root.columnconfigure(0, minsize=100)

style = ThemedStyle(root)
style.set_theme("winxpblue")
style.configure('Treeview', font=('Helvetica', 9, 'bold'), padding=(0, 5), rowheight=20, collunsheight=15,
                foreground='#222222', background='#E1E1E1')
style.configure('Treeview.Heading', background='#0b6ba1', padding=(0, 5), foreground='white',
                font=('Helvetica', 10, 'bold'))
style.map("Treeview.Heading", background=[("active", "#0e557d")])
style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

titulo = customtkinter.CTkLabel(root, font=('Helvetica', 16, 'bold'), fg_color="#fafafa", text_color="#0e557d", text="REQUISIÇÃO - ÁGUA")
titulo.grid(column=0, row=0, padx=50, pady=10, sticky="s")

# Criando a tabela
tabela = ttk.Treeview(root, selectmode='browse', show='headings')

# Definindo as colunas da tabela
tabela['columns'] = ('QUANT', 'DESCRICAO')
tabela.configure(height=0)

# Configurando as colunas da tabela
tabela.column('QUANT', width=80, stretch=tk.NO, anchor=tk.CENTER)
tabela.column('DESCRICAO', width=250, stretch=tk.NO, anchor=tk.CENTER)

# Configurando os cabeçalhos das colunas
tabela.heading('QUANT', text='QUANT.')
tabela.heading('DESCRICAO', text='DESCRICAO')

# Exibindo a tabela na tela
tabela.grid(column=0, row=1, padx=50, pady=10, sticky="se")

# Define as tags para as linhas pares e ímpares
tabela.tag_configure('even', background='black')
tabela.tag_configure('odd', background='black')

root.item_id = 0

frame = customtkinter.CTkFrame(root, border_width=0, fg_color='#E1E1E1', border_color='#dddddd', corner_radius=2)
frame.grid(column=0, row=2, padx=50, pady=0, sticky='nw')

input_quant1 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                      width=60, height=10,
                                      border_width=1,
                                      border_color='#b1b1b1',
                                      fg_color='#eeeeee',
                                      text_color='#222222',
                                      corner_radius=0)
input_quant1.insert(0, "0")  # define o valor padrão como "0"

input_quant1.grid(column=0, row=1, padx=10, pady=0, sticky='w')
# input_quant1.bind("<KeyRelease>", on_input_change(0, input_quant1))

input_quant2 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                      width=60, height=15,
                                      border_width=1,
                                      border_color='#b1b1b1',
                                      fg_color='#eeeeee',
                                      text_color='#222222',
                                      corner_radius=0)
input_quant2.insert(0, "0")  # define o valor padrão como "0"

input_quant2.grid(column=0, row=2, padx=10, pady=0, sticky='w')
# input_quant2.bind("<KeyRelease>", on_input_change(1, input_quant2))

input_quant3 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                      width=60, height=15,
                                      border_width=1,
                                      border_color='#b1b1b1',
                                      fg_color='#eeeeee',
                                      text_color='#222222',
                                      corner_radius=0)
input_quant3.insert(0, "0")  # define o valor padrão como "0"

input_quant3.grid(column=0, row=3, padx=10, pady=0, sticky='w')
# input_quant3.bind("<FocusOut>", on_input_change(2, input_quant3))

# Criando a tabela
tabela_itens = ttk.Treeview(root, selectmode='browse', show='')

# Definindo as colunas da tabela
tabela_itens['columns'] = ('DESCRICAO')

# Configurando as colunas da tabela
tabela_itens.column('DESCRICAO', width=250, stretch=tk.NO, anchor=tk.CENTER)

tabela_itens.configure(height=3)

# Configurando os cabeçalhos das colunas
tabela_itens.heading('DESCRICAO', text='DESCRICAO')
# Exibindo a tabela na tela
tabela_itens.grid(column=0, row=2, padx=50, pady=0, sticky='ne')

tabela_itens.insert('', 'end', text='1', values=('ÁGUA MINERAL - 500ML', ''))
tabela_itens.insert('', 'end', text='2', values=('RECARGA DE ÁGUA - 20L', ''))
tabela_itens.insert('', 'end', text='3', values=('VASILHAME DE ÁGUA - 20L', ''))

# Define as tags para as linhas pares e ímpares
tabela_itens.tag_configure('even', background='black')
tabela_itens.tag_configure('odd', background='black')

setor_label = customtkinter.CTkLabel(root, font=('Helvetica', 14, 'bold'), fg_color="#fafafa", text_color="#0e557d", text="SETOR DA REQUISIÇÃO:")
setor_label.grid(row=5, column=0, padx=50, pady=(10, 0), sticky = "nw")

setor_optionemenu = customtkinter.CTkOptionMenu(root, values=["ALMOXARIFADO", "GUARDA", "RAIO", "TRIBUTOS"],
                                                corner_radius=0
                                                )
setor_optionemenu.grid(row=5, column=0, padx=50, pady=(10, 10), sticky = "ne")

icon_docx = customtkinter.CTkImage(light_image=Image.open("img/word_icon.png"),
                                   dark_image=Image.open("img/word_icon.png"),
                                   size=(40, 40))

# Criando a entrada e o botão personalizado
salvar_xls = customtkinter.CTkButton(root, width=150, text="Salvar EXEL", font=('Helvetica', 14, 'bold'),
                                      image=icon_docx, compound="left", corner_radius=0,
                                      command=salvar_xls)
salvar_xls.grid(column=0, row=6, padx=50, pady=20, sticky="w")


salvar_docx = customtkinter.CTkButton(root, width=150, text="Salvar PDF", font=('Helvetica', 14, 'bold'),
                                      image=icon_docx, compound="left", corner_radius=0,
                                      command=salvar_pdf)
salvar_docx.grid(column=0, row=6, padx=50, pady=20, sticky="e")

root.mainloop()
