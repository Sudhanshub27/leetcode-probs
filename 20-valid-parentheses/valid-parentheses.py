class Solution:
    def isValid(self, s: str) -> bool:
        list=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                list.append(i)
            else:
                if len(list)==0:
                    return False
                if i==')':
                    if list[-1]=='(':
                        list.pop()
                    else:
                        return False
                if i==']':
                    if list[-1]=='[':
                        list.pop()
                    else:
                        return False
                if i=='}':
                    if list[-1]=='{':
                        list.pop()
                    else:
                        return False

        if len(list)==0:
            return True
        else:
            return False

        