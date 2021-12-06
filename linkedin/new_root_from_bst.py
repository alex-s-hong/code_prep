"""
Given a binary tree and a leaf node. 
Holding that leaf node and the whole tree falls down such that 
it is the new root of the tree, return the modified tree.

        1
       / \
      2   3
     / \   \
    4   5   6
   / \   \
  7   8   9 

Input: root, leaf = 6
Output:
             6
            /
           3
          /
         1
        /
       2
      / \
     4   5
    / \   \
   7   8   9 

"""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None # optional


def dropTree(root, leafNode):
    if not root:
        return 
    if root.val == leafNode.val:
        return root

    isLeafNode = dropTree(root.left, leafNode)
    if isLeafNode:
        falldownLeftTree(root.left, root)
        return isLeafNode
    isLeafNode = dropTree(root.right, leafNode)
    if isLeafNode:
        print('haha')
        falldownRightTree(root.right, root)
        return isLeafNode

    return False



def falldownLeftTree(leftNode, root):
    leftNode.right = root
    root.left = root.right
    root.right = root.parent
    root.left = None
    root.right = None


def falldownRightTree(rightNode, root):
    rightNode.left = root
    root.right = root.left
    root.left = root.parent
    root.right = None
    root.left = None

    