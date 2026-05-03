class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [1,2,3,4]
        # target = 3

        for i,num in enumerate(numbers):
            other_part = target-num
            j=i+1

            print(f'i={i}')

            print(f'num={num}')
            print(f'other_part={other_part}')

            while(j<len(numbers)):
                print(f'j={j}')
                print(f'numbers[j]={numbers[j]}')
                if numbers[j] != other_part:
                    j=j+1
                else:
                    ans = [i+1,j+1]
                    return ans
        return ans




































































































    # def twoSum(self, numbers: List[int], target: int) -> List[int]:

    #     i,j=0,len(numbers)-1
    #     while(i<j):
    #         if (numbers[i] + numbers[j] == target) : 
    #             return [i+1, j+1]
    #         elif (numbers[i] + numbers[j] < target):
    #             i = i+1
    #         elif (numbers[i] + numbers[j] > target):
    #             j = j-1



















    #     # l,r = 0, len(numbers) - 1
    #     # while( l < r):
    #     #     cursum = numbers[l] + numbers[r]
    #     #     if(cursum < target):
    #     #         l=l+1
    #     #     elif(cursum > target):
    #     #         r=r-1
    #     #     else:
    #     #         return [l+1, r+1]   
    #     # return []    
        