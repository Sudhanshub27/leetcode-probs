class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        hash_map={}
        for i in range(n):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        for values in hash_map.values():
            if values > 1:
                return True
        return False
        