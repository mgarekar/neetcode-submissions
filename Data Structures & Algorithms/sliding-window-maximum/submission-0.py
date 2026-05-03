class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out=[]
        for i in range( len(nums)-k+1 ):#i start of last window
            max_so_far=nums[i]
            for j in range(i,i+k):
                max_so_far=max(nums[j], max_so_far)
            out.append(max_so_far)
        return out
