class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N=len(stoneValue)
        dp={}
        def rec(alice:bool,i:int)->int:
            if i==N:
                return 0
            
            if (alice,i) in dp:
                return dp[(alice,i)]
            if alice:
                dp[(alice,i)]=float('-inf')
            else:
                dp[(alice,i)]=float('inf')
            running_score=0
            for j in range(i,min(i+3,N)):
                if alice:
                    running_score+=stoneValue[j]
                    dp[(alice,i)]=max(dp[(alice,i)],running_score+rec(not alice,j+1))
                else:
                    dp[(alice,i)]=min(dp[(alice,i)],rec(not alice,j+1))

            return dp[(alice,i)]

        alice=True
        alice_score=rec(alice,0)
        total_score=sum(stoneValue)
        bob_score=total_score-alice_score

        if alice_score>bob_score:
            return "Alice"
        
        if bob_score>alice_score:
            return "Bob"
        
        return "Tie"
        