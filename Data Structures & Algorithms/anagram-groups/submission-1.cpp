class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> m;

        for(auto &str:strs){
            string t=str;
            sort(t.begin(),t.end());
            m[t].push_back(str);
        }
        vector<vector<string>> sol;
        for(auto &it: m){
            sol.push_back(vector<string>{});
            for(auto &str:it.second){
                sol[sol.size()-1].push_back(str);
            }
        }
        return sol;
    }
};
