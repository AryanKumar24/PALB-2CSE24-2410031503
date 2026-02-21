arr = list(map(int, input("Enter array elements: ").split()))

arr.sort()
n = len(arr)

if n % 2 == 1:
    median = arr[n//2]
else:
    median = (arr[n//2] + arr[n//2 - 1]) / 2

print("Output:", median)
