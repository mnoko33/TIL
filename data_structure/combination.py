# 조합 nCr

def combination(arr, idx, r, result):
    if len(result) == r:
        print(result)
    elif idx >= len(arr):
        return 
    else:
        for i in range(idx, len(arr)):
            result.append(arr[i])
            combination(arr, i + 1, r, result)
            result.pop()

combination(['A', 'B', 'C', 'D', 'E'], 0, 3, [])
