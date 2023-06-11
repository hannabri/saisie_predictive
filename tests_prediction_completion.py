from serialization import *

#Infos sur le corpus de test
def unkWords (corpusTest, dictio):
    nbWords = 0
    nbUnkWords=0
    for j in range(len(corpusTest)):
        for i in range(len(corpusTest[j])):
            if ((corpusTest[j][i],) not in dictio):
                nbUnkWords+=1
            nbWords+=1
    return nbUnkWords/nbWords

#Partie test prediction

def predictionWord(dictio, wordContexte, marge): # marge = nb de mots prédits
    return dictio[wordContexte].wordsPred[:marge] if wordContexte in dictio else []

def testPred (corpusTest,dictio, nbB, nbT):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(1,len(corpusTest[j])-1):
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



#Partie test complétion

def testcompletion (trie, corpusTest, sizePre, nbWords):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(0,len(corpusTest[j])):
            pre = corpusTest[j][i][:sizePre+1]
            sort =set(trie.show_most_frequent_children(pre)[:nbWords])
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

# ---------------Execution des tests-----------------

tokens = load("corpus")
tokens_test = load("test")
trie = load("trie")
dictio= load("dictio_trigrammes")

#Infos sur le corpus
print(f"Le taux de mots inconnus dans le corpus de test est {unkWords(tokens_test, dictio)}")

#Prédiction 
print("\nTest de la prédiction : ")
max =0
for i in range (1,11,1):
    for j in range (0,i+1,1):
        result = testPred(tokens_test, dictio, j, i-j)
        print(f"i : {i} -> nbB : {j} / nbT : {i-j} = {result}")
        if result>max:
            max=result
print(f"Le score maximal atteind est : {max}")

# Complétion
print("\nTest de la complétion : ")
max=0
for i in range(1,11,1):
    for j in range(1,6,1):
        result = testcompletion(trie,tokens_test, j, i)
        print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {result}')
        if result>max:
            max=result
print(f"Le score maximal atteind est : {max}")

# Complétion enrichie par la complétion
print("\nTest de la complétion enrichie par la complétion: ")
for i in range(1,11,1):
    for j in range(1,6,1):
        result = testcompletionprediction(dictio, trie,tokens_test, i, 5, j)
        print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {result}')
        if result>max:
            max=result
print(f"Le score maximal atteind est : {max}")