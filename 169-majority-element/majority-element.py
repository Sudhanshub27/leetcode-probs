class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        n=len(nums)
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        for key,val in map.items():
            if val>n//2:
                return key
        