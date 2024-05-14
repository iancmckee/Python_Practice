"""121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104

"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    # lowest value left of the highest value
    max_profit = 0
    if len(prices)>1:
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(prices[r]-prices[l], max_profit)
            else:
                l=r
            r+=1

    return max_profit

if __name__ == "__main__":
    testCases=[
        # [7,1,5,3,6,4],
        # [7,6,4,3,1],
        [1,2,4]]
    for testCase in testCases:
        print(maxProfit(testCase))