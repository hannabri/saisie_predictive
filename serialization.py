import pickle
from data_preparation import *
from trie_test import *

with open("trie.pkl", "wb") as file:
    trie = Trie()
    pickle.dump(trie, file)
