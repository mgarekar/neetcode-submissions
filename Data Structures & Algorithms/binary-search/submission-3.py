class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while(l<=r):
            mid=(l+r)//2
            guess=nums[mid]

            if guess < target:
                l=mid+1
            elif guess > target:
                r = r-1
            else:
                return mid #guess == target
        return -1
            
                
        