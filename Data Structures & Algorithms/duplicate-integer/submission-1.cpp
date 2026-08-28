class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int curr=nums[0];
        for(int i=1;i<nums.size();i++){
            if (nums[i]==curr){
                return true;
            }
            curr=nums[i];
        }
        return false;
    }
};