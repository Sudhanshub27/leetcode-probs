class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=[]
        for i in range(len(nums)):
            a=nums[i]**2
            n.append(a)
        n.sort()
        return n
        