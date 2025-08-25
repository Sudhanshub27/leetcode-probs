class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        result=[]
        if n1<=n2:
            for i in range(n1):
                if nums1[i] in nums2:
                    result.append(nums1[i])
                else:
                    continue
        if n2<n1:
            for i in range(n2):
                if nums2[i] in nums1:
                    result.append(nums2[i])
        return list(set(result))

            
        