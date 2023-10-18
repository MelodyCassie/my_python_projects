def equal_strings(first: str, second:str):
    for letters in first:
        for l in second:

         if letters == l:
            return True
        else:
            return False

result = equal_strings('mel','lem')
print(result)