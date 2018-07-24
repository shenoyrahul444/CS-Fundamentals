

def klargest_BubbleSort(a,k):
    n = len(a)
    for i in range(0, k + 1):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a[n-k:]

def kLargest_MaxHeap(a,k):
    import heapq
    h = []
    for n in a:
        heapq.heappush(h,(-1)*n)
    res = []
    for i in range(k):
        res.insert(0,-1*heapq.heappop(h))
    return res

k = 3
a = [9, -9, 3, -3, 9, -4, -7, -6, 8, -3]
print(klargest_BubbleSort(a,k)) # O(n*k) Time complexiety
print(kLargest_MaxHeap(a,k)) # O(n) O(n+k) Space Complexiety

