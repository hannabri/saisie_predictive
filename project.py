#%%
# The best project !!!

print("Le meileur trio :)")

#test de clara : est-ce que les modifications se font en temps r´éel ?

#%%

# Part 1 : Prédiction

from tokenizer_cleaner import *
from contexte import *
import nltk
nltk.download('punkt')

def fullDict (d, listTokens, nbGramme):
    for i in range(len(listTokens)):
        for j in range(1,len(listTokens[i]),1):
                contexte=[]
                for z in range (1, min(nbGramme,j),1):
                    contexte.insert(0,listTokens[i][j-z])
                    if tuple(contexte) not in d:
                        d[tuple(contexte)]=Contexte(tuple(contexte))
                    d[tuple(contexte)].add_word(listTokens[i][j])

def updateWordsPred (d):
    for v in d.values() :
        v.update_wordsPred()

def initDictio (nbGramme):
    with open("tokens.pkl", "rb") as file:
            listTokens = pickle.load(file)
    dictio={}
    fullDict(dictio, listTokens,nbGramme)
    updateWordsPred(dictio)
    return dictio

def prediction ():
    dictio = initDictio()
    saisie = " "
    while saisie!="":
        saisie = input("mot du contexte : ")
        print(dictio[tuple(saisie.split())].wordsPred if tuple(saisie.split()) in dictio else [])


#partie test prediction
def predictionWord(dictio, wordContexte, marge): # marge = nb de mots prédits
    return dictio[wordContexte].wordsPred[:marge] if wordContexte in dictio else []

def testpred (corpusTest,dictio, nbB, nbT):
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
'''
dictio = initDictio(3)
test = tokenize_test()
max =0
for i in range (1,11,1):
    for j in range (0,i+1,1):
        result = testpred(test, dictio, j, i-j)
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

from trie_test import *
from tokenizer_cleaner import *

# initiate new Trie

trie = Trie()

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
        trie.insert(word)

# complétion du mot: 



def completion():
    
    pre = input()
    while pre[-1] != " ":

         #trier le dicitonnaire et l'afficher s'il n'est pas vide 

        sort = dict(sorted(trie.search(pre).items(), key = lambda x: x[1], reverse = True)[:3])

        if sort == {}:
            return None
        else:
            print(sort)

        #print(trie.show_most_frequent_children(pre))

        print()
        
        # ajouter la prochaine lettre à notre préfix
        pre = pre + input()

#completion()

def testcompletion (trie, corpusTest, sizePre, nbWords):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(0,len(corpusTest[j])+1):
            pre = corpusTest[j][i][:sizePre+1]
            sort = dict(sorted(trie.search(pre).items(), key = lambda x: x[1], reverse = True)[:nbWords])
            if (corpusTest[j][i] in sort.keys()):
                correct+=1
            total+=1
    return (correct/total)

def testcompletionprediction (dictio, trie, corpusTest):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(1,len(corpusTest[j])):
            wordsPred = dictio[(corpusTest[j][i-1],)].wordsPred if (corpusTest[j][i-1],) in dictio else []
            pre = corpusTest[j][i][:2]
            sort = dict(sorted(trie.search(pre).items(), key = lambda x: x[1], reverse = True))
            dictComb = {cle: valeur for cle, valeur in sort.items() if cle in wordsPred}
            wordProp=""
            if len(dictComb) !=0:
                wordProp = max(dictComb, key=dictComb.get)
            elif len(sort)!=0 :
                wordProp = max(sort, key=sort.get)
            if corpusTest[j][i] == wordProp:
                correct+=1
            total+=1
    return (correct/total)

test = tokenize_test()
#for i in range(1,11,1):
#    for j in range(1,6,1):
#        print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {testcompletion(trie,test, j, i)}')

dictio = initDictio(2)
print(testcompletionprediction(dictio, trie, test))
