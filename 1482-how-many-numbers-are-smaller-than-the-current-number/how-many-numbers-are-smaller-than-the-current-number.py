class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        map={}
        sorted_nums=sorted(nums)
        n=len(sorted_nums)
        for i in range(n):
            if sorted_nums[i] not in map:
                map[sorted_nums[i]]=i
        for i in range(n):
            result.append(map[nums[i]])
        return result

                
        