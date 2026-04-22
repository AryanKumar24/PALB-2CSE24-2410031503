from collections import Counter

def sort_by_frequency(s):
    freq = Counter(s)

    sorted_chars = sorted(freq.keys(), key=lambda ch: (freq[ch], ch))

    result = ""
    for ch in sorted_chars:
        result += ch * freq[ch]
    
    return result

s = input("Enter string: ")

result = sort_by_frequency(s)
print("Sorted by frequency:", result)