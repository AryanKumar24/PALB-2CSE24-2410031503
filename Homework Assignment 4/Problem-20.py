class Solution:
    def find3Numbers(self, arr, target):
        arr.sort()  
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                if curr_sum == target:
                    return True
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return False


arr1 = [1, 4, 45, 6, 10, 8]
target1 = 13

arr2 = [1, 2, 4, 3, 6, 7]
target2 = 10

arr3 = [40, 20, 10, 3, 6, 7]
target3 = 24

sol = Solution()

print(sol.find3Numbers(arr1, target1)) 

print(sol.find3Numbers(arr2, target2)) 
