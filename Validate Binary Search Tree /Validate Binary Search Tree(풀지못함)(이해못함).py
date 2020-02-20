# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = True

    def isValidBST(self, root):
        Solution.result = True
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.right == None and root.left == None:
            return True

        if root.right == None and root.left != None:
            self.check_left(root.left, root.val)

        if root.right != None and root.left == None:
            self.check_right(root.right, root.val)

        if root.right != None and root.left != None:
            self.check_right(root.right, root.val)
            self.check_left(root.left, root.val)

        return Solution.result

    def check_left(self, left_node, root_value):
        print(left_node.val)
        print(root_value)
        if root_value > left_node.val:
            if left_node.right is not None:
                self.check_right(left_node.right, left_node.val)
            if left_node.left is not None:
                self.check_left(left_node.left, left_node.val)
        else:
            print('shit')
            Solution.result = False


    def check_right(self, right_node, root_value):
        if root_value < right_node.val:
            if right_node.right is not None:
                self.check_right(right_node.right, right_node.val)
            if right_node.right is not None:
                self.check_left(right_node.left, right_node.val)
        else:
            print('shit2')
            Solution.result = False


