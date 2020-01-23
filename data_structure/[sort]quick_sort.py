def quick_sort(arr, s, e):
    # partition이 낱개일 때
    start = s
    end = e
    if s >= e:
        return

    pivot = arr[(s + e) // 2]
    print(arr, 'pivot : ', s, e, (s + e) // 2)
    while s <= e:
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    quick_sort(arr, start, e)
    quick_sort(arr, e + 1, end)

def quick_sort2(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

def quick_sort3(arr, start, end):
    if start >= end:
        return
    
    initial_start = start
    initial_end = end

    pivot = arr[(start+end)//2]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    quick_sort3(arr, initial_start, start - 1)
    quick_sort3(arr, start, initial_end)

arr = [14, 2, 5, 22, 222, 1, 22, 77, 84, 22, 3]

quick_sort3(arr, 0, len(arr)-1)
print()
print('result: ', arr)