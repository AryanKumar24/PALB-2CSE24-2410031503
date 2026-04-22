def combination_sum3(k, n):
    res = []
    
    def backtrack(start, path, total):
        if len(path) == k:
            if total == n:
                res.append(path[:])
            return
        
        for i in range(start, 10):
            if total + i > n:
                break
            path.append(i)
            backtrack(i + 1, path, total + i)
            path.pop()
    
    backtrack(1, [], 0)
    return res


print(combination_sum3(3, 9))  
print(combination_sum3(3, 3)) 