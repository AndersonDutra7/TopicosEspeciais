import requests
from bs4 import BeautifulSoup

# Fazendo a solicitação HTTP para obter o conteúdo da página
url = "https://www.uol.com.br/"
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Passando o conteúdo da página para o BeautifulSoup para análise
    soup = BeautifulSoup(response.content, 'html.parser')

    # Imprimindo o HTML prettified
    # print(soup.prettify())
    with open('tarefa1104.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
else:
    print("Erro ao acessar a página:", response.status_code)
