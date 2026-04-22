def find132pattern(arr):
    n = len(arr)
    stack = []
    third = float('-inf')

    for i in range(n - 1, -1, -1):
        if arr[i] < third:
            return True
        
        while stack and arr[i] > stack[-1]:
            third = stack.pop()
        
        stack.append(arr[i])

    return False


print(find132pattern([4, 7, 11, 5, 13, 2])) 
print(find132pattern([11, 11, 12, 9]))       