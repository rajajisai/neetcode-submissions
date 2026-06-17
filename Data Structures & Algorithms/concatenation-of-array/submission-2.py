class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list_len=len(nums)
        for i in range(list_len):
            nums.append(nums[i]);
        
        return nums
        