from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Configuração do chatbot
chatbot = ChatBot(
    'StudyAssistant',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(chatbot)

# Dados de treinamento
matematica = [
    "O que é uma função?",
    "Uma função é uma relação entre um conjunto de entradas e um conjunto de saídas onde cada entrada está relacionada a uma única saída."
]

ciencias = [
    "O que é fotossíntese?",
    "A fotossíntese é o processo pelo qual as plantas verdes e alguns outros organismos usam a luz solar para sintetizar alimentos a partir de dióxido de carbono e água."
]

historia = [
    "Quem foi Napoleão Bonaparte?",
    "Napoleão Bonaparte foi um líder militar e político francês que ganhou destaque durante a Revolução Francesa e liderou várias campanhas bem-sucedidas durante as Guerras Revolucionárias Francesas."
]

# Treinamento do chatbot
trainer.train(matematica)
trainer.train(ciencias)
trainer.train(historia)

# Interação com o chatbot
while True:
    try:
        user_input = input("Você: ")
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
