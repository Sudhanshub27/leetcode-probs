class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # self.n=sorted(nums)  tc=o(n3)
        # result=set()
        # for i in range(len(self.n)):
        #     for j in range(i+1,len(self.n)):
        #         for k in range(j+1,len(self.n)):
        #             if self.n[i]+self.n[j]+self.n[k]==0:
        #                 a=tuple([self.n[i],self.n[j],self.n[k]])
        #                 result.add(a)
        #             else:
        #                 continue
        # return [list(i) for i in result]
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result





        
        
        