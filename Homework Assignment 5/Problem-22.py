def chocolate_distribution(arr, m):
    n = len(arr)
    
    if m == 0 or n == 0:
        return 0
    
    if m > n:
        return -1
    
    arr.sort()
    
    min_diff = float('inf')
    
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        
        if diff < min_diff:
            min_diff = diff
    
    return min_diff


arr = list(map(int, input("Enter chocolates in packets (space separated): ").split()))

m = int(input("Enter number of students: "))

result = chocolate_distribution(arr, m)

print("Minimum difference is:", result)
