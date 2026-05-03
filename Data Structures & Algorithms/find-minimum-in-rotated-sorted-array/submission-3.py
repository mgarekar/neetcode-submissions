class Solution:
    def findMin(self, nums: List[int]) -> int:
         res=nums[0]#set some value as minimum
         l,r=0,len(nums)-1#rnge for search

         while(l<=r):
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            #unsorted array / rotated array

            m = (r+l)//2
            res = min(res,nums[m])

            if nums[l] <= nums[m]:
                #min is on right side
                l=m+1
            else:
                #min is on left side
                r=m-1


         return res
