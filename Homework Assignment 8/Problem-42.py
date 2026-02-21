def exist(board, word):
    n = len(board)
    m = len(board[0])
    
    def dfs(i, j, k):
        if k == len(word):
            return True
        
        if i<0 or j<0 or i>=n or j>=m or board[i][j] != word[k]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#'
        
        found = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
        
        board[i][j] = temp
        
        return found
    
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j,0):
                return True
    
    return False


n = int(input("Enter rows: "))
m = int(input("Enter columns: "))

board = []
for i in range(n):
    board.append(input().split())

word = input("Enter word: ")

print(str(exist(board, word)).lower())
