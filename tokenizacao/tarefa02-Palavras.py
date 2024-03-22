import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')

#link: https://gremio.net/noticias/detalhes/27435/gremio-investe-na-excelencia-esportiva-adquirindo-sistema-blazepod
noticia = "Grêmio investe na excelência esportiva adquirindo sistema BlazePod"
noticia += "Sempre buscando a excelência esportiva para otimizar os resultados de campo, o Grêmio Foot-Ball Porto Alegrense fechou parceria com a Espaço Miami, empresa importadora com sede em São Paulo e no Sul dos Estados Unidos. Por meio dela, o Clube passou a ser o primeiro da América Latina a adquirir kits do sistema BlazePod, um equipamento de treino visual e cognitivo que ajuda a melhorar a velocidade, a agilidade, a coordenação e as tomadas de decisões."
noticia += "O sistema consiste em uma série de estações de luzes vibrantes onde os atletas respondem aos sinais piscantes multicoloridos tocando-os o mais rápido possível."
noticia += "A tecnologia, que se destacou primeiramente na Fórmula 1, atualmente é utilizada por mais de trezentos mil atletas de vários esportes, em todo o planeta. O kit adquirido pelo Grêmio é o mesmo aplicado por grandes clubes da Europa, como Liverpool e Real Madrid."
noticia += "O vice-presidente do Tricolor, Gustavo Bolognesi, destacou o pioneirismo gremista no continente: Estamos trazendo ao Grêmio um grande reforço que já é utilizado amplamente em outros esportes como tênis, NBA, NFL e MotoGP, além da F1 e outros clubes de futebol europeus. O Tricolor está inovando sempre e seremos o primeiro time da América Latina a utilizar essa tecnologia, declarou."
noticia += "O sócio da empresa Espaço Miami, Agnelo Cittolin, salientou que a parceria com o Grêmio representa não só a adoção de tecnologia de ponta, mas também é um marco na forma como os clubes latino-americanos abordam o treinamento e a preparação física: Ao introduzirmos os BlazePods no cotidiano do Tricolor, não estamos apenas equipando o Clube com ferramentas modernas, estamos abrindo novos caminhos para a excelência esportiva no continente”, celebrou."

words = word_tokenize(noticia)


print("Palavras Tokenizadas: ", words)
print("Quantidade de Palavras: ", len(words))
