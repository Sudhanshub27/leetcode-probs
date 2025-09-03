class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=""
        for i in digits:
            str_i=str(i)
            number=number+str_i
        int_num=int(number)+1
        result=[]
        while int_num>0:
            n=int_num%10
            result.append(n)
            int_num=int_num//10
        return result[::-1]

        

        