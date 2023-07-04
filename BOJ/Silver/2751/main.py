def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i, j, k = 0, 0, 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    arr += left[i:]
    arr += right[j:]
    return arr


N = int(input())

noList = []

for i in range(N):
    noList.append(int(input()))

noList = merge_sort(noList)

for i in range(N):
    print(noList[i])
