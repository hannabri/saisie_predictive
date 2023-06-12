from deserialization import load
from contexte import *

trie = load("trie")
dictio= load("dictio_trigrammes")
    
def prediction ( user_input):
    if len(user_input)>0 and (user_input[-1],) in dictio :
            return dictio[(user_input[-1],)].wordsPred[:5]
    else:
        return []


def completion(user_input):
    pre = user_input
    while pre[-1] != " ":
        return trie.show_most_frequent_children(pre)

def updatePrediction(message):
    for i in range(1,len(message),1):
        contexte=[]
        for z in range (1, min(2,j),1):
                    contexte.insert(0,message[i-z])
                    if tuple(contexte) not in dict:
                        dict[tuple(contexte)]=Contexte(tuple(contexte))
                    dict[tuple(contexte)].add_word(message[i])
                    dict[tuple(contexte)].update_wordsPred()

def updateCompletion(message): 
    for word in message :
        trie.update_word_count(word)
        trie.update(word)
    

