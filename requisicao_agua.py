import tkinter as tk
from ttkthemes import ThemedStyle
import os
from tkinter import filedialog, ttk
import customtkinter

global pdf_filename
import ctypes
from tkinter import *
from PIL import Image, ImageTk

id_item = 0
NUM = ''
QUANT = [0, 0, 0]
VALOR = [0, 0, 0]

def on_input_change(var_name, input_obj):
    def on_change(event):
        QUANT[var_name] = input_obj.get()
        print(QUANT[var_name])
        if var_name == 0:
            VALOR[var_name] = int(QUANT[var_name])*1.5
            print(VALOR[var_name])
        if var_name == 1:
            VALOR[var_name] = int(QUANT[var_name])*2
            print(VALOR[var_name])
        if var_name == 2:
            VALOR[var_name] = int(QUANT[var_name]) * 3
            print(VALOR[var_name])



    return on_change


def exibir_alerta(titulo, mensagem, tipo_icone):
    ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, tipo_icone)


def salvar_xls():
    nome_do_arquivo = f'{numoficio} - {titulo}.docx'
    diretorio = filedialog.askdirectory()
    print(diretorio)
    if diretorio:
        caminho_completo = os.path.join(diretorio, nome_do_arquivo)
        print(caminho_completo)
        doc.save(caminho_completo)
        os.startfile(caminho_completo)


print(id_item)


def adicionar_item(tabela):
    def entry():
        global pdf_filename
        pdf_filename = filedialog.askopenfilename(title="Selecione o arquivo MAPA PDF",
                                                  filetypes=(("pdf files", "*.pdf"),))
        salvar_arquivo(pdf_filename)
        print("return")
        return

    entry()
    print(entry)
    print("print do adicionar itens11 ")

    global id_item
    print("print do adicionar itens ", cnpj_list[id_item - 1], razao_list[id_item - 1], data_list[id_item - 1])
    # # Adiciona os valores como uma nova linha na tabela

    tabela.insert('', 'end', iid=id_item, text=str(id_item),
                  values=(cnpj_list[id_item - 1], razao_list[id_item - 1], data_list[id_item - 1]))


item_id = 0


class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, **kw):
        customtkinter.CTkButton.__init__(self, master=master, **kw)

    def return_value(self, value):
        self.master.return_value = value
        # self.master.destroy()


def return_value(self, value):
    self.master.return_value = value
    # self.master.destroy()


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('theme/light.json')

root = customtkinter.CTk()
root.geometry("600x300")
root.title("Input Demo")
root.config(bg='#f1f1f1')
root.columnconfigure(0, minsize=100)

style = ThemedStyle(root)
style.set_theme("winxpblue")
style.configure('Treeview', font=('Helvetica', 9, 'bold'), padding=(0, 5), rowheight=20, collunsheight=15,
                foreground='#555555', background='#E1E1E1')
style.configure('Treeview.Heading', background='#0b6ba1', padding=(0, 5), foreground='white',
                font=('Helvetica', 10, 'bold'))
style.map("Treeview.Heading", background=[("active", "#0e557d")])
style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

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
tabela.grid(column=0, row=0, padx=10, pady=10, sticky="s")

# Define as tags para as linhas pares e ímpares
tabela.tag_configure('even', background='black')
tabela.tag_configure('odd', background='black')

root.item_id = 0

# tabela.bind("<Double-1>", editar_item(tabela, "<Double-1>"))
# tabela.bind("<Delete>", remover_item(tabela, "<Delete>"))


frame = customtkinter.CTkFrame(root, border_width=0, fg_color='#E1E1E1', border_color='#dddddd', corner_radius=2)
frame.grid(column=0, row=1, padx=10, pady=0, sticky='nw')

input_quant1 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                      width=60, height=10,
                                      border_width=1,
                                      border_color='#b1b1b1',
                                      fg_color='#eeeeee',
                                      text_color='#333333',
                                      corner_radius=0)
input_quant1.insert(0, "0") # define o valor padrão como "0"

input_quant1.grid(column=0, row=1, padx=10, pady=0, sticky='w')
input_quant1.bind("<FocusOut>", on_input_change(0, input_quant1))

input_quant2 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                      width=60, height=15,
                                      border_width=1,
                                      border_color='#b1b1b1',
                                      fg_color='#eeeeee',
                                      text_color='#333333',
                                      corner_radius=0)
input_quant2.insert(0, "0") # define o valor padrão como "0"

input_quant2.grid(column=0, row=2, padx=10, pady=0, sticky='w')
input_quant2.bind("<FocusOut>", on_input_change(1, input_quant2))

input_quant3 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                      width=60, height=15,
                                      border_width=1,
                                      border_color='#b1b1b1',
                                      fg_color='#eeeeee',
                                      text_color='#333333',
                                      corner_radius=0)
input_quant3.insert(0, "0") # define o valor padrão como "0"

input_quant3.grid(column=0, row=3, padx=10, pady=0, sticky='w')
input_quant3.bind("<FocusOut>", on_input_change(2, input_quant3))

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
tabela_itens.grid(column=0, row=1, padx=10, pady=0, sticky='ne')

tabela_itens.insert('', 'end', text='1', values=('ÁGUA MINERAL - 500ML',''))
tabela_itens.insert('', 'end', text='2', values=('RECARGA DE ÁGUA - 20L', ''))
tabela_itens.insert('', 'end', text='3', values=('VASILHAME DE ÁGUA - 20L', ''))

# Define as tags para as linhas pares e ímpares
tabela_itens.tag_configure('even', background='black')
tabela_itens.tag_configure('odd', background='black')

icon_pdf = PhotoImage(file="img/pdf_icon.png").subsample(15)

botao_pdf = customtkinter.CTkButton(root, width=200, text="Adiconar Cotação", font=('Helvetica', 14, 'bold'),
                                    image=icon_pdf, compound="left", )
botao_pdf.grid(column=1, row=4, padx=10, pady=10, sticky=W)
botao_pdf.bind("<Button-1>", lambda event: adicionar_item(tabela))

icon_docx = customtkinter.CTkImage(light_image=Image.open("img/word_icon.png"),
                                   dark_image=Image.open("img/word_icon.png"),
                                   size=(40, 40))

# Criando a entrada e o botão personalizado
salvar_docx = customtkinter.CTkButton(root, width=200, text="Salvar Word", font=('Helvetica', 14, 'bold'),
                                      image=icon_docx, compound="left",
                                      command=salvar_xls)
salvar_docx.grid(column=1, row=4, padx=10, pady=10, sticky=E)

root.mainloop()
