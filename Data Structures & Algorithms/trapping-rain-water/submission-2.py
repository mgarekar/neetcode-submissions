class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        for i in range(0,len(height)):
            #iterate
            left_list=height[0:i] 
            right_list=height[i+1:]
            if left_list == [] or right_list==[]:
                continue
            m_l=max(left_list)
            m_r=max(right_list)
            water = min(m_l, m_r) - height[i]
            if water <=0:
                continue
            else:
                ans = ans + water
        return ans