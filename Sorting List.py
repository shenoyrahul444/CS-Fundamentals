# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        new_head = self.sort(head, n)
        return new_head

    def sort(self, head, n):
        if n == 1:
            return head

        mid = n // 2
        head1 = head
        head2 = head
        for i in range(mid):
            head2 = head2.next

        head1 = self.sort(head1, mid)
        head2 = self.sort(head2, n - mid)

        return self.merge(head1, mid, head2, n - mid)

    def merge(self, head1, l1, head2, l2):
        if l1 > 0 and l2 > 0:
            curr = dummy = ListNode(0)
            i = j = 0
            while i < l1 and j < l2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                    i += 1
                else:
                    curr.next = head2
                    head2 = head2.next
                    j += 1
                curr = curr.next

            while i < l1:
                curr.next = head1
                head1 = head1.next
                curr= curr.next
                i+=1


            while j < l2:
                curr.next = head2
                head2 = head2.next
                curr = curr.next
                j+=1


            return dummy.next


l = ListNode(10)
l.next = ListNode(4)
l.next.next = ListNode(9)
l.next.next.next = ListNode(19)
l.next.next.next.next = ListNode(1)

curr = l
while curr:
    print(curr.val)
    curr = curr.next

sol = Solution()
curr = sol.sortList(l)

while curr:
    print(curr.val)
    curr = curr.next


