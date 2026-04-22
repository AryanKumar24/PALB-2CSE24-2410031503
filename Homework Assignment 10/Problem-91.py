from math import factorial

def count_unique_vowel_strings(s):
    vowels = set("aeiou")
    
    freq = {}
    
    for ch in s:
        if ch in vowels:
            freq[ch] = freq.get(ch, 0) + 1
    
    if not freq:
        return 0

    product = 1
    k = 0  

    for v in freq:
        product *= freq[v]
        k += 1

    return product * factorial(k)


s = input("Enter string: ")

result = count_unique_vowel_strings(s)
print("Total distinct vowel strings:", result)
