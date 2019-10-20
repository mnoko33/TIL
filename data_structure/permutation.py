# 순열

def permutation(arr, idx):
    if len(arr) - 1 == idx:
        for char in arr:
            print(char, end='')
        print()
    else:
        for i in range(idx, len(arr)):
            arr[idx], arr[i] = arr[i], arr[idx]
            permutation(arr, idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]

permutation(['A', 'B', 'C', 'D'], 0)
# permutation([1, 2, 3, 4], 0)