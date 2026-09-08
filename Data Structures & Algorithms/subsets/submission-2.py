class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol=[]
        temp=[]
        def find(i:int,sol:[],temp:[],nums: List[int]) -> None:
            if (i==len(nums)):
                sol.append(temp.copy())
                return 
            
            find(i+1,sol,temp,nums)
            temp.append(nums[i])
            find(i+1,sol,temp,nums)
            temp.pop()
        
        find(0,sol,temp,nums)
        return sol


