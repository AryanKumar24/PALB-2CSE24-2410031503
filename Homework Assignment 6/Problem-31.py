n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

max_count = 0
index = -1

for i in range(n):
    count = arr[i].count(1)
    if count > max_count:
        max_count = count
        index = i

print("Output:", index)
