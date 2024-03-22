import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

text = "Este é um exemplo de texto que vamos remover palavras"
words = word_tokenize(text)

#Obter a lista de palavras stopwords na Lingua Portuguesa
#Ex: english, spanish ...
stop_words = set(stopwords.words("portuguese"))

#Filtrando as palavras
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Texto Original:", words)
print("Texto Filtrado:", filtered_words)
