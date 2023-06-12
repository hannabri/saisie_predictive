import pickle
from data_preparation import *
from trie import Trie
import sys
from deserialization import load
from dictio_prediction import *

sys.setrecursionlimit(10000)

def serialize_corpus():
    corpus = tokenize_corpus()
    with open("corpus.pkl", "wb") as file:
        pickle.dump(corpus, file)

def serialize_test():
    test = tokenize_test()
    with open("test.pkl", "wb") as file:
        pickle.dump(test, file)

def serialize_dict3():
    dictio3 = initDictio(3)
    with open("dictio_trigrammes.pkl", "wb") as file:
        pickle.dump(dictio3, file)


trie = Trie()
def serialize_trie():
    # ajouter des mots dans le trie
    corpus = load("corpus")
    for listTokens in corpus:
        for token in listTokens:
            trie.insert(token)
    with open ("trie.pkl", "wb") as file: 
        pickle.dump(trie, file)

