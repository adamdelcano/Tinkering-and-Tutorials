# for https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Finds the maximum value obtained from buying a stock and then
        later (ONLY AFTER BUYING IT) selling it, given list of prices ordered
        sequentially by date."""
        buy_price = float("inf")
        best_profit = 0
        for current_price in prices:
            if current_price < buy_price:
                buy_price = current_price
            else:
                best_profit = max(best_profit, current_price - buy_price)
        return best_profit
