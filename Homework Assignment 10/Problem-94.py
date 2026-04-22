from collections import defaultdict

def is_vowel(ch):
    return ch in "aeiou"


def balanced_substrings(arr):
    n = len(arr)
    
    balance_arr = []
    
    for s in arr:
        bal = 0
        for ch in s:
            if is_vowel(ch):
                bal += 1
            else:
                bal -= 1
        balance_arr.append(bal)

    freq = defaultdict(int)
    freq[0] = 1

    prefix = 0
    count = 0

    for val in balance_arr:
        prefix += val
        
        count += freq[prefix]
        freq[prefix] += 1

    return count


n = int(input("Enter number of strings: "))
arr = []

for _ in range(n):
    arr.append(input("Enter string: "))

result = balanced_substrings(arr)
print("Balanced substrings count:", result)
