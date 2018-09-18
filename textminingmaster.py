import pandas as pd
from lexicalrichness import LexicalRichness
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

from similarity_groups import get_groups, get_groups_statistics
from density import term_frequency, means_like, triggers, synonyms, get_similar_and_connected_words, get_density_of_similar_and_connected_words
from keywords_similarity import get_abstract_text_keywords_similarity, extract_abstract_keywords


#ucitavanje podataka iz txt fajla
sample_file = open("LejlaTestEngl.txt", 'r')
text = sample_file.read()
sample_file.close()


fulltext=text
sentence_tokens = sent_tokenize(fulltext) #tokenizacija recenica
sentences = [s.lower() for s in sentence_tokens]





lex = LexicalRichness(text)
print("Stepen bogatstva rjecnika:",lex.mtld(threshold=0.72)) #koliko je bogat rjecnik - Measure of Textual Lexical Diversity (MTLD) - zbog neosjetljivosti na duzinu teksta 
print("Broj unikatnih pojmova:",lex.terms) 





#statistika za grupe dijelova teksta koji se ponavljaju (Udio (%) grupe sa najvecim ponavljanjem, Broj grupa koje prelaze treshold od 10%, 20%, 30%)
groups_statistics = get_groups_statistics(*sentences)

#slicnost kljucnih rijeci iz abstracta i texta
similarity_between_abstract_text_keywords = get_abstract_text_keywords_similarity(text)
print("Slicnost kljucnih rijeci:",similarity_between_abstract_text_keywords)

#gustoca rijeci koje su povezane sa kljucnim rijecima iz abstracta
density_of_similar_and_connected_words = get_density_of_similar_and_connected_words(fulltext)
print("Gustoca kljucnih rijeci i povezanih rijeci s njima u tekstu",density_of_similar_and_connected_words)







 


