n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

arr = []

for i in range(n):
    for j in range(m):
        arr.append(mat[i][j])

arr.sort()

median = arr[(n*m)//2]

print("Output:", median)
