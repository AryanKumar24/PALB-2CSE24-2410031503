def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                backtrack(i, target - candidates[i], path + [candidates[i]])
    
    backtrack(0, target, [])
    return result


candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))

ans = combination_sum(candidates, target)

print("Output:", ans)
