def tug_of_war(arr):
    n = len(arr)
    total = sum(arr)
    
    target_size = n // 2
    
    best = {"diff": float("inf"), "subset": None}
    
    def backtrack(i, curr, curr_sum):
        if len(curr) > target_size:
            return
        
        if i == n:
            if len(curr) == target_size:
                s1 = curr_sum
                s2 = total - curr_sum
                diff = abs(s1 - s2)
                if diff == 0:
                    best["subset"] = curr[:]
            return
        
        curr.append(arr[i])
        backtrack(i + 1, curr, curr_sum + arr[i])
        curr.pop()
        
        backtrack(i + 1, curr, curr_sum)
    
    backtrack(0, [], 0)
    
    subset1 = best["subset"]
    subset2 = []
    
    used = set(subset1)
    for x in arr:
        if x in used:
            subset2.append(x)
            used.remove(x)
    
    return [subset1, subset2]


print(tug_of_war([1, 2, 3, 4]))
print(tug_of_war([5, 10, 15]))