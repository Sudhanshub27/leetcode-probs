class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n=len(height)
        # result=[]
        # a=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         a=min(height[i],height[j])*(j-i)
        #         result.append(a)
        # return max(result)

        n=len(height)
        left=0
        right=n-1
        max_area=0
        area=0
        while left<right:
            length=min(height[left],height[right])
            width=right-left
            area=length*width
            max_area=max(max_area,length*width)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area


      


        