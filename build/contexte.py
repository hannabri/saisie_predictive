"""
Nom du fichier : contexte.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : avril 2023
Description : classe représentant un contexte, 
    Attributs : 
    name (tuple) : le contexte écrit
    allWords (dict) : l'ensemble des mots suivants le contexte et leur nombre d'occurrences 
    wordsPred(list) : la liste des 10 mots les plus fréquents après le contexte
"""

class Contexte:
    def __init__(self, name, allWords=None, wordsPred=None, preWords=None):
        self.name = name
        self.allWords = allWords if allWords is not None else {}
        self.wordsPred = wordsPred if wordsPred is not None else []

    def add_word(self, word):
        if word in self.allWords:
            self.allWords[word] += 1
        else:
            self.allWords[word] = 1

    def update_wordsPred (self):
        top_values = sorted(self.allWords.values(), reverse=True)[:min(10, len(self.allWords))]
        top_keys = [k for k, v in self.allWords.items() if v in top_values]
        self.wordsPred = top_keys[:10]
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"{self.allWords}"