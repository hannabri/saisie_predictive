#%%
# The best project !!!

print("Le meileur trio :)")

#%%

# Part 1 : Prédiction

from data_preparation import *
from contexte import *
import nltk
import pickle
nltk.download('punkt')

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
def updateWordsPred (d):
    for v in d.values() :
        v.update_wordsPred()

# initialisation du dictionnaire
def initDictio (nbGramme):
    with open("tokens.pkl", "rb") as file:
            listTokens = pickle.load(file)
    dictio={}
    fullDict(dictio, listTokens,nbGramme)
    updateWordsPred(dictio)
    return dictio

# PARTIE FONCTION PREDICTION  ()
#structure principale
def structurePred (nbWords, dictio, pred):
    msg = []
    word=""
    end = False
    while end == False:
        saisie=input()
        if saisie=="":
            end=True
        if saisie==" ":
            msg.append(word)
            word=""
            pred(nbWords, msg, dictio)
        else:
            word+=saisie

#liste a afficher pour le cas d'un modèle bigramme
def predBi (nbWords, msg, dictio):
    if len(msg)>0 and (msg[-1],) in dictio :
        print(dictio[(msg[-1]),].wordsPred[:nbWords] )
    else:
        print("[]")

#liste à afficher pour le cas d'un modèle trigramme
def predTri (nbWords, msg, dictio):
    if len(msg)>1 and (msg[-2],msg[-1]) in dictio :
        print(dictio[(msg[-2],msg[-1])].wordsPred[:nbWords] )
    elif len(msg)>0 and (msg[-1],) in dictio :
        print(dictio[(msg[-1]),].wordsPred[:nbWords] )
    else:
        print("[]")

# fonction principale
def prediction (nbWords):
    dictio={}
    if (nbWords==1) or (nbWords==2):
        dictio = initDictio(3)
        structurePred(nbWords, dictio,predTri)
    else:
        dictio = initDictio(2)
        structurePred(nbWords, dictio,predBi)
#prediction(3)


#partie test prediction
def predictionWord(dictio, wordContexte, marge): # marge = nb de mots prédits
    return dictio[wordContexte].wordsPred[:marge] if wordContexte in dictio else []

def testPred (corpusTest,dictio, nbB, nbT):
    correct=0
    total=0
    for j in range(len(corpusTest)): # pour chaque message
        for i in range(1,len(corpusTest[j])-1): # pour chaque mot du message, mis à part le premier et le dernier
            motsPred = predictionWord(dictio, (corpusTest[j][i-1],corpusTest[j][i]),nbT)
            z=0
            motsPredBi = predictionWord(dictio, (corpusTest[j][i],),10)
            while len(motsPred)<(nbB+nbT) and (z<len(motsPredBi)) and (z<nbB):
                if motsPredBi[z] not in motsPred :
                    motsPred.append(motsPredBi[z])
                z+=1
            if (corpusTest[j][i+1] in motsPred):
                correct+=1
            total+=1
    return (correct/total)

def rtUnkWords (corpusTest, dictio):
    nbWords = 0
    nbUnkWords=0
    for j in range(len(corpusTest)):
        for i in range(len(corpusTest[j])):
            if ((corpusTest[j][i],) not in dictio):
                nbUnkWords+=1
            nbWords+=1
    return nbUnkWords/nbWords


#dictio=initDictio(2)

'''
#dictio=initDictio(2)
#test = tokenize_test()
#print(rtUnkWords(test, dictio))


dictio = initDictio(3)
test = tokenize_test()
max =0
for i in range (1,11,1):
    for j in range (0,i+1,1):
        result = testPred(test, dictio, j, i-j)
        print("i : "+str(i)+ " -> nbB : "+str(j)+" ; "+"nbT : "+str(i-j)+" = "+str(result))
        if result>max:
            max=result
print(max)
#for i in range(1,11,1):
#     print(str(i)+ " mots prédits : "+str(testprediction2(test, dictio, i)))
#prediction()
#print(testprediction3(test, dictio))
'''

#%%
# Part 2 : Complétion 

from trie import *
from data_preparation import *

# initiate new Trie

import serialization

# Sérialiser le trie
#serialization.serialize(trie, "trie.json")

# Désérialiser le trie
trie = serialization.deserialize_trie()

# Charger les tokens
tokens = serialization.deserialize_corpus()
tokens_test = serialization.deserialize_test()

def completion():
    
    pre = input()
    while pre[-1] != " ":

         #trier le dicitonnaire et l'afficher s'il n'est pas vide 

        print(trie.show_most_frequent_children(pre))

        print()
        
        # ajouter la prochaine lettre à notre préfix
        pre = pre + input()

    trie.update_word_count(pre[:-1])

#completion()

def update_most_frequent_words(): 
    
    for word in tokens : 
        trie.update(word)



def testcompletion (trie, corpusTest, sizePre, nbWords):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(0,len(corpusTest[j])):
            pre = corpusTest[j][i][:sizePre+1]
            sort =set(trie.show_most_frequent_children(pre)[:nbWords])
            print(sort)
            print(corpusTest[j][i])
            if (corpusTest[j][i] in sort ):
                correct+=1
            total+=1
    return (correct/total)


def testcompletionprediction (dictio, trie, corpusTest, nbWords, pdsPred, sizePre):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(1,len(corpusTest[j])):
            finalSet=set()
            wordsPred = dictio[(corpusTest[j][i-1],)].wordsPred[:pdsPred] if (corpusTest[j][i-1],) in dictio else []
            pre = corpusTest[j][i][:sizePre]
            for word in wordsPred:
                if word.startswith(pre):
                    finalSet.add(word)
                    if len(finalSet)==nbWords:
                        break

            sort =trie.show_most_frequent_children(pre)[:nbWords]
            finalSet.update(sort[:(nbWords-len(finalSet))])
            if corpusTest[j][i] in finalSet :
                correct+=1
            total+=1
    return (correct/total)



for i in range(1,11,1):
    for j in range(1,6,1):
        print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {testcompletion(trie,tokens_test, j, i)}')

'''
dictio = initDictio(2)
for i in range(1,11,1):
    for j in range(1,6,1):
        print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {testcompletionprediction2(dictio, trie,test, i, 5, j)}')
'''