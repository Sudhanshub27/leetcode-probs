class Solution:
    def reverse(self, x: int) -> int:
        result=0
        if x>0 and x<=(2**31)-1 :
            while x>0:
                ld=x%10
                result=(result*10)+ld
                x=x//10
            result+=x
            if result<(2**31)-1 and result>-2**31:
                return result
            else:
                return 0
        elif x<0 and x>=-2**31:
            x*=(-1)
            while x>0:
                ld=x%10
                result=(result*10)+ld
                x=x//10
            result+=x
            ans=result*(-1)
            if ans<(2**31)-1 and ans>-2**31:
                return ans
            else:
                return 0
        else:
            return 0


        