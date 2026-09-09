class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for str_ in strs:
            key=''.join(sorted(str_))
            if key not in dic:
                dic[key]=[]
            
            dic[key].append(str_)
        
        sol=[]
        for str_list in dic.values():
            sol.append(str_list)
        
        return sol
                

        