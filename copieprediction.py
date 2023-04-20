def completer_dictio (corpus, dictio): # corpus = liste de string
    for i in range(1,len(corpus),1):
        if (corpus[i-1]) in dictio and corpus[i] in dictio[corpus[i-1]]:
            dictio[corpus[i-1]][corpus[i]]+=1
        else:
            if corpus[i-1] not in dictio : 
                dictio[corpus[i-1]]={}
            dictio[corpus[i-1]][corpus[i]]=1


def dictio_3_mots (dictio):
    dictio_3_mots={}
    for key in dictio.keys() :
        dictio_3_mots = {key: [x[0] for x in sorted(dictio[key].items(), key=lambda x: x[1], reverse=True)[:min(3, len(dictio[key]))]] for key in dictio.keys()}
    return dictio_3_mots

def prediction_mot (mot, dictio_3_mots):
    print(f"prediction de \"{mot}\" : ")
    if mot in dictio_3_mots : 
        [print(f" {i+1} : {dictio_3_mots[mot][i]}") for i in range(len(dictio_3_mots[mot]))]


dictio={}
corpus = ["<debut>", "le", "chat", "court", "dans", "le", "jardin", "et", "le", "chien", "dans", "le", "salon", "le", "chien", "mange", "le", "gateau"]
completer_dictio(corpus, dictio)
ajout_corpus=["<debut>", "la", "chanteuse", "est", "dans", "le", "jardin"]
completer_dictio(ajout_corpus, dictio)
print(dictio)

dictio_3_mots = dictio_3_mots(dictio)

prediction_mot("le", dictio_3_mots)
prediction_mot("chien", dictio_3_mots)
prediction_mot("carotte", dictio_3_mots)

def init_dictio (listTokens, dictio): # listTokens = liste de string
    for i in range(1,len(listTokens),1):
        if (listTokens[i-1]) in dictio and listTokens[i] in dictio[listTokens[i-1]]:
            dictio[listTokens[i-1]]["allWords"][listTokens[i]]+=1
        else:
            if listTokens[i-1] not in dictio : 
                dictio[listTokens[i-1]]={}
                dictio[listTokens[i-1]]["allWords"]={}
            dictio[listTokens[i-1]]["allWords"][listTokens[i]]=1
    addWordsPred(dictio)

def addWordsPred (dictio):
    for key in dictio.keys() :
        top_values = sorted(dictio[key]["allWords"].values(), reverse=True)[:min(3, len(dictio[key]["allWords"]))]
        top_keys = [k for k, v in dictio[key]["allWords"].items() if v in top_values]
        dictio[key]["wordsPred"] = top_keys[:3]

def prediction ():
    #listTokens #acompleter
    d ={}
    init_dictio(listTokens, d)
    return d

dictio={}
listTokens = ["<debut>", "le", "chat", "court", "dans", "le", "jardin", "et", "le", "chien", "dans", "le", "salon", "le", "chien", "mange", "le", "gateau"]
init_dictio(listTokens, dictio)
ajout_listTokens=["<debut>", "la", "chanteuse", "est", "dans", "la", "jardine"]
init_dictio(ajout_listTokens, dictio)

print(dictio["le"]["wordsPred"])
# PB : met à jour les mots que j'ai jamais utilisé : est ce que c'est important ? OUI
