def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


def merge_sort2(arr, start, end):
    if end - start < 1:
        return

    mid = (start + end) // 2
    merge_sort2(arr, start, mid)
    merge_sort2(arr, mid + 1, end)
    
    temp = []
    first_section = start
    second_section = mid + 1

    while True:
        if arr[first_section] <= arr[second_section]:
            temp.append(arr[first_section])
            first_section += 1
        else:
            temp.append(arr[second_section])
            second_section += 1
        
        if first_section > mid:
            for i in range(second_section, end+1):
                temp.append(arr[i])
            break
        
        if second_section > end:
            for i in range(first_section, mid+1):
                temp.append(arr[i])
            break

    for i in range(start, end + 1):
        arr[i] = temp[i - start]

arr = [14, 124, 3, 1, 4125, 434, 42, 5, 22, 1000, 245]
s = 0
e = len(arr) - 1
merge_sort2(arr, s, e)
print(arr)
