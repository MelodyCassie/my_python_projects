def is_palindrome(s):
    if s is None:
        return False

    s = ''.join(filter(str.isalnum, s)).lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


input_str = "A man, a plan, a canal, Panama"
result = is_palindrome(input_str)
print("Is it a palindrome?", result)
