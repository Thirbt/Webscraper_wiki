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

## 📱 Banco de dados Relacional (SQLite)

Para este projeto, optei por utilizar um banco de dados **relacional (SQL)** em vez de um banco não relacional(NoSQL) ou um simples armazenamento em arquivo por alguns motivos essenciais:

### 1️⃣ Estruturação e Integridade dos Dados

Como os dados coletados possuem um formato bem definido (título, conteúdo, URL, data de postagem e data de coleta), um banco relacional permite organizá-los de maneira estruturada em tabelas, garantindo consistência e integridade.
Em um banco NoSQL (como MongoDB), os dados seriam armazenados como documentos JSON, o que pode gerar inconsistências caso as estruturas variem ao longo do tempo.

### 2️⃣ Facilidade de Consulta e Manipulação 

Bancos relacionais utilizam SQL (Structured Query Language), uma linguagem poderosa para realizar consultas complexas de maneira eficiente.
No projeto, há a necessidade de buscar posts por palavras-chave e filtrar por data de coleta, algo que pode ser feito de forma otimizada com SQL e índices, sem necessidade de processar dados manualmente em código.

### 3️⃣ Relacionamento e Expansibilidade

Embora o projeto atualmente tenha uma única tabela (posts), um banco de dados relacional permite expansibilidade futura, possibilitando a criação de tabelas relacionadas.
Se no futuro for necessário armazenar categorias, autores ou outros metadados dos posts, um modelo relacional facilitará a estruturação e a recuperação dos dados.

### 4️⃣ Garantia de Persistência e Confiabilidade

Diferente de armazenamentos temporários ou em memória, um banco de dados relacional oferece persistência dos dados de maneira confiável. Isso evita perda de informações em caso de falhas no sistema.

