class PrefixTree:
    root=None
    isWord=None
    def __init__(self):
        self.root=[None]*26
        self.isWord=False

    def insert(self, word: str) -> None:
        curr=self
        for w in word:
            if (curr.root[ord(w)-ord('a')] is None):
                curr.root[ord(w)-ord('a')]=PrefixTree()
            curr=curr.root[ord(w)-ord('a')]
            
        curr.isWord=True



    def search(self, word: str) -> bool:
        curr=self
        for w in word:
            if (curr.root[ord(w)-ord('a')]):
                curr=curr.root[ord(w)-ord('a')]
            else:
                return False
        
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr=self
        for w in prefix:
            if (curr.root[ord(w)-ord('a')]):
                curr=curr.root[ord(w)-ord('a')]
            else:
                return False
        
        return True
        
        