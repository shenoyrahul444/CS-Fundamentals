def partition(arr,low,high):
    if low<high:
        i = low - 1
        pivot = arr[high]

        for j in range(low,high):
            if arr[j] >= pivot:
                i+=1
                arr[j],arr[i] = arr[i],arr[j]
        arr[i+1],arr[high] = arr[high],arr[i+1]

        return i+1


def quicksort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)



def sort(arr):
    if arr == None:
        return None

    n = len(arr)

    return quicksort(arr,0,n-1)