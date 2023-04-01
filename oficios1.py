import customtkinter
import tkinter as tk
from tkinter import ttk
from salvar_oficio1 import *
import tkinter as tk
from ttkthemes import ThemedStyle
from tkcalendar import DateEntry

cnpj1 = ""
cnpj2 = ""'1'
cnpj3 = ""

global data1
global data2
global data3

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


def editar_item(event):
    # Obtém o item selecionado na tabela
    item = tabela.selection()[0]

    # Obtém os valores do item selecionado
    cnpj = tabela.item(item, 'values')[0]
    razao_social = tabela.item(item, 'values')[1]
    data_coleta = tabela.item(item, 'values')[2]
    # Preenche os campos do formulário com os valores do item selecionado
    cnpj_entry.delete(0, 'end')
    cnpj_entry.insert(0, cnpj)

    razao_social_entry.delete(0, 'end')
    razao_social_entry.insert(0, razao_social)

    data_coleta_entry.delete(0, 'end')
    data_coleta_entry.insert(0, data_coleta)

def remover_item(event):
    # Obtém o item selecionado na tabela
    item = tabela.selection()[0]

    # Remove o item selecionado da tabela
    tabela.delete(item)


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('theme/light.json')

root = customtkinter.CTk()
root.geometry("800x600")
root.title("Input Demo")
root.config(bg='#f1f1f1')


# Define o estilo da tabela
style = ttk.Style()

style.configure('Treeview', font=('Helvetica', 10, 'bold'), rowheight=15, collunsheight=15, bordercolor='black', borderwidth=1, highlightthickness=0, relief="",  background='#E1E1E1')
style.configure('Treeview.Heading', background='white', foreground='#0b6ba1', font=('Helvetica', 10, 'bold'))
style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

# Cria a tabela
tabela = ttk.Treeview(root, columns=('CNPJ', 'Razão Social', 'Data'))

tabela.column('#0', width=50, stretch=tk.NO)
tabela.column('CNPJ', width=100, anchor=tk.CENTER)
tabela.column('Razão Social', width=300, anchor=tk.CENTER)
tabela.column('Data', width=100, stretch=tk.YES)

tabela.heading('#0', text='ID')
tabela.heading('CNPJ', text='CNPJ')
tabela.heading('Razão Social', text='Razão Social')
tabela.heading('Data', text='Data')
tabela.grid(column=1, row=1, padx=10, pady=10)


tabela.tag_configure('even', background='#ECECEC')
tabela.tag_configure('odd', background='white')


# # Cria o formulário de entrada de dados
# form = tk.Frame(root)
# form.grid(column=1, row=2, padx=10, pady=10)
#
# cnpj_label = tk.Label(form, text='CNPJ:')
# cnpj_entry = tk.Entry(form)
# cnpj_label.grid(row=0, column=0)
# cnpj_entry.grid(row=0, column=1)
#
# razao_social_label = tk.Label(form, text='Razão Social:')
# razao_social_entry = tk.Entry(form)
# razao_social_label.grid(row=1, column=0)
# razao_social_entry.grid(row=1, column=1)
#
# data_coleta_entry = customtkinter.CTkButton(form)
# data_coleta_entry.grid(row=2, column=1)
#
# # add_button = tk.Button(form, text='Adicionar', command=adicionar_dados)
# # add_button.grid(row=3, column=1)

# Cria uma variável para gerenciar o ID dos itens da tabela
root.item_id = 0

# Adiciona eventos à tabela

# tabela.bind("<Double-1>", editar_item(tabela, "<Double-1>"))
# tabela.bind("<Delete>", remover_item(tabela, "<Delete>"))



icon_pdf = PhotoImage(file="img/pdf_icon.png").subsample(15)

botao_pdf = customtkinter.CTkButton(root, width=200, text="Adiconar Cotação",font=('Helvetica', 14, 'bold'), image=icon_pdf, compound="left", )
botao_pdf.grid(column=1, row=3, padx=10, pady=10, sticky=W)
dados1 = botao_pdf.bind("<Button-1>", input_pdf("botao_pdf"))

def adicionar_item(tabela):
    # Adiciona os valores como uma nova linha na tabela
    tabela.insert('', 'end', values=(cnpj, razao, data))

# botao_pdf.bind("<FocusOut>", on_input_change("botao_pdf", botao_pdf))

icon_docx = PhotoImage(file="img/word_icon.png").subsample(15)
# Criando a entrada e o botão personalizado
salvar_docx = customtkinter.CTkButton(root, width=200, text="Salvar Word", font=('Helvetica', 14, 'bold'), image=icon_docx, compound="left",
                                            command=salvar_word)
salvar_docx.grid(column=1, row=4, padx=10, pady=10, sticky=W)

root.mainloop()
