class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        s=nums[0]
        for i in range(n-1):
            s+=nums[i+1]
            if s%2==0:
                return False
            else:
                s=nums[i+1]
        return True



        