class Solution {
    vector<int> sol;
    vector<int> temp;
    int num_tickets;
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string,int> city_id_map;
        vector<string> city_vec;
        num_tickets=tickets.size();
        for(int i=0;i<tickets.size();i++){
            if (city_id_map[tickets[i][0]]==0){
                city_id_map[tickets[i][0]]=1;
                city_vec.push_back(tickets[i][0]);
            }
            if (city_id_map[tickets[i][1]]==0){
                city_id_map[tickets[i][1]]=1;
                city_vec.push_back(tickets[i][1]);
            }
        }
        sort(city_vec.begin(),city_vec.end());
        for(int i=0;i<city_vec.size();i++){
            city_id_map[city_vec[i]]=i;
        }
        int num_cities=city_vec.size();
        vector<vector<int>> adj(num_cities,vector<int>(num_cities,0));

        for(int i=0;i<tickets.size();i++){
            adj[city_id_map[tickets[i][0]]][city_id_map[tickets[i][1]]]+=1;
        }
        int jfk_id=0;
        for(auto &it:city_id_map){
            if (it.first=="JFK"){
                jfk_id=it.second;
                break;
            }
        }
        dfs(jfk_id,0,adj);
        vector<string> ret;
        for(int i=0;i<sol.size();i++){
            ret.push_back(city_vec[sol[i]]);
        }
        return ret;
    }

    void dfs(int node,int count,vector<vector<int>>&adj){
        if (sol.size()>0){
            return ;
        }
        temp.push_back(node);
        count+=1;
        if (count==num_tickets+1){
            sol=temp;
            temp.pop_back();
            return ;
        }

        for(int i=0;i<adj[node].size();i++){
            if (adj[node][i]>=1){
                adj[node][i]-=1;
                dfs(i,count,adj);
                adj[node][i]+=1;
            }
        }

        temp.pop_back();
    }
};
