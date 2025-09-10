class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:                  # While number has more than 1 digit
            s = 0
            while num > 0:                # Sum digits
                s += num % 10
                num //= 10
            num = s                       # Replace num with sum of digits
        return num

            
        