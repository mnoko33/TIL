# Selection sort
# 가장 작은 요소를 **선택** 하여 맨 앞의 요소와 교환하고, 맨 앞을 제외한 리스트에서 선택을 반복한다
# 시간복잡도 N ** 2


def selection_sort_asc(arr):
    N = len(arr)
    for i in range(N - 1):
        min_idx = i
        for j in range(i, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


def selection_sort_desc(arr):
    N = len(arr)
    for i in range(N - 1):
        max_idx = i
        for j in range(i, N):
            if arr[max_idx] < arr[j]:
                max_idx = j
        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]


arr = [14, 2, 5, 1, 4, 6, 77, 84, 3]
selection_sort_asc(arr)
print(arr)
arr = [14, 2, 5, 1, 4, 6, 77, 84, 3]
selection_sort_desc(arr)
print(arr)