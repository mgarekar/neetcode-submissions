class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1 # buy, sell
        # prices = [10,1,5,6,7,1]
        maxP=0

        while (r<len(prices)):
            if prices[l] < prices[r]: #profit condition
                p = prices[r] - prices[l]
                maxP = max(maxP, p)
            else:
                #loss condition
                l = r
            r = r+1

        return maxP
