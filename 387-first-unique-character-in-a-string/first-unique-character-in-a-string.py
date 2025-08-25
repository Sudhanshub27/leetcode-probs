class Solution:
    def firstUniqChar(self, s: str) -> int:
        map={}
        list_s=list(s)
        for i in range(len(list_s)):
            if list_s[i] in map:
                map[list_s[i]]+=1
            else:
                map[list_s[i]]=1
        for key,val in map.items():
            if val==1:
                return s.index(key)
            
        return -1
        
          