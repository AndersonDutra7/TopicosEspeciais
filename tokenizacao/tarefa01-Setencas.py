import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')


#link: https://gremio.net/noticias/detalhes/27438/gurias-gremistas-vencem-botafogo-fora-de-casa-e-se-recuperam-no-brasileirao--

noticia = "Na tarde desta quinta-feira, no Estádio Nilton Santos, no Rio de Janeiro, as Gurias Gremistas venceram o Botafogo, pelo placar de 2 a 0, em jogo válido pela 2ª rodada do Campeonato Brasileiro A1. Com o resultado, a equipe comandada pela técnica Thaissan Passos conquistou os primeiros três pontos na competição se recuperando do revés diante do Corinthians, na estreia. Os gols gremistas foram anotados por Brito e Giovaninha, ambos na segunda etapa. " \
          "Tendo em vista o forte calor que assolou a capital carioca na tarde de hoje, as duas equipes fizeram um primeiro tempo com o freio de mão puxado. " \
          "Detendo um pouco mais a posse de bola, o Tricolor procurou ganhar o meio de campo, mas pouco ameaçou a meta botafoguense. " \
          "Os primeiros 45 minutos tiveram somente três oportunidades de gol, uma para o Botafogo e duas grandes chances para o Grêmio. " \
          "O  Botafogo criou logo aos 5 minutos: após escanteio cobrado por Chai, da direita, Karen se antecipou no primeiro pau e mandou por sobre o travessão, de cabeça. " \
          "No lance seguinte, o Grêmio chegou tocando na frente da área e Caty recebeu entrando livre pela esquerda. Ela deu um leve toque embaixo da bola para tirar da goleira Michelle, mas a conclusão passou à esquerda, rente ao poste. " \
          "Aos 12 minutos, a melhor oportunidade: Jéssica Peña achou Cássia entrando na área outra vez pela esquerda. Ela driblou a goleira e mandou pro gol aberto. A zagueira voltou a tempo e salvou sobre a linha. No rebote, Ludmila chutou forte e Michelle fez um milagre. Grande chance! " \
          "Foi o que de melhor ocorreu no primeiro tempo que poderia ter terminado com a vitória das Gurias Gremistas. " \
          "O Grêmio voltou para etapa final sem modificações, mas com uma postura mais ofensiva. O Botafogo, por sua vez, também ousou colocando uma atacante no lugar de uma jogadora de meio, mas foram as Gurias Gremistas que tomaram conta do jogo. " \
          "Diferente do primeiro tempo, já sem o sol batendo direto no gramado, a partida foi muito mais movimentada. " \
          "Aos 7 minutos, no contra-ataque, quase o gol das Gurias Gremistas: Dayana Rodríguez abriu para Cássia, no bico da grande área pela direita. Ela ajeitou o corpo e colocou por cobertura, buscando o ângulo direito. A bola explodiu no travessão e saiu. " \
          "Cinco minutos depois, outra vez Cássia. Ela tabelou com Ludmila na frente da área e chutou prensado. A bola passou à esquerda, com perigo. " \
          "No minuto 15, três alterações no Grêmio: entraram Luana Spindler, Raíssa Bahia e Rafa Levis nas vagas de Ludmila, Caty e Dayana Rodríguez. " \
          "Aos 21, Rafa Levis cobrou escanteio da equerda e Tayla desviou no primeiro pau mandando no canto oposto. A bola passou raspando. " \
          "Estava amadurecendo o gol do Grêmio. " \
          "Depois de tanto buscar, as Gurias Gremistas abriram o marcador aos 24: novamente escanteio cobrado por Rafa Levis no meio da área. A defesa carioca se atrapalhou e, na segunda tentativa, Brito pegou o rebote e chutou forte para o fundo das redes. Grêmio 1 a 0! " \
          "O Botafogo deu o troco logo em seguida: Luciana Gómez achou Duda Basílio dentro da área, pela direita. A atacante apareceu livre, mas não pegou bem na bola. Ela passou à direita. " \
          "Com a vantagem no marcador, o Tricolor passou a administrar o tempo. " \
          "Aos 39 minutos, surgiu o segundo gol que matou o jogo: Cássia cruzou da esquerda, com a perna direita, buscando o segundo pau. Giovaninha veio de trás, em velocidade, e mandou de canhota, no canto esquerdo da goleira Michelle, que nem se mexeu. Grêmio 2 a 0!" \
          "Na sequência, a técnica Thaissan Passos colocou Shashá no lugar de Jéssica Peña e Sinara no lugar da Luana Spindler. " \
          "O Botafogo até tentou diminuir a vantagem numa pessão final, mas as Gurias Gremistas seguraram a grande vitória fora de casa. " \
          "O Tricolor volta a campo no próximo domingo, às 15h, para enfrentar o Fluminense, no Estádio Airton Ferreira da Silva, no CFT Hélio Dourado, em Eldorado do Sul. "

setences = sent_tokenize(noticia)


print("Notícia Tokenizada: ", setences)
print("Tamanho da Sentença: ", len(setences))
print(setences[0])
print(setences[1])
print(setences[2])
