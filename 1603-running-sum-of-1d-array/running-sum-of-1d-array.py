class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        add=0
        result=[]
        for i in range(1,len(nums)):
            add=add+nums[i-1]
            result.append(add)
        result.append(sum(nums))
        return result
        