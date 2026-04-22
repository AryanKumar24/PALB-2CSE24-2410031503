def min_swaps(s1, s2):
    count01 = 0
    count10 = 0

    for i in range(len(s1)):
        if s1[i] == '0' and s2[i] == '1':
            count01 += 1
        elif s1[i] == '1' and s2[i] == '0':
            count10 += 1

    if (count01 + count10) % 2 != 0:
        return -1

    return (count01 + count10) // 2


s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

result = min_swaps(s1, s2)
print("Minimum swaps:", result)