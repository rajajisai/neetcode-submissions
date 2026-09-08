class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sum=0
        sol=[]
        temp=[]
        def dfs(i:int,sol:[],temp:[],target:int,sum:int):
            if (sum==target):
                sol.append(temp.copy())
                return 

            if (i==len(candidates) or sum>target):
                return
            
            j=i
            while(j<len(candidates) and candidates[i]==candidates[j]):
                j+=1

            s=0

            for k in range(i,j):
                s+=candidates[k]
                temp.append(candidates[i])
                dfs(j,sol,temp,target,sum+s)
            
            for k in range(i,j):
                temp.pop()
            dfs(j,sol,temp,target,sum)
            return

        dfs(0,sol,temp,target,sum)
        return sol

            

            