def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [1, 4, 3, 2, 6, 5]
reverse_array(arr)
print(arr)  
