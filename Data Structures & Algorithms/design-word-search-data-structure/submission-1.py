class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr=curr.children[w]
        
        curr.word=True

    def search(self, word: str) -> bool:
        def dfs(j,root,word):
            if (j==len(word)):
                return root.word
            if (not root):
                return False

            if (word[j]!='.'):
                if word[j] in root.children:
                    return dfs(j+1,root.children[word[j]],word)
            else:
                ret=False
                for child in root.children.values():
                    ret=ret or dfs(j+1,child,word)
                return ret
            return False
        
        return dfs(0,self.root,word)



