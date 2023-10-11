def copy_string(string, n):
    if len(string) < 2:
        return string * n
    else:
        return string[:2] * n



result = copy_string("melody", 3)
print(result)
