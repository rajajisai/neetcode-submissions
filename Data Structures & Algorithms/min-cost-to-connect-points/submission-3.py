class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        adj={i:[] for i in range(N)}
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        


        minH=[[0,0]]
        visited=set()
        total_cost=0
        while len(visited)<N:
            cost,i=heapq.heappop(minH)
            if i in visited:
                continue
            visited.add(i)
            total_cost+=cost

            for cost_j,j in adj[i]:
                if j not in visited:
                    heapq.heappush(minH,[cost_j,j])
            
        
        return total_cost


        


        