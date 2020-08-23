"""
Given an N-ary tree, task is to find subtree with maximum avg in tree.
return: root of the subtree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:

    def findLargestSubTreeSum(self, root):
        if not root:
            return 0

        ans = [-99999999999999999999999] #call-by-reference?

        self.helper(root, ans)

        return ans[0]

    def largest_helper(self, root, ans):
        if not root:
            return 0

        currSum = root.val + self.largest_helper(root.left, ans) + self.largest_helper(root.right, ans)

        ans[0] = max(ans[0], currSum)

        return currSum




if __name__ == '__main__':
    #
    #         1
    #        /  \
    #       /    \
    #     -2      3
    #     / \    / \
    #    /   \  /   \
    #   4    5 -6    2
    root = Node(1)
    root.left = Node(-2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(-6)
    root.right.right = Node(2)

    s = Solution()

    print(s.findLargestSubTreeSum(root))