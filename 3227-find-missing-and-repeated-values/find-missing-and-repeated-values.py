class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash_map=dict()
        n=len(grid)
        a=0
        b=0
        for row in grid:
            for num in row:
                hash_map[num]=hash_map.get(num,0)+1
        for key,value in hash_map.items():
            if value==2:
                a=key
        for i in range(1,n*n+1):
            if i not in hash_map:
                b=i
                break
        return [a,b]
            