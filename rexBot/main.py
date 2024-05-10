from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

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

# Treinar o bot com o corpus de dados em inglês
corpus_trainer.train('chatterbot.corpus.portuguese')

# Personalizar o treinamento para a categoria de diálogo de cumprimentos (greetings)
corpus_trainer.train('chatterbot.corpus.portuguese.greetings')

# Iniciar a sessão de chat
print("Olá! Eu sou o RexBot. Como posso ajudar você hoje?")

# Abrir o arquivo de texto para escrever as conversas
with open("conversas.txt", "w") as file:
    while True:
        try:
            # Obter a entrada do usuário
            user_input = input("Você: ")

            # Escrever a entrada do usuário no arquivo
            file.write(f"Usuário: {user_input}\n")

            # Verificar se o usuário quer sair
            if user_input.lower() == 'sair':
                print("Até logo!")
                break

            # Obter a resposta do bot
            response = bot.get_response(user_input)

            # Imprimir a resposta do bot
            print("RexBot:", response)

            # Escrever a resposta do bot no arquivo
            file.write(f"RexBot: {response}\n")

        except (KeyboardInterrupt, EOFError, SystemExit):
            print("Até logo!")
            break
        except:
            print("Desculpe, não entendi. Poderia repetir, por favor?")

# Recuperar o histórico de conversas
from chatterbot import ChatBot
from chatterbot.storage import SQLStorageAdapter

# Conectar ao banco de dados SQLite
bot = ChatBot(
    'RexBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)

# Recuperar todas as conversas
conversations = bot.storage.filter()

# Abrir o arquivo de texto para escrever as conversas
with open("conversas.txt", "w") as file:
    # Escrever o histórico de conversas no arquivo
    for conversation in conversations:
        file.write(f"Usuário: {conversation.text}\n")
        file.write(f"RexBot: {conversation.in_response_to}\n")
        file.write("\n")
