from contexte import *
from deserialization import load

# remplir le dictionnaire
def fullDict (d, listTokens, nbGramme):
    for i in range(len(listTokens)):
        for j in range(1,len(listTokens[i]),1):
                contexte=[]
                for z in range (1, min(nbGramme,j),1):
                    contexte.insert(0,listTokens[i][j-z])
                    if tuple(contexte) not in d:
                        d[tuple(contexte)]=Contexte(tuple(contexte))
                    d[tuple(contexte)].add_word(listTokens[i][j])

#mettre à jour les 10 mots les plus fréquents après chaque contexte
def updateWordsPred (d):
    for v in d.values() :
        v.update_wordsPred()

# initialisation du dictionnaire
dictio= load("dictio_trigrammes")

def structurePred (nbWords, dictio, pred, user_input):
    msg = []
    word=""
    end = False
    for saisie in user_input:
        if saisie=="":
            end=True
        if saisie==" ":
            msg.append(word)
            word=""
            return pred(nbWords, msg, dictio)
        else:
            word+=saisie

def predBi (nbWords, msg, dictio):
    if len(msg)>0 and (msg[-1],) in dictio :
        return dictio[(msg[-1]),].wordsPred[:nbWords]
    else:
        return []

def predTri (nbWords, msg, dictio):
    if len(msg)>1 and (msg[-2],msg[-1]) in dictio :
        return dictio[(msg[-2],msg[-1])].wordsPred[:nbWords]
    elif len(msg)>0 and (msg[-1],) in dictio :
        return dictio[(msg[-1]),].wordsPred[:nbWords]
    else:
        return []

def prediction (nbWords, user_input):
    if (nbWords==1) or (nbWords==2):
        return structurePred(nbWords, dictio,predTri, user_input)
    else:
        return structurePred(nbWords, dictio,predBi, user_input)

from trie import *

trie = load("trie")

def completion(user_input):
    pre = user_input
    while pre[-1] != " ":
        trie.update_word_count(pre[:-1])
        return trie.show_most_frequent_children(pre)
