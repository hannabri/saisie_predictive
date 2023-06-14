import pickle
from data_preparation import *
import trie as trie
import sys
from deserialization import load
from dictio_prediction import *

sys.setrecursionlimit(10000)

def serialize(object, file):
    with open(file, "wb") as file:
        pickle.dump(object,file)

def serialize_corpus():
    corpus = tokenize_corpus()
    with open("build/corpus.pkl", "wb") as file:
        pickle.dump(corpus, file)

def serialize_test():
    test = tokenize_test()
    with open("build/test.pkl", "wb") as file:
        pickle.dump(test, file)

def serialize_dict3():
    dictio3 = initDictio(3)
    with open("build/dictio_trigrammes.pkl", "wb") as file:
        pickle.dump(dictio3, file)

trie = trie.Trie()
def serialize_trie():
    # ajouter des mots dans le trie
    corpus = load("build/corpus.pkl")
    for listTokens in corpus:
        for token in listTokens:
            trie.insert(token)
    with open ("build/trie.pkl", "wb") as file: 
        pickle.dump(trie, file)

"""serialize_corpus()
serialize_test()
serialize_trie()
serialize_dict3()"""
