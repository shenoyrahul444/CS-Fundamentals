# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or lists == []:
            return None
        tail = dummy = ListNode(-1)

        i = 0
        n = len(lists)
        while i < n-1-i:
            first,last = self.mergeSorted(lists[i],lists[n-1-i])
            tail.next = first
            tail = last
            i+=1
        return dummy.next


    def mergeSorted(self,list1,list2):
        curr = dummy = ListNode(-1)

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                elif list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next

            elif list1:
                curr.next = list1
            else:
                curr.next = list2

        while curr.next:
            curr = curr.next

        return [dummy.next,curr]