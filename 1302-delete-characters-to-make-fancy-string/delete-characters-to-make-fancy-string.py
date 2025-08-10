class Solution:
    def makeFancyString(self, s: str) -> str:
        result=[]
        str_list=list(s)
        for i in range(len(str_list)):
            if i>=2 and str_list[i]==str_list[i-1]==str_list[i-2]:
                continue
            else:
                result.append(str_list[i])
        final=''.join(result)
        return final

