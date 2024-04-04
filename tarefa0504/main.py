import spacy
from nltk.tokenize import sent_tokenize

nlp = spacy.load('pt_core_news_sm')

def generate_summary(text, num_sentences):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    if len(sentences) <= num_sentences:
        return "\n".join(sentences)
    else:
        summary = " ".join(sentences[:num_sentences])
        return summary + " ..."

def chatbot():
    print("\nOlá! Bem vindo ao resumidor de textos Ralph & Teddy.\n" + "=-" *26 + "\n")
    while True:
        user_input = input("Digite 'resumir' para começar ou 'sair' para encerrar: ").strip().lower()
        if user_input == 'sair':
            print("\nOok, muito obrigado ... Até mais!\n" + "=-" *32)
            print("-" * 64)
            break
        elif user_input == 'resumir':
            print("-" * 64)
            print("\nPor favor, digite o texto que você gostaria de resumir:")
            print("-" * 64)
            text = input("")
            while True:
                num_sentences = input("\nQuantas sentenças você gostaria no resumo? ")
                if num_sentences.isdigit():
                    num_sentences = int(num_sentences)
                    break
                else:
                    print("Por favor, insira apenas números inteiros.")
            summary = generate_summary(text, num_sentences)
            print("-" * 64)
            print("\nTexto resumido:")
            print(summary + "\n" + "=-" * 32 + "\n")

chatbot()
