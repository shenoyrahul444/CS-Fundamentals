class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def sortList(self,head):

        if head == None:
            return None

        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next

        return self.sortListHelper(head,n)

    def sortListHelper(self,head,size):
        if size == 1:
            return head
        mid = size//2
        c1 = head
        c2 = head
        for i in range(mid):
            c2 = c2.next

        c1 = self.sortListHelper(c1,mid)
        c2 = self.sortListHelper(c2,size - mid)

        return self.merge(c1,mid,c2,size-mid)

    def merge(self,c1,l1,c2,l2):
        if l1 > 0 and l2 > 0:
            c = dummy = Node(0)
            i = j = 0
            while i < l1 and j < l2:
                if c1.val < c2.val:
                    c.next = c1
                    c1 = c1.next
                    c = c.next
                    i+=1
                else:
                    c.next = c2
                    c2 = c2.next
                    c = c.next
                    j += 1
            if i < l1:
                c.next = c1
            else:
                c.next = c2
            return dummy.next

def printList(head):
    curr = head
    result_string = "Nodes ["
    while curr:
        if curr.next != None:
            result_string += str(curr.val) + ","
        else:
            result_string += str(curr.val)
        curr = curr.next
    result_string += "]"
    print(result_string)


node = Node(1)
node.next = Node(5)
node.next.next = Node(3)
node.next.next.next = Node(2)
node.next.next.next.next = Node(4)
node.next.next.next.next.next = Node(7)
node.next.next.next.next.next.next = Node(9)

printList(node)
sol = Solution()
result_node = sol.sortList(node)
printList(result_node)