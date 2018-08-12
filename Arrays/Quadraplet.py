def find_array_quadruplet(arr, s):
    """
    arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
    [0,0,1,2,3,4,5,7,9]
    [0, 4, 7, 9]
    """
    # O(1) Space
    # nlog(n) + O(n^3)
    # O(n^3)
    if len(arr) < 4:
        return []

    arr = sorted(arr)  # O(nlog(n))
    n = len(arr)
    for i in range(0, n - 3):  # 0 -> n-4
        for j in range(i + 1, n - 2):
            k = j + 1
            l = n - 1

            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total < s:
                    k += 1
                elif total > s:
                    l -= 1
                else:
                    return [arr[i], arr[j], arr[k], arr[l]]
    return []


arr = [2,7,4,0,9,5,1,3]
s = 20

