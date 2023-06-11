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

from trie import *

trie = load("trie")

def completion(user_input):
    pre = user_input
    while pre[-1] != " ":
        trie.update_word_count(pre[:-1])
        return trie.show_most_frequent_children(pre)
    
def kkita(user_input):
    if user_input[-1] == " ":
        return prediction(3,user_input.slip())
    else :
        wordsList = user_input.split()
        return completion(wordsList[-1])

