class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)#possible values of k
        res=r
        #to find k
        while(l<=r):
            k=(l+r)//2
            hours=0
            for p in piles:
                hours = hours + math.ceil(p / k)
            if hours <= h:
                #go left,
                res=min(res,k)
                r=k-1
            else:
                #go right
                l=k+1
        return res
