class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize left and right pointer
        left, right = 0, 1 # left=buy, right=sell
        max_profit = 0

        while right < len(prices):
            # check if profitable
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]

                # determine if profit is greater and assign new max profit
                max_profit = max(max_profit, profit)
            else:
                # if left is greater than right then
                # set left to min to follow principle of buy low, sell high
                left = right
            right += 1
        return max_profit
        