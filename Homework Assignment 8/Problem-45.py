def search_range(nums, target):
    
    def find_first(nums, target):
        low, high = 0, len(nums)-1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                ans = mid
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return ans
    
    
    def find_last(nums, target):
        low, high = 0, len(nums)-1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                ans = mid
                low = mid+1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return ans
    
    
    return [find_first(nums, target), find_last(nums, target)]


nums = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target: "))

result = search_range(nums, target)

print("Output:", result)
