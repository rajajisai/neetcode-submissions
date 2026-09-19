class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q=deque()
        q.append(0)
        if s[0]!='0':
            return False
        visited=set([0])
        while q:
            n=q.popleft()
            if (s[n]=='0'):
                l=n+minJump
                r=n+maxJump
                for i in range(l,min(r+1,len(s))):
                    if (s[i]=='0' and i not in visited):
                        if i==len(s)-1:
                            return True
                        q.append(i)
                        visited.add(i)
                    
            
        
        return False



        