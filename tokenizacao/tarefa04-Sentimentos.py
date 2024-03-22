import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

#Criar uma instância do analisador de sistemas
analyzer = SentimentIntensityAnalyzer()

#Criar uma sentença
sentence_sad = "Akira Toriyama, criador da franquia 'Dragon Ball', morreu aos 68 anos no dia 1º de março. A informação foi divulgada na madrugada desta sexta-feira (8) por estúdios ligados ao artista."
sentence_sad += "Um comunicado publicado no site de Dragon Ball afirmou que a morte de Toriyama foi provocada por um hematoma subdural, que é quando acontece um acúmulo de sangue entre o cérebro e o crânio."
sentence_sad += "O funeral de Toriyama foi reservado apenas para a família."

#Verificar pontuação da análise de sentimento
sentiment_dict = analyzer.polarity_scores(sentence_sad)

#Saída
print("Pontuação dos Sentimentos")
print(f"Positivo: {sentiment_dict['pos'] * 100}%")
print(f"Neutro: {sentiment_dict['neu'] * 100}%")
print(f"Negativo: {sentiment_dict['neg'] * 100}%")
print(f"Compound: {sentiment_dict['compound']}%")

#Criar uma sentença
sentence_happy = "A habilidda de homem que teve uma parada cardíaca em frente ao restaurante de fast food."
sentence_happy += "Paul Myers, estavranças ficaram confusas e nem percebeu o que aconteceu depois."
sentence_happy += "Depois dos primeiros socorros, os funcionários não hesitaram e chamaram os paramédicos e Myers foi rapidamente transportado para um hospital de York, Inglaterra. A agilidade salvou a vida dele! "

#Verificar pontuação da análise de sentimento
sentiment_dict2 = analyzer.polarity_scores(sentence_happy)

#Saída
print("")
print("Pontuação dos Sentimentos")
print(f"Positivo: {sentiment_dict2['pos'] * 100}%")
print(f"Neutro: {sentiment_dict2['neu'] * 100}%")
print(f"Negativo: {sentiment_dict2['neg'] * 100}%")
print(f"Compound: {sentiment_dict2['compound']}%")
