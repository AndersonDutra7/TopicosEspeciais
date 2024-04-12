import requests
from bs4 import BeautifulSoup

# Fazendo a solicitação HTTP para obter o conteúdo da página
url = "http://www.terra.com.br"
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Passando o conteúdo da página para o BeautifulSoup para análise
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando todos os elementos <a> e extraindo o atributo href
    links = soup.find_all('a')

    # Exibindo os links
    for link in links:
        href = link.get('href')
        if href:
            print(href)
else:
    print("Erro ao acessar a página:", response.status_code)
