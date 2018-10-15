def partition(arr,low,high):
    if low < high:
        pivot = arr[high]   # 6
        i = low - 1         # -1


        for j in range(low,high):
            if arr[j] <= pivot:
                i+=1
                arr[j],arr[i] = arr[i],arr[j]
            j+=1
        arr[i+1],arr[high] = arr[high],arr[i+1]

        return i+1

    # [4, 2, 10, 3, 5, 9, 5, 7, 7, 6]


def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

def sort(nums):
    if nums == []:
        return []
    l = 0
    r = len(nums) - 1

    return quickSort(nums,l,r)

def mergesort(nums):
    if len(nums) == 1:
        return nums
    n = len(nums)
    mid = n//2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])

    i,j= 0,0
    ctr = 0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            nums[ctr] = left[i]
            i+=1
            ctr+=1
        else:
            nums[ctr] = right[j]
            j+=1
            ctr+=1
    while i< len(left):
        nums[ctr] = left[i]
        i+=1
        ctr+=1

    while j<len(right):
        nums[ctr] = right[j]
        j+=1
        ctr+=1
    return nums

def insertionSort(nums):
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            j = i
            ref = nums[i]
            while nums[j-1] > ref and j - 1 >= 0:
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = ref
    return nums

def bubblesort(nums):

    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

# [4, 2, 10, 3, 5, 9, 5, 7, 7, 6]


from random import *

nums = [8, 6, 7, 5, 2, 5, 9, 2, 10, 10]
# for i in range(10):
#     nums.append(randint(2,10))
print("Nums",nums)
# print("Merge Sort",mergesort(nums))
# bubblesort(nums)
# print("Bubble Sort",nums)
# sort(nums)
print(insertionSort(nums))

