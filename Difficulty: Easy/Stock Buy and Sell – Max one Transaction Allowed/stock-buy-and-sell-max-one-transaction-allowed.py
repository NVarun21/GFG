class Solution:
    def maxProfit(self, prices):
        # code here
        min_price=prices[0]
        max_profit=0
        profit=0
        for num in prices:
            min_price=min(num,min_price)
            profit=num-min_price
            max_profit=max(profit,max_profit)
        return max_profit