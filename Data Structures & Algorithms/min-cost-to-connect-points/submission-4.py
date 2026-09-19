class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        parent=[i for i in range(N)]
        distances=[]
        for i in range(N):
            for j in range(i+1,N):
                distances.append([abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j])

        distances.sort()
        def findParent(n:node):
            if parent[n]==n:
                return n
            parent[n]=findParent(parent[n])
            return parent[n]

        count=0
        cost=0
        for d,i,j in distances:
            p1=findParent(i)
            p2=findParent(j)

            if (p1!=p2):
                parent[p2]=p1
                count+=1
                cost+=d
                if (count==N-1):
                    break
            
        
        return cost
            



        


        