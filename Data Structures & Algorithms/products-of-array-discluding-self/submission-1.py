class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        for num in nums[:-1]:
            prefix.append(num*prefix[-1])
        
        for num in reversed(nums[1:]):
            suffix.append(num*suffix[-1])

        suffix.reverse()

        sol=[]

        for (s,p) in zip(suffix,prefix):
            sol.append(s*p)

        return sol
        