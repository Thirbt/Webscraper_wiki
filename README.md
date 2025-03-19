# Web Scraping com SQLite

Este projeto realiza Web Scraping em páginas da Wikipédia e armazena os dados coletados em um banco de dados SQLite. 
A aplicação coleta informações como título da página, conteúdo principal, URL, data da postagem e data da coleta.

## 📌 Funcionalidades

- **Coleta de dados** de páginas da Wikipédia.
- **Armazena os dados** coletados em um banco SQLite.
- **Busca** por palavra-chave no título dos posts.
- **Filtra** posts pela data de coleta.
- **Lista** todos os posts coletados.

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- SQLite3
- Requests
- BeautifulSoup4

## 📂 Estrutura do Projeto

```
📁 web_scraper_project/
│-- 📄 main.py            # Script principal para rodar a coleta de dados
│-- 📄 scrape.py          # Módulo responsável pelo Web Scraping
│-- 📄 database.py        # Módulo de conexão e manipulação do banco de dados
│-- 📄 requirements.txt   # Dependências do projeto
│-- 📄 README.md          # Documentação do projeto
```

## 🚀 Como Executar

### 1️⃣ Clonar o repositório

```sh
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)

```sh
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate   # Para Windows
```

### 3️⃣ Instalar as dependências

```sh
pip install -r requirements.txt
```

### 4️⃣ Executar o script

```sh
python main.py
```

## 🔍 Consultas ao Banco de Dados

Você pode buscar dados no banco utilizando os seguintes métodos:

- **Buscar todos os posts coletados**

```python
from database import get_all_posts
print(get_all_posts())
```

- **Buscar posts por palavra-chave**

```python
from database import search_posts_by_keyword
print(search_posts_by_keyword("PlayStation"))
```

- **Buscar posts por data de coleta**

```python
from database import get_posts_by_collection_date
print(get_posts_by_collection_date("2025-03-18"))
```

## 📜 Explicação dos Arquivos

### 1️⃣ ```database.py``` (Gerenciamento do Banco de Dados)

Este arquivo contém funções para criar o banco de dados, salvar e realizar consultas:

- ```create_database()```: Cria o banco de dados ```scrapeDB.db``` e a tabela ```posts```.
- ```save_to_database(post_data)```: Salva um post coletado no banco de dados.
- ```get_all_posts()```: Retorna posts que contêm a palavra-chave no título.
- ```get_posts_by_collection_date(date)```: Retorna posts coletados em uma data específica.

### 2️⃣ ```scrape.py``` (Coletando Dados da Wikipedia)

A função ```metodoScrape(url) coleta os seguintes dados da página:

- Título: Obtido da tag ```<span class='mw-page-title-main'>```
- Data da postagem: Extraído do rodapé da Wikipedia (```footer-info-lastmod```)
- Conteúdo: Extraído dos parágrafos dentro do ```bodyContent```
- Data de Coleta: Data e hora da execução do script

### 3️⃣ ```main.py``` (Execução do Programa)

- Cria o banco de dados
- Percorre uma lista de URLs da Wikipedia
- Executa o scraping e salva os dados no banco
- Exibe os posts coletados e permite consultas por palavra-chave e data


## 📜 Exemplo de Saída

Ao rodar ```main.py```, a saída será semelhante a:

```sh
Coletando dados da URL: https://en.wikipedia.org/wiki/PlayStation_5
Coletando dados da URL: https://en.wikipedia.org/wiki/Brazil
Coletando dados da URL: https://en.wikipedia.org/wiki/Nintendo
Coletando dados da URL: https://en.wikipedia.org/wiki/FIFA

Todos os posts coletados:
(1, 'PlayStation 5', 'https://en.wikipedia.org/wiki/PlayStation_5', 'November 12, 2020', '2025-03-18 14:30:00')
(2, 'Brazil', 'https://en.wikipedia.org/wiki/Brazil', 'August 6, 2022', '2025-03-18 14:30:00')
...
```