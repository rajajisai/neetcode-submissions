class Solution:
    def validPalindrome(self, s: str) -> bool:
        def canRemove(s:str,l:int,r:int,remove:bool)->bool:
            if (l>=r):
                return True
            
            if s[l]!=s[r]:
                if remove:
                    return canRemove(s,l+1,r,False) or canRemove(s,l,r-1,False)
                else:
                    return False
                
            return canRemove(s,l+1,r-1,remove)
        
        return canRemove(s,0,len(s)-1,True)
        