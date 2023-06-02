#%%
# The best project !!!
#cjeuiwfnie
print("Le meileur trio :)")
'''
#test de clara : est-ce que les modifications se font en temps r´éel ?
#%%
# Part 1 : Complétion 

from trie_test import *
from tokenizer_cleaner import *

# initiate new Trie

prediction = Trie()

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
        prediction.insert(word)

# complétion du mot: 

def completion():
    
    pre = input()
    while pre != " ":

        # trier le dicitonnaire et l'afficher s'il n'est pas vide 

        sort = dict(sorted(prediction.search(pre).items(), key = lambda x: x[1], reverse = True)[:3])

        if sort == {}:
            return None
        else:
            print(sort)
        
        # ajouter la prochaine lettre à notre préfix
        pre = pre + input()

completion()
'''
#%%
# Part 2 : Prédiction
from tokenizer_cleaner import *
from contexte import *
import nltk
nltk.download('punkt')

def fullDict (d, listTokens): #listTokens = liste de liste
    for i in range(len(listTokens)): # pour tous les sms
        for j in range(1,len(listTokens[i]),1): # du 2eme au dernier token
                if (listTokens[i][j-1]) not in d:
                    d[listTokens[i][j-1]]=Contexte(listTokens[i][j-1]) # créer le contexte si il existe pas (contexte = listTokens[i][j-1])
                d[listTokens[i][j-1]].add_word(listTokens[i][j]) #ajouter une occurence au mot qui suit le contexte

def fullDictTriGrammes (d, listTokens): #listTokens = liste de liste
    for i in range(len(listTokens)): # pour tous les sms
        for j in range(2,len(listTokens[i]),1): # du 2eme au dernier token
                if (listTokens[i][j-1]) not in d:
                    d[listTokens[i][j-1]]=Contexte(listTokens[i][j-1]) # créer le contexte si il existe pas (contexte = listTokens[i][j-1])
                d[listTokens[i][j-1]].add_word(listTokens[i][j]) #ajouter une occurence au mot qui suit le contexte
                if (listTokens[i][j-2]+" "+listTokens[i][j-1]) not in d:
                    d[listTokens[i][j-2]+" "+listTokens[i][j-1]]=Contexte(listTokens[i][j-2]+" "+listTokens[i][j-1]) # créer le contexte si il existe pas (contexte = listTokens[i][j-1])
                d[listTokens[i][j-2]+" "+listTokens[i][j-1]].add_word(listTokens[i][j]) #ajouter une occurence au mot qui suit le contexte

def updateWordsPred (d):
    for v in d.values() :
        v.update_wordsPred()

def initDictio ():
    with open("tokens.pkl", "rb") as file:
            listTokens = pickle.load(file)
    dictio={}
    fullDict(dictio, listTokens)
    updateWordsPred(dictio)
    return dictio

def prediction ():
    dictio = initDictio()
    saisie = " "
    while saisie!="":
        saisie = input("mot du contexte : ")
        print(dictio[saisie].wordsPred if saisie in dictio else [])

def initDictio2 ():
    with open("tokens.pkl", "rb") as file:
            listTokens = pickle.load(file)
    dictio={}
    fullDictTriGrammes(dictio, listTokens)
    updateWordsPred(dictio)
    return dictio

def prediction2 ():
    dictio = initDictio2()
    saisie = " "
    while saisie!="":
        saisie = input("mot du contexte : ")
        print(dictio[saisie].wordsPred if saisie in dictio else [])


#partie test prediction
def predictionWord(dictio, wordContexte, marge): # marge = nb de mots prédits (entre 0 et 3)
    return dictio[wordContexte].wordsPred[:marge] if wordContexte in dictio else []

def testprediction (corpusTest,dictio,marge):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(len(corpusTest[j])-1):
            if corpusTest[j][i+1] in predictionWord(dictio, corpusTest[j][i], marge):
                correct +=1
            total+=1
    return (correct/total)

def testprediction2 (corpusTest,dictio,marge):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(1,len(corpusTest[j])-1):
            motsPredTri = predictionWord(dictio, corpusTest[j][i-1]+" "+corpusTest[j][i], marge)
            trouve=False
            if ( len(motsPredTri) > 0 ) :
                if (corpusTest[j][i+1] in motsPredTri):
                    correct +=1
                    trouve=True
            
            if (trouve==False) and (corpusTest[j][i+1] in predictionWord(dictio, corpusTest[j][i], marge)):
                correct+=1
            total+=1
    return (correct/total)

#meilleure option trouvée
def testprediction3 (corpusTest,dictio):
    correct=0
    total=0
    for j in range(len(corpusTest)):
        for i in range(1,len(corpusTest[j])-1):
            motsPred = predictionWord(dictio, corpusTest[j][i-1]+" "+corpusTest[j][i],3)
            z=0
            motsPredBi = predictionWord(dictio, corpusTest[j][i],3)
            while len(motsPred)<3 and (z<len(motsPredBi)):
                if motsPredBi[z] not in motsPred :
                    motsPred.append(motsPredBi[z])
                z+=1
            if (corpusTest[j][i+1] in motsPred):
                correct+=1
            total+=1
    return (correct/total)

dictio2 = initDictio2()
test = tokenize_test()
#for i in range(1,11,1):
#     print(str(i)+ " mots prédits : "+str(testprediction2(test, dictio, i)))
#prediction()
#prediction2()
print(testprediction3(test, dictio2))