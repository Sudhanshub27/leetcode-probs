class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        map={}
        result=[]
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]]+=1
            else:
                map[nums[i]]=1
        for key,value in map.items():
            if key!=val:
                result.extend([key]*value)
        nums[:len(result)]=result
        return len(result)

        