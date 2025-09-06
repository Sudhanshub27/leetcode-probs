class Solution:
    def reverse(self, x: int) -> int:
        string=""
        if x>(2**31-1):
            return 0
        else:
            if x>0:
                while x>9:
                    n=x%10
                    string+=str(n)
                    x=x//10
                string+=str(x)
                string=int(string)
                if string>(2**31-1):
                    return 0
                else:
                    return string
            elif x<0:
                x=x*(-1)
                while x>9:
                    n=x%10
                    string+=str(n)
                    x=x//10
                string+=str(x)
                string="-"+string
                string=int(string)
                if string<(-2**31):
                    return 0
                else:
                    return string
            else:
                return 0
        