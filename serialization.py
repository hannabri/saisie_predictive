import pickle
from data_preparation import *
from trie_test import *
from trie_test import *

list_tokens = tokenize_corpus()
with open("tokens.pkl", "wb") as file:
    pickle.dump(list_tokens, file)

with open("tokens.pkl", "rb") as file:
    tokens = pickle.load(file)

trie = Trie()

for list_tokens in tokens:
    for word in list_tokens:
        trie.insert(word)

with open("trie.pkl", "wb") as file:
    pickle.dump(trie, file)

