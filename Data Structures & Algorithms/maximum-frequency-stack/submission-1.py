class FreqStack:

    def __init__(self):
        self.cnt={}
        self.stacks=[[]]
        

    def push(self, val: int) -> None:
        if (val not in self.cnt):
            self.cnt[val]=1
        else:
            self.cnt[val]+=1

        if self.cnt[val]==len(self.stacks):
            self.stacks.append([])
        
        self.stacks[self.cnt[val]].append(val)
        
        

    def pop(self) -> int:
        print(len(self.stacks))
        res=self.stacks[-1][-1]
        self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        self.cnt[res]-=1
        if (self.cnt[res]==0):
            del self.cnt[res]
        
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()