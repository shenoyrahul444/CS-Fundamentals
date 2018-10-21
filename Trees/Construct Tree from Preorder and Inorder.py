class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder[0])
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder[1:], inorder[0:ind])
            root.right = self.buildTree(preorder[1:], inorder[ind+1:])
            return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
print(sol.buildTree(preorder,inorder))