class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,3,4,5,10,20]
        # [2,3,4,5,19,20]        
        longest_seq_l=1
        nums = sorted(nums)
        current_length = 1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif (nums[i] == 1+nums[i-1]):
                #seq
                current_length = current_length + 1
            else:
                #not a seq
                longest_seq_l = max(longest_seq_l,current_length )
                current_length = 1
        longest_seq_l = max(longest_seq_l,current_length )                
        return longest_seq_l


























































        # longest_seq_l = 0
        # nums_set = set(nums)

        # for num in nums:
        #     #is num a start of a seq? 
        #     if (num-1) not in nums_set:
        #         #Start of a sequence with num.
        #         #how long is it?
        #         length=1
        #         while( (num + length) in nums_set   ):
        #             #subsequent element exists so series contiues
        #             length = length + 1
        #         #end of series
        #         longest_seq_l = max(longest_seq_l, length )


        # return longest_seq_l