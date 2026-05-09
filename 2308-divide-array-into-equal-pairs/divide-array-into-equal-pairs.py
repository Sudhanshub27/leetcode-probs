class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map=dict()
        n=len(nums)
        for i in range(n):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        for value in hash_map.values():
            if value%2==1:
                return False
        return True
        
        