class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        minus = False
        if 0 > x:
            x = 0 - x
            minus = True

        length = len(str(x)) - 1
        res = 0
        
        for i in range(0, length + 1):
            this = x % 10
            x = int(x / 10)
            res += this * (10 ** (length - i))

        if minus:
            res = 0 - res

        if res < - (2**31):
            return 0

        if (2**31) - 1 < res:
            return 0

        return res

if __name__ == '__main__':
    sol = Solution()
    sol.reverse(1534236469)
