class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i,n in enumerate(nums):
            a=target-n
            if a in hash_map:
                return [hash_map[a],i]
            hash_map[n]=i


  
        