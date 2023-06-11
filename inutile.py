# toutes les fonctions qui je crois sont inutiles mais dans le doute je veux pas faire de la merde
# fichier à evidemment supprimer en fin de projet

#vient du fichier : project_copie
def kkita(prediction,user_input):
    if user_input[-1] == " ":
        return prediction(3,user_input.slip())
    else :
        wordsList = user_input.split()
        return completion(wordsList[-1])
    

    
# PARTIE FONCTION PREDICTION  () vient du fichier project()
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

def update(dict,message):
    for i in range(1,len(message),1):
        contexte=[]
        for z in range (1, min(2,j),1):
                    contexte.insert(0,message[i-z])
                    if tuple(contexte) not in dict:
                        dict[tuple(contexte)]=Contexte(tuple(contexte))
                    dict[tuple(contexte)].add_word(message[i])
                    dict[tuple(contexte)].update_wordsPred()

def completion():
    
    pre = input()
    while pre[-1] != " ":

        #print(trie.show_most_frequent_children(pre))

        #print()
        
        # ajouter la prochaine lettre à notre préfix
        pre = pre + input()