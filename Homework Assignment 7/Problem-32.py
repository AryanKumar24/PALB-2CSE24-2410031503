def search_insert(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

result = search_insert(nums, target)

print("Output:", result)
