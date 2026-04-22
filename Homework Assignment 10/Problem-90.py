def lexicographically_largest(s, k):
    stack = []

    for ch in s:
        while k > 0 and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        
        stack.append(ch)
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)


s = input("Enter string: ")
k = int(input("Enter k: "))

result = lexicographically_largest(s, k)
print("Result:", result)