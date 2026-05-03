class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}#num -> index
        for i,part in enumerate(nums):
            other_part=target-part
            if other_part in hm: return [hm[other_part],i]
            else: hm[part] = i
        return




























    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         diff=target-nums[i]
    #         j=i+1
    #         while(j<len(nums)):
    #             if nums[j] == diff:
    #                 return [i,j]
    #             else:
    #                 j=j+1


































    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     number_index_hm={}
    #     for index,num in enumerate(nums):
    #         #checks
    #         diff = target - num
    #         if diff in number_index_hm:
    #             i=number_index_hm[diff]
    #             return [i,index]
            
    #         #update
    #         if num not in number_index_hm:
    #             number_index_hm[num] = index

