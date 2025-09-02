class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result=s.split(" ")
        n=len(result)-1
        while True:
            if len(result[n])!=0:
                return len(result[n])
            n=n-1
        