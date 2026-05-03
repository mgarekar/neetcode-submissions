class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0,2,0,3,1,0,1,3,2,1]  
        ans = 0

        if not height:
            return 0        


        prev_max=[0]*len(height)
        after_max=[0]*len(height)
        # Initialize the first and last elements
        prev_max[0] = height[0]
        after_max[-1] = height[-1]
                
        for i in range(1, len(height)):
            if i == 1:
                print('First position')
                print(f' comparing {height[i]} and {height[i-1]} ')                            
            prev_max[i] = max( height[i], prev_max[i-1] )
        for i in range(len(height)-2, -1, -1):
            if i == len(height)-2:
                print('last position')
                print(f' comparing {height[i]} and {height[i+1]} ')            
            after_max[i] = max( height[i], after_max[i+1] )
        print(prev_max)
        print(after_max)

        for i,h in enumerate(height):
            print('at position {i} with height {h}')
            store = min( prev_max[i],after_max[i]   ) - h
            print(f'at position {i} with height {h}, we store {store} water')
            ans = ans + store
        return ans










































    # def trap(self, height: List[int]) -> int:
    #     ans=0
    #     for i in range(0,len(height)):
    #         #iterate
    #         left_list=height[0:i] 
    #         right_list=height[i+1:]
    #         if left_list == [] or right_list==[]:
    #             continue
    #         m_l=max(left_list)
    #         m_r=max(right_list)
    #         water = min(m_l, m_r) - height[i]
    #         if water <=0:
    #             continue
    #         else:
    #             ans = ans + water
    #     return ans