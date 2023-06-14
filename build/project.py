from build.contexte import *

def prediction (user_input, dictio):
    if len(user_input)>0 and (user_input[-1],) in dictio :
            return dictio[(user_input[-1],)].wordsPred[:5]
    else:
        return []

def completion(wordsList, trie):
    pre = wordsList
    while pre[-1] != " ":
        return trie.show_most_frequent_children(pre)

def updatePrediction(message, dictio):
    for i in range(1,len(message),1):
        contexte=[]
        for z in range (1, min(2,i),1):
                    contexte.insert(0,message[i-z])
                    if tuple(contexte) not in dictio:
                        dictio[tuple(contexte)]=Contexte(tuple(contexte))
                    dictio[tuple(contexte)].add_word(message[i])
                    dictio[tuple(contexte)].update_wordsPred()
                    #print(dictio[tuple(contexte)].allWords)

def updateCompletion(message,trie): 
    for word in message :
        trie.update_word_count(word)
        trie.update(word)