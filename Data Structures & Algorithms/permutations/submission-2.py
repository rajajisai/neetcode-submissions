class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        count=0
        sol=[]
        temp=[]
        flag=[False]*len(nums)
        def dfs(count:int ,sol:[],temp:[],flag:[]):
            if (count==len(nums)):
                sol.append(temp.copy())
                return 
            
            for i in range(len(nums)):
                if (flag[i]==False):
                    flag[i]=True
                    temp.append(nums[i])
                    dfs(count+1,sol,temp,flag)
                    temp.pop()
                    flag[i]=False
        
        dfs(count,sol,temp,flag)
        return sol
        