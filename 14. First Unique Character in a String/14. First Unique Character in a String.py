class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ch in s:
            if ch not in dic:
                dic.update({ch: 1})
            else:
                dic.update({ch: dic[ch] + 1})

        idx = 0
        for ch in s:
            if dic[ch] == 1:
                return idx

            idx = idx + 1

        return -1


if __name__ == '__main__':
    sol = Solution()
    sol.firstUniqChar("leetcode")
