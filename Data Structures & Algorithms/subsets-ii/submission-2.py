class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol=[]
        temp=[]
        def dfs(i:int,sol:[],temp:[]):

            if (i==len(nums)):
                sol.append(temp.copy())
                return
            
            j=i

            while(j<len(nums) and nums[i]==nums[j]):
                j+=1

            for k in range(i,j):
                temp.append(nums[i])
                dfs(j,sol,temp)
            
            for k in range(i,j):
                temp.pop()
            dfs(j,sol,temp)
            return

        dfs(0,sol,temp)
        return sol

            

            