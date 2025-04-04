import pdfplumber
import pandas as pd
import zipfile

anexo_i = "versao_final\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Crio uma lista para armazenar os dados extraídos
dados_tabela = []

# Abro o PDF e extrair dados
with pdfplumber.open(anexo_i) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                dados_tabela.append(linha)

# Convero os dados em DataFrame e crio o DataFrame
# Uso a primeira linha como cabeçalho
df = pd.DataFrame(dados_tabela[1:], columns=dados_tabela[0])

# Substituo as abreviações
df.columns = (
    df.columns
    .str.replace('OD', 'Odontológica')
    .str.replace('AMB', 'Ambulatorial')
    .str.replace('HCO', 'Hospitalar Com Obstetrícia')
    .str.replace('HSO', 'Hospitalar Sem Obstetrícia')
)

# Salvando em CSV
nome_arquivo_csv = "versao_final/files/rol_procedimentos.csv"
df.to_csv(nome_arquivo_csv, index=False)

# Compactando o CSV em um arquivo ZIP
nome_zip_csv = "versao_final/files/Teste_Pedro.zip"
with zipfile.ZipFile(nome_zip_csv, "w") as arquivo_zip:
    arquivo_zip.write(nome_arquivo_csv)

print(f"CSV compactado em {nome_zip_csv}")
