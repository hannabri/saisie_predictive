#%%
# The best project !!!

print("Le meileur trio :)")

#test de clara : est-ce que les modifications se font en temps r´éel ?
# Part 1 : Complétion 

from trie_test import *
from tokenizer_cleaner import *

# initiate new Trie

prediction = Trie()

# add words in our trie

vocab = tokenize()


def vocab2dict (vocab):
    vocab_sans_doublon = list(set(vocab))
    dict = {w : vocab.count(w) for w in vocab_sans_doublon}
    return dict

words = vocab2dict(vocab)


for word in words.keys():
    prediction.insert(word, words[word])

# complétion du mot: 

def completion():
    
    pre = input()
    while pre != " ":

        # trier le dicitonnaire et l'afficher s'il n'est pas vide 

        sort = dict(sorted(prediction.search(pre).items(), key = lambda x: x[1], reverse = True)[:3])

        if sort == {}:
            return None
        else:
            print(sort)
        
        # ajouter la prochaine lettre à notre préfix
        pre = pre + input()

completion()


# Part 2 : Prédiction
