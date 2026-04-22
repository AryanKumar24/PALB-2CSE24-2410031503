from collections import defaultdict

def shortest_substring(s1, s2):
    need = defaultdict(int)
    
    for ch in s1:
        need[ch] = 1

    required = len(need)
    window = defaultdict(int)

    left = 0
    formed = 0
    min_len = float('inf')

    for right in range(len(s2)):
        ch = s2[right]
        window[ch] += 1

        if ch in need and window[ch] == need[ch]:
            formed += 1

        while left <= right and formed == required:
            min_len = min(min_len, right - left + 1)

            left_char = s2[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1

    return min_len if min_len != float('inf') else -1


s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

result = shortest_substring(s1, s2)
print("Shortest substring length:", result)