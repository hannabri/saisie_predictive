#--------------- PARTIE COMPLETION ---------------

import operator

#------------------------
#PARTIE A : transformer le vocabulaire en dictionnaire de mots et de leur occurences

def vocab2dict (vocab):
    vocab_sans_doublon = set(vocab);
    dict = {w : vocab.count(w) for w in vocab_sans_doublon}
    return dict

def sortedVocab (dictio):
    sortedDictio = dict(sorted(dictio.items(), key=lambda item:item[1], reverse=True))
    return sortedDictio

#------------------------
# PARTIE B : faire la prédiction d'un mot pendant sa saisie

# réduire le dictionnaire aux mots commençant par le préfixe
def reduceDictio (redDictio, pre):
    dictioTmp={}
    for key, values in redDictio.items():
            if key.startswith(pre):
                dictioTmp[key]=values
    return dictioTmp

#afficher les 3 propositions
def printCompletion(redDictio):
    keys = list(redDictio.keys())
    for i in range(min(3, len(redDictio))):
        print(str(i+1)+" : "+keys[i])

# la fonction principale, qui fait appel aux autres fonctions
def completionWord (sortedDictio):
    pre=""
    c = ""
    redDictio = sortedDictio
    while c!= " ":
        c=input("Entrez le prochain caractère : ").lower()
        if c=="":
            return (True, pre)
        elif c.isdigit():
            keys = list(redDictio.keys())
            pre=(keys[int(c)-1])        # si l'utilisateur tape le numéro du mot prédit
        else:
            pre += c
            redDictio=reduceDictio (redDictio, pre)
            printCompletion(redDictio)
        print(pre)
    return (False, pre)

#------------------------
# PARTIE C : prédiction des mots jusqu'à la fin du message

# ajouter une occurence au mot saisie dans le dictionnaire 
def addOcc (sortedDictio, pre):
    if pre.rstrip() in sortedDictio:
        sortedDictio[pre.rstrip()]+=1
    else:
        sortedDictio[pre]=1

# la fonction principale
def completionAllMess (sortedDictio):
    fin=False
    msg=""
    while not fin : 
        fin, pre = completionWord(sortedDictio)
        msg+=pre
        print(msg)
        addOcc(sortedDictio, pre)
        sortedDictio=sortedVocab(sortedDictio)


#------------------------
# PARTIE TEST
vocabTest = ["a", "alphabet", "absolu", "ardoise", "arrêter", "ardoise", "andouille", "arrêter","a", "absolu", "ardoise", "andouille", "arrêter","a", "absolu", "ardoise", "andouille", "arrêter","a", "alphabet", "arracher", "absolu", "ardoise", "andouille", "arrêter","a", "arbre", "alphabet", "arracher", "absolu", "ardoise", "andouille", "arrêter","a", "arbre", "alphabet", "arracher", "absolu", "andouille", "arrêter","a",  "alphabet", "arracher", "absolu", "ardoise", "andouille", "arrêter", "a","arrêter","arrêter","arrêter","arrêter","arrêter", "le", "la", "mange"]
dictTest = vocab2dict(vocabTest)
sortedDictTest = sortedVocab(dictTest)

completionAllMess(sortedDictTest)