def filter_multiple_occurrence(sample_input):
    sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
    result = []
    item_count = {}

    for item in sample_input:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    for item, count in item_count.items():
        if count > 2:
            result.append(item)

    return result


sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
result = filter_multiple_occurrence(sample_input)
print(result)
