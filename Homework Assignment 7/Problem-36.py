def group_anagrams(strs):
    d = {}
    
    for word in strs:
        key = ''.join(sorted(word))
        
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    
    return list(d.values())


strs = input("Enter words: ").split()

result = group_anagrams(strs)

print("Output:", result)
