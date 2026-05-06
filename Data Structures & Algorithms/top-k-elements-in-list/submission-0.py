class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,1,1,1,1,1]
        # k = 6
        # ans = [2,3]
        # 1 -> 6 ( num -> count )

        hm={} 
        ds=[]
        ans=[]

        for num in nums: hm[num] = hm.get(num,0)+1                

        ds = [[] for _ in range(len(nums) + 1)]
        for num, count in hm.items(): ds[count].append(num)
        # l = [[],[],[],[],[],[],[1]]
#             0, 1, 2,  3, 4, 5, 6

        for i in range( len(ds)-1,0,-1):
            
            for value in ds[i]:
                if (len(ans) != k): 
                    ans.append(value)
                else:
                    return ans

        return ans
                    