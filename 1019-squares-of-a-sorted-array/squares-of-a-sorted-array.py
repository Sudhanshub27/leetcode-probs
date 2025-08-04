class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # n=[]  tc=nlogn because of sorting
        # for i in range(len(nums)):
        #     a=nums[i]**2
        #     n.append(a)
        # n.sort()
        # return n

        left=0
        right=len(nums)-1
        result=[]
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result.append(nums[left]**2)
                left+=1
            else:
                result.append(nums[right]**2)
                right-=1
        result.reverse()
        return result
        