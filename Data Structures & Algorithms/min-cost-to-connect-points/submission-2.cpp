class Solution {
public:
vector<int > parent;
    int minCostConnectPoints(vector<vector<int>>& points) {
        parent.resize(points.size());
        for(int i=0;i<points.size();i++){
            parent[i]=i;
        }
        vector<vector<int>> dist;
        for(int i=0;i<points.size();i++){
            for(int j=i+1;j<points.size();j++){
                dist.push_back({abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j});
            }
        }
        sort(dist.begin(),dist.end());
        int cost=0;
        int count=0;
        for(int i=0;i<dist.size();i++){
            int n1=dist[i][1];
            int n2=dist[i][2];
            int p1=findparent(n1);
            int p2=findparent(n2);

            if(p1!=p2){
                parent[p2]=p1;
                count+=1;
                cost+=dist[i][0];
                if (count==points.size()-1){
                    break;
                }
            }
        }
        return cost;
    }

    int findparent(int node){
        if (parent[node]==node){
            return node;
        }
        return findparent(parent[node]);
    }
};
