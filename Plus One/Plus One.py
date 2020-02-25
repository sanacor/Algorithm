class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        integer = 0
        for idx, val in enumerate(digits):
            position = self.get_deci(len(digits) - 1 - idx)
            # print(position)
            integer = integer + (position * val)
            # print(val)

        # print(integer)
        integer = integer + 1
        # print(integer)
        return self.put_to_list(integer)


    def put_to_list(self, integer):
        if integer < 10:
            return [integer]

        res = []
        deci = 10
        while True:
            val = integer % deci
            res.insert(0, val)
            integer = int(integer / 10)
            if integer == 0:
                break
            # deci = deci * 10

        return res

    def get_deci(self, idx):
        res = 1

        for v in range(0, idx):
            res = res * 10

        return res


if __name__ == '__main__':
    digits = [1, 8, 9]

    sol = Solution()
    print(sol.plusOne(digits))