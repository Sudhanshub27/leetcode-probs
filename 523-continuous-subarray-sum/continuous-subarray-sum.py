class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr_sum = 0
        prefixsums = {}

        for i, n in enumerate(nums):
            curr_sum += n
            r = curr_sum if k == 0 else curr_sum % k

            if r == 0 and i > 0:
                return True

            if r in prefixsums:
                if i - prefixsums[r] >= 2:
                    return True
            else:
                prefixsums[r] = i

        return False