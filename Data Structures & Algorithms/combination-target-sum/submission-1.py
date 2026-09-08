class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp=[]
        sol=[]
        sum=0
        def rec(i:int,temp:[],sol:[],nums:List[int],target:int,sum:int):
            if (sum==target):
                sol.append(temp.copy())
                return 
            
            if (i==len(nums) or sum>target):
                return 
            
            sum=sum+nums[i]
            temp.append(nums[i])
            rec(i,temp,sol,nums,target,sum)
            sum=sum-nums[i]
            temp.pop()
            rec(i+1,temp,sol,nums,target,sum)

        rec(0,temp,sol,nums,target,sum)
        return sol
