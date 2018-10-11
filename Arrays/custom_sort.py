def custom_sort(arr):
    arr = arr[1:]
    counter = {}
    for num in arr:
        if str(num) in counter:
            counter[str(num)] += 1
        else:
            counter[str(num)] = 1
    new_arr = [(counter[str(num)],num)for num in arr]
    pre_res = sorted(new_arr,key=lambda item:(item[0],item[1]))
    res = []
    for freq,num in pre_res:
        res.append(num)

    return res
arr = [5,3,1,2,2,4]
print(custom_sort(arr))


