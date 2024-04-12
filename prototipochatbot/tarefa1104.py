import requests
from bs4 import BeautifulSoup
 
def extrair_links_e_titulos(url):
    # Fazendo a solicitação HTTP para obter o conteúdo da página
    response = requests.get(url)
 
    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Passando o conteúdo da página para o BeautifulSoup para análise
        soup = BeautifulSoup(response.content, 'html.parser')
 
        # Encontrando todos os elementos <a> que contenham links para notícias
        links = soup.find_all('a', href=True)
 
        # Verificando cada link para ver se contém "Elon Musk" no texto do link ou no título da notícia
        for link in links:
            href = link.get('href')
            if href and 'musk' in href.lower():
                title = link.text.strip()
                print("Título:", title)
                print("Link:", href)
                print()
 
# Varrendo a página inicial do UOL
print("Notícias do UOL sobre Elon Musk:")
extrair_links_e_titulos("https://www.uol.com.br/")
 
# Varrendo a página inicial do Terra
print("Notícias do Terra sobre Elon Musk:")
extrair_links_e_titulos("https://www.terra.com.br/")