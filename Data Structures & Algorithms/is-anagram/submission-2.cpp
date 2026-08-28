class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> m;

        for(int i=0;i<s.size();i++){
            m[s[i]]++;
        }

        for(int i=0;i<t.size();i++){
            if (m.find(t[i])==m.end()){
                return false;
            }else{
                m[t[i]]--;
                if (m[t[i]]==0){
                    m.erase(t[i]);
                }
            }
        }
        return m.size()==0;
    }
};
