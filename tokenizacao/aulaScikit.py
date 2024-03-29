import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from heapq import nlargest
import string

def preprocess_text_pt(text):
    tokens = word_tokenize(text.lower(), language='portuguese')

    stop_words = set(stopwords.words('portuguese'))
    words = [word for word in tokens if word.isalnum() and word not in stop_words and word not in string.punctuation]
    return " ".join(words)


def generate_summary(text, num_sentences):
    sentences = sent_tokenize(text, language='portuguese')
    preprocess_text = preprocess_text_pt(text)

    tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords.words('portuguese'))
    tfidf_matrix = tfidf_vectorizer.fit_transform([preprocess_text])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    word_scores = {}
    for word, score in zip(feature_names, tfidf_matrix.toarray()[0]):
        word_scores[word] = score

    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        sentence_words = word_tokenize(sentence.lower(), language='portuguese' )
        score = sum(word_scores[word] for word in sentence_words if word in word_scores)
        sentence_scores[i] = score / len(sentence_words) if len(sentence_words) > 0 else 0
        selected_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(sentences[i] for i in sorted(selected_sentences))
        return summary

texto = """Pug[Nota] (em chinês: 巴哥犬) é uma raça de cão de companhia de pequeno porte, com focinho achatado e cauda enrolada.[1]
São cães braquicefálicos, ou seja, têm o focinho "achatado". Cães com essa características tem o sistema respiratório superior comprimido e portanto não toleram muito exercício físico.[2]
Os ancestrais da raça vieram originalmente da China. Tal afirmação é baseada no fato de terem encontrado cães similares na nação Oriental nos anos de 700 a.C. Todavia, apenas quando levada à Europa, primeiramente pelos holandeses e em seguida pelos ingleses é que a raça atingiu o padrão moderno. Adotada pela realeza europeia, foi a preferida de Josefina, esposa de Napoleão Bonaparte.[1] Com o aumento de sua popularidade, conquistou ainda diversos nomes, dependendo do país. Foi chamada de mop, mol, carlin, carlino, calindogue,[3] pug-dog e mops.
Fisicamente, o pug pode chegar a pesar até 13 kg.[4] Pelo seu tamanho e por não necessitarem de muito exercício, o pug é o tipo de cachorro ideal para apartamento.[5]
O pug é classificado como “cão de companhia“, fazendo parte do grupo dos cães “Toys” ou “de Companhia”, o grupo 9. Os pugs deveriam pesar entre 6,3 e 8,1 kg, sendo cães pesados para a sua estatura. Sua aparência geral deve ser quadrada e maciça, deve mostrar “multum in parvo ” (muita substância em um pequeno volume), o que transparece em sua forma compacta, com proporcionalidade entre as partes e musculatura firme.
A cabeça do pug é a característica mais original e típica da raça. Deve ser redonda quando você a olha de frente e o focinho completamente chato quando olhado de perfil. Os olhos de um pug são redondos, escuros, expressivos e cheios da vida. Suas orelhas são ajustadas na cabeça, devendo ser pretas. As rugas na cabeça de um pug devem ser profundas e fáceis de ver, porque dentro delas a cor é mais escura do que fora. Deve existir uma grande ruga sobre o nariz.Outra característica importante do pug é sua cauda. A cauda é implantada acima da garupa e deve ser fortemente enrolada. A cauda duplamente enrolada é a ideal que os criadores buscam, mas uma única volta apertada é aceitável. Os pugs têm basicamente duas cores: fulvo (abricó) em várias tonalidades e preta.[6]"""


summary = generate_summary(texto, 5)

print(summary)
