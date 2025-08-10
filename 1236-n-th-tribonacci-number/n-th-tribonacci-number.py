class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        list_l=[0]*(n+1)
        list_l[0]=0
        list_l[1]=1
        list_l[2]=1
        if n>=3:
            for i in range(3,len(list_l)):
                list_l[i]=list_l[i-1]+list_l[i-2]+list_l[i-3]
            return list_l[n]
        
        


            
            


        