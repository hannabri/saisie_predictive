"""
Nom du fichier : initialisatopn_objets.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier initialise le dictionnaire de prédiction et le trie de complétion avec les donnée du corpus.
"""

from build.contexte import *

def prediction (user_input, dictio):
    if len(user_input)>0 and (user_input[-1],) in dictio :
            return dictio[(user_input[-1],)].wordsPred[:5]
    else:
        return []

def completion(wordsList, trie):
    pre = wordsList
    while pre[-1] != " ":
        return trie.show_most_frequent_children(pre)

def updatePrediction(message, dictio):
    for i in range(1,len(message),1):
        contexte=[]
        for z in range (1, min(2,i),1):
                    contexte.insert(0,message[i-z])
                    if tuple(contexte) not in dictio:
                        dictio[tuple(contexte)]=Contexte(tuple(contexte))
                    dictio[tuple(contexte)].add_word(message[i])
                    dictio[tuple(contexte)].update_wordsPred()

def updateCompletion(message,trie): 
    for word in message :
        trie.update_word_count(word)
        trie.update(word)