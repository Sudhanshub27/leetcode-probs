class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=['a','e','i','o','u']
        vowel={}
        consonents={}
        n=len(s)
        for i in range(n):
            if s[i] in vowels:
                if s[i] in vowel:
                    vowel[s[i]]+=1
                else:
                    vowel[s[i]]=1
            if s[i] not in vowels:
                if s[i] in consonents:
                    consonents[s[i]]+=1
                else:
                    consonents[s[i]]=1
        if not vowel:
            a=0
        else:
            a=vowel[max(vowel,key=vowel.get)]
        if not consonents:
            b=0
        else:
            b=consonents[max(consonents,key=consonents.get)]
        return a+b
                    
        