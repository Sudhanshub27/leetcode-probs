class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        hash_map=set()
        n=len(s)
        for r in range(n):
            while s[r] in hash_map:  
                hash_map.remove(s[l])
                l+=1
            w=(r-l)+1
            longest=max(longest,w)
            hash_map.add(s[r])
        return longest


        