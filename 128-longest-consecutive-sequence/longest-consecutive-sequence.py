class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # n=list(set(nums))  tc=nlogn because of sorting
        # n.sort()
        # count=1
        # max_count=1
        # length=len(n)
        # if length==0:
        #     return 0
        # for i in range(length-1):
        #     if n[i+1]==n[i]+1:
        #         count+=1
        #     else:
        #         count=1
        #     max_count=max(max_count,count)
        # return max_count
        number=set(nums)
        longest=0
        for n in number:
            if (n-1) not in number:
                length=0
                while (n+length) in number:
                    length+=1
                longest=max(length,longest)
        return longest

        




        