/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        
        vector<vector<int>> interv;
        for(auto & interval:intervals){
            interv.push_back({interval.start,interval.end});
        }
        sort(interv.begin(),interv.end());
        priority_queue<int,vector<int>,greater<int>> pq;
        int sol=0;
        for(auto & interval:interv){
     
            while(!pq.empty() && interval[0]>=pq.top()){
                pq.pop();
            }
            pq.push(interval[1]);
        
            sol=max(sol,(int)pq.size());
        }
        return sol;
    }
};
