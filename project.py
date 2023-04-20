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

with open("tokens.pkl", "rb") as file:
    tokens = pickle.load(file)


# def vocab2dict (vocab):
#     vocab_sans_doublon = list(set(vocab))
#     dict = {w : vocab.count(w) for w in vocab_sans_doublon}
#     return dict

# words = vocab2dict(vocab)

for list_tokens in tokens:
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
from tokenizer_cleaner import *
from contexte import *
import nltk
nltk.download('punkt')

def initDict (d, listTokens): #listTokens = liste de liste
    for i in range(len(listTokens)): # pour tous les sms
        for j in range(1,len(listTokens[i]),1): # du 2eme au dernier token
                if (listTokens[i][j-1]) not in d:
                    d[listTokens[i][j-1]]=Contexte(listTokens[i][j-1]) # créer le contexte si il existe pas (contexte = listTokens[i][j-1])
                d[listTokens[i][j-1]].add_word(listTokens[i][j]) #ajouter une occurence au mot qui suit le contexte

def updateWordsPred (d):
    for v in d.values() :
        v.update_wordsPred()

def prediction ():
    with open("tokens.pkl", "rb") as file:
        listTokens = pickle.load(file)
    dictio={}
    initDict(dictio, listTokens)
    updateWordsPred(dictio)
    saisie = " "
    while saisie!="":
        saisie = input("mot du contexte : ")
        print(dictio[saisie].wordsPred if saisie in dictio else [])

prediction()