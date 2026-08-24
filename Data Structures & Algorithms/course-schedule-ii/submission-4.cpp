class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> degree(numCourses,0);
        for(auto &prereq: prerequisites){
            adj[prereq[1]].push_back(prereq[0]);
            degree[prereq[0]]++;
        }
        queue<int> q;
        
        for(int i=0;i<numCourses;i++){
            if (degree[i]==0){
                q.push(i);
            }
        }
        vector<int> sol;
        while(!q.empty()){
            int course=q.front();
            sol.push_back(course);
            q.pop();
            for(auto &c:adj[course]){
                
                degree[c]--;
                if (degree[c]==0){
                    q.push(c);
                }
            }
        }
        
        return sol.size()==numCourses?sol:vector<int>{};
    }
};
