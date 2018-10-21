"""
Binary Search has:
    O(1) --> Space Complexiety
    O(log(n)) --> Time Complexiety

It is considered to be an optimal approach.

For binary search, the pre-requisites are:
   1> Array must not have duplicate elements
   2> Elements must be sorted

We can use achieve it using:
1> Recursion approach
2> Iterative approach

"""

def binary_search_rec(arr,target):
    if arr == []:
        return False
    n = len(arr)
    if n == 1:
        if arr[0] == target:
            return True
        else:
            return -1
    i,j = 0,len(arr)-1
    mid = (i + j)//2
    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return binary_search_rec(arr[:mid-1],target)
    else:
        return binary_search_rec(arr[mid+1:],target)
    return False

def binary_search_iter(arr,target):
    if not arr:
        return False
    n = len(arr)
    if n == 1:
        if arr[0] == target:
            return True
        else:
            return False

    i,j = 0,n-1
    while i < j:
        mid = (i+j)//2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return False



arr = [1,3,4,5,8,9,10]
target = 7
print(binary_search_rec(arr,target))
print(binary_search_iter(arr,target))