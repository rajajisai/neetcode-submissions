class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr_interval=intervals[0]
        sol=[]
        for interval in intervals[1:]:
            if interval[0]<=curr_interval[1]:
                curr_interval[0]=min(curr_interval[0],interval[0])
                curr_interval[1]=max(curr_interval[1],interval[1])
            
            else:
                sol.append(curr_interval)
                curr_interval=interval
        
        sol.append(curr_interval)
        return sol

        