def min_jumps(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1

    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        if i == n - 1:
            return jumps
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i

    return -1


arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr2 = [1, 4, 3, 2, 6, 7]
arr3 = [0, 10, 20]

print(min_jumps(arr1))
print(min_jumps(arr2))
print(min_jumps(arr3))
