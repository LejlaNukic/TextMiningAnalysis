from datamuse import datamuse
from keywords_similarity import extract_abstract_keywords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

similar_and_connected_words = []
means_like_words=[]
trigger_words=[]
synonym_words=[]
MAX_WORDS = 10

#frekvencija ponavljanja rijeci u tekstu
def term_frequency(text,word):
    fdist = FreqDist(w.lower() for w in word_tokenize(text))
    return fdist[word]/len(word_tokenize(text))

#rijeci koje su slicne po znacenju sa datom 
def means_like(means_like_words,word):
    api = datamuse.Datamuse()
    means_like_result = api.words(ml=word,topics=['computer science','informatics','information technology'], max=MAX_WORDS)
    for w in means_like_result:
        means_like_words.append(w['word'])

#rijeci koje se cesto pojavljuju sa datom
def triggers(triggers_words,word):
    api = datamuse.Datamuse()
    triggers_result = api.words(rel_trg=word, max=MAX_WORDS)
    for w in triggers_result:
        triggers_words.append(w['word'])

#rijeci koje su sinonimi sa datom
def synonyms(synonyms_words,word):
    api = datamuse.Datamuse()
    synonyms_result = api.words(rel_syn=word,topics=['computer science','informatics','information technology'], max=MAX_WORDS)
    for w in synonyms_result:
        synonyms_words.append(w['word'])

#funkcija koja vraca povezane rijeci sa datom rijecju
def get_similar_and_connected_words(keywords):

    for keyword in keywords:
        means_like(means_like_words,keyword)
        triggers(trigger_words,keyword)
        synonyms(synonym_words,keyword)

    similar_and_connected_words = means_like_words + trigger_words + synonym_words

    return similar_and_connected_words


def get_density_of_similar_and_connected_words(text):
    abstract_keywords = extract_abstract_keywords(text)
    density_of_similar_and_connected_words = 0

    similar_and_connected_words = get_similar_and_connected_words(abstract_keywords)
    for word in similar_and_connected_words:
        density_of_similar_and_connected_words += term_frequency(text,word)

    density_of_similar_and_connected_words*=100
    return density_of_similar_and_connected_words

    

