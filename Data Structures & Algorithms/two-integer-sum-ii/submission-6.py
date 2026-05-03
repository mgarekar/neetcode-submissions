class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i,j=0,len(numbers)-1
        while(i<j):
            if (numbers[i] + numbers[j] == target) : 
                return [i+1, j+1]
            elif (numbers[i] + numbers[j] < target):
                i = i+1
            elif (numbers[i] + numbers[j] > target):
                j = j-1



















        # l,r = 0, len(numbers) - 1
        # while( l < r):
        #     cursum = numbers[l] + numbers[r]
        #     if(cursum < target):
        #         l=l+1
        #     elif(cursum > target):
        #         r=r-1
        #     else:
        #         return [l+1, r+1]   
        # return []    
        