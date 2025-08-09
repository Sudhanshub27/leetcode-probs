class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result=set()
        for i in nums:
            result.add(i)
        nums.clear()
        for i in result:
            nums.append(i)
        nums.sort()
        return len(nums)


        