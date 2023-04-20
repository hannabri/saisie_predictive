# %% 
# création des neuds du trie
class TrieNode:
    #cette classe initalise un noeud du trie

    def __init__(self, char) -> None:
        self.children = {}
        self.endOfWord = False
        self.char = char
        self.count = 0

    def increment_count(self):
        self.count += 1

class Trie:
    # cette classe initialise la structure du trie avec les noeuds du TrieNode

    def __init__(self) -> None:
        self.root = TrieNode("") # on initialise le trie avec la racine

    def insert(self, word: str) -> None:
        cur = self.root # le noeud courant est la racine

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c) # si notre noeud courant n'a pas d'enfant avec le caractère, on crée le noeud
            cur = cur.children[c] # s'il y a un enfant avec ce caractère, le noeud courant va être l'enfant avec ce caractère
        cur.endOfWord = True

        if cur.endOfWord:
            cur.count +=1

        


    def dfs(self, node, pre):
 
       if node.endOfWord:
           self.output[(pre + node.char)] = node.count
        
       for child in node.children.values():
           self.dfs(child, pre + node.char)

    
    def search(self, prefix: str):
        cur = self.root
        
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c] # si la lettre du préfixe existe dans le trie, le noeud courant change pour l'enfant avec le caractère
            else:
                return {}
            
        self.output = {}

        self.dfs(cur, prefix[:-1])

        return self.output
    

    def startsWith(self, prefix:str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
    