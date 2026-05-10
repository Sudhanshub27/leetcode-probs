class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n= len(nums)
        l=nums.copy()
        for i in range(n-1):
            if l[i]==l[i+1]:
                l[i]*=2
                l[i+1]=0
        ans=[]
        for i in l:
            if i!=0:
                ans.append(i)
        while len(ans)<n:
            ans.append(0)

        return ans
        