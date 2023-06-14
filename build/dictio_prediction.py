"""
Nom du fichier : dictio_prediction.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier construit le dictionnaire qui sert pour la prédiction.
"""

# Initialisation du dictionnaire de prédiction

from build.data_preparation import *
from build.contexte import *
import pickle

# remplir le dictionnaire
def fullDict (d, listTokens, nbGramme):
    for i in range(len(listTokens)): # pour chaque message
        for j in range(1,len(listTokens[i]),1): # pour chaque mot du message
                contexte=[]
                for z in range (1, min(nbGramme,j),1): # pour z de 0 au nombre de gramme maximal
                    contexte.insert(0,listTokens[i][j-z]) # on crée un contexte du bon nombre de gramme
                    if tuple(contexte) not in d:
                        d[tuple(contexte)]=Contexte(tuple(contexte))
                    d[tuple(contexte)].add_word(listTokens[i][j]) # on ajoute une occurrence au mot suivant ce contexte

#mettre à jour les 10 mots les plus fréquents après chaque contexte
def updateWordsPred (dict):
    for v in dict.values() :
        v.update_wordsPred()

# initialisation du dictionnaire
def initDictio (nbGramme):
    with open("build/data/corpus.pkl", "rb") as file:
            listTokens = pickle.load(file)
    dictio={}
    fullDict(dictio, listTokens,nbGramme)
    updateWordsPred(dictio)
    return dictio


