class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=1000000000
        def calculateHours(rate:int)->bool:
            cost=0
            for pile in piles:
                cost+=pile//rate
                if (pile%rate!=0):
                    cost+=1
            
            return cost<=h

        
        while(l<r):
            mid = (l+r)//2
            if (calculateHours(mid)):
                r=mid
            else:
                l=mid+1
        
        return l
            
                    
