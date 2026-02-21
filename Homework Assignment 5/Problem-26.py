def is_palindrome(n):
    return str(n) == str(n)[::-1]


def check_array(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


arr = list(map(int, input("Enter array elements: ").split()))

result = check_array(arr)

print(str(result).lower())
