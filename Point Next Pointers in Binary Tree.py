# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
def preorder(root):
    if root:
        print(root.left.val if root.left else None,root.val,root.next.val if root.next else None,root.right.val if root.right else None)
        preorder(root.left)
        preorder(root.right)

class Solution:
    def pointRight(self,root):
        while root:
            cur = tmp = TreeLinkNode(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next

                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = tmp.next



a = TreeLinkNode(10)
b = TreeLinkNode(5)
c = TreeLinkNode(1)
d = TreeLinkNode(3)
e = TreeLinkNode(7)

a.left = b
a.right = c
b.left = d
c.right = e

preorder(a)
print("---------------")

sol = Solution()
sol.pointRight(a)

preorder(a)