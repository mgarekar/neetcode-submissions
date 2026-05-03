class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #iterate over array
        #at every ele, look at window+ elements
        #compute max for every lookup
        #store max
        #return max

        out=[]
        for i in range( len(nums)-k+1 ):
            max_so_far=nums[i]
            for j in range(i,i+k):
                possible_max=nums[j]
                max_so_far=max(possible_max,max_so_far)
            out.append(max_so_far)
        return out


































































        # out=[]
        # for i in range( len(nums)-k+1 ):#i start of last window
        #     max_so_far=nums[i]
        #     for j in range(i,i+k):
        #         max_so_far=max(nums[j], max_so_far)
        #     out.append(max_so_far)
        # return out
