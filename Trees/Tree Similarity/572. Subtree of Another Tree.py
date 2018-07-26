"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def isSametree(r1, r2):
            if not r1 and not r2:
                return True
            if (r1 and not r2) or (r2 and not r1):
                return False
            return r1.val == r2.val and isSametree(r1.left, r2.left) and isSametree(r1.right, r2.right)

        if not s and not t:
            return True

        if (s and not t) or (t and not s):
            return False

        if s.val == t.val:
            if isSametree(s, t):
                return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

Å
