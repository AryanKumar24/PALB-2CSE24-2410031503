def lower_equal_count(arr, l, r, x):
    res = l - 1
    
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    
    return res + 1


def find_pivot(arr):
    l, r = 0, len(arr) - 1
    
    while l < r:
        mid = (l + r) // 2
        
        if arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid
    
    return l


def count_leq_rotated(arr, x):
    n = len(arr)
    pivot = find_pivot(arr)
    
    left = lower_equal_count(arr, 0, pivot - 1, x) if pivot > 0 else 0
    right = lower_equal_count(arr, pivot, n - 1, x)
    
    return left + right


print(count_leq_rotated([4, 5, 8, 1, 3], 6))           
print(count_leq_rotated([6, 10, 12, 15, 2, 4, 5], 14))  