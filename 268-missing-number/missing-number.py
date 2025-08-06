class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n=len(nums) tc=O(N2)
        # for i in range(n+1):
        #     if i in nums:
        #         continue
        #     else:
        #         return i
        # better approach is to use formula
        n=len(nums)
        total_sum=n*(n+1)//2
        actual_sum=sum(nums)
        return total_sum-actual_sum

        