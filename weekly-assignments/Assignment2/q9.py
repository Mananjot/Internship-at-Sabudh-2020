"""

Question: Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3

"""

class TreeNode():
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

# Algoritnm Reference
# https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/

def maxDepth(parent):
    if parent:
        return max(maxDepth(parent.left), maxDepth(parent.right)) + 1
    return 0

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))