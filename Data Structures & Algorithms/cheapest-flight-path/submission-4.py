import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost=[float('inf')]*n

        adj={}
        for flight in flights:
            if flight[0] not in adj:
                adj[flight[0]]=[]
            adj[flight[0]].append([flight[1],flight[2]])
        
        cost[src]=0
        temp_cost=list(cost)
        q=deque()
        q.append(src)
        num=0
        while q and num<=k :
            temp=deque()
            while q:
                node=q.popleft()
                for nodes in adj.get(node,[]):
                    if (cost[node]+nodes[1]<temp_cost[nodes[0]]):
                        temp_cost[nodes[0]]=cost[node]+nodes[1]
                        temp.append(nodes[0])
                
            num+=1
            q=temp
            cost=list(temp_cost)
        
        return cost[dst] if cost[dst]!=float('inf') else -1


