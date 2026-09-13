class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost=[float('inf')]*(n+1)
        cost[k]=0
        temp_cost=cost.copy()
        for i in range(n):
            for u,v,t in times:
                if cost[u]==float('inf'):
                    continue
                elif cost[u]+t<temp_cost[v]:
                    temp_cost[v]=cost[u]+t
                
            cost=temp_cost.copy()
        sol=max(cost[1:])
        return -1 if sol==float('inf') else sol

        