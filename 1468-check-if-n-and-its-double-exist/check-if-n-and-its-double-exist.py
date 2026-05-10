class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            a=arr[i]
            b=a*2
            if b in arr and arr.index(b)!=i:
                return True
        return False

        