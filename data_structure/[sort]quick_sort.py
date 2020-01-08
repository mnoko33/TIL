def quick_sort(arr, s, e):
    # partition이 낱개일 때
    start = s
    end = e
    if s >= e:
        return

    pivot = arr[(s + e) // 2]
    print(arr, 'pivot : ', (s + e) // 2)
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


arr = [14, 2, 5, 2, 2, 2, 77, 84, 3]
quick_sort(arr, 0, len(arr) - 1)