class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq_l = 0
        nums_set = set(nums)

        for num in nums:
            #is num a start of a seq? 
            if (num-1) not in nums_set:
                #Start of a sequence with num.
                #how long is it?
                length=1
                while( (num + length) in nums_set   ):
                    #subsequent element exists so series contiues
                    length = length + 1
                #end of series
                longest_seq_l = max(longest_seq_l, length )


        return longest_seq_l