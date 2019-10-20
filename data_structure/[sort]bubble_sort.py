# Bubble sort
# 인접한 원소를 비교하여 정렬하는 알고리즘
# 시간복잡도 N ** 2


def bubble_sort_asc(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(0, N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


def bubble_sort_desc(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(0, N - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


arr = [14, 2, 5, 1, 4, 6, 77, 84, 3]
bubble_sort_asc(arr)
print(arr)
bubble_sort_desc(arr)
print(arr)