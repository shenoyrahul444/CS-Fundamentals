class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def SortList(head):
    # Edge Case
    if head is None:
        return

    curr = head
    counter = 0
    while curr != None:
        curr = curr.next
        counter += 1

    return sort(head, counter)


def sort(head, size):
    # sort is a recursive function that will divide the list into individual elements (list1 and list2) and then send to merge() which will merge them in a sorted order

    if size == 1:
        return head
    list1 = head
    list2 = head
    for i in range(size // 2):
        list2 = list2.next

    list1 = sort(list1, size // 2)
    list2 = sort(list2, size - (size // 2))
    return merge(list1, size // 2, list2, size - (size // 2))


def merge(list1, size1, list2, size2):
    dummy = list = Node(0)

    pointer1 = pointer2 = 0

    while pointer1 < size1 and pointer2 < size2:
        if list1.value < list2.value:
            list.next = list1
            list1 = list1.next
            pointer1 += 1
        else:
            list.next = list2
            list2 = list2.next
            pointer2 += 1
        list = list.next

    while pointer1 < size1:
        list.next = list1
        list1 = list1.next
        list = list.next
        pointer1 += 1

    while pointer2 < size2:
        list.next = list2
        list2 = list2.next
        list = list.next
        pointer2 += 1

    return dummy.next


def printList(head):
    curr = head
    result_string = "Nodes ["
    while curr:
        if curr.next != None:
            result_string += str(curr.value) + ","
        else:
            result_string += str(curr.value)
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
result_node = SortList(node)

printList(result_node)