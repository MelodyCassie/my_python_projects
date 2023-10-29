def remove_empty_string(sample_input):
    sample_input = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']

    new_list = [""]

    updated_list = [x for x in sample_input if x not in new_list]

    return updated_list


sample_input = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
result = remove_empty_string(sample_input)
print(result)