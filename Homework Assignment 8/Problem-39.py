def search_matrix(matrix, m, n, target):
    low = 0
    high = m*n - 1
    
    while low <= high:
        mid = (low + high) // 2
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False


m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))

target = int(input("Enter target: "))

result = search_matrix(matrix, m, n, target)

print(str(result).lower())
