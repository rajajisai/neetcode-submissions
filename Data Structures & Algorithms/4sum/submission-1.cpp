class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> sol;
        for(int i=0;i<nums.size();i++){
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for(int j=i+1;j<nums.size()-2;j++){
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                long long  target_=(long long )target-nums[i]-nums[j];
                int l=j+1;
                int r=nums.size()-1;
                if( nums[l]>0 && target_<0 ){
                    continue;
                }
                while(l<r){
                    int sum=nums[l]+nums[r];
                    if (sum==target_){
                        sol.push_back({nums[i],nums[j],nums[l],nums[r]});
                        do{
                            l++;
                        }while(nums[l]==nums[l-1]);
                        do{
                        r--;
                        }while(nums[r]==nums[r+1]);
                    }else if (sum<target_){
                        do{
                            l++;
                        }while(nums[l]==nums[l-1]);
                    }else {
                        do{
                        r--;
                        }while(nums[r]==nums[r+1]);
                    }
                }
            }
        }
        return sol;
    }
};