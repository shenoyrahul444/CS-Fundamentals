# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head:

            n = 0
            c1 = head
            while c1:
                n += 1
                c1 = c1.next
            mid = n // 2

            c2 = head
            for i in range(mid):
                c2 = c2.next
            mid = c2.next
            c2.next = None

            c2 = mid
            prev = None
            while c2:
                nxt = c2.next
                c2.next = prev
                prev = c2
                c2 = nxt
            c2 = prev
            c1 = head

            while c1 and c2:
                # print(c1.val,c2.val)
                nxt1 = c1.next
                nxt2 = c2.next
                c1.next = c2
                c2.next = nxt1
                c1 = nxt1
                c2 = nxt2



nodes = [1,2,3,4,5,6,7,8,9]
nodes = [Node(nd) for nd in nodes]
n = len(nodes)
for i in range(n-1):
    nodes[i].next = nodes[i+1]

head = nodes[0]
Solution().reorderList(head)
#
while head:
    print(head.val)
    head = head.next
