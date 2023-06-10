#%%

import pickle
from data_preparation import *
from trie import *
from serialization import *
import sys


sys.setrecursionlimit(10000)

trie = Trie()


def pickle_trie():
    # ajouter des mots dans le trie
    tokens = deserialize_corpus()

    for list_tokens in tokens:
        for word in list_tokens:
            trie.insert(word)

    with open ("trie.pkl", "wb") as file: 
        pickle.dump(trie, file)

def depickle_trie():
    with open ("trie.pkl", "rb") as file:
        return pickle.load(file)
    
trie = depickle_trie()

def completion():
    
    pre = input()
    while pre[-1] != " ":

         #trier le dicitonnaire et l'afficher s'il n'est pas vide 

        print(trie.show_most_frequent_children(pre))

        print()
        
        # ajouter la prochaine lettre à notre préfix
        pre = pre + input()

    trie.update_word_count(pre[:-1])

completion()

