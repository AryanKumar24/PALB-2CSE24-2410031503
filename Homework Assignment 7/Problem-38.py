def set_zeroes(matrix, n, m):
    rows = set()
    cols = set()
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    
    for i in range(n):
        for j in range(m):
            if i in rows or j in cols:
                matrix[i][j] = 0
    
    return matrix


n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

result = set_zeroes(matrix, n, m)

print("Output:")
for row in result:
    print(row)

