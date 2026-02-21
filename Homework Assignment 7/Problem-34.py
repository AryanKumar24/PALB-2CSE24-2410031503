def combination_sum2(candidates, target):
    candidates.sort()
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            if candidates[i] > target:
                break
            
            backtrack(i+1, target - candidates[i], path + [candidates[i]])
    
    backtrack(0, target, [])
    return result


candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))

ans = combination_sum2(candidates, target)

print("Output:", ans)
