# Passo 01- File > Settings > Projeto > Python Interpreter > + > nltk

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')

#Texto para exemplo
text = "Olá Mundo! Projeto de Linguagem Natural com Tokenzização..."

#Tokenização para Setenças
# Função sent_tokenize(text) faz a tokenizazação de setences
setences = sent_tokenize(text)


print("Setenças Tokenizadas: ", setences)

#Tokenização de palavras da primeira setença, ele separa de acordo com o . (ponto)
print(setences[0])
print(setences[1])
# print(setences[2])
