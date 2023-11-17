class Solution:
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        max_val = 0

        while sell < len(prices):
            current_val = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_val = max(current_val, max_val)
            else:
                buy = sell
            sell += 1
        return max_val
