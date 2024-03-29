import spacy

nlp = spacy.load('pt_core_news_sm')

noticia = "Originárias de diferentes regiões do Brasil, as raças brasileiras de cachorro têm características únicas que as tornam especiais e valiosas para amantes de pets ao redor do mundo. Cada uma delas carrega consigo uma história, uma função específica e traços que as diferenciam de cães de outros países."

doc = nlp(noticia)

for token in doc:
    print(f"{token.text}: {token.pos_}")


