import requests
from bs4 import BeautifulSoup
import re

def copiar_texto_noticia(url):
    response = requests.get(url)
    texto_noticia = ""
    if response.status_code == 200:
        print("Processando URL:", url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        if paragraphs:
            for paragraph in paragraphs:
                texto_noticia += paragraph.get_text() + '\n'
            print("Conteúdo da notícia encontrado:", texto_noticia[:100])
        else:
            print("Não foi possível encontrar o conteúdo da notícia:", url)
    else:
        print("Erro ao acessar a página:", response.status_code, url)
    return texto_noticia

def buscar_links_e_titulos(url):
    links_titulos = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            href = link.get('href')
            if href and 'musk' in href.lower():
                titulo = link.text.strip()
                links_titulos.append((titulo, href))
    return links_titulos

def limpar_titulo(titulo):
    titulo_limpo = re.sub(r'[^\w\s.-]', '', titulo)[:100]
    return titulo_limpo

url_uol = "https://noticias.uol.com.br/"

links_titulos_uol = buscar_links_e_titulos(url_uol)

print("Links e títulos encontrados:")
for titulo, link in links_titulos_uol:
    print("Título:", titulo)
    print("Link:", link)
    print()

textos_noticias = []
for titulo, link in links_titulos_uol:
    print("Copiando texto da notícia:", titulo)
    texto_noticia = copiar_texto_noticia(link)
    textos_noticias.append((titulo, texto_noticia))
    print("Texto copiado!\n")

for titulo, texto_noticia in textos_noticias:
    nome_arquivo = limpar_titulo(titulo) + ".txt"
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto_noticia)
        print(f"Notícia '{titulo}' salva em '{nome_arquivo}'")
