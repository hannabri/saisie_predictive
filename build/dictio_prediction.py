"""
Nom du fichier : dictio_prediction.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier construit le dictionnaire qui sert pour la prédiction.
"""
from build.data_preparation import *
from build.contexte import *
import pickle

def fullDict (d, listTokens, nbGramme):
    for i in range(len(listTokens)): 
        for j in range(1,len(listTokens[i]),1):
                contexte=[]
                for z in range (1, min(nbGramme,j),1):
                    contexte.insert(0,listTokens[i][j-z])
                    if tuple(contexte) not in d:
                        d[tuple(contexte)]=Contexte(tuple(contexte))
                    d[tuple(contexte)].add_word(listTokens[i][j])

def updateWordsPred (dict):
    for v in dict.values() :
        v.update_wordsPred()

def initDictio (nbGramme):
    with open("build/data/corpus.pkl", "rb") as file:
            listTokens = pickle.load(file)
    dictio={}
    fullDict(dictio, listTokens,nbGramme)
    updateWordsPred(dictio)
    return dictio


