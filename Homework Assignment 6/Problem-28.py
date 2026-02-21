def spiral(mat, n, m):
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    result = []
    
    while top <= bottom and left <= right:
        
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    
    return result


n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

ans = spiral(mat, n, m)

print("Output:", ans)
