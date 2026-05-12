class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums=[1,2,4,6,8,10]
        ans=[1]*len(nums)
        pa=[1]*len(nums) # product before i
        po=[1]*len(nums) # product after i        

        # pa=[(1),1*2,1*2*4,1*2*4*6,1*2*4*6*8,(1*2*4*6*8*10)]
        for i in range(1,len(nums)):
            pa[i] = pa[i-1] * nums[i-1] 

        # po=[(1*2*4*6*8*10),(2*4*6*8*10),(4*6*8*10),(6*8*10),(8*10),(10)]
        for i in range( len(nums)-2, -1,-1  ):
            po[i] = po[i+1] * nums[i+1]

        for i in range(len(nums)):
            res = pa[i]*po[i]
            ans[i] = res
        return ans