from gensim.summarization import keywords
import textdistance
import re

def extract_abstract_keywords(text):
    regex_for_abstract = re.compile(r'^Abstract(.*?)(?=Content)', re.MULTILINE|re.DOTALL)#regex za izdvajanje dijela teksta koji je abstract
    match_for_abstract = re.findall(regex_for_abstract, text)
    abstract = match_for_abstract[0]
    
    abstract_keywords = keywords(text=abstract,words=10,split=True,pos_filter=['NN'],scores=False,lemmatize = True) #kljucne rijeci za sazetak

    return abstract_keywords

def extract_text_keywords(text):
    fulltext = text
    regex_for_summary = re.compile(r'^Summary(.*?)(?=Content)', re.MULTILINE|re.DOTALL)#regex za izdvajanje dijela teksta koji je summary
    match_for_summary = re.findall(regex_for_summary, text)
    remaining_text = fulltext.replace(match_for_summary[0],'') #otklanjanje sazetka iz teksta

    text_keywords = keywords(text=remaining_text,words=10,split=True,pos_filter=['NN'],scores=False,lemmatize = True)  #kljucne rijeci za ostatak teksta
 
    return text_keywords
    


def calculate_similarity_of_keywords(abstract_keywords, text_keywords):
    similarity_between_abstract_text_keywords = textdistance.cosine.similarity(abstract_keywords, text_keywords) #slicnost kljucnih rijeci
    return similarity_between_abstract_text_keywords

def get_abstract_text_keywords_similarity(text):
    abstract_keywords = extract_abstract_keywords(text)
    text_keywords = extract_text_keywords(text)
    similarity_between_abstract_text_keywords = calculate_similarity_of_keywords(abstract_keywords, text_keywords)
   
    return similarity_between_abstract_text_keywords
