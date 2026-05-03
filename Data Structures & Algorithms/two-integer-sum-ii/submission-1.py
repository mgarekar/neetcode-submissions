class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0, len(numbers) - 1
        while( l < r):
            cursum = numbers[l] + numbers[r]
            if(cursum < target):
                l=l+1
            elif(cursum > target):
                r=r-1
            elif(cursum == target):
                return [l+1, r+1]   
        return []    
        