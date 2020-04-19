# for https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            biggest_profit = 0
            for day, buy_price in enumerate(prices):
                profits = [sell_price - buy_price for sell_price in prices[day:]]
                if max(profits) > biggest_profit:
                    biggest_profit = max(profits)
            return biggest_profit
                        