class Solution {
public:
    vector<bool> visited;
    int countComponents(int n, vector<vector<int>>& edges) {
        int count=0;
        visited.resize(n,false);
        vector<vector<int>> adj(n);
        for(auto edges:edges){
            adj[edges[0]].push_back(edges[1]);
            adj[edges[1]].push_back(edges[0]);
        }
        for(int i=0;i<n;i++){
            if (!visited[i]){
                dfs(i,adj);
                count++;
            }
        }
        return count;
    }
    void dfs(int n,vector<vector<int>> &adj){
        visited[n]=true;

        for(auto adj_n: adj[n]){
            if (!visited[adj_n]){
                dfs(adj_n,adj);
            }
        }
    }
};
