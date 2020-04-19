# for https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	"""Finds the maximum value obtained from buying a stock and then
        later (ONLY AFTER BUYING IT) selling it, given list of prices ordered
        sequentially by date."""
        if not prices:  # This seems suboptimal but see line 13
            return 0
        sell_price = 0
        buy_price = prices[0]  # This fails if prices = []
        best_profit = 0
        for current_price in prices:
            profit = current_price - buy_price
            if profit > best_profit:
                best_profit = profit
                sell_price = current_price
            if current_price < buy_price:
                buy_price = current_price
        return best_profit
