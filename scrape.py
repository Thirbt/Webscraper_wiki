import requests
from bs4 import BeautifulSoup
from datetime import datetime

def metodoScrape(url):
    
    response = requests.get(url) # utilizando a lib request para puxar requisitar a URL
    soup = BeautifulSoup(response.text, 'html.parser') # utilizando o BeautifulSoup para fazer o parse do HTML

    title = soup.find('span', {'class': 'mw-page-title-main'}).get_text() # buscando a informação do título da wikipedia localizada na tag SPAN com a classe

    post_date_tag = soup.find('li', {'id': 'footer-info-lastmod'}) # buscando a data de postagem do conteúdo na wikipedia
    post_date = post_date_tag.get_text().split(" on ")[1].split(" at ")[0]  

    content_div = soup.find('div', {'id': 'bodyContent'})  # buscando o conteúdo principal da página através do ID bodyContent
    paragraphs = content_div.find_all('p')  # coletando todos os parágrafos <p> do conteúdo principal

    content = ' '.join([p.get_text() for p in paragraphs if p.get_text().strip() != '']) # concatenando o conteúdo dos parágrafos

    scrape_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # definindo o horário do scrape para a data da coleta (horário do sistema)

    post_data = { # criando um dicionário com os dados coletados para retornar no método
        'title': title,
        'content': content,
        'url': url,
        'post_date': post_date,
        'scrape_date': scrape_date
    }

    return post_data
