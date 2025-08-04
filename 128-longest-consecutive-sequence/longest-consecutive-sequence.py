class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=list(set(nums))
        n.sort()
        count=1
        max_count=1
        length=len(n)
        if length==0:
            return 0
        for i in range(length-1):
            if n[i+1]==n[i]+1:
                count+=1
            else:
                count=1
            max_count=max(max_count,count)
        return max_count




        