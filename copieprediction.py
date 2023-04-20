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
    listTokens = #acompleter
    d ={}
    init_dictio(listTokens, d)
    return d

dictio={}
listTokens = ["<debut>", "le", "chat", "court", "dans", "le", "jardin", "et", "le", "chien", "dans", "le", "salon", "le", "chien", "mange", "le", "gateau"]
init_dictio(listTokens, dictio)
ajout_listTokens=["<debut>", "la", "chanteuse", "est", "dans", "le", "jardin"]
init_dictio(ajout_listTokens, dictio)

print(dictio["la"]["wordsPred"])
# PB : met à jour les mots que j'ai jamais utilisé : est ce que c'est important ? 
