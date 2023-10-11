my_list = [23, "apple", "car", 0, "one", -1, -3]
for i in my_list:
    print(i)

    if i:
        print(f'"this is a truthy value" {i}')
    else:
        print(f'"this is a falsy value" {i}')