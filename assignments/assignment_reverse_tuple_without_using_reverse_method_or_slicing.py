tuple1 = (10, 20, 30, 40, 50)

reversed_elements = ()

for values in tuple1[::-1]:
    reversed_elements += (values,)
print(reversed_elements)
