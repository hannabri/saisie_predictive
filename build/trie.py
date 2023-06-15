"""
Nom du fichier : trie.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier définit la classe trie pour la complétion
"""

# création des neuds du trie
class TrieNode:
    def __init__(self, char) -> None:
        self.children = {}
        self.frequentChildren = []
        self.endOfWord = False
        self.char = char
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.endOfWord = True

        if cur.endOfWord:
            cur.count += 1

    def dfs_search(self, node, pre):
        if node.endOfWord:
            self.output[pre + node.char] = node.count

        for child in node.children.values():
            self.dfs_search(child, pre + node.char)

    def stock(self, prefix):
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]

        self.output = {}
        self.dfs_search(cur, prefix[:-1])

        sort = dict(sorted(self.output.items(), key=lambda x: x[1], reverse=True)[:10])

        cur.frequentChildren = list(sort.keys())

    def show_most_frequent_children(self, pre):
        cur = self.root

        for c in pre:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return []

        if not cur.frequentChildren:
            self.stock(pre)

        return cur.frequentChildren[:5]

    def update_word_count(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]

        cur.endOfWord = True
        cur.count += 1

    def update(self, word):
        cur = self.root

        for c in word:
            cur = cur.children[c]
            cur.frequentChildren = []
            