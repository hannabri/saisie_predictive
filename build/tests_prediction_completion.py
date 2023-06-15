"""
Nom du fichier : tests_prediction_completion.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier réunit les fonctions qui ont servies à tester notre programme.
"""

from build.serialization import *

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

def resultsPred (dictio, corpus_test):
    d_results = {}
    for i in range (1,11,1):
        for j in range (0,i+1,1):
            d_results[f"i : {i} -> nbB : {j} / nbT : {i-j}"] = testPred(corpus_test, dictio, j, i-j)
    return d_results



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

def resultsCompl (trie, corpus_test):
    d_results = {}
    for i in range(1,11,1):
        for j in range(1,6,1):
            d_results[f'nb mots prédits : {i} , taille du prefixe : {j}'] = testcompletion(trie,corpus_test, j, i)
    return d_results


def testCompletionPrediction (dictio, trie, corpusTest, nbWords, pdsPred, sizePre):
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

def resultsComplPred(dictio, trie, corpus_test):
    d_results={}
    for i in range(1,11,1):
        for j in range(1,6,1):
            d_results[f'nb mots prédits : {i} , taille du prefixe : {j}']= testCompletionPrediction(dictio, trie,corpus_test, i, 10, j)
    return d_results

def df_results ():
    corpus_test = load("build/data/test.pkl")
    trie = load("build/data/trie.pkl")
    dictio= load("build/data/dictio_trigrammes.pkl")

    df_pred_results = pd.DataFrame.from_dict(resultsPred (dictio, corpus_test), orient='index', columns=['Résultat'])
    df_pred_results['Test prédiction'] = df_pred_results.index
    df_pred_results = df_pred_results[['Test prédiction', 'Résultat']]
    print(df_pred_results)
    df_pred_results.to_csv('src/prediction_results.csv', index=False)

    df_compl_results = pd.DataFrame.from_dict(resultsCompl (trie, corpus_test), orient='index', columns=['Résultat'])
    df_compl_results['Test complétion'] = df_compl_results.index
    df_compl_results = df_compl_results[['Test complétion', 'Résultat']]
    print(df_compl_results)
    df_compl_results.to_csv('src/complétion_results.csv', index=False)

    df_compl_pred_results = pd.DataFrame.from_dict(resultsComplPred (dictio,trie, corpus_test), orient='index', columns=['Résultat'])
    df_compl_pred_results['Test complétion enrichi par prédiction'] = df_compl_pred_results.index
    df_compl_pred_results = df_compl_pred_results[['Test complétion enrichi par prédiction', 'Résultat']]
    print(df_compl_pred_results)
    df_compl_pred_results.to_csv('src/complétion_prediction_results.csv', index=False)
