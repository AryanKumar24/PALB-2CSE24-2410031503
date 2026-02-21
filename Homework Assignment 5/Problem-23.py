def smallest_subarray(x, arr):
    n = len(arr)
    min_len = n + 1
    curr_sum = 0
    start = 0
    
    for end in range(n):
        curr_sum += arr[end]
        
        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1
    
    if min_len == n + 1:
        return 0
    else:
        return min_len


x = int(input("Enter value of x: "))
arr = list(map(int, input("Enter array elements: ").split()))

result = smallest_subarray(x, arr)

print("Output:", result)
