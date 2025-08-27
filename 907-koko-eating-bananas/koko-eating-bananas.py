class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hour=0
            for pile in piles:
                hour+=math.ceil(pile/k)
            return hour<=h
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans      

        