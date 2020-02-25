class Solution(object):
    a = {}
    a['0'] = 0
    a['1'] = 1
    a['2'] = 2

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if str(n) in Solution.a:
            return Solution.a[str(n)]

        Solution.a[str(n)] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return Solution.a[str(n)]


if __name__ == '__main__':

    sol = Solution()
    print(sol.climbStairs(2))