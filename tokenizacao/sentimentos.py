import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

#Criar uma instância do analisador de sistemas
analyzer = SentimentIntensityAnalyzer()

#Criar uma sentença
#sentence = "Aos 7 minutos, no contra-ataque, quase o gol das Gurias Gremistas: Dayana Rodríguez abriu para Cássia, no bico da grande área pela direita. Ela ajeitou o corpo e colocou por cobertura, buscando o ângulo direito. A bola explodiu no travessão e saiu. "
#sentence = "Estou triste"
sentence = "Estou feliz"

#Verificar pontuação da análise de sentimento
sentiment_dict = analyzer.polarity_scores(sentence)

#Saída
print("Pontuação dos Sentimentos")
print(f"Positivo: {sentiment_dict['pos'] * 100}%")
print(f"Neutro: {sentiment_dict['neu'] * 100}%")
print(f"Negativo: {sentiment_dict['neg'] * 100}%")
print(f"Compound: {sentiment_dict['compound']}%")
