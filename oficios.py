import os
import docx
import requests
from bs4 import BeautifulSoup
from docx import Document
from pdfminer.high_level import extract_pages, extract_text
from tkinter import filedialog
import sqlite3
import tkinter
import customtkinter
import subprocess
from tkinter import *
from PIL import Image, ImageTk



cnpj1 = ""
cnpj2 = ""
cnpj3 = ""

class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, **kw):
        customtkinter.CTkButton.__init__(self, master=master, **kw)
    def return_value(self, value):
        self.master.return_value = value
        self.master.destroy()




def input_dados():
    root = customtkinter.CTk()
    root.geometry("600x300")
    root.title("Input Demo")

    def on_input_change(var_name, input_obj):
        def on_change(event):
            globals()[var_name] = input_obj.get()

        return on_change

    # Definindo a função que será executada quando o botão for clicado
    def input_pdf():
        try:
            entry = filedialog.askopenfilename(title="Selecione o arquivo MAPA PDF", filetypes=(("pdf files", "*.pdf"),))
            custom_button.return_value(entry)
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except:
            print("Ocorreu um erro inesperado.")
        finally:
            print("Importação do arquivo concluída.")

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
    custom_button = CustomButton(root, text="Abrir Mapa PDF", command=input_pdf)
    custom_button.grid(column=1, row=4, padx=10, pady=10, sticky=W)


    # Iniciando a janela principal e esperando pelo retorno de valor
    root.mainloop()

    return root.return_value



dados = input_dados()
print(dados)

# Extrai texto do arquivo PDF PAGINA 1
pag1 = extract_text(dados, page_numbers=[0])

# Divide o texto em linhas
linhas = pag1.split("\n")

# Imprime todas as linhas
print(linhas)

# Imprime a linha de índice 7
print(linhas[7] + "\n\n")

try:
    # Extrai o número do processo da linha de índice 5
    num = linhas[5].split(" ")[1]
    print(num)

    # Extrai a data do processo da linha de índice 5
    data = linhas[5].split(" ")[4]
    dia = data.split('/')[0]
    mes = data.split('/')[1]
    ano = data.split('/')[2]
    print(data)

    # Extrai o título do processo da linha de índice 7
    titulo = linhas[7].split(" ")
    titulo.remove('DESCRIÇÃO:')
    titulo = " ".join(titulo)
    titulo = titulo.replace('  ', ' ')
    print(titulo)

    # Extrai a descrição do processo da linha de índice 9
    descricao = linhas[9].split(" ")
    descricao.remove('ESPECIFICAÇÃO:')
    descricao = " ".join(descricao)
    descricao = descricao.replace('  ', ' ')
    print(descricao + "\n")

except Exception as e:
    print("Erro: " + str(e))

#Função para extrair dados do cnpj
def dados_cnpj(a):
    url = f'https://cnpj.biz/{a}'
    response = requests.get(url)
    content = response.content
    dados_cnpj = BeautifulSoup(content, 'html.parser')
    print(dados_cnpj)

    dados_cnpj = dados_cnpj.findAll('b', attrs={'class': 'copy'})
    print(url)
    print(dados_cnpj)
    cnpj = dados_cnpj[0].text
    razao = dados_cnpj[2].text
    return cnpj, razao

empresa1 = dados_cnpj(cnpj1)
cnpj1_input = empresa1[0]
razao1 = empresa1[1]

empresa2 = dados_cnpj(cnpj2)
cnpj2_input = empresa2[0]
razao2 = empresa2[1]

empresa3 = dados_cnpj(cnpj3)
cnpj3_input = empresa3[0]
razao3 = empresa3[1]


numoficio = f'{dia}' + f'{mes}' + '-0001.' + f'{ano}'


doc = Document('oficio1.docx')

p = doc.add_paragraph('Oficio nº ')
p.add_run(numoficio).bold = True
p.add_run(' - LICITAÇÃO \t\t\t\t\t')

p.add_run('ITAREMA-CE, ')
p.add_run(data + '\n\n').bold = True

doc.add_paragraph('INEZ Helena Braga')
doc.add_paragraph('Presidente da Comissão de Licitação\n\n')

p2 = doc.add_paragraph(
    '\t\tConsiderando a realização de pesquisa de preço via e-mail junto ao sistema de cotação pública aCotação processo nº: ')
p2.add_run(num).bold = True
p2.add_run(' para: ')
p2.add_run(descricao).bold = True
p2.add_run(', encaminha-se ao Setor de Licitação as respectivas propostas juntamente com o mapa de preço médio e comprovações junto ao TCE/CE para providências cabíveis quanto ao seguimento do processo licitatório.\t\t\n')

p2.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.JUSTIFY


table = doc.tables[0]

referencias = {
    "CNPJ1": f'{cnpj1_input}',
    "CNPJ2": f'{cnpj2_input}',
    "CNPJ3": f'{cnpj3_input}',
    "RAZAO1": f'{razao1}',
    "RAZAO2": f'{razao2}',
    "RAZAO3": f'{razao3}',
    "DATA1": f'{data1}',
    "DATA2": f'{data2}',
    "DATA3": f'{data3}',

}
for i in range(len(table.rows)):
    for j in range(len(table.columns)):
        cell = table.cell(i, j)
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                for codigo in referencias:
                    valor = referencias[codigo]
                    new_text = run.text.replace(codigo, valor)
                    run.text = new_text.upper()

for para in doc.paragraphs:
    for run in para.runs:
        run.font.name = 'Calibri Light'
print("final")

doc.save(f'{numoficio}' + ' - ' + f'{titulo}' + '.docx')


# records = (
#     ('1', f'{cnpj}', f'{razao}', 'E-MAIL – SISTEMA aCotação', '10/03/2023', '60 DIAS'),
#     ('2', f'{cnpj}', f'{razao}', 'E-MAIL – SISTEMA aCotação', '10/03/2023', '60 DIAS'),
#     ('3', f'{cnpj}', f'{razao}', 'E-MAIL – SISTEMA aCotação', '10/03/2023', '60 DIAS')
# )
#
# table = doc.add_table(rows=1, cols=6)
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = 'ITEM'
# hdr_cells[1].text = 'CNPJ/CPF'
# hdr_cells[2].text = 'EMPRESA'
# hdr_cells[3].text = 'MÉTODO'
# hdr_cells[4].text = 'DATA DA PROPOSTA'
# hdr_cells[5].text = 'VALIDADE'
#
# for item, cnpj, empresa, método, data, validade  in records:
#     row_cells = table.add_row().cells
#     row_cells[0].text = item
#     row_cells[1].text = cnpj
#     row_cells[2].text = empresa
#     row_cells[3].text = método
#     row_cells[4].text = data
#     row_cells[5].text = validade
#
#
# referencias = {
#     "CNPJ1": cnpj,
#     "CNPJ2": cnpj,
#     "CNPJ3": cnpj,
#     "RAZAO1": razao,
#     "RAZAO2": razao,
#     "RAZAO3": razao,
#
# }
#
# for paragrafo in doc.paragraphs:
#     for codigo in referencias:
#         valor = referencias[codigo]
#         paragrafo.text = paragrafo.text.replace(codigo, valor)
