class Solution:
    def maxArea(self, height):
        i=0
        j=len(height)-1
        maxw=0
        while i<j:
            w=j-i
            h=min(height[i],height[j])
            maxw=max(maxw,w*h)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxw
        