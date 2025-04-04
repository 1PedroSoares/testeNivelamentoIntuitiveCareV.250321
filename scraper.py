import requests
from bs4 import BeautifulSoup
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
dados_pagina = BeautifulSoup(response.content, "html.parser")

links = dados_pagina.find_all("a", href=True)

# Crio uma lista para armazenar os links dos PDFs
links_pdf = []
for link in links:
    if "Anexo I" in link.text or "Anexo II" in link.text:
        if link['href'].startswith("http"):
            links_pdf.append(link['href'])
        else:
            links_pdf.append(url + '/' + link['href'])

# Inicio o download dos PDFs encontrados
for pdf_link in links_pdf:
    pdf_response = requests.get(pdf_link)
    file_name = pdf_link.split("/")[-1]
    with open("versao_final/files/"+file_name, "wb") as arquivo_pdf:
        arquivo_pdf.write(pdf_response.content)

# Compacto os PDFs em um único arquivo ZIP
nome_arquivo_zip = "versao_final/files/anexos.zip"
with zipfile.ZipFile(nome_arquivo_zip, "w") as zip_file:
    for pdf_link in links_pdf:
        file_name = pdf_link.split("/")[-1]
        zip_file.write("versao_final/files/"+file_name)

print(f"Anexos compactados em {nome_arquivo_zip}")
