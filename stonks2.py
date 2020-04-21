# for https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Finds the maximum value obtained from buying a stock and then
        later (ONLY AFTER BUYING IT) selling it, given list of prices ordered
        sequentially by date, with the option of doing more than
        one transaction but not per date."""
        buy_price = float("inf")
        best_profit = 0
        previous_price = 0  # Maybe enumerate(prices) and uses indexes instead?
        total_profit = 0
        for current_price in prices:
            if current_price < buy_price \  # Is this split idiomatic?
            or current_price < previous_price:  # aka Transaction Complete?
                total_profit += best_profit
                best_profit = 0
                buy_price = current_price
            else:
                best_profit = max(best_profit, current_price - buy_price)
            previous_price = current_price
        total_profit += best_profit  # Collects the last transaction
        return total_profit
