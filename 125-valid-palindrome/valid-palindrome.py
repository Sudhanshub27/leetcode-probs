class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''.join(c for c in s if c.isalnum()).lower()
        left=0
        right=len(list(a))-1
        while left<=right:
            if a[left]==a[right]:
                left+=1
                right-=1
                continue
            else:
                return False
        return True