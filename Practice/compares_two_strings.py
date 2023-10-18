def equal_strings(string_one, string_two):

    #if sorted(string_one) == sorted(string_two):
    if len(string_one) == len(string_two):
        return True
    else:
        return False

string1 = 'melody'
string2 = 'ydolem'
result = equal_strings(string1, string2)
print(result)