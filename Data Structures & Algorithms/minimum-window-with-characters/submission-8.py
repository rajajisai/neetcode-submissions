class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t={}
        for c in t:
            dict_t[c]=dict_t.get(c,0)+1
        
        cp=dict_t.copy()
        dict_s={}
        i=0
        for c in s:
            dict_s[c]=dict_s.get(c,0)+1
            i+=1
            if c in dict_t:
                dict_t[c]-=1
                if dict_t[c]==0:
                    del dict_t[c]

                if (len(dict_t)==0):
                    break

        if (len(dict_t)!=0):
            return ""
        dict_t=cp
        l=0
        while(True):
            if (s[l] not in dict_t):
                l+=1

            else:
                if (dict_s[s[l]]==dict_t[s[l]]):
                    break
                else:
                    dict_s[s[l]]-=1
                    l+=1
        
        r=i
        length=r-l
        sol=s[l:r]

        while(r<len(s)):
            dict_s[s[r]]=dict_s.get(s[r],0)+1
            r+=1
            while(True):
                if (s[l] not in dict_t):
                    dict_s[s[l]]-=1
                    l+=1

                else:
                    if (dict_s[s[l]]==dict_t[s[l]]):
                        break
                    else:
                        dict_s[s[l]]-=1
                        l+=1
            
            if (r-l)<len(sol):
                sol=s[l:r]
            
        
        return sol
        
        


            

        

        



        