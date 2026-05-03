class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1
        area = 0

        while(l<r):        
            print(f'l is {l}')
            print(f'height at l is {heights[l]}')
            print(f'r is {r}')            
            print(f'height at r is {heights[r]}')            
            print(f'area is  is {area}')         

            cur_area = (r-l) * min( heights[l],heights[r] )
            area = max(area, cur_area )

            if  heights[l]<heights[r] and l < r: l = l +1 
            elif heights[l]>heights[r] and l < r: r = r - 1
            else: l = l + 1

        return area

































































    # def maxArea(self, heights: List[int]) -> int:
    #     l,r=0,len(heights)-1
    #     area=0

    #     while(l<r):
    #         width= r-l
    #         height = min(heights[l],heights[r] )
    #         area = max(area, width*height)

    #         if heights[l] < heights[r]:
    #             l=l+1
    #         elif heights[l] > heights[r]:
    #             r=r-1
    #         else:
    #             l=l+1
    #     return area