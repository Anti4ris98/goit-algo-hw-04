import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])  # Виправлено тут
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def test_sorting_algorithm(sort_func, arr):
    setup_code = f"from __main__ import {sort_func}"
    stmt = f"{sort_func}({arr})"
    time = timeit.timeit(stmt, setup=setup_code, number=1)
    return time

if __name__ == "__main__":
    arr = [8, 3, 10, 9, 1, 5, 2, 6, 4, 7]
    merge_time = test_sorting_algorithm("merge_sort", arr.copy())
    insertion_time = test_sorting_algorithm("insertion_sort", arr.copy())
    timsort_time = timeit.timeit(lambda: sorted(arr.copy()), number=1)

    print(f"Час виконання сортування злиттям: {merge_time} сек")
    print(f"Час виконання сортування вставками: {insertion_time} сек")
    print(f"Час виконання Timsort: {timsort_time} сек")
