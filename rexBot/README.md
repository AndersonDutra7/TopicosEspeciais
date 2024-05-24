from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import requests
import re

# Função para obter a previsão do tempo para uma determinada cidade

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

# Função para extrair o nome da cidade da pergunta do usuário

def extract_city(user_input):
city_pattern = r'previsão.\*para\s+([A-Za-zÀ-ÖØ-öø-ÿ\s]+)'
match = re.search(city_pattern, user_input.lower())
if match:
return match.group(1).strip()
else:
return None

# Criar um objeto de ChatBot

bot = ChatBot(
'RexBot',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///db.sqlite3'
)

# Treinar o bot com conversas específicas fornecidas por ListTrainer

trainer = ListTrainer(bot)
conversations = [
"Qual é o seu nome?", "Meu nome é RexBot.",
"Qual é a sua função?", "Eu sou um assistente de chat projetado para ajudar com suas perguntas.",
"Qual o maior time de futebol do Brasil?", "O maior time do Brasil é o Grêmio!",
"Você consegue informar as temperaturas locais?", "Sim, sou integrado a uma API externa onde consigo a temperatura atual.",
"Você possui sentimentos?", "Eu não tenho sentimentos, pois sou um programa de computador."
]
trainer.train(conversations)

# Criar um treinador de ChatBot para carregar os dados de treinamento do corpus externo

corpus_trainer = ChatterBotCorpusTrainer(bot)

# Treinar o bot com o corpus de dados em português

corpus_trainer.train('chatterbot.corpus.portuguese')

# Personalizar o treinamento para a categoria de diálogo de cumprimentos (greetings)

corpus_trainer.train('chatterbot.corpus.portuguese.greetings')

# Iniciar a sessão de chat

print("Olá! Eu sou o RexBot. Como posso ajudar você hoje?")

# Abrir o arquivo de texto para escrever as conversas

with open("conversas.txt", "w", encoding='utf-8') as file:
while True:
try: # Obter a entrada do usuário
user_input = input("Você: ")

            # Escrever a entrada do usuário no arquivo
            file.write(f"Usuário: {user_input}\n")

            # Verificar se o usuário quer sair
            if user_input.lower() == 'sair':
                print("Até logo!")
                break

            # Verificar se o usuário está pedindo a previsão do tempo
            city = extract_city(user_input)
            if city:
                print(f"Cidade extraída: {city}")  # Adicionado para depuração
                response = get_weather(city)
                print(f"Resposta da API: {response}")  # Adicionado para depuração
            else:
                # Obter a resposta do bot para a entrada do usuário
                response = bot.get_response(user_input)

            # Imprimir a resposta do bot
            print("RexBot:", response)

            # Escrever a resposta do bot no arquivo
            file.write(f"RexBot: {response}\n")

        except (KeyboardInterrupt, EOFError, SystemExit):
            print("Até logo!")
            break
        except Exception as e:
            print("Desculpe, ocorreu um erro:", e)
