class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = 0

        for key in range(n + 1):      # changed
            value = 0
            for j in range(n):
                if citations[j] >= key:
                    value += 1

            if value >= key:
                ans = max(ans, key)

        return ans