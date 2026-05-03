class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_index_hm={}
        for index,num in enumerate(nums):
            #checks
            diff = target - num
            if diff in number_index_hm:
                i=number_index_hm[diff]
                return [i,index]
            
            #update
            if num not in number_index_hm:
                number_index_hm[num] = index

