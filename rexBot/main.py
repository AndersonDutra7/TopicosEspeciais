from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import requests
import re

def get_weather(city):
    api_key = "693cd0a90b4d856b03e5c3c7706d3440"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()

        if response.status_code == 200:
            if "main" in data and "weather" in data:
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                return f"A temperatura em {city} é {temperature}°C com umidade {humidity}%."
            else:
                return "Não foi possível obter informações sobre o clima."
        else:
            return f"Erro ao consultar a API de previsão do tempo: {data.get('message', 'Erro desconhecido')}."
    except Exception as e:
        return f"Ocorreu um erro ao tentar obter a previsão do tempo: {e}"

def extract_city(user_input):
    city_pattern = r'previsão.*para\s+([A-Za-zÀ-ÖØ-öø-ÿ\s]+)'
    match = re.search(city_pattern, user_input.lower())
    if match:
        return match.group(1).strip()
    else:
        return None

bot = ChatBot(
    'RexBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)

trainer = ListTrainer(bot)
conversations = [
    "Qual é o seu nome?", "Meu nome é RexBot.",
    "Qual é a sua função?", "Eu sou um assistente de chat projetado para ajudar com suas perguntas.",
    "Qual o maior time de futebol do Brasil?", "O maior time do Brasil é o Grêmio!",
    "Você consegue informar as temperaturas locais?", "Sim, sou integrado a uma API externa onde consigo a temperatura atual.",
    "Você possui sentimentos?", "Eu não tenho sentimentos, pois sou um programa de computador."
]
trainer.train(conversations)

corpus_trainer = ChatterBotCorpusTrainer(bot)

corpus_trainer.train('chatterbot.corpus.portuguese')

corpus_trainer.train('chatterbot.corpus.portuguese.greetings')

print("Olá! Eu sou o RexBot. Como posso ajudar você hoje?")

with open("conversas.txt", "w", encoding='utf-8') as file:
    while True:
        try:
            user_input = input("Você: ")

            file.write(f"Usuário: {user_input}\n")

            if user_input.lower() == 'sair':
                print("Até logo!")
                break

            city = extract_city(user_input)
            if city:
                print(f"Cidade extraída: {city}")
                response = get_weather(city)
                print(f"Resposta da API: {response}")
            else:
                response = bot.get_response(user_input)

            print("RexBot:", response)

            file.write(f"RexBot: {response}\n")

        except (KeyboardInterrupt, EOFError, SystemExit):
            print("Até logo!")
            break
        except Exception as e:
            print("Desculpe, ocorreu um erro:", e)
