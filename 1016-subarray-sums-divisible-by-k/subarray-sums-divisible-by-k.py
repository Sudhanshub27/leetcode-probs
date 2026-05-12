class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result=0
        curr_sum=0
        rem={0:1}
        for n in nums:
            curr_sum+=n
            r=curr_sum%k
            result+=rem.get(r,0)
            rem[r]=1+rem.get(r,0)
        return result
        