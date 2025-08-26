class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    #    m=len(matrix)
    #    n=len(matrix[0])
    #    for i in range(m):
    #     for j in range(n):
    #         if matrix[i][j]==target:
    #             return True
    #    return False 
        new_list=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_list.append(matrix[i][j])
        l=0
        r=len(new_list)-1
        while l<=r:
            m=(l+r)//2
            if new_list[m]<target:
                l=m+1
            elif new_list[m]>target:
                r=m-1
            else:
                return True
        return False                