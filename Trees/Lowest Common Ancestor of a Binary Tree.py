# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        return l if l else r
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

nd = Node(3)
nd.left = Node(9)
nd.right = Node(8)
nd.left.left = Node(4)
nd.left.right = Node(0)
nd.right.right = Node(7)
nd.right.left = Node(1)

print(Solution().lowestCommonAncestor(nd,nd.left.right,nd.left.left).val)

''