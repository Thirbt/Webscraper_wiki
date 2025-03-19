from database import create_database, save_to_database, get_all_posts, search_posts_by_keyword, get_posts_by_collection_date
from scrape import metodoScrape

def main():
    create_database()  # criando o banco de dados sqlite

    urls = [ # criando um dicionários para armazenar as URLs que serão coletadas
        "https://en.wikipedia.org/wiki/PlayStation_5",
        "https://en.wikipedia.org/wiki/Brazil",
        "https://en.wikipedia.org/wiki/Nintendo",
        "https://en.wikipedia.org/wiki/FIFA"
    ]
    
    for url in urls: # criando um loop para percorrer por todas as URLs
        print(f"Coletando dados da URL: {url}")
        post_data = metodoScrape(url)  # utilizando o método que faz o scrape
        save_to_database(post_data)  # salvando os dados coletados no banco de dados
        
    print("\nTodos os posts coletados:") # realiza a consulta para buscar todos os posts
    for post in get_all_posts():
        print(post)

    print("\nTodos os posts com palavra-chave:") # realiza a consulta para buscar posts que contenham a palavra 'PlayStation'
    for post in search_posts_by_keyword("PlayStation"): 
        print(post)

    print("\nTodos os posts com data específica:") # realiza a consulta para buscar posts coletados na data especificada
    for post in get_posts_by_collection_date("2025-03-18"): 
        print(post)

if __name__ == "__main__":
    main()  # chamando a função main para executar o script
