class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0],-x[1]))
        high=intervals[0][1]
        count=0
        for interval in intervals[1:]:
            if (interval[0]<high):
                count+=1
                high=min(high,interval[1])
            else:
                high=interval[1]
        
        return count
