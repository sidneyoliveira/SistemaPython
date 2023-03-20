import re
import tabula
from tabula.io import read_pdf

lista_tabelas = tabula.read_pdf('index.pdf', pages = 'all')
print(len(lista_tabelas))
import pandas as pd
from IPython.core.display_functions import display
from pdfminer.high_level import extract_pages, extract_text
import requests
from bs4 import BeautifulSoup
from docx import Document
from datetime import datetime


dia = "17"
mes = "03"
ano = "2023"

# Extrai texto do arquivo PDF PAGINA 1

pag1= extract_text("mapa.pdf", page_numbers=[0])

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
    print(descricao+"\n")

except Exception as e:
    print("Erro: " + str(e))


# Substitua o valor abaixo pelo CNPJ que deseja consultar
cnpj = '14818544000170'

# Faz a solicitação HTTP para a API
url = f'https://cnpj.biz/{cnpj}'

response = requests.get(f'https://cnpj.biz/{cnpj}')
content = response.content

dados_cnpj = BeautifulSoup(content, 'html.parser')
dados_cnpj = dados_cnpj.findAll('b', attrs={'class': 'copy'})

cnpj = dados_cnpj[0].text
razao = dados_cnpj[2].text


print(cnpj)
print(razao)

numoficio = f'{dia}' + f'{mes}' + '-01.' + f'{ano}'
data = f'{dia}' + '/' + f'{mes}' + '/' + f'{ano}'



referencias = {
    "NUMOFICIO": numoficio,
    "TITULO": titulo,
    "DIA1": data,
    "NUMPROCESSO": num,
    "DESCRICAO": descricao,
}


doc = Document("oficio.docx")

for paragrafo in doc.paragraphs:
    for codigo in referencias:
        valor = referencias[codigo]
        paragrafo.replace(codigo, valor)


doc.save('OFICIO ' + f'{numoficio}' + ' - ' + f'{titulo}' + '.docx')



# Extrai o nome da empresa da resposta da API
