class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        heap=[]
        curr=nums[0]
        freq=1
    
        for num in nums[1:]:
            if (num==curr):
                freq+=1
            else:
                if (len(heap)<k):
                    heapq.heappush(heap,(freq,curr))
                else:
                    if (freq>heap[0][0]):
                        heapq.heappop(heap)
                        heapq.heappush(heap,(freq,curr))
                curr=num
                freq=1
        
        if (len(heap)<k):
            heapq.heappush(heap,(freq,curr))
        else:
            if (freq>heap[0][0]):
                heapq.heappop(heap)
                heapq.heappush(heap,(freq,curr))
        sol=[]
        for e in heap:
            sol.append(e[1])
        
        return sol

        