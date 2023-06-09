# %% 
# création des neuds du trie
class TrieNode:
    #cette classe initalise un noeud du trie

    def __init__(self, char) -> None:
        self.children = {}
        self.frequentChildren = []
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
            cur = cur.children[c]    
        cur.endOfWord = True

        if cur.endOfWord:
            cur.count +=1

    def dfs_search(self, node, pre):
        if node.endOfWord:
            self.output[pre + node.char] = node.count

        for child in node.children.values():
            self.dfs_search(child, pre + node.char)

        
    def stock(self, prefix):
        cur = self.root

        # vérifier si le préfixe existe
        for c in prefix: 
            if c in cur.children:
                cur = cur.children[c]

        self.output = {}

        self.dfs_search(cur, prefix[:-1])

        # trier le dictionnaire obtenu pour avoir les trois mots avec le plus d'occurences

        sort = dict(sorted(self.output.items(), key = lambda x: x[1], reverse = True) [:10])
        
        # ajouter l'information dans le noeud : 
        
        cur.frequentChildren.extend(list(sort.keys()))

    def show_most_frequent_children(self, pre):
        
        cur = self.root

        for c in pre: 
            if c in cur.children:
                cur = cur.children[c]
            else:
                return []

        if cur.frequentChildren == []:
            self.stock(pre)

        return cur.frequentChildren

    def update_word_count(self, word):
        
        cur = self.root

        for c in word: 
            cur = cur.children[c]

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
        
        # vérifie si le préfixe existe
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
