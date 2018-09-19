from sentences_cosine_similarity import get_cosine_sim

def get_groups(mat,similarity_factor):
    groups = []
    size = len(mat)
    for i in range(0,size):
        s = {i}
        appended = False
        for j in range(0,size):
            if i!=j:
                if mat[i][j]>= similarity_factor:
                    s.add(j)
        if len(s)==1:
            groups.append(s)
        else:
            for k in range(0,len(groups)):
                if len(groups[k].intersection(s))>0:
                    groups[k]=groups[k].union(s)
                    appended = True
                    break
            if appended == False:
                groups.append(s)
    return groups



def get_groups_statistics(*sentences):    
    sentences_similarity_factor = 0.65 #prag slicnosti koji odredjuje da li se ponavlja recenica
    repetition_treshhold=10 #prag ponavljanja (%)

    #matrica slicnosti recenica u textu
    similarity_sentences_matrix = get_cosine_sim(*sentences)
    number_of_sentences = len(similarity_sentences_matrix) #ukupan broj recenica

    groups = get_groups(similarity_sentences_matrix,sentences_similarity_factor) #grupisanje recenica po slicnosti
    groups=sorted(groups,key=len,reverse=True) #sortiranje grupa po velicini
    group_repetition_factors = [(len(g)/number_of_sentences)*100 for g in groups] #odredjivanje procenta koji grupa zauzima u tekstu rada

    size_of_the_highest_repetition_group = group_repetition_factors[0]
    number_of_groups_10 = len(list(filter(lambda a: a >= 10, group_repetition_factors)))
    number_of_groups_20 = len(list(filter(lambda a: a >= 20, group_repetition_factors)))
    number_of_groups_30 = len(list(filter(lambda a: a >= 30, group_repetition_factors)))
    
    return (size_of_the_highest_repetition_group, number_of_groups_10, number_of_groups_20, number_of_groups_30)

    #print("Udio grupe sa najvecim ponavljanjem: (%)",size_of_the_highest_repetition_group)
    #print("Broj grupa koje prelaze treshold od 10%:",number_of_groups_10)
    #print("Broj grupa koje prelaze treshold od 20%:",number_of_groups_20)
    #print("Broj grupa koje prelaze treshold od 30%:",number_of_groups_30)
    

    
