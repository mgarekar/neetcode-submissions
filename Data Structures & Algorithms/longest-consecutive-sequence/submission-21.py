class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        nums=set(nums)
        # nums = [2,20,10,3,4,5]

        longest=0
        for num in nums:

            if (num-1) not in nums: 
                #start of seq?
                #track lenght and compare to longest
                length=1
                current_num=num
                while( current_num+1 in nums ):
                    #seq continues
                    length=length+1
                    current_num=current_num+1
                    
                #done with seq
                longest=max(longest,length)


            else:
                continue


        return longest


