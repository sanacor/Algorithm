class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        indexA = m-1
        indexB = n-1

        while indexA >= 0 and indexB >= 0:

            if A[indexA] > B[indexB]:
                A[indexA+indexB+1] = A[indexA]
                indexA -= 1
            else:
                A[indexA+indexB+1] = B[indexB]
                indexB -= 1

        while indexB >= 0:
             A[indexB] = B[indexB]
             indexB -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0, 0]
    m = 3

    nums2 = [1, 2, 5, 6]
    n = 4
    sol = Solution()
    sol.merge(nums1, m, nums2, n)