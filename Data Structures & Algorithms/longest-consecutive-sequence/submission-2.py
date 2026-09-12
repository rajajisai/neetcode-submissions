class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count=1
        curr=nums[0]
        sol=0
        for num in nums[1:]:
            if num==curr+1:
                curr+=1
                count+=1

            elif num>curr:
                sol=max(sol,count)
                curr=num
                count=1
        
        sol=max(sol,count)
        
        return sol

        