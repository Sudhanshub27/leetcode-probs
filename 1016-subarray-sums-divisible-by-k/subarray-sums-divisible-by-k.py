class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result=0
        curr_sum=0
        prefixsums={0:1}
        for i in nums:
            curr_sum+=i
            rem=curr_sum%k
            result+=prefixsums.get(rem,0)
            prefixsums[rem]=1+prefixsums.get(rem,0)
        return result
        