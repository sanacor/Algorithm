class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        strObj = s
        # print(s.find('e'))
        for ch in t:
            idx = strObj.find(ch)

            if idx == -1:
                return False
            elif idx == 0:
                strObj = strObj[1 : : ]
            elif idx == len(t):
                strObj = strObj[:-1:]
            else:
                strObj = strObj[0 : idx : ] + strObj[idx + 1 : :]

        if len(strObj) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    # s = 'abcd'
    # t =  'dcba'
    s = 'anagram'
    t = 'nagaram'
    sol = Solution()
    sol.isAnagram(s, t)