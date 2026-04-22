def score_of_parentheses(s):
    score = 0
    depth = 0

    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
        else:
            depth -= 1
            if s[i - 1] == '(':
                score += 1 << depth  

    return score


s = input("Enter balanced parentheses string: ")

result = score_of_parentheses(s)
print("Score:", result)
