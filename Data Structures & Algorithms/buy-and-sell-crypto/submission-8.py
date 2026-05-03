class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        # prices=[7]

        l=0
        r=1
        maxP=0
        if not prices: return 0
        if len(prices)==1: return 0
        for day,price in enumerate(prices):
            if prices[r] - prices[l] >0:                 #valid profit
                p = prices[r] - prices[l]
                maxP = max(p, maxP)
                print(f'prices of l = {prices[l]} & prices of r = {prices[r]}')
                print(f'Profit condition maxP={maxP}, l={l}, r={r}')

            else: #move left, loss, buy at new value
                l = r
                print(f'Loss condition, l={l}, r={r}')                

            r = r + 1
            print(f'updating pointers, l={l}, r={r}')

            if len(prices) <= r: break
        return maxP









































































    # def maxProfit(self, prices: List[int]) -> int:    
    #     l,r=0,1
    #     maxP=0
    #     for r in range(1, len(prices)):
    #         if prices[r] prices[l]
                







































# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l,r = 0,1 # l == buy, r == sell
#         maxP = 0
#         while(r<len(prices)):
#             if prices[r] > prices[l]:
#                 p = prices[r] - prices[l]
#                 maxP = max(maxP, p)
#             else:
#                 l = r
#             r = r+1
#         return maxP













































#     # def maxProfit(self, prices: List[int]) -> int:
#     #     l,r = 0,1 # buy, sell
#     #     # prices = [10,1,5,6,7,1]
#     #     maxP=0

#     #     while (r<len(prices)):
#     #         if prices[l] < prices[r]: #profit condition
#     #             p = prices[r] - prices[l]
#     #             maxP = max(maxP, p)
#     #         else:
#     #             #loss condition
#     #             l = r
#     #         r = r+1

#     #     return maxP
