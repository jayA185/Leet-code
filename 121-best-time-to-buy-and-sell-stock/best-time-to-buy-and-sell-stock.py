class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:

            # Keep track of minimum buying price
            if price < min_price:
                min_price = price

            # Calculate current profit
            profit = price - min_price

            # Update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit