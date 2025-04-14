'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        currMinPrice = math.inf

        for i in range(len(prices)):
            if prices[i] < currMinPrice:
                currMinPrice = prices[i]

            if prices[i] - currMinPrice > profit:
                profit = prices[i] - currMinPrice

        return profit



prices = [7,1,5,3,6,4]
x = Solution()
print(x.maxProfit(prices))
        