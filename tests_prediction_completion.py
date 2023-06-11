from serialization import *
#partie test prediction

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

def rtUnkWords (corpusTest, dictio):
    nbWords = 0
    nbUnkWords=0
    for j in range(len(corpusTest)):
        for i in range(len(corpusTest[j])):
            if ((corpusTest[j][i],) not in dictio):
                nbUnkWords+=1
            nbWords+=1
    return nbUnkWords/nbWords

#partie test complétion

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


#partie test complétion avec prédiciton

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


#Prédiction 

#dictio=initDictio(2)
#test = tokenize_test()
#print(rtUnkWords(test, dictio))


dictio = initDictio(3)
test = load("test")
max =0
for i in range (1,11,1):
    for j in range (0,i+1,1):
        result = testPred(test, dictio, j, i-j)
        print("i : "+str(i)+ " -> nbB : "+str(j)+" ; "+"nbT : "+str(i-j)+" = "+str(result))
        if result>max:
            max=result
#print(max)
#for i in range(1,11,1):
#     print(str(i)+ " mots prédits : "+str(testprediction2(test, dictio, i)))
#prediction()
#print(testprediction3(test, dictio))

# Complétion

# dictio = initDictio(2)
# for i in range(1,11,1):
#     for j in range(1,6,1):
#         print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {testcompletionprediction2(dictio, trie,test, i, 5, j)}')

# Charger les tokens
tokens = load("corpus")
tokens_test = load("test")

for i in range(1,11,1):
    for j in range(1,6,1):
        print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {testcompletion(trie,tokens_test, j, i)}')



