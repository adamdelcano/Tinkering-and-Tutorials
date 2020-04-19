# for https://leetcode.com/problems/best-time-to-buy-and-sell-stock


# so the problem is this looks at the whole list for every entry in the list.
# I need a version without nested loops if I want to look at a huge range
# I think it makes the most sense to look at the list backward then?
# OH SHIT I JUST HAD A BREAKTHROUGH

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            sell_price = 0
            buy_price = prices[0]
            best_profit = 0
            for current_price in prices:
                profit = current_price - buy_price
                if profit > best_profit:
                    best_profit = profit
                    sell_price = current_price
                if current_price < buy_price:
                    buy_price = current_price
            return best_profit
