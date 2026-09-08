class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol=[]
        cl=0
        cr=0
        temp=[]
        def generate(cl:int,cr:int,sol:[],temp:[]):
            if (cl==n):
                for i in range(cr,n):
                    temp.append(")")
                sol.append("".join(temp))
                for i in range(cr,n):
                    temp.pop()
                return 

            if (cl>cr):
                temp.append(")")
                generate(cl,cr+1,sol,temp)
                temp.pop()
            
            temp.append("(")
            generate(cl+1,cr,sol,temp)
            temp.pop()
        

        generate(cl,cr,sol,temp)
        return sol