class Solution:
    def maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]) -> int:
        max_wealth = 0
        for account in accounts:
            current_val = sum(account)
            max_wealth = max(max_wealth, current_val)
        return max_wealth
