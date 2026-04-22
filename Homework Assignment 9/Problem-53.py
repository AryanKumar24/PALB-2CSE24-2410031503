import heapq

def min_operations(arr):
    total = sum(arr)
    target = total / 2
    
    heap = [-x for x in arr]
    heapq.heapify(heap)
    
    current_sum = total
    operations = 0
    
    while current_sum > target:
        largest = -heapq.heappop(heap)
        half = largest / 2
        
        current_sum -= half
        heapq.heappush(heap, -half)
        
        operations += 1
    
    return operations

arr1 = [8, 6, 2]
arr2 = [9, 1, 2]

print(min_operations(arr1)) 
print(min_operations(arr2))  