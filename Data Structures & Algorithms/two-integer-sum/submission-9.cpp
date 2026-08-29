class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> n;
        for (int i = 0; i < nums.size(); i++) {
            n.push_back({nums[i], i});
        }
        sort(n.begin(),n.end());
        int l=0,r=n.size()-1;
        vector<int> sol;
         while(l<r){
            int sum=n[l].first+n[r].first;
            if (sum==target){
                sol={n[l].second,n[r].second};
                break;
            }else if (sum<target){
                l++;
            }else{
                r--;
            }
        }
        sort(sol.begin(),sol.end());
        return sol;
    }
};
