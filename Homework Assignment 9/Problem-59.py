def max_visible_people(arr):
    n = len(arr)

    left = [-1] * n
    right = [n] * n

    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    ans = 0

    for i in range(n):
        ans = max(ans, right[i] - left[i] + 1)

    return ans


print(max_visible_people([6, 2, 5, 4, 5, 1, 6])) 
print(max_visible_people([1, 3, 6, 4]))         