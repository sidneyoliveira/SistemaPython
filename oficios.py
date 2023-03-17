import tabula
import pandas as pd
from IPython.core.display_functions import display
from pdfminer.high_level import extract_pages, extract_text
import requests



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



pag2= extract_text("mapa.pdf", page_numbers=[1])

# Divide o texto em linhas
linhas = pag2.split("\n")

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
    print(descricao)

except Exception as e:
    print("Erro: " + str(e))


# Define opções de exibição do pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)




# Substitua o valor abaixo pelo seu token de acesso à API
token = 'SEU_TOKEN_DE_ACESSO'

# Substitua o valor abaixo pelo CNPJ que deseja consultar
cnpj = '00000000000191'

# Faz a solicitação HTTP para a API
url = f'https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}'
resposta = requests.get(url)
resposta = resposta.json()
print(resposta)
resposta = pd.DataFrame([resposta])


print(resposta["RAZAO SOCIAL"])




# Extrai o nome da empresa da resposta da API
