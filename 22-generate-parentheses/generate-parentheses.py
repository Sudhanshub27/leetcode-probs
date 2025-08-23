class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(string,left,right):
            if len(string)==2*n:
                result.append(string)
            if left<n:
                backtrack(string+'(',left+1,right)
            if right<left:
                backtrack(string+')',left,right+1)
        backtrack("",0,0)
        return result
      


            

        




        