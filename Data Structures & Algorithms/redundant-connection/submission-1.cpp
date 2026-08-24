class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int> degree(edges.size() + 1, 0);
        vector<vector<int>> adj(edges.size() + 1);
        queue<int> q;
        
        // 1. Build the undirected graph correctly
        for(auto & edge : edges){
            degree[edge[0]]++;
            degree[edge[1]]++;
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]); // Undirected!
        }
        
        // 2. Add all leaves to the queue
        for(int i = 1; i < degree.size(); i++){ // Nodes are 1-indexed (1 to n)
            if (degree[i] == 1){
                q.push(i);
            }
        }
        
        // 3. Process the queue (Standard Kahn's algorithm structure)
        while(!q.empty()){
            int n = q.front();
            q.pop();
            degree[n]--; // Remove the leaf
            
            // Iterate through all neighbors
            for(int neighbor : adj[n]) {
                // If the neighbor hasn't been removed yet

                    degree[neighbor]--;
                    if (degree[neighbor] == 1){
                        q.push(neighbor);
                    }

            }
        }
        
        // 4. Find the last edge in the input that connects two nodes still in the cycle
        vector<int> sol;
        for(int i = edges.size() - 1; i >= 0; i--){
            if (degree[edges[i][0]] > 0 && degree[edges[i][1]] > 0){
                sol = {edges[i][0], edges[i][1]};
                break;
            }
        }
        return sol;
    }
};