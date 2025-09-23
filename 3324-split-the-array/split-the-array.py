class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        frequency=Counter(nums)
        for i in frequency:
            if frequency[i]>2:
                return False
        return True
        