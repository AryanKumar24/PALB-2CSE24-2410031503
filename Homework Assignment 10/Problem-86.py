def sort_by_length(arr):
    return sorted(arr, key=len)


n = int(input("Enter number of strings: "))
arr = []

for _ in range(n):
    arr.append(input("Enter string: "))

result = sort_by_length(arr)

print("Sorted array:")
print(result)
