"""
Problem Name: Reverse Kth Node

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

"""

# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if k == 1:
            return head
        c = head
        n = 1
        while c.next:
            n += 1
            c = c.next
            if n == k:
                break
        if n < k:
            return head

        nextKthNode = c.next
        lastNode = self.rev(head, k)
        lastNode.next = self.reverseKGroup(nextKthNode, k)
        return c

    def rev(self, root, n):
        # Return the head (Which now becomes the tail/lastNode)
        tailRet = root
        prev = None
        curr = root

        for i in range(n):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return tailRet
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
def printN(root):
    c = root
    while c:
        print(c.val)
        c = c.next
printN(root)
print("\n")
sol = Solution()
newHead = sol.reverseKGroup(root,3)
printN(newHead)