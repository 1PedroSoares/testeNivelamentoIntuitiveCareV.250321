# README - Teste de Nivelamento Intuitive Care V.250321

## Sobre o Projeto

Este repositório contém a solução para o teste de nivelamento para a vaga de estágio na **Intuitive Care**. O projeto envolve **extração de dados**, **transformação**, **compressão de arquivos** e **operações com banco de dados**.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes itens instalados:

- Python 3.8+
- Bibliotecas Python necessárias (pandas, requests, BeautifulSoup4, pdfplumber, zipfile, SQLAlchemy)
- MySQL 8.0+ ou PostgreSQL 10+

Instale as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
```

---

## 🚀 Execução do Script

### 1. Teste de Web Scraping e Download

Este teste realiza o download dos anexos do site da ANS e compacta os arquivos.

Execute:

```bash
python scraper.py
```

Saída esperada:

- **Anexos I e II baixados e salvos** ``** na pasta files **``
- **Arquivo compactado**`` ** criado na pasta versao_final/files/anexos.zip **``

---

### 2. Teste de Transformação de Dados

O script extrai dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do **Anexo I**, transforma e salva em CSV.

Execute:

```bash
python process_data.py
```

Saída esperada:

- **CSV compactado em**``**versao_final/Teste_Pedro.zip**``
---

### 3. Teste de Banco de Dados

O script cria tabelas, importa os dados baixados e executa queries analíticas.

Passos:

1. Baixe os arquivos dos últimos 2 anos e os dados cadastrais das operadoras;
2. Execute as queries para criar e importar os dados;
3. Execute a análise de despesas;
---

## 📂 Estrutura do Repositório

```
/
├── versao_final/
│   ├── scraper.py   # Baixa e compacta os anexos do site informado em um arquivo.ZIP
│   ├── process_data.py  # Extrai, processa os dados do PDF, estrutura em um arquivo CSV e compacta em um arquivo.ZIP
│   ├── query_analiticas.sql  #  Estrutura as tabelas necessárias para o arquivo CSV e importa o conteúdo dos arquivos preparados.
│   ├── query_analiticas.sql   # Querie analítica
│
├── files/   # Armazena os arquivos gerados
│   ├── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf
│   ├── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.xlsx
│   ├── Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf
│   ├── rol_procedimentos.csv
│   ├── anexos.zip
│   ├── Teste_Pedro.zip
│
├── requirements.txt  # Dependências do projeto
├── README.md  # Este documento
```

---

## 🛠 Tecnologias Utilizadas

- **Python** (requests, BeautifulSoup, pandas, pdfplumber, zipfile, SQLAlchemy)
- **MySQL/PostgreSQL** (para armazenamento e análise de dados)
- **SQL** (queries analíticas)

Caso tenha dúvidas ou precise de suporte, entre em contato!🚀😊

