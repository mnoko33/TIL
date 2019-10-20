# Insertion sort 
#  두 번쨰 index부터 그 전의 원소들과 비교해 위치에 삽입한다
# 시간복잡도 N ** 2
# 단 정렬되어있을 경우 더 빠르다


def Insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
        value = arr[i] # i번쨰 요소의 값을 저장
        j = i - 1 # i의 앞의 요소들을 탐색하기 위해 값 설정
        while value < arr[j] and j >= 0: # 위치가 확정되면 while 문 종료
            arr[j + 1] = arr[j] # insertion을 위해 하나씩 밀기
            j -= 1
        arr[j + 1] = value # 앞에서 j -= 1 했기 때문에 j + 1 위치에 원래 i 번째 요소의 값을 할당


arr = [14, 2, 5, 1, 4, 6, 77, 84, 3]
Insertion_sort(arr)
print(arr)
