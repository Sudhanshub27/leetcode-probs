class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result=0
        curr_sum=0
        prefixsums={0:1}
        for n in nums:
            curr_sum+=n
            diff=curr_sum-k
            result+=prefixsums.get(diff,0)
            prefixsums[curr_sum]=1+prefixsums.get(curr_sum,0)
        return result        