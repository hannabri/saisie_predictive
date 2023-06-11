from deserialization import load

# initialisation du dictionnaire
dictio= load("dictio_trigrammes")

def prediction (nbWords, user_input):
    if len(user_input)>1 and (user_input[-2],user_input[-1]) in dictio :
        return dictio[(user_input[-2],user_input[-1])].wordsPred[:nbWords]
    elif len(user_input)>0 and (user_input[-1],) in dictio :
        return dictio[(user_input[-1]),].wordsPred[:nbWords]
    else:
        return []

def prediction (nbWords, user_input):
    if (nbWords==1) or (nbWords==2):
        return structurePred(nbWords, dictio,predTri, user_input)
    else:
<<<<<<< HEAD
        return structurePred(nbWords, dictio,predBi, user_input)
=======
        return []
    
def predictionTest (message, nbWords, d):
    if len(message)<=2 or nbWords>2:
        contexte = tuple(message[-1],)
        if contexte in d :
            return d[contexte)].wordsPred[:nbWords]
    else:
        contexte = tuple(message[-2], message[-1])
        if contexte in d :
            return d[contexte)].wordsPred[:nbWords]
        
>>>>>>> 1ceabee3da57afc734c4113dd31be8c47d9acee4

from trie import *

trie = load("trie")

def completion(user_input):
    pre = user_input
    while pre[-1] != " ":
        trie.update_word_count(pre[:-1])
        return trie.show_most_frequent_children(pre)
