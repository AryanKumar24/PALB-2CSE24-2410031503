from collections import Counter

def count_even_letters(s):
    freq = Counter(s)
    
    count = 0
    for ch in freq:
        if freq[ch] % 2 == 0:
            count += 1
    
    return count


s = input("Enter string: ")

result = count_even_letters(s)
print("Count of even frequency characters:", result)
