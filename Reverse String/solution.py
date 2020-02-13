# 맞춤
class Solution(object):
    def reverseString(self, s):
        length = len(s)
        half_length = int(length/2)

        length_m = length - 1
        print(length)
        print(s)

        for i in range(half_length):
            tmp = s[i]
            s[i] = s[length_m - i]
            s[length_m - i] = tmp

        print(s)



if __name__ == '__main__':
    iput = ["h", "e", "l", "l", "o"]
    sol = Solution()
    sol.reverseString(iput)