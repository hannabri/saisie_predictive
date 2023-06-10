import pickle
from data_preparation import *
from trie import *
from trie import *
import json

#RUN this file to serialize 'tokens.pkl', 'tokens_test.pkl' and 'trie.pkl'
#pour utiliser le Trie dans project.py ou autre, faire : trie = serialization.deserialize_trie()

#pour charger les tokens faire : tokens = serialization.deserialize_corpus()

def serialize_corpus():
    list_tokens = tokenize_corpus()
    with open("tokens.pkl", "wb") as file:
        pickle.dump(list_tokens, file)

def serialize_test():
    list_tokens = tokenize_test()
    with open("tokens_test.pkl", "wb") as file:
        pickle.dump(list_tokens, file)


def deserialize_corpus():
    with open("tokens.pkl", "rb") as file:
        return pickle.load(file)
    
def deserialize_test():
    with open("tokens_test.pkl", "rb") as file:
        return pickle.load(file)

trie = Trie()

# ajouter des mots dans le trie
tokens = deserialize_corpus()

for list_tokens in tokens:
    for word in list_tokens:
        trie.insert(word)

def serialize(trie):
    # Initialiser une file d'attente avec le noeud racine
    queue = [trie.root]
    result = []

    while queue:
        node = queue.pop(0)
        # Ajouter le noeud actuel au résultat
        result.append({
            'char': node.char,
            'endOfWord': node.endOfWord,
            'count': node.count,
            'frequentChildren': node.frequentChildren,
            'children': list(node.children.keys())
        })

        # Ajouter les enfants à la file d'attente
        for child in node.children.values():
            queue.append(child)

    serialized_trie = json.dumps(result)

    # Écrire le Trie sérialisé dans un fichier
    with open('trie.json', "w") as file:
        file.write(serialized_trie)


def deserialize_trie():
    with open("trie.json", "r") as file:
        data = file.read()

    # Convertir la chaîne JSON en une liste
    data = json.loads(data)

    trie.root = TrieNode(data[0]['char'])
    trie.root.endOfWord = data[0]['endOfWord']
    trie.root.count = data[0]['count']
    trie.root.frequentChildren = data[0]['frequentChildren']

    queue = [(trie.root, data[0]['children'])]

    # On garde un index de l'élément courant dans data
    index = 1
    while queue:
        parent, children_names = queue.pop(0)

        while index < len(data) and data[index]['char'] in children_names:
            item = data[index]
            node = TrieNode(item['char'])
            node.endOfWord = item['endOfWord']
            node.count = item['count']
            node.frequentChildren = item['frequentChildren']
            parent.children[node.char] = node
            queue.append((node, item['children']))
            index += 1

    return trie.root

serialize(trie)
serialize_corpus()
serialize_test()