__import__("sampleTree")
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Sol:
    def VerticalSum(self,root):
        if root == None:
            return 0
        mem = {}
        self._helper(root,0,mem)
        return mem[0]

    def _helper(self,node,pos,mem):
        # Base Condition

        if pos in mem :
            mem[pos] += node.val
        else:
            mem[pos] = node.val

        if node.left:
            self._helper(node.left,pos-1,mem)

        if node.right:
            self._helper(node.right,pos+1,mem)

sol = Sol()
print(sol.VerticalSum(nd))


