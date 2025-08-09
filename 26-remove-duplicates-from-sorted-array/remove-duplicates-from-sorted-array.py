import itertools
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # result=set()
        # for i in nums:
        #     result.add(i)
        # nums.clear()
        # for i in result:
        #     nums.append(i)
        # nums.sort()
        # return len(nums)
        # map={}
        # n=len(nums)
        # for i in nums:
        #     if i in map:
        #         map[i]+=1
        #     else:
        #         map[i]=1
        # nums.clear()
        # for key,val in map.items():
        #     nums.append(key)
        # return len(nums)
     

        nums[:] = [key for key, _ in itertools.groupby(nums)]
        return len(nums)


        


        