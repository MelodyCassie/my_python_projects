def replace_first_char(string):
    first_char = string[0]
    modified_string = first_char

    for char in string[1:]:
        if char.lower() == first_char.lower():
            modified_string += '$'
        else:
            modified_string += char

    return modified_string


sample_string = 'restart'
result = replace_first_char(sample_string)
print(result)    