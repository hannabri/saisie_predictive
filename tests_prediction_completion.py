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



