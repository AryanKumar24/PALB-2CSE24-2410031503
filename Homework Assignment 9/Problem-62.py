def can_place(arr, k, dist):
    count = 1
    last = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - last >= dist:
            count += 1
            last = arr[i]
    
    return count >= k


def maximize_min_difference(arr, k):
    arr.sort()
    
    left, right = 0, arr[-1] - arr[0]
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_place(arr, k, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans

print(maximize_min_difference([2, 6, 2, 5], 3))           
print(maximize_min_difference([1, 4, 9, 0, 2, 13, 3], 4)) 