# O(n) solution to find LCS of two given values n1 and n2

# A binary tree node
# class Node:
#     # Constructor to create a new binary node
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None


# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath(root, path, k):
    # Baes Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.key)

    # See if the k is same as root's key
    if root.key == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False


# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root or not p or not q:
            return None

        p_nodes = []
        q_nodes = []
        self.getNodes(root, p, p_nodes)
        self.getNodes(root, q, q_nodes)
        # p_nodes = p_nodes[::-1]
        # q_nodes = q_nodes[::-1]
        self.reverse(p_nodes)
        self.reverse(q_nodes)
        last_common = None
        for i in range(min(len(p_nodes), len(q_nodes))):
            if id(p_nodes[i]) == id(q_nodes[i]):
                last_common = p_nodes[i]
            else:
                break
        return last_common

    def getNodes(self, root, target, nodes):
        if root:
            if root.val == target:
                nodes.append(root)
                return True

            if self.getNodes(root.left, target, nodes):
                nodes.append(root)
                return True
            if self.getNodes(root.right, target, nodes):
                nodes.append(root)
                return True

    def reverse(self, arr):
        n = len(arr)
        half = 0
        if n % 2 == 1:
            half = n // 2 + 1
        else:
            half = n // 2
        for i in range(half):
            arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]


# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
print(sol.lowestCommonAncestor(root,4,2).val)
# print
# "LCA(4, 5) = %d" % (findLCA(root, 4, 5, ))
# print
# "LCA(4, 6) = %d" % (findLCA(root, 4, 6))
# print
# "LCA(3, 4) = %d" % (findLCA(root, 3, 4))
# print
# "LCA(2, 4) = %d" % (findLCA(root, 2, 4))


