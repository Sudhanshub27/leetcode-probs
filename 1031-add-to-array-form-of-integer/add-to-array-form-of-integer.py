class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(10000)
        sum=""
        for i in num:
            sum+=str(i)
        sum=int(sum)
        sum=sum+k
        result=[]
        while sum>9:
            a=sum%10
            result.append(a)
            sum=sum//10
        result.append(sum)
        return result[::-1]