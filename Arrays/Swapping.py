def getDifferentNumber(arr):
    n = arr.length
    temp = 0

    # put each number in its corresponding index, kicking out
    # the original number, until the target index is out of range.
    for i in range(n):
        temp = arr[i]
        while temp < n and arr[temp] != temp:
            arr[i], arr[arr[i]] = arr[arr[i]],arr[i]

    for i in range(n):
        if (arr[i] != i):
            return i  # i isn’t in arr, hence we can return it

    # we got here since every number from 0 to n-1 is in arr.
    # By definition then, n isn’t in arr. Otherwise, the size of arr
    # would have been n+1 and not n.
    return n

