import random
import time


def qsort(arr, start, end):
    if end <= start:
        return
    low = start
    high = end

    pivot = arr[(low+high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low +1, high -1
    mid = low

    qsort(arr, start, mid-1)
    qsort(arr, mid, end)


def quick_sort(arr):
    qsort(arr, 0, len(arr)-1)


count_arr = [1000, 10000, 12000, 15000]

for count in count_arr:
    tmp_arr = [random.randint(10000, 99999) for _ in range(count)]
    quick_arr = tmp_arr[:]

    print(f"데이터 수 : {count} 개")
    start= time.time()
    quick_sort(quick_arr)
    end = time.time()
    print("퀵 정렬 : %10.3f 초" % (end - start))
    print()

    count *=5