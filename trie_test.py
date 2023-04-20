# %% 
# création des neuds du trie
class TrieNode:
    #cette classe initalise un noeud du trie

    def __init__(self, char) -> None:
        self.children = {}
        self.endOfWord = False
        self.char = char
        self.count = 0



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
        # la fonction cherche tous les mots commencants avec ce préfixe

       if node.endOfWord:
           self.output[(pre + node.char)] = node.count # si le préfixe est un mot, il sera ajouté au dictionnaire avec le nombre d'occurences
        
        # si le préfixe n'est pas un mot, on descends dans l'arbre pour chercher la fin du mot
       for child in node.children.values():
           self.dfs(child, pre + node.char)

    
    def search(self, prefix: str):
        cur = self.root
        
        # vérifie sie le préfixe existe
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c] 
            else:
                return {}
            
        self.output = {}

        # cette fonction cherche tous les mots qui commencent avec ce préfixe et les ajoute à self.output
        self.dfs(cur, prefix[:-1])

        return self.output
    

    def startsWith(self, prefix:str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
    