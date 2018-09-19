import pandas as pd
import os
import csv
from lexicalrichness import LexicalRichness
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

from similarity_groups import get_groups, get_groups_statistics
from density import term_frequency, means_like, triggers, synonyms, get_similar_and_connected_words, get_density_of_similar_and_connected_words
from keywords_similarity import get_abstract_text_keywords_similarity, extract_abstract_keywords

path_to_folder = './2017'
files = []
for i in os.listdir(path_to_folder):
    if i.endswith('.txt'):
        files.append(i)

print(files)

with open('rezultati2017.csv', 'w') as csvfile:
    fieldnames = ['Stepen bogatstva rjecnika', 'Broj unikatnih pojmova','Udio (%) grupe sa najvecim ponavljanjem','Broj grupa koje prelaze treshold od 10%','Broj grupa koje prelaze treshold od 20%','Broj grupa koje prelaze treshold od 30%','slicnost kljucnih rijeci iz abstracta i texta','Gustoca kljucnih rijeci i povezanih rijeci s njima u tekstu']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
 

for f in files:
	#ucitavanje podataka iz txt fajla
	sample_file = open('./2017/'+f, 'r')
	text = sample_file.read()
	sample_file.close()


	fulltext=text
	sentence_tokens = sent_tokenize(fulltext) #tokenizacija recenica
	sentences = [s.lower() for s in sentence_tokens]





	lex = LexicalRichness(text)
	lex_richness = lex.mtld(threshold=0.72)
	print("Stepen bogatstva rjecnika:",lex_richness) #koliko je bogat rjecnik - Measure of Textual Lexical Diversity (MTLD) - zbog neosjetljivosti na duzinu teksta 
	print("Broj unikatnih pojmova:",lex.terms) 





	#statistika za grupe dijelova teksta koji se ponavljaju (Udio (%) grupe sa najvecim ponavljanjem, Broj grupa koje prelaze treshold od 10%, 20%, 30%)
	groups_statistics = get_groups_statistics(*sentences)

	#slicnost kljucnih rijeci iz abstracta i texta
	similarity_between_abstract_text_keywords = get_abstract_text_keywords_similarity(text)
	print("Slicnost kljucnih rijeci:",similarity_between_abstract_text_keywords)

	#gustoca rijeci koje su povezane sa kljucnim rijecima iz abstracta
	density_of_similar_and_connected_words = get_density_of_similar_and_connected_words(fulltext)
	print("Gustoca kljucnih rijeci i povezanih rijeci s njima u tekstu",density_of_similar_and_connected_words)



	with open('rezultati2017.csv', 'a', newline='') as csvfile:
	    fieldnames = ['Stepen bogatstva rjecnika', 'Broj unikatnih pojmova','Udio (%) grupe sa najvecim ponavljanjem','Broj grupa koje prelaze treshold od 10%','Broj grupa koje prelaze treshold od 20%','Broj grupa koje prelaze treshold od 30%','slicnost kljucnih rijeci iz abstracta i texta','Gustoca kljucnih rijeci i povezanih rijeci s njima u tekstu']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writerow({'Stepen bogatstva rjecnika': lex_richness, 'Broj unikatnih pojmova': lex.terms,'Udio (%) grupe sa najvecim ponavljanjem':groups_statistics[0],'Broj grupa koje prelaze treshold od 10%':groups_statistics[1],'Broj grupa koje prelaze treshold od 20%':groups_statistics[2],'Broj grupa koje prelaze treshold od 30%':groups_statistics[3],'slicnost kljucnih rijeci iz abstracta i texta':similarity_between_abstract_text_keywords,'Gustoca kljucnih rijeci i povezanih rijeci s njima u tekstu':density_of_similar_and_connected_words})

