#%%
# The best project !!!
#cjeuiwfnie

print("Le meileur trio :)")

#test de clara : est-ce que les modifications se font en temps r´éel ?
#%%
# Part 1 : Complétion 

from trie_test import *
from tokenizer_cleaner import *

# initiate new Trie

prediction = Trie()

# add words in our trie

list_tokens = tokenize()


# def vocab2dict (vocab):
#     vocab_sans_doublon = list(set(vocab))
#     dict = {w : vocab.count(w) for w in vocab_sans_doublon}
#     return dict

# words = vocab2dict(vocab)


for word in list_tokens:
    prediction.insert(word)

# complétion du mot: 

def completion():
    
    pre = input()
    while pre != " ":

        # trier le dicitonnaire et l'afficher s'il n'est pas vide 

        sort = dict(sorted(prediction.search(pre).items(), key = lambda x: x[1], reverse = True)[:3])

        if sort == {}:
            return None
        else:
            print(sort)
        
        # ajouter la prochaine lettre à notre préfix
        pre = pre + input()

completion()

#%%
# Part 2 : Prédiction
from trie_test import *
from tokenizer_cleaner import *

def completer_dictio (corpus, dictio): # corpus = liste de string
    for i in range(1,len(corpus),1):
        if (corpus[i-1]) in dictio and corpus[i] in dictio[corpus[i-1]]:
            dictio[corpus[i-1]][corpus[i]]+=1
        else:
            if corpus[i-1] not in dictio : 
                dictio[corpus[i-1]]={}
            dictio[corpus[i-1]][corpus[i]]=1


def dictio_3_mots (dictio):
    dictio_3_mots={}
    for key in dictio.keys() :
        dictio_3_mots = {key: [x[0] for x in sorted(dictio[key].items(), key=lambda x: x[1], reverse=True)[:min(3, len(dictio[key]))]] for key in dictio.keys()}
    return dictio_3_mots

def prediction_mot (mot, dictio_3_mots):
    print(f"prediction de \"{mot}\" : ")
    if mot in dictio_3_mots : 
        [print(f" {i+1} : {dictio_3_mots[mot][i]}") for i in range(len(dictio_3_mots[mot]))]


dictio={}
corpus = tokenize()
completer_dictio(corpus, dictio)
ajout_corpus=["<debut>", "la", "chanteuse", "est", "dans", "le", "jardin"]
completer_dictio(ajout_corpus, dictio)
print(dictio)

dictio_3_mots = dictio_3_mots(dictio)

prediction_mot("le", dictio_3_mots)
prediction_mot("chien", dictio_3_mots)
prediction_mot("carotte", dictio_3_mots)

