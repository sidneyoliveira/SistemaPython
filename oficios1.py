from salvar_oficio1 import *
import tkinter as tk
from ttkthemes import ThemedStyle
import customtkinter
from PIL import Image, ImageTk


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


def remover_item(event):
    # Obtém o item selecionado na tabela
    item = tabela.selection()[0]

    # Remove o item selecionado da tabela
    tabela.delete(item)


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('theme/light.json')

root = customtkinter.CTk()
root.geometry("630x320+350+150")
root.title("Expedir Oficios")
root.config(bg='#fafafa')



style = ThemedStyle(root)
style.set_theme("winxpblue")
style.configure('Treeview', font=('Helvetica', 9, 'bold'),padding=(0, 5), rowheight=15, collunsheight=15, foreground='#555555', background='#E1E1E1')
style.configure('Treeview.Heading', background='#0b6ba1', padding=(0, 5), foreground='white', font=('Helvetica', 10, 'bold'))
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
tabela.grid(column=0, row=1, padx=(30,0), pady=(20, 0))


# Define as tags para as linhas pares e ímpares
tabela.tag_configure('even', background='black')
tabela.tag_configure('odd', background='black')


setor_label = customtkinter.CTkLabel(root, font=('Helvetica', 14, 'bold'),
                                     fg_color="#fafafa",
                                     text_color="#0e557d",
                                     text="DATA DE FECHAMENTO:")
setor_label.grid( column=0, row=2, padx=(320,0), pady=5, sticky = "w")


input_data = customtkinter.CTkEntry(root, placeholder_text="",
                              width=100, height=20,
                              border_width=2,
                              border_color='#dddddd',
                              corner_radius=2,
                              )

input_data.grid(column=0, row=2, padx=0, pady=0,sticky = "e" )
input_data.bind("<KeyRelease>", on_input_change('input_data', input_data))

root.item_id = 0

# tabela.bind("<Double-1>", editar_item(tabela, "<Double-1>"))
# tabela.bind("<Delete>", remover_item(tabela, "<Delete>"))



icon_docx = customtkinter.CTkImage(light_image=Image.open("img/word_icon.png"),
                                 dark_image=Image.open("img/word_icon.png"),
                                 size=(40, 40))


botao_pdf = customtkinter.CTkButton(root, width=200,corner_radius=3, text="Adiconar Cotação",font=('Helvetica', 14, 'bold'), image=icon_docx, compound="left", )
botao_pdf.grid(column=0, row=3, padx=30, pady=10, sticky="W")
botao_pdf.bind("<Button-1>", lambda event: adicionar_item(tabela))


# Criando a entrada e o botão personalizado
salvar_docx = customtkinter.CTkButton(root, width=200, text="Salvar Word", font=('Helvetica', 14, 'bold'), image=icon_docx, compound="left",
                                            corner_radius=3, command=salvar_word)
salvar_docx.grid(column=0, row=3, padx=0, pady=10, sticky="E")



root.mainloop()

