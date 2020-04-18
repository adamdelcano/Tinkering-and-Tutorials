class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = []
        for day, price in enumerate(prices):
            possible_selling_days = prices[day + 1:]
            profit = [selling_price - price for selling_price in possible_selling_days]
            if profit:
                best_profit.append(max(profit))
        if best_profit:
            if max(best_profit) > 0:
                return max(best_profit)
            else:
                return 0
        else:
            return 0
