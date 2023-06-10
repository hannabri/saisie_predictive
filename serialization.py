import pickle
from data_preparation import *
import trie
import sys
from project import initDictio

sys.setrecursionlimit(10000)

def serialize_corpus():
    corpus = tokenize_corpus()
    with open("corpus.pkl", "wb") as file:
        pickle.dump(corpus, file)

def serialize_test():
    test = tokenize_test()
    with open("test.pkl", "wb") as file:
        pickle.dump(test, file)

def deserialize_corpus():
    with open("corpus.pkl", "rb") as file:
        return pickle.load(file)
    
def deserialize_test():
    with open("test.pkl", "rb") as file:
        return pickle.load(file)

dictio3 = initDictio(3)

def serialize_dict3():
    with open("dictio_trigrammes.pkl", "wb") as file:
        pickle.dump(dictio3, file)

def deserialize_dictio3():
    with open("dictio_trigrammes.pkl", "rb") as file:
        return pickle.load(file)

trie = trie.Trie()
def serialize_trie():
    # ajouter des mots dans le trie
    corpus = deserialize_corpus()

    for listTokens in corpus:
        for token in listTokens:
            trie.insert(token)

    with open ("trie.pkl", "wb") as file: 
        pickle.dump(trie, file)

def deserialize_trie():
    with open ("trie.pkl", "rb") as file:
        return pickle.load(file)

serialize_corpus()
serialize_test()
serialize_trie()
serialize_dict3()
