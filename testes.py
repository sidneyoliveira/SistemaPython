import requests
from bs4 import BeautifulSoup
import openpyxl

cidades = ["Abaiara", "Acarape", "Acarau"]

resultados = []

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Prefeitos do Ceará"
ws.append(["Cidade", "Prefeito"])
for i in range(len(cidades)):

    url = f"https://aprece.org.br/municipio/{cidades[i]}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find("div", class_="inf")
    if result:
        resultados.append(result)
        print(result)
        prefeito = str(resultados[i]).split("                    ")
        prefeito = str(prefeito[1])
        prefeito = prefeito.replace("    ", "")
        print(prefeito)
        nome = prefeito.split(" ")
        print(nome)
        nome_sobre = nome[0]+nome[1]
        ws.append([cidades[i],prefeito])
    else:
        print(f"Nenhum resultado encontrado para {cidades[i]}")

wb.save("prefeitos_do_ceara.xlsx")

