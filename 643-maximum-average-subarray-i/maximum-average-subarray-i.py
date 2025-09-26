class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window_sum=0
        result=[]
        average=0.0
        for i in range(0,k):
            window_sum+=nums[i]
        average=window_sum/k
        result.append(average)
        
        for i in range(k,n):
            window_sum=window_sum+nums[i]-nums[i-k]
            average=window_sum/k
            result.append(average)
        return max(result)
        
        