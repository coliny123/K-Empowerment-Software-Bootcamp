def sort_arr(arr):
    for i in range(0, len(arr)-1):
        min_idx = i
        for k in range(i+1, len(arr)):
            if arr[min_idx] > arr[k]:
                min_idx = k
        tmp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = tmp
    return arr

two_dimension_arr = [[55, 33,250, 44], [88, 1, 76, 23], [199, 222, 38, 47], [155, 145, 20, 99]]

one_demension_arr = []

for i in range(len(two_dimension_arr)):
    for k in range(len(two_dimension_arr[i])):
        one_demension_arr.append(two_dimension_arr[i][k])

print(f"1차원 배열 정렬 전 : {one_demension_arr}")
one_demension_arr = sort_arr(one_demension_arr)
print(f"1차원 배열 정렬 후 : {one_demension_arr}")
print(f"중앙값 : {one_demension_arr[len(one_demension_arr) // 2]}")