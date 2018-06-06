def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) or j < len(right):
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i+=1
                    k+=1
                else:
                    arr[k] = right[j]
                    j+=1
                    k+=1
            elif i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            else:
                arr[k] = right[j]
                j+=1
                k+=1

arr = [6,2,4,6,8,1,3,5,2]
print(arr)
mergeSort(arr)
print(arr)



