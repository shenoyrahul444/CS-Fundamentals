"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.



"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        def areSame(r1, r2):
            if not r1 and not r2:
                return True
            if (r1 and not r2) or (r2 and not r1):
                return False
            if r1 and r2:
                if r1.val != r2.val:
                    return False
                return areSame(r1.right, r2.left) and areSame(r1.left, r2.right)

        return areSame(root.left, root.right)
