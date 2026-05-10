class Solution:
    def check(self, nums: List[int]) -> bool:
        l=nums.copy()
        l.sort()
        for i in range(len(l)):
            x=l.pop(0)
            l.append(x)
            if l==nums:
                return True
        return False

        