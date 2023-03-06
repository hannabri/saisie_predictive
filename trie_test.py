# %% 
# création des neuds du trie
class TrieNode:
    def __init__(self, char) -> None:
        self.children = {}
        self.endOfWord = False
        self.char = char
        self.count = 0

    def increment_count(self):
        self.count += 1

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def insert(self, word: str, count) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.endOfWord = True

        if cur.endOfWord:
            cur.count = count


    def dfs(self, node, pre):
 
       if node.endOfWord:
           self.output[(pre + node.char)] = node.count
        
       for child in node.children.values():
           self.dfs(child, pre + node.char)
    
    def search(self, prefix: str):
        cur = self.root
        
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
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

# initiate new Trie

prediction = Trie()

# add words in our trie

words = {"potatoe" : 3, "pizza" : 4, "pancake" : 1, "biscuit" : 5, "radio" : 2, "tasse" : 4}

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

    