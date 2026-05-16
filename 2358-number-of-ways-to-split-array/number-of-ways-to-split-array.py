class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result=0
        total=sum(nums)
        curr_sum=0
        for i in range(len(nums)-1):
            curr_sum+=nums[i]
            diff=total-curr_sum
            if curr_sum>=diff:
                result+=1
        return result
