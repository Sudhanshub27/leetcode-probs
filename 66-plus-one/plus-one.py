class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = "".join(str(i) for i in digits)
        result=[]
        int_num=int(number)+1
        while int_num>0:
            n=int_num%10
            result.append(n)
            int_num=int_num//10
        return result[::-1]

        

        