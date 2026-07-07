class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        stack.append(0)

        for i,temp in enumerate(temperatures[1:],start=1):
            while(len(stack)>0 and temp>temperatures[stack[-1]]):
                result[stack[-1]]=i-stack[-1]
                stack.pop();
            
            stack.append(i)
        
        return result
        