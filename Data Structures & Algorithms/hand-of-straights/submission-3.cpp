class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {

        map<int, int> count;
        for (int num : hand) count[num]++;

        auto it =count.begin();
        while(count.size()>0){
            it=count.begin();
            int start = count.begin()->first;
            int startCnt = count.begin()->second;
            for (int i = start; i < start + groupSize; i++) {
                if (count.find(i)==count.end() || count[i]<startCnt){
                    return false;
                }
                count[i]=count[i]-startCnt;
                if (count[i]==0){
                    count.erase(i);
                }
            }
        }

        return true;
        
    }
};