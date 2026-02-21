def partition_array(arr, a, b):
    start = 0
    end = len(arr) - 1
    i = 0
    
    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1
    return True


arr = list(map(int, input("Enter array elements: ").split()))
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

result = partition_array(arr, a, b)

print(result)
print("Modified array:", *arr)
