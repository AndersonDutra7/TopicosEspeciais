from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import xlsxwriter
import os

# Criação do chatbot
chatbot = ChatBot("MeuBot")

# Carregamento do corpus de treinamento diretamente do arquivo db.sqlite3
trainer = ListTrainer(chatbot)

# Dados de treinamento (exemplo)
training_data = [
    "Oi",
    "Bem vindo a Hamburgueria MeuBot, como posso ajudar?",
    "Quanto custa um hambúrguer?",
    "O hambúrguer custa R$20,00",
    # Adicione mais dados de treinamento conforme necessário
]


# Treinamento com os dados do arquivo db.sqlite3
trainer.train("TopicosEspeciais/chatBotVoz/venv/db.sqlite3")

# Diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Função para obter resposta do chatbot
def chatbot_response(text):
    """Processa o texto do usuário e gera uma resposta com o ChatterBot."""
    if text:
        response = chatbot.get_response(text)
        return response.text
    else:
        return "Desculpe, não entendi. Pode repetir, por favor?"

# Função para fornecer feedback ao chatbot
def get_user_feedback(text, response):
    """Solicita feedback do usuário e armazena a resposta correta para treinamento."""
    feedback = input("Esta resposta foi útil? (Sim/Não): ")
    correct_response = ""
    if feedback.lower() == 'não':
        correct_response = input("Qual seria a resposta correta?: ")
    # Armazene o feedback e a resposta correta para treinamento
    store_feedback(text, correct_response)


# Função para armazenar feedback e respostas corretas para treinamento
def store_feedback(question, correct_response):
    """Armazena o par pergunta e resposta correta para treinamento posterior."""
    with open(os.path.join(diretorio_atual, "feedback_data.txt"), "a") as file:
        file.write(f"{question} | {correct_response}\n")
    # Treine o bot imediatamente com o novo par
    trainer.train([question, correct_response])

# Função para coletar métricas
def collect_metrics():
    """Coleta métricas relevantes."""
    # Implementação básica das métricas
    accuracy_rate = 0.75  # Taxa de acerto de exemplo
    response_time = 5.2  # Tempo médio de resposta em segundos
    interaction_count = 15  # Número total de interações
    satisfaction_rate = 0.85  # Taxa de satisfação de exemplo
    abandonment_rate = 0.1  # Taxa de abandono de exemplo

    metrics = {
        "Accuracy Rate": accuracy_rate,
        "Response Time (s)": response_time,
        "Interaction Count": interaction_count,
        "Satisfaction Rate": satisfaction_rate,
        "Abandonment Rate": abandonment_rate
    }

    return metrics


# Função para salvar métricas em um arquivo Excel
def save_metrics_to_excel(metrics):
    """Salva as métricas em um arquivo Excel."""
    if metrics:
        with xlsxwriter.Workbook(os.path.join(diretorio_atual, 'metrics.xlsx')) as workbook:
            worksheet = workbook.add_worksheet()

            row = 0
            col = 0
            for metric, value in metrics.items():
                worksheet.write(row, col, metric)
                worksheet.write(row, col + 1, value)
                row += 1
    else:
        print("Nenhuma métrica para salvar.")

# Loop principal para interação com o chatbot
while True:
    user_text = input("Você: ")

    if user_text.lower() == 'finalizar':
        print('Bot: Tchau! Até logo.')
        break

    response = chatbot_response(user_text)
    print('Bot:', response)

    # Coletar feedback
    get_user_feedback(user_text, response)
    # Coletar métricas
    metrics = collect_metrics()
    # Salvar métricas em um arquivo Excel
    save_metrics_to_excel(metrics)
