import customtkinter
import tkinter as tk
from tkinter import ttk
from salvar_oficio import *

cnpj1 = ""
cnpj2 = ""
cnpj3 = ""

global data1
global data2
global data3
global item_id


class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, **kw):
        customtkinter.CTkButton.__init__(self, master=master, **kw)

    def return_value(self, value):
        self.master.return_value = value
        # self.master.destroy()


def return_value(self, value):
    self.master.return_value = value
    # self.master.destroy()

def adicionar_dados():
    # Obtém os valores dos campos do formulário
    cnpj = cnpj_entry.get()
    razao_social = razao_social_entry.get()
    data_coleta = data_coleta_entry.get()

    # Adiciona os dados à tabela
    tabela.insert(parent='', index='end', iid=0, text=str(0),
                           values=(cnpj, razao_social, data_coleta))

    # Limpa os campos do formulário
    cnpj_entry.delete(0, 'end')
    razao_social_entry.delete(0, 'end')
    data_coleta_entry.delete(0, 'end')

    # Incrementa o ID dos itens da tabela
    item_id += 1

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
root.geometry("800x500")
root.title("Input Demo")


# Define o estilo da tabela
style = ttk.Style()
style.configure('Treeview', rowheight=40, bordercolor="white", borderwidth=0, highlightthickness=0, relief="flat")
style.configure('Treeview.Heading', background='#FFA500', foreground='white', font=('Arial', 12, 'bold'))
style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

# Cria a tabela
tabela = ttk.Treeview(root, columns=('CNPJ', 'Razão Social', 'Data da Coleta'))
tabela.heading('#0', text='ID')
tabela.heading('CNPJ', text='CNPJ')
tabela.heading('Razão Social', text='Razão Social')
tabela.heading('Data da Coleta', text='Data da Coleta')
tabela.grid(column=1, row=1, padx=10, pady=10)

# Define a coloração das linhas da tabela
for i, item in enumerate(tabela.get_children()):
    if i % 2 == 0:
        tabela.item(item, tags=('even',))
    else:
        tabela.item(item, tags=('odd',))

tabela.tag_configure('even', background='#ECECEC')
tabela.tag_configure('odd', background='white')

# # Cria a tabela
# tabela = ttk.Treeview(root, columns=('CNPJ', 'Razão Social', 'Data da Coleta'))
# tabela.heading('#0', text='ID')
# tabela.heading('CNPJ', text='CNPJ')
# tabela.heading('Razão Social', text='Razão Social')
# tabela.heading('Data da Coleta', text='Data da Coleta')
# tabela.grid(column=1, row=1, padx=10, pady=10)

# Cria o formulário de entrada de dados
form = tk.Frame(root)
form.grid(column=1, row=2, padx=10, pady=10)

cnpj_label = tk.Label(form, text='CNPJ:')
cnpj_entry = tk.Entry(form)
cnpj_label.grid(row=0, column=0)
cnpj_entry.grid(row=0, column=1)

razao_social_label = tk.Label(form, text='Razão Social:')
razao_social_entry = tk.Entry(form)
razao_social_label.grid(row=1, column=0)
razao_social_entry.grid(row=1, column=1)

data_coleta_label = tk.Label(form, text='Data da Coleta:')
data_coleta_entry = tk.Entry(form)
data_coleta_label.grid(row=2, column=0)
data_coleta_entry.grid(row=2, column=1)

add_button = tk.Button(form, text='Adicionar', command=adicionar_dados)
add_button.grid(row=3, column=1)

# Cria uma variável para gerenciar o ID dos itens da tabela
root.item_id = 0

# Adiciona eventos à tabela

# tabela.bind("<Double-1>", editar_item(tabela, "<Double-1>"))
# tabela.bind("<Delete>", remover_item(tabela, "<Delete>"))



icon_pdf = PhotoImage(file="img/pdf_icon.png").subsample(15)

botao_pdf = customtkinter.CTkButton(root, width=200, text="Abrir Cotação Empresa1", image=icon_pdf, compound="left", )
botao_pdf.grid(column=1, row=3, padx=10, pady=10, sticky=W)
botao_pdf.bind("<Button-1>", input_pdf("botao_pdf"))
# botao_pdf.bind("<FocusOut>", on_input_change("botao_pdf", botao_pdf))

icon_docx = PhotoImage(file="img/word_icon.png").subsample(15)
# Criando a entrada e o botão personalizado
salvar_docx = customtkinter.CTkButton(root, width=200, text="Salvar Word", image=icon_docx, compound="left",
                                      command=salvar_arquivo)
salvar_docx.grid(column=1, row=4, padx=10, pady=10, sticky=W)

root.mainloop()
