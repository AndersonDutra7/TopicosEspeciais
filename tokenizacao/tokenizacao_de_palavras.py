import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')

#Texto para exemplo
text = "Olá Mundo! Projeto de Linguagem Natural com Tokenzização... Vamos tokenizar essa frase por palavras!"

#Tokenização para Palavras
# Função word_tokenize(text) faz a tokenizazação de palavras
words = word_tokenize(text)


print("Palavras Tokenizadas: ", words)
