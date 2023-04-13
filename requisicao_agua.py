import tkinter as tk
from ttkthemes import ThemedStyle
import os
import docx
from docx import Document
from pdfminer.high_level import extract_text
from tkinter import filedialog, ttk
import customtkinter

global pdf_filename
import ctypes
from tkinter import *
from PIL import Image, ImageTk

id_item = 0
NUM = ''
QUANT = [0, 0, 0]


def on_input_change(var_name, input_obj):
    def on_change(event):
        globals()[var_name] = input_obj.get()
        print(globals()[var_name])

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
root.columnconfigure(0, minsize=200)

style = ThemedStyle(root)
style.set_theme("winxpblue")
style.configure('Treeview', font=('Helvetica', 9, 'bold'), padding=(0, 5), rowheight=1, collunsheight=15,
                foreground='#555555', background='#E1E1E1')
style.configure('Treeview.Heading', background='#0b6ba1', padding=(0, 5), foreground='white',
                font=('Helvetica', 10, 'bold'))
style.map("Treeview.Heading", background=[("active", "#0e557d")])
style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])



# Criando a tabela
tabela = ttk.Treeview(root, selectmode='browse', show='headings')

# Definindo as colunas da tabela
tabela['columns'] = ('DESCRICAO', 'V_UNID', 'V_TOTAL')

# Configurando as colunas da tabela
tabela.column('DESCRICAO', width=300, stretch=tk.NO, anchor=tk.CENTER)
tabela.column('V_UNID', width=80, anchor=tk.CENTER)
tabela.column('V_TOTAL', width=80, stretch=tk.YES, anchor=tk.CENTER)

# Configurando os cabeçalhos das colunas
tabela.heading('DESCRICAO', text='DESCRICAO')
tabela.heading('V_UNID', text='V. UNID')
tabela.heading('V_TOTAL', text='V. TOTAL')
# Exibindo a tabela na tela
tabela.grid(column=1, row=0, padx=0, pady=2)

# Define as tags para as linhas pares e ímpares
tabela.tag_configure('even', background='black')
tabela.tag_configure('odd', background='black')

root.item_id = 0

# tabela.bind("<Double-1>", editar_item(tabela, "<Double-1>"))
# tabela.bind("<Delete>", remover_item(tabela, "<Delete>"))

header_label = customtkinter.CTkLabel(root, text="Tabela de Quantidades", font_size=16, font_weight="bold")
header_label.grid(column=0, row=0, padx=10, pady=10, sticky="n")

frame = customtkinter.CTkFrame(root, border_width=0, border_color='#dddddd', corner_radius=2)
frame.grid(column=0, row=1, padx=0, pady=10)

input_quant1 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                      width=60, height=15,
                                      border_width=2,
                                      border_color='#b1b1b1',
                                      fg_color='#eeeeee',
                                      text_color='#333333',
                                      corner_radius=3 )

input_quant1.grid(column=0, row=1, padx=10, pady=2, sticky='w')
input_quant1.bind("<FocusOut>", on_input_change("QUANT[0]", input_quant1))

input_quant2 = customtkinter.CTkEntry(frame, placeholder_text="0",
                                  width=60, height=15,
                                  border_width=2,
                                  border_color='#b1b1b1',
                                  fg_color='#eeeeee',
                                  text_color='#333333',
                                  corner_radius=3 )

input_quant2.grid(column=0, row=2, padx=10, pady=2, sticky='w')
input_quant2.bind("<FocusOut>", on_input_change("QUANT[1]", input_quant2))

input_quant3= customtkinter.CTkEntry(frame, placeholder_text="0",
                                  width=60, height=15,
                                  border_width=2,
                                  border_color='#b1b1b1',
                                  fg_color='#eeeeee',
                                  text_color='#333333',
                                  corner_radius=3 )
input_quant3.grid(column=0, row=3, padx=10, pady=2, sticky='w')
input_quant1.bind("<FocusOut>", on_input_change("QUANT[3]", input_quant3))

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
