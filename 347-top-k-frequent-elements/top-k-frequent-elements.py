class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter=Counter(nums)
        heap=[(-freq,num) for num,freq in counter.items()]
        heapq.heapify(heap)

        result=[]
        for i in range(k):
            freq,num=heapq.heappop(heap)
            result.append(num)
        return result

