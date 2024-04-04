from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def obter_resumo(texto, sentences_count=3):
    parser = PlaintextParser.from_string(texto, Tokenizer("english"))
    summarizer = LsaSummarizer()
    resumo = summarizer(parser.document, sentences_count)
    return resumo

def main():
    print("Olá! Por favor, insira o texto para o qual você deseja um resumo:")
    texto = input()
    print("\nAqui está o resumo do texto:")
    resumo = obter_resumo(texto)
    for sentenca in resumo:
        print(sentenca)

if __name__ == "__main__":
    main()
