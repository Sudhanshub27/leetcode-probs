class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result=[]
        i=0
        n=len(needle)
        m=len(haystack)
        while i<=m:
            result.append(haystack[i:i+n])
            i+=1
        for i in range(len(result)):
            if result[i]==needle:
                return i
        return -1