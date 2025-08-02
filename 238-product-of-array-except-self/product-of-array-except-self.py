class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # tc=O(N) same , but sc=O(N) as it has 
        # input arrays intialized to size n . result array doesnt count
        # as it is output which is required - rest 2 are inputs.

        # n = len(nums)  
        # left_product = [1] * n
        # right_product = [1] * n
        # result = [1] * n
        
        # # Build left_product
        # for i in range(1, n):
        #     left_product[i] = left_product[i - 1] * nums[i - 1]
        
        # # Build right_product
        # for i in range(n - 2, -1, -1):
        #     right_product[i] = right_product[i + 1] * nums[i + 1]
        
        # # Final result
        # for i in range(n):
        #     result[i] = left_product[i] * right_product[i]
        
        # return result

        # tc=O(N) same but sc=O(1) as just variables rae only declared.
        # result doesnt count as it is output and not input
        n=len(nums)
        result=n*[1]
      
        left=1
        for i in range(n):
            result[i]=left
            left=left*nums[i]
           
        right=1
        for i in range(n-1,-1,-1):
            result[i]=result[i]*right
            right=right*nums[i]

        return result
     

            
            



        