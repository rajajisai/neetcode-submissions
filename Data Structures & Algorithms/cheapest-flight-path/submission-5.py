class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost=[float('inf')]*n
        cost[src]=0
        temp_cost=cost.copy()

        for i in range(k+1):
            for s,d,p in flights:
                if cost[s]==float('inf'):
                    continue
                
                if cost[s]+p<temp_cost[d]:
                    temp_cost[d]=cost[s]+p
            
            cost=temp_cost.copy()
        
        return -1 if cost[dst]==float('inf') else cost[dst]

        