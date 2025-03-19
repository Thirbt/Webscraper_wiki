import sqlite3

def create_database(): # criando método para criar o banco de dados
    connect = sqlite3.connect('scrapeDB.db') # nomeando o banco de dados como scrapeDB.db
    cursor = connect.cursor() # criando um cursor para executar os scripts do banco

    # Criando a tabela posts no banco de dados
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            url TEXT,
            post_date TEXT,
            scrape_date TEXT
        );
    ''')

    connect.commit() # commitando as alterações no banco
    connect.close() # fechando a conexão
    print("Banco de dados criado com sucesso")


def save_to_database(post_data): # criando método para salvar os dados no banco
    connect = sqlite3.connect('scrapeDB.db')
    cursor = connect.cursor()

    # Inserindo os dados do post na tabela
    cursor.execute('''
        INSERT INTO posts (title, content, url, post_date, scrape_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (post_data['title'], post_data['content'], post_data['url'], post_data['post_date'], post_data['scrape_date']))

    connect.commit() # commitando as alterações no banco
    connect.close() # fechando a conexão
    print("Dados salvos com sucesso")
    
def get_all_posts():  # método responsável por recuperar todos os posts no banco de dados
    connect = sqlite3.connect('scrapeDB.db')
    cursor = connect.cursor()
    cursor.execute("SELECT id, title, url, post_date, scrape_date FROM posts") # query para selecionar todos os posts
    posts = cursor.fetchall() 
    connect.close()
    return posts


def search_posts_by_keyword(keyword):  # Busca posts por palavra-chave no título do post
    connect = sqlite3.connect('scrapeDB.db')
    cursor = connect.cursor()
    query = "SELECT id, title, url, post_date, scrape_date FROM posts WHERE title LIKE ?" # query para buscar posts por palavra-chave
    cursor.execute(query, (f"%{keyword}%",)) # filtro para alterar ? por keyword do parâmetro
    results = cursor.fetchall()
    connect.close()
    return results


def get_posts_by_collection_date(date):  # Filtra posts pela data de coleta
    connect = sqlite3.connect('scrapeDB.db')
    cursor = connect.cursor()
    query = "SELECT id, title, url, post_date, scrape_date FROM posts WHERE scrape_date LIKE ?"
    cursor.execute(query, (f"{date}%",))  # Filtra pelo início da string (YYYY-MM-DD)
    results = cursor.fetchall()
    connect.close()
    return results
