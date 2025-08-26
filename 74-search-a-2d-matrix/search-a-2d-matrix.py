class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    #    m=len(matrix)
    #    n=len(matrix[0])
    #    for i in range(m):
    #     for j in range(n):
    #         if matrix[i][j]==target:
    #             return True
    #    return False 
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=(m*n)-1
        while l<=r:
            mid=(l+r)//2
            row=mid//n
            col=mid%n
            val=matrix[row][col]
            if val<target:
                l=mid+1
            elif val>target:
                r=mid-1
            else:
                return True
        return False                