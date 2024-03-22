from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

trainer = ListTrainer(bot)

trainer.train([
    'Oi',
    'Olá, como posso ajudar?',
    'Estou procurando passagens aéreas.',
    'Para qual destino e data você está procurando?',
    'Preciso de uma passagem para Nova York no dia 20 de março.',
    'Deixe-me verificar a disponibilidade... Sim, temos várias opções para Nova York em 20 de março. Você prefere alguma faixa de horário?',
    'Prefiro voos pela manhã.',
    'Temos um voo saindo às 08:00 e outro às 11:00. Qual você prefere?',
    'Vou ficar com o das 08:00.',
    'Perfeito! Posso reservar para você. Preciso apenas de alguns detalhes adicionais.',
    'Ok, obrigado pela ajuda.',
    'De nada! Estou aqui para ajudar. Tenha uma boa viagem!'
])


while True:
    request = input('você :')
    if request.lower() == 'ok':
        print('Bot: tchau')
        break
    else:
        response = bot.get_response(request)
        print('Bot:', response)
