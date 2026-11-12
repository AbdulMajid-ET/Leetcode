class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for p in prices[1:]:

            today_profit = p - min_price

            if today_profit > max_profit:
                max_profit = today_profit

            if p < min_price:
                min_price = p

        return max_profit