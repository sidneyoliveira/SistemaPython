import os
import docx
import requests
from bs4 import BeautifulSoup
from docx import Document
from pdfminer.high_level import extract_pages, extract_text



# Verifica se o arquivo PDF existe
if not os.path.exists("mapa.pdf"):
    print("Arquivo PDF não encontrado.")
    exit()

# Extrai texto do arquivo PDF PAGINA 1
pag1 = extract_text("mapa.pdf", page_numbers=[0])

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


# Substitua o valor abaixo pelo CNPJ que deseja consultar
cnpj_input = input('Qual CNPJ?')

# Faz a solicitação HTTP para a API
url = f'https://cnpj.biz/{cnpj_input}'

response = requests.get(url)
content = response.content

dados_cnpj = BeautifulSoup(content, 'html.parser')
dados_cnpj = dados_cnpj.findAll('b', attrs={'class': 'copy'})

cnpj = dados_cnpj[0].text
razao = dados_cnpj[2].text
print(cnpj)
print(razao)


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
    "CNPJ1": f'{cnpj[0]}',
    "CNPJ2": f'{cnpj[1]}',
    "CNPJ3": f'{cnpj[2]}',
    "RAZAO1": f'{razao[0]}',
    "RAZAO2": f'{razao[1]}',
    "RAZAO3": f'{razao[2]}',
    "DATA1": f'{data}',
    "DATA2": f'{data}',
    "DATA3": f'{data}',

}
for i in range(len(table.rows)):
    for j in range(len(table.columns)):
        cell = table.cell(i, j)
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                for codigo in referencias:
                    valor = referencias[codigo]
                    new_text = run.text.replace(codigo, valor)
                    run.text = new_text

for para in doc.paragraphs:
    for run in para.runs:
        run.font.name = 'Calibri Light'


doc.save('OFICIO ' + f'{numoficio}' + ' - ' + f'{titulo}' + '.docx')





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
