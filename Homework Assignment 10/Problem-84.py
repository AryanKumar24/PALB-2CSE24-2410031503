def to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s


def min_time_difference(arr):
    times = [to_seconds(t) for t in arr]
    
    times.sort()
    
    min_diff = float('inf')
    
    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i - 1])
    
    full_day = 24 * 3600
    circular_diff = full_day - (times[-1] - times[0])
    
    return min(min_diff, circular_diff)


n = int(input("Enter number of time strings: "))
arr = []

for _ in range(n):
    arr.append(input("Enter time (HH:MM:SS): "))

result = min_time_difference(arr)
print("Minimum difference (seconds):", result)
