class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        for idx, price in enumerate(prices):
            if idx == 0:
                continue

            if prices[idx] > prices[idx-1]:
                profit = profit + (prices[idx] - prices[idx-1])

        return profit


if __name__ == '__main__':
    prices = [1,2,3,4,5]
    sol = Solution()
    print(sol.maxProfit(prices))