from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
from nltk.corpus import wordnet
import os

# Baixar os pacotes necessários do nltk
nltk.download('punkt')
nltk.download('wordnet')

# Funções de pré-processamento
def preprocess(text):
    tokens = nltk.word_tokenize(text)
    lemmatizer = nltk.WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_tokens)

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

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
    "Uma função é uma relação entre um conjunto de entradas e um conjunto de saídas onde cada entrada está relacionada a uma única saída.",
    "O que é uma equação quadrática?",
    "Uma equação quadrática é uma equação polinomial de segundo grau, cuja forma geral é ax^2 + bx + c = 0, onde a, b e c são constantes e a ≠ 0.",
    "Como resolver uma equação linear?",
    "Para resolver uma equação linear, isolamos a variável em um lado da equação, garantindo que ela fique sozinha. Em seguida, aplicamos as operações inversas para simplificar e resolver a equação."
]

ciencias = [
    "O que é fotossíntese?",
    "A fotossíntese é o processo pelo qual as plantas verdes e alguns outros organismos usam a luz solar para sintetizar alimentos a partir de dióxido de carbono e água.",
    "O que é a teoria da evolução?",
    "A teoria da evolução é um conjunto de ideias científicas que explicam como as espécies de organismos mudam ao longo do tempo através do processo de seleção natural.",
    "Qual é a estrutura do átomo?",
    "Um átomo é composto por um núcleo central, composto por prótons e nêutrons, e uma nuvem de elétrons que orbitam ao redor do núcleo."
]

historia = [
    "Quem foi Napoleão Bonaparte?",
    "Napoleão Bonaparte foi um líder militar e político francês que ganhou destaque durante a Revolução Francesa e liderou várias campanhas bem-sucedidas durante as Guerras Revolucionárias Francesas.",
    "O que foi a Revolução Industrial?",
    "A Revolução Industrial foi um período de transformação econômica, social e tecnológica que começou na Inglaterra durante o século XVIII, caracterizado pelo surgimento da maquinaria, urbanização e mudanças significativas na produção.",
    "Quem foi Cleópatra?",
    "Cleópatra foi a última rainha do Egito, conhecida por sua inteligência, beleza e influência política. Ela governou o Egito durante um período de grande tumulto e desafios para o país."
]

# Treinamento inicial do chatbot
trainer.train(matematica)
trainer.train(ciencias)
trainer.train(historia)

# Função para salvar feedback de respostas corretas
def save_feedback(question, correct_answer, user_feedback):
    feedback_file = "feedback.txt"
    with open(feedback_file, 'a') as f:
        f.write(f"Pergunta: {question}\n")
        f.write(f"Resposta Correta: {correct_answer}\n")
        f.write(f"Feedback do Usuário: {user_feedback}\n\n")

# Saudação inicial
print("Olá! Eu sou o Assistente de Estudos e ajudarei você com os estudos.")
print("Escolha uma das disciplinas para conversarmos: \n  Matemática\n  Ciências\n  História")

# Interação com o chatbot
selected_discipline = None
while True:
    try:
        user_input = input("Você: ")
        user_input = preprocess(user_input)
        
        # Verifica se o usuário saudou o chatbot
        if user_input.lower() in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]:
            print("Olá! Como posso ajudar você hoje? Converso sobre Matemática, Ciências e/ou História.")
            continue
        
        # Verifica se o usuário deseja selecionar uma disciplina
        if user_input.lower() in ["matemática", "matematica", "ciências", "ciencias", "história", "historia"]:
            selected_discipline = user_input.lower()
            print(f"Muito bem! Vamos conversar sobre {selected_discipline.capitalize()}.")
            continue
        
        # Se uma disciplina foi selecionada, processa a pergunta
        if selected_discipline:
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")
            
            # Solicita feedback do usuário
            feedback = input("Essa resposta foi útil? (sim/não): ")
            if feedback.lower() == "não":
                correct_answer = input("Qual seria a resposta correta? ")
                trainer.train([user_input, correct_answer])
                save_feedback(user_input, correct_answer, feedback)
                print("Obrigado pelo seu feedback! Aprendi a resposta correta.")
            else:
                save_feedback(user_input, response, feedback)
        else:
            print("Por favor, selecione uma disciplina primeiro.")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
