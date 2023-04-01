import customtkinter
from tkinter import ttk

from salvar_oficio1 import *
import tkinter as tk
from ttkthemes import themed_style
from tkcalendar import DateEntry
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle


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
root.geometry("600x300")
root.title("Input Demo")
root.config(bg='#f1f1f1')



style = ThemedStyle(root)
style.set_theme("winxpblue")
style.configure('Treeview', font=('Helvetica', 9, 'bold'),padding=(0, 5), rowheight=15, collunsheight=15, foreground='#555555', background='#E1E1E1')
style.configure('Treeview.Heading', background='#0b6ba1', padding=(0, 5), foreground='white', focus = "red", font=('Helvetica', 10, 'bold'))
style.map("Treeview.Heading", background=[("active", "#0e557d")])
style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])



tabela = ttk.Treeview(root, columns=('CNPJ', 'Razão Social', 'Data'))

tabela.column('#0', width=50, stretch=tk.NO)
tabela.column('CNPJ', width=140, anchor=tk.CENTER)
tabela.column('Razão Social', width=300, anchor=tk.CENTER)
tabela.column('Data', width=80, stretch=tk.YES)

tabela.heading('#0', text='ID')
tabela.heading('CNPJ', text='CNPJ')
tabela.heading('Razão Social', text='Razão Social')
tabela.heading('Data', text='Data')
tabela.grid(column=1, row=1, padx=10, pady=10)


# Define as tags para as linhas pares e ímpares
tabela.tag_configure('even', background='black')
tabela.tag_configure('odd', background='black')




root.item_id = 0

# tabela.bind("<Double-1>", editar_item(tabela, "<Double-1>"))
# tabela.bind("<Delete>", remover_item(tabela, "<Delete>"))



icon_pdf = PhotoImage(file="img/pdf_icon.png").subsample(15)

botao_pdf = customtkinter.CTkButton(root, width=200, text="Adiconar Cotação",font=('Helvetica', 14, 'bold'), image=icon_pdf, compound="left", )
botao_pdf.grid(column=1, row=3, padx=10, pady=10, sticky=W)
botao_pdf.bind("<Button-1>", lambda event: adicionar_item(tabela))


icon_docx = PhotoImage(file="img/word_icon.png").subsample(15)
# Criando a entrada e o botão personalizado
salvar_docx = customtkinter.CTkButton(root, width=200, text="Salvar Word", font=('Helvetica', 14, 'bold'), image=icon_docx, compound="left",
                                            command=salvar_word)
salvar_docx.grid(column=1, row=3, padx=10, pady=10, sticky=E)

root.mainloop()
