def count_pairs(arr):
    n = len(arr)
    count = 0
    length = len(arr[0])

    for i in range(n):
        for j in range(i + 1, n):
            diff = 0
            
            for k in range(length):
                if arr[i][k] != arr[j][k]:
                    diff += 1
                    if diff > 1:
                        break
            
            if diff == 1:
                count += 1

    return count


n = int(input("Enter number of strings: "))
arr = []

for _ in range(n):
    arr.append(input("Enter string: "))

result = count_pairs(arr)
print("Number of valid pairs:", result)
