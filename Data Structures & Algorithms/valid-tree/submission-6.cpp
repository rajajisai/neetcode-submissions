class Solution {
public:
    bool cycle=false;
    vector<int> visited;
    bool validTree(int n, vector<vector<int>>& edges) {

        vector<vector<int>> adj(n);
        visited.resize(n,false);
        if (edges.size()>n-1 || edges.size()<n-1 ){
            return false;
        }

        for(auto &edge: edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        dfs(0,0,adj);
        if (cycle){
            return false;
        }
        int sum=accumulate(visited.begin(),visited.end(),0);
        return n==sum;
    }
    void dfs(int n,int parent,vector<vector<int>> &adj){
            if (cycle){
                return ;
            }
            if (visited[n]){
                cycle=true;
                return ;
            }
            visited[n]=true;

            for(auto & node:adj[n]){
                if (parent!=node){
                    dfs(node,n,adj);
                }
            }
    }
};
