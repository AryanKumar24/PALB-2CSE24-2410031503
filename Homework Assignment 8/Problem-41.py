def subsets(nums):
    result = [[]]
    
    for num in nums:
        new = []
        for subset in result:
            new.append(subset + [num])
        result += new
    
    return result


nums = list(map(int, input("Enter elements: ").split()))

ans = subsets(nums)

print("Output:", ans)
