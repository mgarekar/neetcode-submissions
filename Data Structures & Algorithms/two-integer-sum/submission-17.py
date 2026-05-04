class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [1,3,4,2]
        # target = 6
        
        ans = []
        i=0
        print("hi")

        while( i<len(nums) ):
            diff = target - nums[i]
            if diff not in nums[i+1:]: 
                i = i+1
                continue


            #diff in nums, whats the index? 
            first_number = i
            other_number = i + 1
            ans.append(first_number)


            print(f'Diff is {diff}')
            print(f'i is {i}')            
            print(ans)

            while( other_number < len(nums)  ):
                if (nums[other_number] == diff):
                    ans.append(other_number)
                    return ans
                other_number = other_number + 1

            i =i +1




